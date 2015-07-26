

from .base import *

INSTALLED_APPS += ('django.contrib.admin',)

DEBUG = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    "./static/",
    )
