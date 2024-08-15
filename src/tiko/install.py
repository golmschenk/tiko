import shutil
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Self

import logging
from tiko.logging import set_up_default_logger
from tiko.module_processing import process_list
from tiko.terminal import Terminal


@dataclass
class Installer:
    terminal: Terminal

    @classmethod
    def new(cls) -> Self:
        instance = cls(Terminal.new())
        return instance

    def install(self) -> None:
        tiko_configuration_path = Path('tiko_configuration.toml')
        if tiko_configuration_path.exists():
            with tiko_configuration_path.open('rb') as tiko_configuration_file:
                tiko_configuration_dictionary = tomllib.load(tiko_configuration_file)
        process_list(['rust', 'nu', 'zellij', 'bottom', 'dua'], self.terminal)


if __name__ == '__main__':
    set_up_default_logger()
    logger = logging.getLogger('tiko')
    logger.setLevel(logging.DEBUG)
    installer = Installer.new()
    installer.install()
