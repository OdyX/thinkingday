# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
from apps.event.models import Event


def home(request):
    try:
        event = Event.objects\
            .untranslated()\
            .use_fallbacks()\
            .order_by('start')[0]
    except:
        event = None

    return render(request, 'home.html', {
                  'event': event
                  })
