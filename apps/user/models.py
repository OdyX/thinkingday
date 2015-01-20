# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from allauth.socialaccount.models import SocialAccount


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    socialaccount = models.ForeignKey(SocialAccount,
        blank=True, null=True, unique=True)
    scoutname = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user_scoutname())

    class Meta:
        db_table = 'user_profile'


def user_scoutname(self):
    if self.profile.scoutname:
        return self.profile.scoutname
    elif self.first_name and self.last_name:
        return u'{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name
            )
    else:
        return self.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
User.__unicode__ = user_scoutname