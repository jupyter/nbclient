#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

# the name of the package
name = 'nbclient'

def read(path):
    with open(path) as f:
        return f.read()

long_description = read(os.path.join(os.path.dirname(__file__), "README.md"))
requirements = read(os.path.join(os.path.dirname(__file__), "requirements.txt"))

setup(
    name="nbclient",
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='https://jupyter.org',
    description="A client library for executing notebooks. Formally nbconvert's ExecutePreprocessor.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['nbclient'],
    include_package_data=True,
    python_requires=">=3.5,
    install_requires=requirements,
    extras_require={"test": ["tox"]},
    project_urls={
        'Documentation': 'TODO',
        'Funding'      : 'https://numfocus.org/',
        'Source'       : 'https://github.com/jupyter/nbclient',
        'Tracker'      : 'https://github.com/jupyter/nbclient/issues',
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)


if __name__ == '__main__':
    setup(**setup_args)
