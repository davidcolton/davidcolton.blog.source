#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "David Colton"
SITENAME = "David's Blog"
SITESUBTITLE = "The ramblings of a frustated Python Data Scientist ..."
SITEIMAGE = "/images/python_programming.png width=150 height=150"
DISQUS_SITENAME = "davidcoltonblog"
# SITEURL = ""
SITEURL = "https://davidcolton.github.io"

PATH = "content"
OUTPUT_PATH = "../output"

THEME = "themes/pelican-alchemy/alchemy"
# THEME_CSS_OVERRIDES = ["jupyter.css"]

TIMEZONE = "Europe/Dublin"

DEFAULT_LANG = "en"

PLUGIN_PATHS = ["plugins/"]
PLUGINS = [
    "pelican-bootstrapify",
    "i18n_subsites",
    "pelican-ipynb.markup",
    "render_math",
]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

BOOTSTRAPIFY = {
    "table": ["table", "table-striped", "table-hover"],
    "img": ["img-fluid"],
    "blockquote": ["blockquote"],
}
BOOTSTRAP_THEME = "flatly"

PYGMENTS_STYLE = "manni"

ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]

MATH_JAX = {"color": "blue", "align": "center"}

STATIC_PATHS = ["extras", "images", "pdf"]
# For example
# ![python logo]({static}/img/python_icon.png)
# [Pelican Documenation]({static}/pdf/pelican.pdf)

EXTRA_PATH_METADATA = {
    "extras/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extras/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extras/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extras/browserconfig.xml": {"path": "browserconfig.xml"},
    "extras/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extras/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extras/favicon.ico": {"path": "favicon.ico"},
    "extras/manifest.json": {"path": "manifest.json"},
    "extras/mstile-150x150.png": {"path": "mstile-150x150.png"},
    "extras/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
}

RFG_FAVICONS = True

HIDE_AUTHORS = True

# Output format
ARTICLE_URL = "articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Python", "http://python.org/"), ("PyBites", "http://codechalleng.es/"))

ICONS = (
    ("twitter", "https://twitter.com/David__Colton"),
    ("github", "https://github.com/davidcolton/"),
    ("linkedin", "https://www.linkedin.com/in/davidcolton/"),
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/David__Colton"),
    ("Github", "https://github.com/davidcolton/"),
)

DEFAULT_PAGINATION = False

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "sitemap"]
SITEMAP_SAVE_AS = "sitemap.xml"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Adding Jupyter Notebooks Support
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True
IPYNB_SKIP_CSS = False
