import json
import platform
import re
import shutil
import tarfile
from pathlib import Path

import requests

from tiko.simple_module import SimpleModule
from tiko.terminal import Terminal, TerminalError


def download_file(url: str, path: Path):
    with requests.get(url, stream=True) as response:
        with path.open('wb') as file:
            shutil.copyfileobj(response.raw, file)


class HelixModule(SimpleModule):
    def check_if_installed(self) -> bool:
        return self.terminal.check_if_command_exists('nu')

    def install(self) -> None:
        latest_helix_release_url = 'https://api.github.com/repos/helix-editor/helix/releases/latest'
        response = requests.get(latest_helix_release_url)
        latest_release_dictionary = json.loads(response.content)
        assets_dictionary = latest_release_dictionary['assets']
        machine = platform.machine()
        if machine == 'x86_64':
            machine_string = 'x86_64'
        elif machine == 'aarch64' or machine == 'arm64':
            machine_string = 'aarch64'
        else:
            raise TerminalError(f'Unknown machine {machine}.')
        system = platform.system()
        if system == 'Linux':
            system_string = 'linux'
        elif system == 'Darwin':
            system_string = 'macos'
        else:
            raise TerminalError(f'Unknown system {system}.')

        correct_browser_download_url = None
        for asset in assets_dictionary:
            browser_download_url = asset['browser_download_url']
            match = re.search(fr'helix-[\d\.]+-{machine_string}-{system_string}.tar.xz', browser_download_url)
            if match is not None:
                correct_browser_download_url = browser_download_url
                break
        if correct_browser_download_url is None:
            raise TerminalError(f'Could not find {system} and {machine} pair in assets at {latest_helix_release_url}.')
        tiko_directory = Path.home().joinpath('.tiko')
        tiko_temporary_directory = tiko_directory.joinpath('temporary')
        helix_compressed_path = tiko_temporary_directory.joinpath('helix.tar.xz')
        helix_path = tiko_directory.joinpath('helix')
        tiko_directory.mkdir(exist_ok=True, parents=True)
        tiko_temporary_directory.mkdir(exist_ok=True, parents=True)
        download_file(correct_browser_download_url, helix_compressed_path)
        with tarfile.open(helix_compressed_path) as file:
            file.extractall(helix_path)
        original_name_release_directory = [path for path in helix_path.iterdir() if path.is_dir()][0]
        for path in original_name_release_directory.iterdir():
            path.rename(helix_path.joinpath(path.name))
        original_name_release_directory.rmdir()
        with Path.home().joinpath('.bash_profile').open('a') as bash_profile_file:
            bash_profile_file.write('\nexport PATH=$HOME/.tiko/helix:$PATH')
        # TODO: Continue here. Add it to path. Add the library stuff.


if __name__ == '__main__':
    terminal = Terminal.new()
    module = HelixModule(terminal)
    module.install()
