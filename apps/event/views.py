# -*- coding: utf-8 -*-
from django.utils import timezone
from django.shortcuts import render
from apps.event.models import get_event_by_codename


def map(request, event_codename=None):
    event = get_event_by_codename(event_codename)
    dt_now = timezone.now()
    if dt_now < event.start:
        return render(request, 'event_not_started.html', {
                'event': event,
            })
    elif dt_now > event.end:
        assert False, 'event\'s over'

    return render(request, 'map.html', {
            'event': event,
            })


def messages(request, event_codename=None):
    return render(request, 'map.html', {
            'event': get_event_by_codename(event_codename),
            })  # change to respond messages