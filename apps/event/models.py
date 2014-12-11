from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _


class Event(TranslatableModel):
    codename = models.CharField(max_length=256, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    translations = TranslatedFields(
        name=models.CharField(max_length=512),
        description=models.TextField(),
    )

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.safe_translation_getter('name', str(self.pk))
