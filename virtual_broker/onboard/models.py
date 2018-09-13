# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Onboard(models.Model):
    user = models.ForeignKey(User, related_name='onboard')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    debts = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    computed = models.DecimalField(max_digits=30, decimal_places=2, null=True)

    def get_computed(self):
        result = self.debts + self.income
        return result

    def save(self, *args, **kwargs):
        self.computed = self.get_computed()
        super(Onboard,self).save(*args,**kwargs)

    def __str__(self):
        return self.user.username
