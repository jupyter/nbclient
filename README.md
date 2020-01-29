[![Travis Build Status](https://travis-ci.org/jupyter/nbclient.svg?branch=master)](https://travis-ci.org/jupyter/nbclient)
[![image](https://codecov.io/github/jupyter/nbclient/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbclient?branch=master)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# nbclient

A client library for executing notebooks. Formally nbconvert's ExecutePreprocessor.

**NBClient** is a tool for parameterizing and executing Jupyter Notebooks.

NBClient lets you:

    **execute** notebooks

Similar in nature to jupyter_client, as the jupyter_client is to the jupyter
protocol nbclient is to notebooks allowing for execution contexts to be run.

## Origins

This library used to be part of [nbconvert](https://nbconvert.readthedocs.io/en/latest/) and was extracted into its own library for easier updating and importing by downstream libraries and applications.

## Python Version Support

This library currently supports python 3.5+ verisons. As minor python
versions are officially sunset by the python org nbclient will similarly
drop support in the future.

## Documentation

See [readthedocs](https://nbclient.readthedocs.io/en/latest/) for more in-depth details about the project and API capabilities.
