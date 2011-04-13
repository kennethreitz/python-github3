# -*- coding: utf-8 -*-

import os
from fabric.api import *


DOCS_URL = 'https://gist.github.com/raw/71c2878f53e886dc921a/general.md'


def get_docs():
    """Removed Trashcan.
    """
    os.chdir('ext')
    os.system('curl -O {0}'.format(DOCS_URL))

