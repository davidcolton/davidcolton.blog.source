#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "David Colton"
SITENAME = "David Colton's Blog"
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "../output"

THEME = "theme"

TIMEZONE = "Europe/Dublin"

DEFAULT_LANG = "en"

PLUGIN_PATHS = ["plugins/"]
PLUGINS = ["i18n_subsites"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

BOOTSTRAP_THEME = "flatly"

PYGMENTS_STYLE = "monokai"

ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]

STATIC_PATHS = ["images", "pdf"]
# For example
# ![python logo]({static}/img/python_icon.png)
# [Pelican Documenation]({static}/pdf/pelican.pdf)

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
LINKS = (
    ("Python.org", "http://python.org/"),
    ("PyBites", "http://codechalleng.es/"),
    ("Pelican", "http://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/David__Colton"),
    ("Github", "https://github.com/davidcolton/"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

