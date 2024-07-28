import shutil
import tomllib
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from tiko.logging import set_up_default_logger
from tiko.terminal import Terminal


@dataclass
class Installer:
    terminal: Terminal

    @classmethod
    def new(cls) -> Self:
        set_up_default_logger()
        instance = cls(Terminal.new())
        return instance

    def install(self) -> None:
        tiko_configuration_path = Path('tiko_configuration.toml')
        with tiko_configuration_path.open('rb') as tiko_configuration_file:
            tiko_configuration_dictionary = tomllib.load(tiko_configuration_file)
        pass


    def is_rust_installed(self) -> bool:
        self.terminal.run_command('which cargo')


    def install_rust(self) -> None:
        pass


    def process_rust(self) -> None:
        if not self.is_rust_installed():
            self.install_rust()



if __name__ == '__main__':
    installer = Installer.new()
    installer.is_rust_installed()
