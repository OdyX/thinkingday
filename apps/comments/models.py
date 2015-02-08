# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models
#from django.core.exceptions import PermissionDenied
from apps.event.models import EventMark

COMMENT_MAX_LENGTH = getattr(settings, 'COMMENT_MAX_LENGTH', 3000)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_messages')
    eventmark = models.ForeignKey(EventMark, related_name='event_messages')
    datetime = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=COMMENT_MAX_LENGTH)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __unicode__(self):
        return '{user} commented \'{message}\' on a point'.format(
            user=self.user,
            message=self.message
            )