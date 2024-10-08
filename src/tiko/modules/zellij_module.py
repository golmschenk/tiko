from tiko.modules.rust_module import RustModule
from tiko.simple_module import SimpleModule


class ZellijModule(SimpleModule):
    dependencies = [RustModule]
    installed_command_name = 'zellij'

    def install(self) -> None:
        self.terminal.install_cargo_crate('zellij')
