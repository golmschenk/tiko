from pathlib import Path

home_directory = Path.home()
tiko_directory = home_directory.joinpath('.tiko')
user_bin_directory = home_directory.joinpath('.local/bin')