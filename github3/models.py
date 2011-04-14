# -*- coding: utf-8 -*-

"""
github3.models
~~~~~~~~~~~~~~

This module provides the GitHub3 object models.

"""



class User(object):
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



class Repo(object):
    """GitHub Repository."""
    pass



class Gist(object):
    """GitHub Gist.

    gist.files['filename.py']
    """

    def __init__(self):
        pass



class GistComment(object):
    """GitHub GistComment."""

    def __init__(self):
        pass


class Issue(object):


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
        self.milestone
        self.assignee



class Milestone(object):


    def __init__(self):pass

