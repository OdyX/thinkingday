# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
from django.contrib.auth.models import User
from apps.user.forms import RegisterForm
from apps.event.models import Event
from django.conf import settings


def home(request):
    try:
        event = Event.objects.untranslated()\
        .use_fallbacks(settings.LANGUAGE_CODE).order_by('start')[0]
    except:
        event = None

    return render(request, 'home.html', {
            'event': event
            })
