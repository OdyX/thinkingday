# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect

def map(request):
    return render(request, 'map.html')
