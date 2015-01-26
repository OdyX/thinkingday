# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from .models import get_event_by_codename, EventMark


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
    event = get_event_by_codename(event_codename)
    marks = EventMark.objects.filter(event=event)
    all_marks = []
    # Serialize the points for that event
    for mark in marks:
        that_mark = {}
        that_mark['id'] = mark.id
        that_mark['x'] = mark.point.x
        that_mark['y'] = mark.point.x
        all_marks.append(that_mark)
    return HttpResponse(json.dumps(all_marks), content_type="application/json")