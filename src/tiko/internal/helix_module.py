import platform
import uuid

from tiko.internal.default_paths import tiko_directory, user_bin_directory, home_directory
from tiko.internal.download import download_github_asset
from tiko.internal.exceptions import PlatformError


def install_helix() -> None:
    machine = platform.machine()
    if machine == 'x86_64':
        machine_string = 'x86_64'
    elif machine == 'aarch64' or machine == 'arm64':
        machine_string = 'aarch64'
    else:
        raise PlatformError(f'Unsupported machine `{machine}` for `helix` module.')
    system = platform.system()
    if system == 'Linux':
        system_string = 'linux'
    elif system == 'Darwin':
        system_string = 'macos'
    else:
        raise PlatformError(f'Unsupported system `{system}` for `helix` module.')
    github_owner = 'helix-editor'
    github_repository = 'helix'
    asset_pattern = fr'helix-[\d.]+-{machine_string}-{system_string}.tar.xz'
    temporary_directory = tiko_directory.joinpath(f'temporary/{uuid.uuid4()}')
    temporary_directory.mkdir()
    download_github_asset(github_owner, github_repository, asset_pattern, temporary_directory)
    executable_path = user_bin_directory.joinpath('hx')
    temporary_directory.joinpath('hx').rename(executable_path)
    helix_runtime_directory = home_directory.joinpath('.config/helix/runtime')
    helix_runtime_directory.parent.mkdir(exist_ok=True, parents=True)
    temporary_directory.joinpath('runtime').rename(helix_runtime_directory)


if __name__ == '__main__':
    install_helix()
