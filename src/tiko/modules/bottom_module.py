from tiko.modules.rust_module import RustModule
from tiko.simple_module import SimpleModule


class BottomModule(SimpleModule):
    dependencies = [RustModule]
    installed_command_name = 'btm'

    def install(self) -> None:
        self.terminal.install_cargo_crate('bottom')
