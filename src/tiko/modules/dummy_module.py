from tiko.module import Module


class DummyModule(Module):
    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('fdjsakldfjal')

    def install(self) -> None:
        self.terminal.run_command('echo djafkldajflkdajkfldsa')
