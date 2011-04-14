# -*- coding: utf-8 -*-

"""
github3.core
~~~~~~~~~~~~

This module contains the core GitHub 3 interface.

"""


from .api import API_URL, get



class GitHub(object):
    """Central GitHub object."""

    rate_limit = None
    rate_left = None
    per_page = 30

    def __init__(self, apiurl=API_URL):
        self.__basic_auth = None

    def _get(self, *path):
        r = get(*path, auth=self.__basic_auth)

        rate_limit = r.headers.get('x-ratelimit-remaining', None)
        rate_left = r.headers.get('x-ratelimit-limit', None)

        if (rate_limit is not None) or (rate_left is not None):
            self.rate_limit = rate_limit
            self.rate_left = rate_left

        return r

    def auth(self, username, password):
        self.__basic_auth = (username, password)
        return self.logged_in

    def oauth(self):
        # TODO: oAuth
        pass

    @property
    def logged_in(self):
        r = self._get('')
        print

        if r.status_code == 200:
            return True
        else:
            return False



# Default instance
github = GitHub()