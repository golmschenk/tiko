import json
import re
import shutil
import tarfile
from pathlib import Path

import requests

from tiko.internal.exceptions import GitHubAssetError


def download_github_asset(github_owner: str, github_repository: str, asset_pattern: str, destination_directory: Path):
    github_token = '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'
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