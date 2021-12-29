# -*- coding: utf-8 -*-

##
## Sphinx configuration file
##

import os
from pathlib import Path

##
## Project data
##

project = 'replab-sandbox'
copyright = '2018-2021, Denis Rosset, Jean-Daniel Bancal and collaborators'
author = 'Denis Rosset, Jean-Daniel Bancal and collaborators'
version = Path('../../version.txt').read_text().strip()
release = version
html_title = 'RepLAB Sandbox'
html_base_url = 'https://replab.github.io/sandbox/'

##
## Extensions
##

extensions = [
    'sphinx.ext.autodoc',     # for enumeration of objects stuff
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'nbsphinx',
#    'sphinxcontrib.bibtex',   # academic references
    'sphinx_togglebutton',
#    'sphinxcontrib.fulltoc',  # for sidebar TOC
    'sphinxcontrib.matlab',   # support for Matlab
    'sphinx.ext.napoleon',    # support for shorthand syntax
    'sphinx.ext.mathjax',     # LaTeX support
    'texext.math_dollar',     # lightweight LaTeX filter
    'sphinx.ext.intersphinx', # cross references
    'sphinx_design',          # for panels
]

##
## Misc settings
##

templates_path = ["_templates"]
primary_domain = 'mat'
default_role = 'obj'
source_suffix = '.rst' # The suffix(es) of source filenames.
master_doc = 'index' # The master toctree document.
language = None # The language for content autogenerated by Sphinx
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints', '**_source.ipynb', '_src'] # List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
pygments_style = 'sphinx' # The name of the Pygments (syntax highlighting) style to use.

##
## Autodoc settings
##

autodoc_default_options = {'members': True, 'show-inheritance': True}
autosummary_generate = True

##
## Matlab domain settings
##

matlab_keep_package_prefix = False
matlab_src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__ + "/")))+"/src"

##
## sphinxcontrib.bibtex
##

#bibtex_bibfiles = ['refs.bib']

##
## sphinx.ext.intersphinx
##

intersphinx_mapping = {'api': ('https://replab.github.io/api', None),
                       'web': ('https://replab.github.io/web', None)}
intersphinx_cache_limit = -1 # always fetch the latest version
intersphinx_timeout = 10 # timeout so we don't wait indefinitely if the website is unavailable

##
## nbsphinx / notebook execution
##

import jupytext
nbsphinx_kernel_name = 'octave'
nbsphinx_custom_formats = {
    '.m': lambda s: jupytext.reads(s, fmt='m:light'),
}

##
## HTML template
##

import guzzle_sphinx_theme

html_show_sourcelink = True

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

html_static_path = ['_static']

# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": html_title,
    "base_url": html_base_url
}

html_css_files = [
    'css/custom.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css'
]

html_js_files = [
    'js/collapse_helper.js',
]

html_sidebars = {
    '**': ['logo-text.html', 'globaltoc.html']
}
