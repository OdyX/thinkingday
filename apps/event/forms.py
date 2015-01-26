# -*- coding: utf-8 -*-
from django.contrib.gis import forms


class TDOSMWidget(forms.OSMWidget):
    def __init__(self, *args, **kwargs):
        super(TDOSMWidget, self).__init__(*args, **kwargs)

    class Media:
        # Override to use cloudflare's JS CDN
        extend = False
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js',
            'http://www.openstreetmap.org/openlayers/OpenStreetMap.js',
            'gis/js/OLMapWidget.js',
        )


class AddEventMarkForm(forms.Form):
    point = forms.PointField(widget=TDOSMWidget())
    event = False

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        # TODO: Use the event to create the center
        super(AddEventMarkForm, self).__init__(*args, **kwargs)