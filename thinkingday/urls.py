from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lang/', include('django.conf.urls.i18n')),
    url(r'^accounts/profile/$', 'apps.user.views.profile', name='user_profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^comments/', include('django_comments.urls')),
)

urlpatterns += i18n_patterns('',
    url(r'^$', 'thinkingday.views.home', name='home'),
    url(r'^thanks/$', 'thinkingday.views.thanks', name='thanks'),
    url(r'^(?P<event_codename>\w+)/', include('apps.event.urls')),
)
