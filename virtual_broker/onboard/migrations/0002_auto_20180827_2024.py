# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-28 00:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onboard', to=settings.AUTH_USER_MODEL),
        ),
    ]