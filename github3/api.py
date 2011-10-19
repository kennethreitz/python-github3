# -*- coding: utf-8 -*-

"""
github3.api
~~~~~~~~~~~

This module provies the core GitHub3 API interface.
"""

from urlparse import urlparse, parse_qs

import requests
from decorator import decorator

from .packages import omnijson as json
from .packages.link_header import parse_link_value

from .models import *
from .helpers import is_collection, to_python, to_api, get_scope
from .config import settings




PAGING_SIZE = 100

class GithubCore(object):

    _rate_limit = None
    _rate_limit_remaining = None

    def __init__(self):
        self.session = requests.session()
        self.session.params = {'per_page': PAGING_SIZE}


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


    def _requests_post_hook(self, r):
        """Post-processing for HTTP response objects."""

        self._ratelimit = int(r.headers.get('x-ratelimit-limit', -1))
        self._ratelimit_remaining = int(r.headers.get('x-ratelimit-remaining', -1))

        return r


    def _http_resource(self, verb, endpoint, params=None, check_status=True, **etc):

        url = self._generate_url(endpoint)
        args = (verb, url)

        if params:
            kwargs = {'params': params}
            kwargs.update(etc)
        else:
            kwargs = etc

        r = self.session.request(*args, **kwargs)
        r = self._requests_post_hook(r)

        if check_status:
            r.raise_for_status()

        return r


    def _get_resource(self, resource, obj, **kwargs):

        r = self._http_resource('GET', resource, params=kwargs)
        item = self._resource_deserialize(r.content)

        return obj.new_from_dict(item, gh=self)

    def _patch_resource(self, resource, data, **kwargs):
        r = self._http_resource('PATCH', resource, data=data, params=kwargs)
        msg = self._resource_deserialize(r.content)

        return msg


    @staticmethod
    def _total_pages_from_header(link_header):

        if link_header is None:
            return link_header

        page_info = {}

        for link in link_header.split(','):

            uri, meta = map(str.strip, link.split(';'))

            # Strip <>'s
            uri = uri[1:-1]

            # Get query params from header.
            q = parse_qs(urlparse(uri).query)
            meta = meta[5:-1]

            page_info[meta] = q

        try:
            return int(page_info['last']['page'].pop())
        except KeyError:
            return True

    def _get_resources(self, resource, obj, limit=None, **kwargs):

        if limit is not None:
            assert limit > 0

        moar = True
        is_truncated = (limit > PAGING_SIZE) or (limit is None)
        r_count = 0
        page = 1

        while moar:

            if not is_truncated:
                kwargs['per_page'] = limit
                moar = False
            else:
                kwargs['page'] = page
                if limit:
                    if (limit - r_count) < PAGING_SIZE:
                        kwargs['per_page'] = (limit - r_count)
                        moar = False

            r = self._http_resource('GET', resource, params=kwargs)
            max_page = self._total_pages_from_header(r.headers['link'])

            if (max_page is True) or (max_page is None):
                moar = False

            d_items = self._resource_deserialize(r.content)

            for item in d_items:
                if (r_count < limit) or (limit is None):
                    r_count += 1
                    yield obj.new_from_dict(item, gh=self)
                else:
                    moar = False

            page += 1


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


    def get_me(self):
        """Get the authenticated user."""
        return self._get_resource(('user'), CurrentUser)

    def get_repo(self, username, reponame):
        """Get the given repo."""
        return self._get_resource(('repos', username, reponame), Repo)

    def get_org(self, login):
        """Get organization."""
        return self._get_resource(('orgs', login), Org)


class ResponseError(Exception):
    """The API Response was unexpected."""

