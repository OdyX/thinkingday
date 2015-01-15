from . import get_env_variable
from .base import *  # noqa

DEBUG = bool(get_env_variable('DEBUG', True))
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = 'notsosecret'
NEVERCACHE_KEY = 'notsosecret'

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

STATICFILES_LOCAL = get_env_variable('STATICFILES_LOCAL', True)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}

INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Print all emails into the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'