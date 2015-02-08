# -*- coding: utf-8 -*-
from hvad.models import TranslatableModel, TranslatedFields
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models
from django.core.exceptions import PermissionDenied


class Event(TranslatableModel, models.Model):
    codename = models.CharField(max_length=256, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    translations = TranslatedFields(
        name=models.CharField(max_length=512),
        description=models.TextField(),
        subscription_motivator=models.TextField(),
    )

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.safe_translation_getter('name', str(self.pk))


class EventMark(models.Model):
    event = models.ForeignKey(Event, related_name="marks")
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='marks')

    point = models.PointField()
    objects = models.GeoManager()

    class Meta:
        verbose_name = _('Event mark')
        verbose_name_plural = _('Event marks')

    def __unicode__(self):
        return _(u'{id} - Point ({x}, {y}) created on {event}').format(
            id=self.id,
            x=self.point.x,
            y=self.point.y,
            event=self.event.codename,
            )


def get_event_by_codename(event_codename):
    try:
        # On-purpose fallback for incomplete translation DB-wise
        return Event.objects\
                .untranslated()\
                .use_fallbacks()\
                .get(codename=event_codename)
    except:
        # TODO: Better error handling
        raise PermissionDenied()
