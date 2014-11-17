"""
WSGI config for thinkingday project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

from thinkingday import get_project_root_path, import_env_vars

import_env_vars(os.path.join(get_project_root_path(), 'envdir', 'local'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thinkingday.settings.base")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
