# Configuration file for the Sphinx documentation builder.
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'GmCapsule Docker'
copyright = f'{datetime.now().year}, Eibo Richter'
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
    'sphinx_copybutton',        # Add copy button to code blocks
    'sphinx_design',            # Cards, tabs, grids, etc.
]

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",      # ::: fences
    "deflist",          # Definition lists
    "fieldlist",        # Field lists
    "substitution",     # Variable substitutions
    "tasklist",         # Task lists with checkboxes
    "attrs_inline",     # Inline attributes {.class}
    "attrs_block",      # Block attributes
]

# Support both RST and Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Templates and exclusions
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Custom CSS
html_css_files = [
    'custom.css',
]

# -- Options for LaTeX/PDF output --------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

latex_documents = [
    (master_doc, 'gmcapsule-docker.tex', 'GmCapsule Docker Documentation',
     author, 'manual'),
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
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# Suppress warnings for missing references
suppress_warnings = ['ref.myst']
