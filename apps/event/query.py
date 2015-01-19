# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect

def messages(request):
    return render(request, 'map.html') # change to respond messages
