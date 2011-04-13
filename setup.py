#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# from distutils.core import setup
from setuptools import setup, find_packages

import clint



def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

required = ['requests==0.3.1']

setup(
    name='github3',
    version='0.0.1',
    description='Python wrapper for the github v3 api!',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/python-github3',
    packages= find_packages('github3'),
    install_requires=required,
    license='ISC',
    classifiers=(
#       'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
