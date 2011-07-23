# -*- coding: utf-8 -*-

"""
github3.core
~~~~~~~~~~~~

This module provides the entrance point for the GitHub3 module.
"""

__version__ = '0.0.0'
__license__ = 'MIT'
__author__ = 'Kenneth Reitz'

from .api import Github, settings


def no_auth():
    """Returns an un-authenticated Github object."""

    gh = Github()

    return gh


def basic_auth():
    """Returns an authenticated Github object, via HTTP Basic."""

    gh = Github()

    return gh