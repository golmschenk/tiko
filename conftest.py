import logging
import sys

from tiko.logging import set_up_default_logger, create_default_formatter


def pytest_configure(config):
    set_up_default_logger()
    formatter = create_default_formatter()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger = logging.getLogger('tiko')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
