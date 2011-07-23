"""
github3.models
~~~~~~~~~~~~~~

This module provides the Github3 object model.
"""

from .helpers import to_python, to_api


class BaseResource(object):
    """A BaseResource object."""

    _strings = []
    _ints = []
    _datetimes = []
    _booleans = []
    _map = {}


    def __init__(self):
        self._bootstrap()
        super(BaseResource, self).__init__()


    def __dir__(self):
        d = self.__dict__.copy()

        try:
            del d['_gh']
        except KeyError:
            pass

        return d.keys()


    def _bootstrap(self):
        """Bootstraps the model object based on configured values."""

        for attr in (self._strings + self._ints + self._datetimes + self._booleans + self._map.keys()):
            setattr(self, attr, None)

    @classmethod
    def new_from_dict(cls, d, gh=None):

        return to_python(
            obj=cls(), in_dict=d,
            string_keys = cls._strings,
            date_keys = cls._datetimes,
            _gh = gh
        )


class User(BaseResource):
    """Github User object model."""

    _strings = ['login', 'gravatar_url', 'url', 'name', 'company',
        'blog', 'location', 'email', 'bio', 'html_url']

    _ints = ['id', 'public_repos', 'public_gists', 'followers', 'following']
    _datetimes = ['created_at',]
    _booleans = ['hireable', ]
    _map = {}


    def __init__(self):
        super(User, self).__init__()

    def __repr__(self):
        return '<user {0}>'.format(self.login)