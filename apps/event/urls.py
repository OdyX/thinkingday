from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.event.views.map', name='map'),
    url(r'^points.json$', 'apps.event.views.points', name='points'),
    url(r'^(?P<point_id>\d+)?/messages.json$', 'apps.event.views.messages', name='messages'),
)
