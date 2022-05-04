#!/usr/bin/env python3
#
# nbclient documentation build configuration file, created by
# sphinx-quickstart on Mon Jan 26 16:00:00 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import shutil
import sys

import nbclient

sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    # 'autodoc_traits',  # TODO
    'myst_parser',
]

autodoc_mock_imports = ['pytest', 'nbconvert', 'testpath']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'nbclient'
copyright = '2020, Project Jupyter'
author = 'Project Jupyter'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The short X.Y version.
version = '.'.join(nbclient.__version__.split('.')[0:2])

# The full version, including alpha/beta/rc tags.
release = nbclient.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line foexitr these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'UPDATE.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

default_role = 'any'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/jupyter/nbclient",
    "repository_branch": "master",
    "use_edit_page_button": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
# html_sidebars = {}

html_title = "nbclient"

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'nclientdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, 'nbclient.tex', 'nbclient Documentation', 'jupyter team', 'manual')]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'nbclient', 'nbclient Documentation', [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'nbclient',
        'nbclient Documentation',
        author,
        'nbclient',
        'One line description of project.',
        'Miscellaneous',
    )
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}


def setup(app):
    HERE = os.path.abspath(os.path.dirname(__file__))
    dest = os.path.join(HERE, 'changelog.md')
    shutil.copy(os.path.join(HERE, '..', 'CHANGELOG.md'), dest)

    autogen_config = os.path.join(HERE, "autogen_config.py")
    prev_dir = os.getcwd()
    os.chdir(HERE)
    with open(autogen_config) as f:
        exec(compile(f.read(), autogen_config, "exec"), {})
        print('Updated cli docs')
    os.chdir(prev_dir)
