# -*- coding: utf-8 -*-

"""
github3.core
~~~~~~~~~~~~

This module contains the core GitHub 3 interface.

"""


from .api import API_URL



class GitHub(object):
    """Central GitHub object."""

    ratelimit = None
     = None

    def __init__(self, apiurl=API_URL):
        pass

    def login(self):
        pass


# Default instance
github = GitHub()