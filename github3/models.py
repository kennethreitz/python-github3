# -*- coding: utf-8 -*-

"""
github3.models
~~~~~~~~~~~~~~

This module provides the GitHub3 object models.

"""


class GitHubModel(object):

    def __init__(self):
        pass



class User(GitHubModel):
    pass

    def __init__(self):
        self.email = None,
        self.type = None,
        self.url = None,
        self.login = None,
        self.created_at = None,
        self.gravatar_url = None
        self.blog = None,
        self.name = None,
        self.company = None,
        self.location = None

    def __repr__(self):
        return '<user \'{0}\''.format(self.name)

    def from_dict(self, d):
        self.email = d.get('email', None),
        self.type = d.get('type', None),
        self.url = d.get('url', None),
        self.login = d.get('login', None),
        self.created_at = d.get('created_at', None),
        self.gravatar_url = d.get('gravatar_url', None),
        self.blog = d.get('blog', None),
        self.name = d.get('name', None),
        self.company = d.get('company', None),
        self.location = d.get('location', None)






class Repo(GitHubModel):
    """GitHub Repository."""

    def __init__(self):
        self.has_downloads = None,
        self.forks = None,
        self.url = None,
        self.created_at = None,
        self.watchers = None,
        self.description = None,
        self.master_branch = None,
        self.has_wiki = None,
        self.open_issues = None,
        self.fork = None,
        self.html_url = None,
        self.homepage = None,
        self.has_issues = None,
        self.pushed_at = None,
        self.language = None,
        self.private = None,
        self.size = None,
        self.integrate_branch = None,
        self.owner = None,
        self.name = None

    def __repr__(self):
        return '<repo \'{0}/{1}\''.format(self.owner, self.name)

    def from_dict(self, d):
        self.has_downloads = d.get('has_downloads', None),
        self.forks = d.get('forks', None),
        self.url = d.get('url', None),
        self.created_at = d.get('created_at', None),
        self.watchers = d.get('watchers', None),
        self.description = d.get('description', None),
        self.master_branch = d.get('master_branch', None),
        self.has_wiki = d.get('has_wiki', None),
        self.open_issues = d.get('open_issues', None),
        self.fork = d.get('fork', None),
        self.html_url = d.get('html_url', None),
        self.homepage = d.get('homepage', None),
        self.has_issues = d.get('has_issues', None),
        self.pushed_at = d.get('pushed_at', None),
        self.language = d.get('language', None),
        self.private = d.get('private', None),
        self.size = d.get('size', None),
        self.integrate_branch = d.get('integrate_branch', None),
        self.owner = User()
        self.owner.from_dict(d.get('owner', dict()))
        self.name = d.get('name', None),



class Gist(GitHubModel):
    """GitHub Gist.

    gist.files['filename.py']
    """

    def __init__(self):
        self.api_url = None



class GistComment(GitHubModel):
    """GitHub GistComment."""

    def __init__(self):
        pass


class Issue(GitHubModel):


    def __init__(self):
        self.number = None
        self.updated_at = None
        self.closed_at = None
        self.labels = []
        self.title= None
        self.comments = []
        self.user = None
        self.body = None
        self.url = None
        self.state = None
        self.api_url = None

        # api
        self.milestone = None
        self.assignee = None



class Milestone(GitHubModel):

    def __init__(self):
        self.api_url = None

