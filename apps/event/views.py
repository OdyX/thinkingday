# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import get_event_by_codename, EventMark
from .forms import AddEventMarkForm
from apps.comments.models import Comment


def map(request, event_codename=None):
    event = get_event_by_codename(event_codename)
    dt_now = timezone.now()
    if dt_now < event.start:
        return render(request, 'event_not_started.html', {
                'event': event,
            })
    elif dt_now > event.end:
        assert False, 'event\'s over'

    if request.method == 'POST' and request.user.is_authenticated():
        aemform = AddEventMarkForm(request.POST, event=event)
        if aemform.is_valid():
            em = EventMark()
            em.event = event
            em.point = aemform.cleaned_data['point']
            em.user = request.user
            em.save()
            cm = Comment()
            cm.eventmark = em
            cm.user = em.user
            cm.message = aemform.cleaned_data['message']
            cm.save()
            # Cleanup form and re-start
            aemform = AddEventMarkForm(event=event)
    else:
        aemform = AddEventMarkForm(event=event)

    return render(request, 'map.html', {
            'event': event,
            'aemform': aemform,
            })


@never_cache
def points(request, event_codename=None):
    event = get_event_by_codename(event_codename)
    marks = EventMark.objects.filter(event=event, event_messages__isnull=False)
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


@never_cache
def messages(request, event_codename=None, point_id=None):
    try:
        event = get_event_by_codename(event_codename)
        mark = EventMark.objects.get(event=event, id=point_id)
        messages = mark.event_messages.order_by('datetime').all()
    except:
        raise PermissionDenied()

    jdata = {}
    jdata['count'] = messages.count()
    jdata['point_id'] = point_id
    jdata['messages'] = [m.as_dict() for m in messages]

    return HttpResponse(json.dumps(jdata, indent=2),
        content_type='application/json')