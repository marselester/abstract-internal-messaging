# coding: utf-8
"""Settings that are the same for both development and production."""
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPOSITORY_DIR = os.path.dirname(BASE_DIR)

# Allow all host headers
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djcelery',
    'gunicorn',

    'messaging.apps.account',
    'messaging.apps.message',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'messaging.urls'

WSGI_APPLICATION = 'messaging.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)


MESSAGE_APP_REDIS_URL = 'redis://localhost:6379'
MESSAGE_APP_REDIS_DB = 0

BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_DISABLE_RATE_LIMITS = True

import djcelery
djcelery.setup_loader()


LOGIN_REDIRECT_URL = '/'
