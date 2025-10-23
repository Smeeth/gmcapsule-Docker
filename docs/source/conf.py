# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'GmCapsule Docker'
copyright = f'2025, Eibo Richter'
author = 'Eibo Richter'
release = '1.0.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',              # Markdown support
    'sphinx.ext.autodoc',       # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',      # Google/NumPy docstring style
    'sphinx.ext.viewcode',      # Add links to source code
    'sphinx.ext.intersphinx',   # Link to other project's documentation
    'sphinx.ext.todo',          # Support for todo items
    'sphinx_copybutton',        # Add copy button to code blocks
    'sphinxcontrib.mermaid',    # Mermaid diagram support
    'sphinx_tabs.tabs',         # Tabbed content
]

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
]

# Source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Templates
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = None
html_favicon = None

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Custom CSS
html_css_files = [
    'custom.css',
]

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

latex_documents = [
    (master_doc, 'gmcapsule-docker.tex', 'GmCapsule Docker Documentation',
     author, 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, 'gmcapsule-docker', 'GmCapsule Docker Documentation',
     [author], 1)
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_exclude_files = ['search.html']

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'docker': ('https://docker-py.readthedocs.io/en/stable/', None),
}

# -- Extension configuration -------------------------------------------------
todo_include_todos = True
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
