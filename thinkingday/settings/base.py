"""
Django settings for thinkingday project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

import dj_database_url
from django.utils.translation import ugettext_lazy as _

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
    'django.core.context_processors.i18n',
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
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.angellist',
    #'allauth.socialaccount.providers.bitbucket',
    #'allauth.socialaccount.providers.bitly',
    #'allauth.socialaccount.providers.coinbase',
    #'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.flickr',
    #'allauth.socialaccount.providers.feedly',
    #'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.hubic',
    #'allauth.socialaccount.providers.instagram',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.linkedin_oauth2',
    #'allauth.socialaccount.providers.odnoklassniki',
    #'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.persona',
    #'allauth.socialaccount.providers.soundcloud',
    #'allauth.socialaccount.providers.stackexchange',
    #'allauth.socialaccount.providers.tumblr',
    #'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.vimeo',
    #'allauth.socialaccount.providers.vk',
    #'allauth.socialaccount.providers.weibo',
    #'allauth.socialaccount.providers.xing',
    'hvad',
)

# Project apps tested by jenkins (everything in apps/)
APPS_DIR = os.path.join(PROJECT_ROOT, 'apps')
PROJECT_APPS = ['apps.' + aname
                     for aname in os.listdir(APPS_DIR)
                     if os.path.isdir(os.path.join(APPS_DIR, aname))]

PROJECT_APPS += ['thinkingday']

INSTALLED_APPS = UPSTREAM_APPS + tuple(PROJECT_APPS)

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
    'default': dj_database_url.parse(get_env_variable('DATABASE_URL')),
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'fr'

LANGUAGES = (
    ('de', _('German')),
    ('fr', _('French')),
    ('it', _('Italian')),
    ('en', _('English')),
    )

TIME_ZONE = 'Europe/Zurich'

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

STATICFILES_LOCAL = False

# Email sender settings
SERVER_EMAIL = get_env_variable('SERVER_EMAIL', 'noreply@thinkingday.ch')
DEFAULT_FROM_EMAIL = get_env_variable('DEFAULT_FROM_EMAIL', 'noreply@thinkingday.ch')

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False  # For now

# Social accounts configuration
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}
