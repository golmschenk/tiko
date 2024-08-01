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
        instance = cls(process=process)
        process.sendline(f'export PS1="{prompt_prefix}> "')
        process.expect(prompt_prefix)
        process.expect(prompt_prefix)
        return instance

    def run_command(self, command: str) -> str:
        self.process.sendline(command)
        self.process.expect(prompt_prefix)
        output = self.log_and_return_before()
        return output

    def log_and_return_before(self) -> str:
        output = self.process.before
        output = output.replace('\r\n', '\n')
        for output_line in output.splitlines():
            logger.info(output_line)
        return output

    def check_if_command_exists(self, command: str) -> bool:
        output = self.run_command(f'which {command}')
        return len(output) > 0
