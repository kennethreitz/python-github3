# -*- coding: utf-8 -*-
"""
    github3.api
    ~~~~~~~~~~~

    This module implements the GitHub3 API wrapper objects.

    :copyright: (c) 2011 by Kenneth Reitz.
    :license: ISC, see LICENSE for more details.
"""

from . import models
from .packages.anyjson import deserialize

import requests




API_URL = 'https://api.github.com'
API_MIME = 'application/vnd.github.v3+json'




# =======
# Helpers
# =======

def _safe_response(r, error=None):

    try:
        r.raise_for_status()
        return r
    except requests.HTTPError:
        if (r.status_code == 404) or (r.status_code == 401):
            raise LoginFailed
        else:
            raise APIError(error) if error else APIError


def get(*path, **params):
    """
    Accepts optional error parameter, which will be passed in the event of a
    non-401 HTTP error.

    api.get('groups')
    api.get('groups', 'id')
    api.get('accounts', 'verify')
    """

    url = '{0}{1}'.format(API_URL, '/'.join(map(str, path)))

    # params = kwargs.get('params', None)

    r = requests.get(url, params=params, auth=None)

    return _safe_response(r)


def post(params, *path):

    url =  '%s%s%s' % (API_URL, '/'.join(map(str, path)), '.json')
    r = requests.post(url, params=params, auth=auth)
    return _safe_response(r)


# ==========
# Exceptions
# ==========

class LoginFailed(RuntimeError):
    """Login falied!"""

class APIError(RuntimeError):
    """There was a problem properly accessing the Convore API."""



def login(username, password):
    """Configured API Credentials"""
    global auth

    auth = (username, password)
    # print requests.auth_manager.__dict__

# ==========
# End Points
# ==========

