""" Settings file. """
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dr. Volker Steuber'
SITENAME = u'UH Biocomputation Group'

PATH = 'content'
STATIC_PATHS = ['images','files']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Disclaimer', 'http://homepages.stca.herts.ac.uk/~nngroup/disclaimer.php'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
THEME = "./pelican-theme-gum"

RELATIVE_URLS = False
INDEX_SAVE_AS = 'blog_index.html'
