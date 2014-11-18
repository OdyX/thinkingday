# -*- coding: utf-8 -*-
# from django.shortcuts import render  # , redirect
from django.http import HttpResponseRedirect


def home(request):
    # Redirect to scout.ch temporarily
    return HttpResponseRedirect('http://www.scouts.ch/')
    # return render(request, 'home.html')
