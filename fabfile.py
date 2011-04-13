# -*- coding: utf-8 -*-

import os
from fabric.api import *


DOCS_URL = 'https://gist.github.com/raw/71c2878f53e886dc921a/'


def get_docs():
    """Removed Trashcan.
    """
    os.chdir('ext')
    os.system('curl -s -O {0}{1}'.format(DOCS_URL, 'general.md'))
    os.system('curl -s -O {0}{1}'.format(DOCS_URL, 'issue_comments.md'))
    os.system('curl -s -O {0}{1}'.format(DOCS_URL, 'issues.md'))
    os.system('curl -s -O {0}{1}'.format(DOCS_URL, 'labels.md'))
    os.system('curl -s -O {0}{1}'.format(DOCS_URL, 'milestones.md'))

