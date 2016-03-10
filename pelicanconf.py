""" Settings file. """
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Volker Steuber'
SITENAME = u'UH Biocomputation Group'
#SITESUBTITLE = u'University of Hertfordshire, Hatfield, UK'

PATH = 'content'
STATIC_PATHS = ['images','files', 'extras/favicon.ico']
EXTRA_PATH_METADATA = {
        'extras/favicon.ico': {'path':'favicon.ico'}
}

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['tag_cloud']
PLUGINS = ['tag_cloud', 'share_post',]

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

ARTICLE_PATHS = ['']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Blogroll
#LINKS = (('UHBiocomputation on Github', 'https://github.com/UHBiocomputation'),
        #)

# Social widget
#GITHUB_URL = 'https://github.com/UHBiocomputation'
#SOCIAL = (('Github', 'https://github.com/UHBiocomputation'),
#         )


DEFAULT_PAGINATION = 10
THEME = "./pelican-theme-gum"

RELATIVE_URLS = False
INDEX_SAVE_AS = 'blog_index.html'

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'random'

DISPLAY_CATEGORIES_ON_MENU = False

# Minor customization to make some info appear on our home page
#CUSTOM_POST_ON_HOME_PAGE = 'Please check the <a href="blog_index.html">news page</a> for information on an open PhD studentship that is currently available at the Biocomputation group.'
LATEST_ARTICLE_ON_HOME_PAGE = True
