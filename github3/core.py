# -*- coding: utf-8 -*-

"""
github3.core
~~~~~~~~~~~~~

This module provides the base entrypoint for github3.
"""

from .api import Github

def login(username, password):
    """Returns an authenticated Github instance, via API Key."""

    gh = Github()

    # Login.
    gh.login(username, password)

    return gh
