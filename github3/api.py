# -*- coding: utf-8 -*-

"""
github3.api
~~~~~~~~~~~

This module provies the core GitHub3 API interface.
"""

import omnijson as json

from .models import *
from .helpers import is_collection, to_python, to_api, get_scope
from .config import settings


import requests

from decorator import decorator


class GithubCore(object):

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


    @staticmethod
    def _generate_url(endpoint):
        """Generates proper endpoint URL."""

        if is_collection(endpoint):
            resource = map(str, endpoint)
            resource = '/'.join(endpoint)
        else:
            resource = endpoint

        return (settings.base_url + resource)


    def _requests_pre_hook(*args, **kwargs):
        return args, kwargs


    def _http_resource(self, verb, endpoint, params=None, authed=True):

        url = self._generate_url(endpoint)

        if authed:
            args, kwargs = self._requests_pre_hook(verb, url, params=params)
        else:
            args = (verb, url)
            kwargs = {'params': params}

        r = requests.request(*args, **kwargs)

        r.raise_for_status()

        return r


    def _get_resource(self, resource, obj, authed=True, **kwargs):

        r = self._http_resource('GET', resource, params=kwargs, authed=authed)
        item = self._resource_deserialize(r.content)

        return obj.new_from_dict(item, gh=self)


    def _to_map(self, obj, iterable):
        """Maps given dict iterable to a given Resource object."""

        a = list()

        for it in iterable:
            a.append(obj.new_from_dict(it, rdd=self))

        return a

    def _get_url(self, resource):

        if is_collection(resource):
            resource = map(str, resource)
            resource = '/'.join(resource)

        return resource



class Github(GithubCore):
    """docstring for Github"""

    def __init__(self):
        super(Github, self).__init__()
        self.is_authenticated = False


    def get_user(self, username):
        """Get a single user."""
        return self._get_resource(('users', username), User, authed=False)


    def get_me(self):
        """Get the authenticated user."""
        return self._get_resource(('user'), User)



class ResponseError(Exception):
    """The API Response was unexpected."""

