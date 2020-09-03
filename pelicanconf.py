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

PLUGIN_PATHS = ['pelican-plugins', 'pelican-plugins-other']
PLUGINS = ['tag_cloud', 'share_post', 'pelican-bibtex']

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

TAG_CLOUD_STEPS = 6
TAG_CLOUD_MAX_ITEMS = 30
TAG_CLOUD_SORTING = 'random'

DISPLAY_CATEGORIES_ON_MENU = False

# Minor customization to make some info appear on our home page
# CUSTOM_POST_ON_HOME_PAGE = '<br /><a href="category/vacancies"><i class="icon-attention"></i>Please check the vacancies section for information on an open Lecturer or Senior Lecturer position at the School of Computer Science.</a>'
LATEST_ARTICLE_ON_HOME_PAGE = True

# Bibliography and publications
MY_PUBLICATIONS_SRC = 'content/labpubs.bib'
PUBLICATIONS_SAVE_AS = 'pages/04-publications.html'
DIRECT_TEMPLATES = ['index', 'archives', 'categories', 'tags', 'publications', 'authors']

# Need to do it manually to maintain an order
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Research', '/pages/02-research.html'),
    ('People', '/pages/03-people.html'),
    ('Publications', '/pages/04-publications.html'),
    ('Seminars', '/pages/05-seminars.html'),
    ('Collaborators', '/pages/06-collaborators.html'),
    ('CNS*2019 Workshop', '/pages/2019-cns-workshop.html'),
    ('CS Research Colloquium', 'https://cs-colloq.cs.herts.ac.uk/'),
             )
