# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from allauth.socialaccount.models import SocialAccount


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    socialaccount = models.ForeignKey(SocialAccount,
        related_name='profile',
        blank=True, null=True, unique=True)
    scoutname = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
