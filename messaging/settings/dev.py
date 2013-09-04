# coding: utf-8
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'development.db',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
