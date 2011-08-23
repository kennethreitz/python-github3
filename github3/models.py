"""
github3.models
~~~~~~~~~~~~~~

This module provides the Github3 object model.
"""

from .helpers import to_python, to_api


class BaseResource(object):
    """A BaseResource object."""

    _strs = []
    _ints = []
    _dates = []
    _bools = []
    _map = {}
    _writeable = []
    _modified = []


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

        for attr in (self._strs + self._ints + self._dates + self._bools + self._map.keys()):
            setattr(self, attr, None)


    @classmethod
    def new_from_dict(cls, d, gh=None):

        return to_python(
            obj=cls(), in_dict=d,
            str_keys = cls._strs,
            int_keys = cls._ints,
            date_keys = cls._dates,
            bool_keys = cls._bools,
            object_map = cls._map,
            _gh = gh
        )

    def update(self):
        pass

    def setattr(self, k, v):
        # TODO: when writable key changed,
        pass


class Plan(BaseResource):
    """Github Plan object model."""

    _strs = ['name']
    _ints = ['space', 'collaborators', 'private_repos']

    def __repr__(self):
        return '<plan {0}>'.format(str(self.name))



class User(BaseResource):
    """Github User object model."""

    _strs = [
        'login','gravatar_url', 'url', 'name', 'company', 'blog', 'location',
        'email', 'bio', 'html_url']

    _ints = ['id', 'public_repos', 'public_gists', 'followers', 'following']
    _dates = ['created_at',]
    _bools = ['hireable', ]
    # _map = {}
    # _writeable = []

    def __repr__(self):
        return '<user {0}>'.format(self.login)

    def repos(self):
         # return self._gh.get_repos(username=self.login)
         repos = self._gh._get_resources(('users', self.login, 'repos'), Repo)
         return repos


class Organization(User):

    _bools = []

    def __repr__(self):
        return '<org {0}>'.format(self.login)

    def repos(self, repo_type="all"):
         repos = self._gh._get_resources(('orgs', self.login, 'repos'), Repo,
                 type=repo_type)
         return repos


class CurrentUser(User):
    """Github Current User object model."""

    _ints = [
        'id', 'public_repos', 'public_gists', 'followers', 'following',
        'total_private_repos', 'owned_private_repos', 'private_gists',
        'disk_usage', 'collaborators']
    _map = {'plan': Plan}
    _writeable = ['name', 'email', 'blog', 'company', 'location', 'hireable', 'bio']

    def __repr__(self):
        return '<current-user {0}>'.format(self.login)


class Repo(BaseResource):
    _strs = [
        'url', 'html_url', 'clone_url', 'git_url', 'ssh_url', 'svn_url',
        'name', 'description', 'homepage', 'language', 'master_branch']
    _bools = ['private', 'fork']
    _ints = ['forks', 'watchers', 'size',]
    _dates = ['pushed_at', 'created_at']
    _map = {'owner': User}

    def __repr__(self):
        return '<repo {0}/{1}>'.format(self.owner.login, self.name)

    def issues(self, **params):
        return self._gh._get_resources(('repos', self.owner.login,
            self.name, 'issues'), Issue, **params)

    def milestones(self, **params):
        return self._gh._get_resources(('repos', self.owner.login,
            self.name, 'milestones'), Milestone, **params)


class IssueLabel(BaseResource):
    _strs = ['url', 'name', 'color']

    def __repr__(self):
        return '<label {0}>'.format(self.name)


class Milestone(BaseResource):
    _strs = ['url', 'state', 'title', 'description']
    _ints = ['number', 'open_issues', 'closed_issues']
    _dates = ['created_at', 'due_on']
    _map = {'creator': User}

    def __repr__(self):
        return '<milestone {0}-{1}>'.format(self.number, self.title)


class Issue(BaseResource):
    _map = {'assignee': User, 'user': User, 'milestone': Milestone,
            'labels': IssueLabel}
    _ints = ['number', 'comments']
    _strs = ['url', 'html_url', 'body', 'title', 'state']
    _dates = ['closed_at', 'created_at', 'updated_at']

    @property
    def repo_user(self):
        return self.url.split('/')[-4]

    @property
    def repo_name(self):
        return self.url.split('/')[-3]

    @property
    def repo_full(self):
        return '/'.join((self.repo_user, self.repo_name))

    def __repr__(self):
        return '<issue {0}/{1}-{2}>'.format(self.repo_user, self.repo_name,
                                            self.number)
