# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'YagDrive'
copyright = '2021'
author = 'Sergio Delgado Quintero'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx.ext.napoleon', 'sphinx_panels', 'sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ['css/custom.css']

html_theme_options = {
    'use_download_button': False,
    'extra_navbar': '',
}

html_title = ''
html_logo = '_static/img/yagdrive-logo.svg'
html_favicon = '_static/img/yagdrive-favicon.png'

# MyST

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]

panels_add_bootstrap_css = False
myst_heading_anchors = 3

myst_substitutions = {
    'pypi': '[![PyPI badge]'
    '(https://img.shields.io/pypi/v/yagdrive)]'
    '(https://pypi.org/project/yagdrive/)',
    'github': '[![GitHub badge]'
    '(https://img.shields.io/github/stars/sdelquin/yagdrive?style=social)]'
    '(https://github.com/sdelquin/yagdrive/)',
}

# autodoc

autodoc_mock_imports = ['pydrive', 'mimetype_description']
