#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Duarte Pompeu'
#~ SITEURL = u'http://localhost:8000'
SITENAME = u"Pompas blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'CS Student'
SITEDESCRIPTION = u'%s\'s Projects and References' % AUTHOR
SITELOGO = u"http://duarte-pompeu.github.io/res/profile.png"

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = [
    # ...
    #~ 'pelican_fontawesome',
    'pelicanfly',
    # ...
]

# Blogroll
#~ LINKS = (('Pelican', 'http://getpelican.com/'),
         #~ ('Python.org', 'http://python.org/'),
         #~ ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (("github", "https://www.github.com/duarte-pompeu"),
          ("linkedin", "https://linkedin.com/in/duartepompeu"),
          ("envelope-o", "mailto:mail@duartepompeu.com"),)
# work around to be able to make html
STATIC_PATHS = [
    'extra/main.css',
]
EXTRA_PATH_METADATA = {
    'extra/main.css': {'path': 'theme/css/main.css'},
}

DEFAULT_PAGINATION = 10
THEME="Flex"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
