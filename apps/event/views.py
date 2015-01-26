# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import get_event_by_codename, EventMark
from .forms import AddEventMarkForm


def map(request, event_codename=None):
    event = get_event_by_codename(event_codename)
    dt_now = timezone.now()
    if dt_now < event.start:
        return render(request, 'event_not_started.html', {
                'event': event,
            })
    elif dt_now > event.end:
        assert False, 'event\'s over'

    if request.method == 'POST':
        aemform = AddEventMarkForm(request.POST, event=event)
        if aemform.is_valid():
            em = EventMark()
            em.event = event
            em.point = aemform.cleaned_data['point']
            em.save()
            # TODO: Do someting smart with that new point
    aemform = AddEventMarkForm(event=event)

    return render(request, 'map.html', {
            'event': event,
            'aemform': aemform,
            })


@never_cache
def messages(request, event_codename=None):
    event = get_event_by_codename(event_codename)
    marks = EventMark.objects.filter(event=event)
    all_marks = {}
    if marks.count() > 0:
        all_marks['srid'] = marks[0].point.srid
        all_marks['data'] = []
        # Serialize the points for that event
        for mark in marks:
            that_mark = {}
            that_mark['id'] = mark.id
            that_mark['x'] = mark.point.x
            that_mark['y'] = mark.point.y
            all_marks['data'].append(that_mark)

    return HttpResponse(json.dumps(all_marks), content_type="application/json")