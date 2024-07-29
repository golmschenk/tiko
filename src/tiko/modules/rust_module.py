from tiko.module import Module


class RustModule(Module):
    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('cargo')

    def install(self) -> None:
        self.terminal.run_command('curl https://sh.rustup.rs -sSf | sh -s -- -y')
