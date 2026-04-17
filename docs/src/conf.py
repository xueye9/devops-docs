# Configuration file for the Sphinx documentation builder.

# -- Project information

project = u'DevOps 规划'
copyright = u'2026, 薛冰冰'
author = u'薛冰冰'
version = '0.1.0'
release = '0.1'

# -- General configuration
source_suffix = '.rst'
master_doc = 'contents'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for EPUB output
epub_show_urls = 'footnote'