from django import template
from django.conf import settings
from re import sub

register = template.Library()


@register.filter
def setlang(request, newlang):
    """ Replace language code in request.path with the new language code
    """
    return sub('^/(%s)/' % request.LANGUAGE_CODE,
               '/%s/' % newlang, request.path)


@register.filter
def resource_remotelocal(remoteurl):
    """ Return link for remote or static url for a file in ext/
    """
    if settings.STATICFILES_LOCAL:
        return settings.STATIC_URL + "ext/"
    else:
        return remoteurl
