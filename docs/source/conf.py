# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Photo Tech & TMI'
copyright = 'Twoflower and Others, CC-BY-SA 4.0 or All right Reserved'
author = 'Twoflower and Others'

release = '42'
version = '42'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_extra_path = ['robots.txt']

# -- Options for EPUB output
epub_show_urls = 'footnote'
