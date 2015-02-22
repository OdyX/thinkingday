# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ungettext, ugettext as _
from django.contrib.gis.db import models
from apps.event.models import EventMark
from django.utils import timezone

COMMENT_MAX_LENGTH = getattr(settings, 'COMMENT_MAX_LENGTH', 3000)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_messages')
    eventmark = models.ForeignKey(EventMark, related_name='event_messages')
    datetime = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=COMMENT_MAX_LENGTH)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def as_dict(self):
        selfdict = {}
        selfdict['id'] = self.id
        # Display in the system's timezone
        #selfdict['datetime'] = timezone.localtime(self.datetime).strftime('%c')
        selfdict['datetime'] = date_diff(self.datetime)
        selfdict['message'] = self.message
        selfdict['user'] = self.user.__unicode__()
        selfdict['avatar'] = self.user.profile.get_avatar_url()
        return selfdict

    def __unicode__(self):
        return u'{user} commented \'{message}\' on point {pointid}'.format(
            user=self.user,
            message=self.message,
            pointid=self.eventmark.id
            )


def date_diff(d):
    # https://djangosnippets.org/snippets/1409/ - adapted
    now = timezone.now()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = now - d
    delta_midnight = today - d
    days = delta.days
    hours = round(delta.seconds / 3600., 0)
    minutes = round(delta.seconds / 60., 0)
    chunks = (
        (365.0, lambda n: ungettext('year', 'years', n)),
        (30.0, lambda n: ungettext('month', 'months', n)),
        (7.0, lambda n: ungettext('week', 'weeks', n)),
        (1.0, lambda n: ungettext('day', 'days', n)),
    )
    if days == 0:
        if hours == 0:
            if minutes > 0:
                return ungettext('1 minute ago',
                    '%(minutes)d minutes ago', minutes) % {'minutes': minutes}
            else:
                return _("less than 1 minute ago")
        else:
            return ungettext('1 hour ago', '%(hours)d hours ago', hours) \
            % {'hours': hours}

    if delta_midnight.days == 0:
        return _("yesterday at %s") % d.strftime("%H:%M")

    count = 0
    for i, (chunk, name) in enumerate(chunks):
        if days >= chunk:
            count = round((delta_midnight.days + 1) / chunk, 0)
            break

    return _('%(number)d %(type)s ago') % \
        {'number': count, 'type': name(count)}