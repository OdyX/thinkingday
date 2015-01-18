# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
from apps.event.models import Event

def map(request):
    try:
        event = Event.objects\
            .untranslated()\
            .use_fallbacks()\
            .order_by('start')[0]
    except:
        event = None

    return render(request, 'map.html', {
            'event': event,
            })
