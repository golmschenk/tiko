from tiko.install import Installer


def test_full_install():
    installer = Installer.new()
    installer.install()
