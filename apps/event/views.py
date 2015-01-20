# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.event.models import get_event_by_codename


def map(request, event_codename):
    return render(request, 'map.html', {
            'event': get_event_by_codename(event_codename),
            })


def messages(request, event_codename):
    return render(request, 'map.html', {
            'event': get_event_by_codename(event_codename),
            })  # change to respond messages