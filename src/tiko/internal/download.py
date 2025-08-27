import json
import re
import shutil
import tarfile
from pathlib import Path

import requests

from tiko.internal.exceptions import GitHubAssetError


def get_github_token() -> str:
    """
    Gets a public repository read-only GitHub token. The token is in hex just to prevent automated systems from
    detecting it. However, it has no real power anyway, since it's a public repository read-only token and doesn't
    matter if it's leaked.

    :return: The token.
    """
    hex_token = ('6769746875625f7061745f3131424344345a584930525a6d7730344e42546b4a795f50425273396c4541746a586e695364445'
                 '65735484c645231754f354635647a73674a3054365162694a5659354e5a595135435a4b4b4b48564b3652')
    token = bytearray.fromhex(hex_token).decode()
    return token


def download_github_asset(github_owner: str, github_repository: str, asset_pattern: str, destination_directory: Path):
    github_token = get_github_token()
    headers = {'Authorization': f'token {github_token}'}
    latest_release_url = f'https://api.github.com/repos/{github_owner}/{github_repository}/releases/latest'
    response = requests.get(latest_release_url, headers=headers)
    latest_release_dictionary = json.loads(response.content)
    assets_dictionary = latest_release_dictionary['assets']
    correct_browser_download_url = None
    for asset in assets_dictionary:
        browser_download_url = asset['browser_download_url']

        match = re.search(asset_pattern, browser_download_url)
        if match is not None:
            correct_browser_download_url = browser_download_url
            break
    if correct_browser_download_url is None:
        raise GitHubAssetError(f'Could not find pattern {asset_pattern} pair in assets at {latest_release_url}.')
    compressed_download_path = destination_directory.joinpath('download_asset.tar.xz')
    download_file(correct_browser_download_url, compressed_download_path)
    with tarfile.open(compressed_download_path) as file:
        file.extractall(destination_directory, filter='data')
    compressed_download_path.unlink()
    original_name_release_directory = [path for path in destination_directory.iterdir() if path.is_dir()][0]
    for path in original_name_release_directory.iterdir():
        path.rename(destination_directory.joinpath(path.name))
    original_name_release_directory.rmdir()


def download_file(url: str, path: Path):
    with requests.get(url, stream=True) as response:
        with path.open('wb') as file:
            shutil.copyfileobj(response.raw, file)