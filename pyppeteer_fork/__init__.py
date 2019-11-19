#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Meta data for pyppeteer_fork."""

import logging
import os

from appdirs import AppDirs

__author__ = """Hiroyuki Takagi"""
__email__ = 'miyako.dev@gmail.com'
__version__ = '0.0.26'
__chromium_revision__ = '706915'
__base_puppeteer_version__ = 'v1.6.0'
__pyppeteer_fork_home__ = os.environ.get(
    'PYPPETEER_HOME', AppDirs('pyppeteer_fork').user_data_dir)  # type: str
DEBUG = False

# Setup root logger
_logger = logging.getLogger('pyppeteer_fork')
_log_handler = logging.StreamHandler()
_fmt = '[{levelname[0]}:{name}] {msg}'
_formatter = logging.Formatter(fmt=_fmt, style='{')
_log_handler.setFormatter(_formatter)
_log_handler.setLevel(logging.DEBUG)
_logger.addHandler(_log_handler)
_logger.propagate = False

from pyppeteer_fork.launcher import connect, launch, executablePath  # noqa: E402
from pyppeteer_fork.launcher import defaultArgs  # noqa: E402

version = __version__
version_info = tuple(int(i) for i in version.split('.'))

__all__ = [
    'connect',
    'launch',
    'executablePath',
    'defaultArgs',
    'version',
    'version_info',
]
