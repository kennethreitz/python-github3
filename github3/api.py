# -*- coding: utf-8 -*-
"""
github3.api
~~~~~~~~~~~

This module implements the GitHub3 API wrapper objects.

:copyright: (c) 2011 by Kenneth Reitz.
:license: ISC, see LICENSE for more details.

"""

import urllib


from .config import settings
from .helpers import is_collection
from .packages import omnijson as json


class GithubCore(object):
    """The main GitHub API Interface."""

    def __init__(self):
        self.username = None
        self._auth = None


    @staticmethod
    def _resource_serialize(o):
        """Returns JSON serialization of given object."""
        return json.dumps(o)


    @staticmethod
    def _resource_deserialize(s):
        """Returns dict deserialization of a given JSON string."""

        try:
            return json.loads(s)
        except ValueError:
            raise ResponseError('The API Response was not valid.')


    def _generate_url(self, resource, params):
        """Generates Readability API Resource URL."""

        if is_collection(resource):
            resource = map(str, resource)
            resource = '/'.join(resource)

        if params:
            resource += '?%s' % (urllib.urlencode(params))

        return settings.domain + '/' + resource


class Github(GithubCore):
    """The user-facing GitHub API Interface."""

    def __init__(self):
        super(Github, self).__init__()


# ----------
# Exceptions
# ----------

class APIError(Exception):
    """There was an API Error."""

class PermissionsError(APIError):
    """You do not have proper permission."""

class AuthenticationError(APIError):
    """Authentication failed."""

class ResponseError(APIError):
    """The API Response was unexpected."""

class MissingError(APIError):
    """The Resource does not exist."""

class BadRequestError(APIError):
    """The request could not be understood due to bad syntax. Check your request and try again."""

class ServerError(APIError):
    """The server encountered an error and was unable to complete your request."""