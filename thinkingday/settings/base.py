"""
Django settings for thinkingday project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

import dj_database_url

from . import get_env_variable
from .. import get_project_root_path
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


PROJECT_ROOT = get_project_root_path()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(get_env_variable('DEBUG', False))
TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'thinkingday/templates'),
)

ALLOWED_HOSTS = tuple(get_env_variable('ALLOWED_HOSTS', '').splitlines())


# Application definition

UPSTREAM_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'hvad',
)

# Project apps tested by jenkins (everything in apps/)
APPS_DIR = os.path.join(PROJECT_ROOT, 'apps')
PROJECT_APPS = tuple(['apps.' + aname
                     for aname in os.listdir(APPS_DIR)
                     if os.path.isdir(os.path.join(APPS_DIR, aname))])

INSTALLED_APPS = UPSTREAM_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'thinkingday.urls'

WSGI_APPLICATION = 'thinkingday.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(get_env_variable('DATABASE_URL'))
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = (
    ('fr', 'French'),
    ('de', 'German'),
    ('it', 'Italian'),
    ('en', 'English'),
    )

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# This allows you to put project-wide translations in the "locale" directory of
# your project
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = get_env_variable('STATIC_ROOT',
                               os.path.join(PROJECT_ROOT, 'static_files'))

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    'thinkingday/statics',
)

COMPRESS_PARSER = 'compressor.parser.Html5LibParser'
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_OFFLINE = True

COMPRESS_PRECOMPILERS = (
    ('text/less',
        os.path.join(
            get_env_variable('VIRTUAL_ENV',
                             os.path.join(PROJECT_ROOT, 'venv')),
            'bin', 'lesscpy') + ' {infile}'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter'
    ]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
    ]

SITE_ID = 1