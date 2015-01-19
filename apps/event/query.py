# -*- coding: utf-8 -*-
import json
from django.shortcuts import render  # , redirect
from django.http import HttpResponse

def messages(request):
    return render(request, 'map.html') # change to respond messages
