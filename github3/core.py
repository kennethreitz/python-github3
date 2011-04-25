# -*- coding: utf-8 -*-

"""
github3.core
~~~~~~~~~~~~

This module contains the core GitHub 3 interface.

"""


from .api import API_URL, get
import json
import models
# TODO: switch to anyjson


class GitHub(object):
    """Central GitHub object."""

    rate_limit = None
    rate_left = None
    per_page = 30
    accept = 'application/vnd.github.v3+json'

    def __init__(self, apiurl=API_URL):
        self.__basic_auth = None


    def _get(self, *path, **kwargs):
        """optional json=False, paged=False"""

        headers = {'Accept': self.accept}

        is_json = kwargs.get('json', False)
        is_paged = kwargs.get('paged', False)

        r = get(*path, auth=self.__basic_auth, headers=headers)

        rate_left = r.headers.get('x-ratelimit-remaining', None)
        rate_limit = r.headers.get('x-ratelimit-limit', None)

        if (rate_limit is not None) or (rate_left is not None):
            self.rate_limit = rate_limit
            self.rate_left = rate_left

        if is_json:
            r = json.loads(r.content)

        if is_paged:
            pass
            # TODO: paged support (__iter__)
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

        if r.status_code == 200 and self.__basic_auth:
            return True
        else:
            return False

    def repo(self, username, reponame):
        d = self._get('repos', username, '{0}.json'.format(reponame), json=True)


        repo = models.Repo()
        repo.from_dict(d)

        return repo


# {
#   "has_downloads": true,
#   "forks": 10,
#   "url": "https://api.github.com/repos/kennethreitz/requests.json",
#   "created_at": "2011-02-13T18:38:17Z",
#   "watchers": 166,
#   "description": "Python HTTP modules suck. This one doesn't.",
#   "master_branch": "develop",
#   "has_wiki": true,
#   "open_issues": 5,
#   "fork": false,
#   "html_url": "https://github.com/kennethreitz/requests",
#   "homepage": "http://pypi.python.org/pypi/requests/",
#   "has_issues": true,
#   "pushed_at": "2011-04-21T21:39:45Z",
#   "language": "Python",
#   "private": false,
#   "size": 2748,
#   "integrate_branch": null,
#   "owner": {
#     "email": "_@kennethreitz.com",
#     "type": "User",
#     "url": "https://api.github.com/users/kennethreitz.json",
#     "login": "kennethreitz",
#     "created_at": "2009-08-26T21:17:47Z",
#     "gravatar_url": "https://secure.gravatar.com/avatar/2eccc4005572c1e2b12a9c00580bc86f?s=30&d=https://d3nwyuy0nl342s.cloudfront.net%2Fimages%2Fgravatars%2Fgravatar-140.png",
#     "blog": "http://kennethreitz.com",
#     "name": "Kenneth Reitz",
#     "company": "NetApp, Inc",
#     "location": "Washington, DC"
#   },
#   "name": "requests"
# }

# Default instance
github = GitHub()