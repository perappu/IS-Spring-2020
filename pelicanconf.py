#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazimir Fodor'
SITENAME = 'IS 2020'
SITEURL = 'https://stokori.github.io/IS-Spring-2020/'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True