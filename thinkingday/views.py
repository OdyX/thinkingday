# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
#from django.http import Http404


def home(request):
    return render(request, 'home.html')
