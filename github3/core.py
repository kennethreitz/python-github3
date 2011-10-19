# -*- coding: utf-8 -*-

"""
github3.core
~~~~~~~~~~~~

This module provides the entrance point for the GitHub3 module.
"""

__version__ = '0.0.0'
__license__ = 'MIT'
__author__ = 'Kenneth Reitz'


import envoy

from .api import Github, settings



def no_auth():
    """Returns an un-authenticated Github object."""

    gh = Github()

    return gh


def basic_auth(username, password):
    """Returns an authenticated Github object, via HTTP Basic."""

    gh = Github()
    gh.is_authenticated = True
    gh.session.auth = (username, password)

    return gh



# def git_config():
#     """Returns an authenticated Github object, via HTTP Basic.

#     GitHub API token is taken from `git config`.
#     """

#     username = envoy.run('git config github.user').std_out.strip()
#     token = envoy.run('git config github.token').std_out.strip()

#     def enable_auth(*args, **kwargs):
#         kwargs['auth'] = (username, token)
#         return args, kwargs

#     gh = Github()
#     gh.is_authenticated = True
#     gh._requests_pre_hook = enable_auth

#     return gh