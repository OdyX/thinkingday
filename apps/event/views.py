# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
from apps.event.models import Event
from django.core.exceptions import PermissionDenied


def map(request, event_codename):
    try:
        event = Event.objects.get(codename=event_codename)
    except:
        raise PermissionDenied()

    return render(request, 'map.html', {
            'event': event,
            })
