# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Onboard(models.Model):
    user = models.ForeignKey(User, related_name='onboard') #error with user model being connected to onboard model
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    income = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
