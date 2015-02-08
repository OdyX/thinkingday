# -*- coding: utf-8 -*-
from django.contrib.gis import forms


class TDOSMWidget(forms.OSMWidget):
    template_name = 'TDOSMwidget.html'

    class Media:
        # Override to use cloudflare's JS CDN
        extend = False
        js = ()


class AddEventMarkForm(forms.Form):
    point = forms.PointField(widget=TDOSMWidget())
    event = False

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')
        # TODO: Use the event to create the center
        super(AddEventMarkForm, self).__init__(*args, **kwargs)