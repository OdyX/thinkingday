# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
from django.contrib.auth.models import User
from apps.user.forms import RegisterForm


def home(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User()
            user.email = form.cleaned_data['email']
            #user.username = form.cleaned_data['email']
            user.save()
    else:
        form = RegisterForm()

    return render(request, 'home.html', {
            'form': form
            })
