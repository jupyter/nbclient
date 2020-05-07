#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
from setuptools import setup

# the name of the package
name = 'nbclient'

local_path = os.path.dirname(__file__)
# Fix for tox which manipulates execution pathing
if not local_path:
    local_path = '.'
here = os.path.abspath(local_path)


def version():
    with open(here + '/nbclient/_version.py', 'r') as ver:
        for line in ver.readlines():
            if line.startswith('version ='):
                return line.split(' = ')[-1].strip()[1:-1]
    raise ValueError('No version found in nbclient/version.py')


def read(path):
    with open(path, 'r') as fhandle:
        return fhandle.read()


def read_reqs(fname):
    req_path = os.path.join(here, fname)
    return [req.strip() for req in read(req_path).splitlines() if req.strip()]


long_description = read(os.path.join(os.path.dirname(__file__), "README.md"))
requirements = read(os.path.join(os.path.dirname(__file__), "requirements.txt"))
dev_reqs = read_reqs(os.path.join(os.path.dirname(__file__), 'requirements-dev.txt'))
doc_reqs = read_reqs(os.path.join(os.path.dirname(__file__), 'docs/requirements-doc.txt'))
extras_require = {"test": dev_reqs, "dev": dev_reqs, "sphinx": doc_reqs}

setup(
    name=name,
    version=version(),
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='https://jupyter.org',
    description="A client library for executing notebooks. Formally nbconvert's ExecutePreprocessor.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['nbclient'],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require=extras_require,
    project_urls={
        'Documentation': 'https://nbclient.readthedocs.io',
        'Funding': 'https://numfocus.org/',
        'Source': 'https://github.com/jupyter/nbclient',
        'Tracker': 'https://github.com/jupyter/nbclient/issues',
    },
    license='BSD',
    platforms="Linux, Mac OS X, Windows",
    keywords=['jupyter', 'pipeline', 'notebook', 'executor'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
