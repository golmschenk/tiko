from pathlib import Path

home_directory = Path.home()
tiko_directory = home_directory.joinpath('.tiko')
tiko_directory.mkdir(exist_ok=True, parents=True)
tiko_bin_directory = tiko_directory.joinpath('bin')
tiko_bin_directory.mkdir(exist_ok=True, parents=True)
tiko_temporary_directory = tiko_directory.joinpath('temporary')
tiko_temporary_directory.mkdir(exist_ok=True, parents=True)
