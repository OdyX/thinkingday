# -*- coding: utf-8 -*-
from django.shortcuts import render  # , redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount


@login_required
def profile(request):
    socaccounts = SocialAccount.objects.filter(user_id=request.user.id)
    return render(request, 'profile.html', {'socaccounts': socaccounts})
