# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from .forms import ProfileForm
from .models import UserProfile


@login_required
def profile(request):
    socaccounts = SocialAccount.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        profileform = ProfileForm(request.POST, instance=request.user)
        if profileform.is_valid():
            user = User.objects.get(id=request.user.id)
            user.first_name = profileform.cleaned_data['first_name']
            user.last_name = profileform.cleaned_data['last_name']
            user.save()
            request.user = user
            profile, isnew = UserProfile.objects.get_or_create(user_id=user)
            profile.scoutname = profileform.cleaned_data['scoutname']
            profile.socialaccount = profileform.cleaned_data['socialaccount']
            profile.save()
    else:
        initials = {}
        if hasattr(request.user, 'profile'):
            initials['scoutname'] = request.user.profile.scoutname
            initials['socialaccount'] = request.user.profile.socialaccount
        profileform = ProfileForm(
            instance=request.user,
            initial=initials)

    return render(request, 'profile.html', {
        'socaccounts': socaccounts,
        'profileform': profileform,
        })
