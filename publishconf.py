""" Publish settings."""
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#SITEURL = 'http://homepages.stca.herts.ac.uk/~nngroup/'
SITEURL = 'http://biocomputation.herts.ac.uk'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/categories/{slug}.atom.xml'
TAG_FEED_ATOM = 'feeds/tags/{slug}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/authors/{slug}.atom.xml'
FEED_MAX_ITEMS = 30

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
