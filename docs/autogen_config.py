#!/usr/bin/env python
"""
autogen_config.py

Create config_options.rst, a Sphinx documentation source file.
Documents the options that may be set in nbconvert's configuration file,
jupyter_nbconvert_config.py.

"""
import os
import os.path

from nbclient.cli import NbClientApp

header = """\

.. This is an automatically generated file.
.. do not modify by hand.

.. _other-full-config:

Config file and command line options
====================================
Jupyter ``nbclient`` can be run with a variety of command line arguments.
A list of available options can be found below in the :ref:`options section
<options>`.

.. _options:

Options
-------
This list of options can be generated by running the following and hitting
enter::

  $ jupyter execute --help-all

"""

try:
    indir = os.path.dirname(__file__)
except NameError:
    indir = os.getcwd()

destination = os.path.join(indir, "reference/config_options.rst")

with open(destination, "w") as f:
    app = NbClientApp()
    f.write(header)
    f.write(app.document_config_options())
