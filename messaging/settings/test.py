# coding: utf-8
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SECRET_KEY = 'some secret key'

TEST_RUNNER = 'discover_runner.DiscoverRunner'
INSTALLED_APPS += (
    'discover_runner',
)
TEST_DISCOVER_TOP_LEVEL = REPOSITORY_PATH

# Speeding up the tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
