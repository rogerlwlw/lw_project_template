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
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

import recommonmark
from recommonmark.transform import AutoStructify


#%% -- Project information -----------------------------------------------------

project = 'project_lib'
copyright = '2020, rogerluo'
author = 'rogerluo'

# The full version, including alpha/beta/rc tags
from project_lib import __version__
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__


#%% -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# The master toctree document.
master_doc = 'index'
# The files to include

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
]

# source_suffix
# The file extensions of source files. Sphinx considers the files 
# with this suffix as sources. The value can be a dictionary mapping 
# file extensions to file types. For example:

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# source_parsers
# If given, a dictionary of parser classes for different source suffices. 
# The keys are the suffix, the values can be either a class or a string giving 
# a fully-qualified name of a parser class. The parser class can be either 
# docutils.parsers.Parser or sphinx.parsers.Parser. Files with a suffix that 
# is not in the dictionary will be parsed with the default reStructuredText 
# parser.


# master_doc
# The document name of the “master” document, that is, 
# the document that contains the root toctree directive. 
# Default is 'index'.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']



# rst_epilog
# A string of reStructuredText that will be included at the 
# end of every source file that is read. This is a possible 
# place to add substitutions that should be available in every 
# file (another being rst_prolog). An example:

# rst_epilog = """
# .. |psf| replace:: Rogerluo open source lib
# """


# rst_prolog
# A string of reStructuredText that will be included at the beginning 
# of every source file that is read. This is a possible place to add 
# substitutions that should be available in every file
#  (another being rst_epilog). An example:

# rst_prolog = """
# .. |psf| replace:: Python Software Foundation
# """


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None


#%% -- Options for autodoc -------------------------------------------------
# generate autosummary even if no references
autosummary_generate = True

autodoc_default_flags = ['members', 'inherited-members']

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'project_lib_doc'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']