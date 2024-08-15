from pathlib import Path

from pexpect import spawn

import logging
from dataclasses import dataclass
from typing import Self


logger = logging.getLogger(__name__)


class TerminalError(Exception):
    pass


prompt_prefix = '<>prompt_prefix<>'


@dataclass
class Terminal:
    process: spawn

    @classmethod
    def new(cls) -> Self:
        process = spawn('/bin/bash', encoding='utf-8')
        process.logfile = Path('pexpect.log').open('a')
        instance = cls(process=process)
        logger.debug('Setting up prompt.')
        process.sendline(f'export PS1="{prompt_prefix}> "')
        process.sendline(f'echo 0')
        output0 = process.expect(f'{prompt_prefix}> echo 0', timeout=None)
        logger.debug(f'Prompt pexpect before 0: {output0}')
        output1 = process.expect(prompt_prefix, timeout=None)
        logger.debug(f'Prompt pexpect before 1: {output1}')
        return instance

    def run_command(self, command: str) -> str:
        logger.debug(f'Sending command: `{command}`')
        self.process.sendline(command)
        self.process.expect(prompt_prefix, timeout=None)
        output = self.log_and_return_before()
        return output

    def log_and_return_before(self) -> str:
        output = self.process.before
        output = output.replace('\r\n', '\n')
        for output_line in output.splitlines():
            logger.debug('Pexpect output start.')
            logger.info(output_line)
            logger.debug('Pexpect output end.')
        return output

    def check_if_command_exists(self, command: str) -> bool:
        output = self.run_command(f'which {command}')
        output_lines = output.splitlines()
        updated_output_lines: list[str] = []
        for output_line in output_lines:
            output_line = output_line.strip()
            if len(output_line) > 0:
                updated_output_lines.append(output_line)
        return len(output_lines) > 1

    def install_cargo_crate(self, crate_name: str) -> None:
        locked_install_output = self.run_command(f'cargo install --locked {crate_name}')
        if 'error: failed to compile' in locked_install_output:
            unlocked_install_output = self.run_command(f'cargo install {crate_name}')
            if 'error: failed to compile' in unlocked_install_output:
                raise TerminalError(f'Failed to install cargo crate {crate_name}.')
