#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

import github3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

required = ['requests>=0.8.6', 'python-dateutil==1.5']


setup(
    name='github3',
    version=github3.__version__,
    description='Github API Wrapper.',
    long_description=open('README.rst').read(), # + '\n\n' +
                     # open('HISTORY.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/python-github3',
    packages=['github3'],
    package_data={'': ['LICENSE',]},
    include_package_data=True,
    install_requires=required,
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
