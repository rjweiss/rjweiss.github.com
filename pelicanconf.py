#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rebecca Weiss'
SITENAME = u'Rebecca Weiss'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'

# Pelican Plugins stuff
PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['liquid_tags.notebook', 'rmd_reader']
PLUGINS = ['liquid_tags.notebook', 'rmd_reader']

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css', 'drafts/figure']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

# For IPython Notebooks
#EXTRA_HEADER = open('_nb_header_minimal.html').read().decode('utf-8')
NOTEBOOK_DIR = 'notebooks'

CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'readable'

# CC_LICENSE="CC-BY"
# DISPLAY_RECENT_POSTS_ON_SIDEBAR=True

# Blogroll - disabled for now
#LINKS =  (('Political Communication Laboratory', 'http://pcl.stanford.edu/'),
#          ('Stanford Comm', 'http://comm.stanford.edu/'),)

# Social widget - disabled for now
#SOCIAL = (('Github', 'www.github.com/rjweiss'),)
# SOCIAL = (('linkedin', 'http://www.linkedin.com/in/rjweiss'),
          # ('github', 'www.github.com/rjweiss'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# pelican-bootstrap3
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = True
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False
SITELOGO = 'images/rjw_2013-8-17.jpg'
SITELOGO_SIZE = '90%'
# BOOTSTRAP_NAVBAR_INVERSE = True
# BOOTSTRAP_NAVBAR_FIXEDTOP = False	

# ABOUT_ME = "I'm the jam."
# AVATAR = 'images/rjw_2013-8-17.jpg'

#Disqus stuff
DISQUS_SITENAME = 'rebeccaweissinfo'
#DISQUS_DISPLAY_COUNTS = 

#Google Analytics stuff
GOOGLE_ANALYTICS = 'UA-39179035-2'

#Github stuff
GITHUB_URL = 'http://www.github.com/rjweiss'
GITHUB_USER = 'rjweiss'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True