from tiko.module import Module, InstallConfirmationError
from tiko.modules.rust_module import RustModule


class NuModule(Module):
    dependencies = [RustModule]

    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('nu')

    def install(self) -> None:
        if not self.check_if_installed():
            self.terminal.run_command('cargo install nu')
            self.terminal.run_command('cargo install nu_plugin_polars')
            # TODO: Run `plugin add ~/.cargo/bin/nu_plugin_polars` inside a nu instance.
            if not self.check_if_installed():
                raise InstallConfirmationError
