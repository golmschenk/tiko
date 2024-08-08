from tiko.module import Module, InstallConfirmationError
from tiko.modules.rust_module import RustModule


class ZellijModule(Module):
    dependencies = [RustModule]

    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('zellij')

    def install(self) -> None:
        if not self.check_if_installed():
            self.terminal.install_cargo_crate('zellij')
            if not self.check_if_installed():
                raise InstallConfirmationError
