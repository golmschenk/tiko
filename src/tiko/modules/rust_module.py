from tiko.simple_module import SimpleModule


class RustModule(SimpleModule):
    installed_command_name = 'cargo'

    def install(self) -> None:
        self.terminal.run_command('curl https://sh.rustup.rs -sSf | sh -s -- -y')
