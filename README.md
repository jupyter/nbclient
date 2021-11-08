[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter/nbclient/master?filepath=binder%2Frun_nbclient.ipynb)
[![Build Status](https://github.com/jupyter/nbclient/workflows/CI/badge.svg)](https://github.com/jupyter/nbclient/actions)
[![Documentation Status](https://readthedocs.org/projects/nbclient/badge/?version=latest)](https://nbclient.readthedocs.io/en/latest/?badge=latest)
[![image](https://codecov.io/github/jupyter/nbclient/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbclient?branch=master)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# nbclient

**NBClient** lets you **execute** notebooks.

A client library for programmatic notebook execution, **NBClient** is a tool for running Jupyter Notebooks in
different execution contexts, including the command line.

## Interactive Demo

To demo **NBClient** interactively, click this Binder badge to start the demo:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter/nbclient/master?filepath=binder%2Frun_nbclient.ipynb)

## Installation

In a terminal, run:

    python3 -m pip install nbclient

## Documentation

See [ReadTheDocs](https://nbclient.readthedocs.io/en/latest/) for more in-depth details about the project and the
[API Reference](https://nbclient.readthedocs.io/en/latest/reference/index.html).


## Python Version Support

This library currently supports Python 3.6+ versions. As minor Python
versions are officially sunset by the Python org, nbclient will similarly
drop support in the future.

## Origins

This library used to be part of the [nbconvert](https://nbconvert.readthedocs.io/en/latest/) project. NBClient extracted nbconvert's `ExecutePreprocessor`into its own library for easier updating and importing by downstream libraries and applications.

## Relationship to JupyterClient

NBClient and JupyterClient are distinct projects.

`jupyter_client` is a client library for the jupyter protocol. Specifically, `jupyter_client` provides the Python API
for starting, managing and communicating with Jupyter kernels.

While, nbclient allows notebooks to be run in different execution contexts.
