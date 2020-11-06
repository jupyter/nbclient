Welcome to nbclient
===================

.. image:: https://img.shields.io/github/stars/jupyter/nbclient?label=stars&style=social
   :alt: GitHub stars
   :target: https://github.com/jupyter/nbclient
.. image:: https://github.com/jupyter/nbclient/workflows/CI/badge.svg
   :alt: GitHub Actions
   :target: https://github.com/jupyter/nbclient/actions
.. image:: https://codecov.io/github/jupyter/nbclient/coverage.svg?branch=master
   :alt: CodeCov
   :target: https://codecov.io/github/jupyter/nbclient

---

**NBClient**, a client library for programmatic notebook execution, is a tool for running Jupyter Notebooks in
different execution contexts. NBClient was spun out of `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_'s
former ``ExecutePreprocessor``.

**NBClient** lets you **execute** notebooks.

Demo
----

To demo **NBClient** interactively, click the Binder link below:

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/jupyter/nbclient/master?filepath=binder%2Frun_nbclient.ipynb

Origins
-------

This library used to be part of `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_ and was extracted into its own
library for easier updating and importing by downstream libraries and
applications.

Python Version Support
----------------------

This library currently supports python 3.6+ verisons. As minor python
versions are officially sunset by the python org nbclient will similarly
drop support in the future.

Documentation
-------------

These pages guide you through the installation and usage of nbclient.

.. toctree::
   :maxdepth: 1
   :caption: Documentation

   installation
   client
   changelog


API Reference
-------------

If you are looking for information about a specific function, class, or method,
this documentation section will help you.

.. toctree::
   :maxdepth: 3
   :caption: Reference

   reference/index.rst
   reference/nbclient.tests.rst

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
