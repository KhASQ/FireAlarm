from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _
from datetime import date
from django.contrib import admin
import os


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	home_owner_first_name = models.CharField(max_length=50, default='')
	home_owner_mid_name = models.CharField(max_length=50, default='')
	home_owner_last_name = models.CharField(max_length=50, default='')
	home_owner_phone = models.CharField(max_length=9, default='')
	fire_date = models.DateField(_("Date"), default=date.today)
	location_image_url = models.TextField(default='')
	is_admin = models.BooleanField(default=False)

    def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


if omar > 0:
