#!/usr/bin/env python

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

from setuptools import setup

# the name of the package
name = 'nbclient'

local_path = os.path.dirname(__file__)
here = os.path.abspath(local_path)


def read(path):
    with open(path) as fhandle:
        return fhandle.read()


def read_reqs(fname):
    req_path = os.path.join(here, fname)
    return [req.strip() for req in read(req_path).splitlines() if req.strip()]


long_description = read(os.path.join(os.path.dirname(__file__), "README.md"))
requirements = read(os.path.join(os.path.dirname(__file__), "requirements.txt"))
dev_reqs = read_reqs(os.path.join(os.path.dirname(__file__), 'requirements-dev.txt'))
doc_reqs = read_reqs(os.path.join(os.path.dirname(__file__), 'docs/requirements-doc.txt'))
extras_require = {"test": dev_reqs, "sphinx": doc_reqs}

setup(
    name=name,
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='https://jupyter.org',
    description=(
        "A client library for executing notebooks. Formerly nbconvert's ExecutePreprocessor."
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['nbclient'],
    include_package_data=True,
    python_requires=">=3.7.0",
    install_requires=requirements,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'jupyter-execute = nbclient.cli:main',
        ],
    },
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
