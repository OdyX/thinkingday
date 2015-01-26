from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.event.views.map', name='map'),
    url(r'^points.json$', 'apps.event.views.messages', name='points'),
)
