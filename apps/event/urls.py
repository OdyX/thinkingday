from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.event.views.map', name='map'),
    url(r'^messages.json$', 'apps.event.views.messages', name='messages'),
)
