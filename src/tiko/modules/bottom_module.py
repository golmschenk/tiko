from tiko.module import Module, InstallConfirmationError
from tiko.modules.rust_module import RustModule


class BottomModule(Module):
    dependencies = [RustModule]

    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('btm')

    def install(self) -> None:
        if not self.check_if_installed():
            self.terminal.run_command('cargo install bottom --locked')
            if not self.check_if_installed():
                raise InstallConfirmationError
