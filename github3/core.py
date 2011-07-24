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


def basic_auth(username, password):
    """Returns an authenticated Github object, via HTTP Basic."""

    def enable_auth(*args, **kwargs):
        kwargs['auth'] = (username, password)
        return args, kwargs

    gh = Github()
    gh._requests_pre_hook = enable_auth

    return gh