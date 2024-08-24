from pathlib import Path

from tiko.module import Module, InstallConfirmationError
from tiko.modules.rust_module import RustModule


class NuModule(Module):
    dependencies = [RustModule]

    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('nu')

    def process(self) -> None:
        if not self.check_if_installed():
            self.terminal.install_cargo_crate('nu')
            self.terminal.install_cargo_crate('nu_plugin_polars')
            self.terminal.run_command(f'nu -c "plugin add {str(Path.home().joinpath('/.cargo/bin/nu_plugin_polars'))}"')
            if not self.check_if_installed():
                raise InstallConfirmationError
