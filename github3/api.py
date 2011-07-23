# -*- coding: utf-8 -*-

"""
github3.api
~~~~~~~~~~~

This module provies the core GitHub3 API interface.
"""

import omnijson as json

from .helpers import is_collection, to_python, to_api, get_scope
from .config import settings

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


    def _to_map(self, obj, iterable):
        """Maps given dict iterable to a given Resource object."""

        a = []

        for it in iterable:
            a.append(obj.new_from_dict(it, rdd=self))

        return a


    def _get_resources(self, key, obj, limit=None, **kwargs):
        """GETs resources of given path, maps them to objects, and
        handles paging.
        """
        pass


    def _get_resource(self, http_resource, obj, **kwargs):
        """GETs API Resource of given path."""

        item = self._get_http_resource(http_resource, params=kwargs)
        item = self._resource_deserialize(item)

        return obj.new_from_dict(item, rdd=self)


    def _post_resource(self, http_resource, **kwargs):
        """POSTs API Resource of given path."""

        r = self._post_http_resource(http_resource, params=kwargs)

        return r

    def _delete_resource(self, http_resource):
        """DELETEs API Resource of given path."""

        r = self._delete_http_resource(http_resource)

        if r['status'] in ('200', '204'):
            return True
        else:
            return False



class Github(GithubCore):
    """docstring for Github"""

    def __init__(self):
        super(Github, self).__init__()




class ResponseError(Exception):
    """The API Response was unexpected."""

