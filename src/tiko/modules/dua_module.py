from tiko.modules.rust_module import RustModule
from tiko.simple_module import SimpleModule


class DuaModule(SimpleModule):
    dependencies = [RustModule]
    installed_command_name = 'dua'

    def install(self) -> None:
        self.terminal.install_cargo_crate('dua-cli')
