from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.event.views.map', name='map'),
    url(r'^messages/$', 'apps.event.views.messages', name='messages'),
)
