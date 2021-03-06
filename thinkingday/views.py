# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render, redirect
from django.utils import timezone
from apps.user.forms import EmailOnlyForm
from apps.event.models import Event
from allauth.account.utils import send_email_confirmation


def home(request):
    try:
        qs = Event.objects.untranslated().use_fallbacks()
        try:
            today = datetime.now()
            event = qs.filter(start__gte=now).first()
        except:
            event = qs.order_by('start').last()
    except:
        event = None

    if request.method == 'POST':
        form = EmailOnlyForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            send_email_confirmation(request, user)
            return redirect('thanks')

    form = EmailOnlyForm()

    if event:
        dt_now = timezone.now()
        if dt_now > event.start and dt_now < event.end:
            return redirect('map', event_codename=event.codename)

    return render(request, 'home.html', {
            'event': event,
            'form': form,
            'current_page': 'home',
            })


def thanks(request):
    return render(request, 'registration_thanks.html')