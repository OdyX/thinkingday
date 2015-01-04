from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import Event


class EventAdmin(TranslatableAdmin):
    pass

admin.site.register(Event, EventAdmin)
