# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 23:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]