from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


class Event(TranslatableModel):
    codename = models.CharField(max_length=256, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    translations = TranslatedFields(
        name=models.CharField(max_length=512),
        description=models.TextField(),
    )

    def __unicode__(self):
        return self.safe_translation_getter('name', str(self.pk))
