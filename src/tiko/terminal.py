import logging
from dataclasses import dataclass
from subprocess import Popen, PIPE
from typing import Self


logger = logging.getLogger(__name__)


@dataclass
class Terminal:
    process: Popen

    @classmethod
    def new(cls) -> Self:
        process = Popen('/bin/bash', shell=True, text=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        instance = cls(process=process)
        return instance

    def run_command(self, command: str):
        logger.info(f'> {command}')
        stdout, stderr = self.process.communicate(command)
        for stdout_line in stdout.splitlines():
            logger.info(stdout_line)
        for stderr_line in stderr.splitlines():
            logger.error(stderr_line)
