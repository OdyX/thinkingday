# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.user.forms import EmailOnlyForm
from apps.event.models import Event


def home(request):
    try:
        event = Event.objects\
            .untranslated()\
            .use_fallbacks()\
            .order_by('start')[0]
    except:
        event = None

    form = EmailOnlyForm()

    return render(request, 'home.html', {
            'event': event,
            'form': form,
            'current_page': 'home',
            })


def thanks(request):
    return render(request, 'registration_thanks.html')