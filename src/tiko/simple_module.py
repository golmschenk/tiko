from abc import ABC, abstractmethod

from tiko.module import Module, InstallConfirmationError


class SimpleModule(Module, ABC):
    installed_command_name: str = 'some_command_name'

    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists(self.installed_command_name)

    def process(self) -> None:
        if not self.check_if_installed():
            self.process()
            if not self.check_if_installed():
                raise InstallConfirmationError

    @abstractmethod
    def install(self):
        pass
