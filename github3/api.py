# -*- coding: utf-8 -*-

"""
github3.api
~~~~~~~~~~~

This module provies the core GitHub3 API interface.
"""

from .packages import omnijson as json
from .packages.link_header import parse_link_value

from .models import *
from .helpers import is_collection, to_python, to_api, get_scope
from .config import settings


import requests

from decorator import decorator


class GithubCore(object):

    _rate_limit = None
    _rate_limit_remaining = None


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


    def _requests_pre_hook(self, *args, **kwargs):
        """Pre-processing for HTTP requests arguments."""
        return args, kwargs


    def _requests_post_hook(self, r):
        """Post-processing for HTTP response objects."""

        self._ratelimit = int(r.headers.get('x-ratelimit-limit', -1))
        self._ratelimit_remaining = int(r.headers.get('x-ratelimit-remaining', -1))

        return r


    def _http_resource(self, verb, endpoint, params=None, authed=True):

        url = self._generate_url(endpoint)

        if authed:
            args, kwargs = self._requests_pre_hook(verb, url, params=params)
        else:
            args = (verb, url)
            kwargs = {'params': params}

        r = requests.request(*args, **kwargs)
        r = self._requests_post_hook(r)

        # print self._ratelimit_remaining

        r.raise_for_status()

        return r


    def _get_resource(self, resource, obj, authed=True, **kwargs):

        r = self._http_resource('GET', resource, params=kwargs, authed=authed)
        item = self._resource_deserialize(r.content)

        return obj.new_from_dict(item, gh=self)


    def _get_resources(self, resource, obj, authed=True, **kwargs):

        r = self._http_resource('GET', resource, params=kwargs, authed=authed)
        d_items = self._resource_deserialize(r.content)

        items = []

        for item in d_items:
            items.append(obj.new_from_dict(item, gh=self))

        return items


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
        return self._get_resource(('users', username), User)

    def get_org(self, orgname):
        """Get a single organization."""
        return self._get_resource(('orgs', orgname), Organization)

    def get_me(self):
        """Get the authenticated user."""
        return self._get_resource(('user'), CurrentUser)

    # def get_repos(self, username):
        # """Get repos."""
         # return self._get_resource(('user', 'username', 'repos'), Repo)

    def get_repo(self, username, reponame):
        """Get the authenticated user."""
        return self._get_resource(('repos', username, reponame), Repo)

    def get_issues(self, username, reponame):
        return self._get_resources(('repos', username, reponame, 'issues'),
                Issue)


class ResponseError(Exception):
    """The API Response was unexpected."""

