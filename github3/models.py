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
        self.type = None
        self.email = None
        self.location = None
        self.name = None
        self.company = None
        self.login = None
        self.blog = None
        self.gravatar_url = None



class Repo(GitHubModel):
    """GitHub Repository."""
    pass



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

