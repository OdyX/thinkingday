from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

urlpatterns = patterns('',
    url(r'^$', 'apps.event.views.map', name='map'),
    url(r'^messages$', 'apps.event.query.messages', name='messages'),
)
