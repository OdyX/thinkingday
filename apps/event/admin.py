from django.contrib.gis import admin
from hvad.admin import TranslatableAdmin
from .models import Event, EventMark


class EventAdmin(TranslatableAdmin):
    pass


class EventMarkAdmin(admin.OSMGeoAdmin):
    # Environ Milieu du rectangle contenant la Suisse
    default_lon = 915792.035884697
    default_lat = 5918996.831547979
    default_zoom = 7

admin.site.register(Event, EventAdmin)
admin.site.register(EventMark, EventMarkAdmin)
