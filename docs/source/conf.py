import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Expense Tracker'
copyright = '2025, Lethokuhle Shandu'
author = 'Lethokuhle Shandu'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # Auto-generate API docs from docstrings
    'sphinx.ext.napoleon',      # Support Google/NumPy style docstrings
    'sphinx.ext.viewcode',      # Add “View Source” links
    'sphinx.ext.intersphinx',   # Link to Python’s docs and others
    'sphinx.ext.todo',          # Support TODO directives
    'sphinx_copybutton',        # Add copy buttons to code blocks
]


templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}
html_static_path = ['_static']

# -- Options for Intersphinx ---------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Use light and dark syntax themes
pygments_style = "friendly"
pygments_dark_style = "native"

# Add custom static files (like CSS)
html_static_path = ['_static']

