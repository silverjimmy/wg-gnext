# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-25 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180125_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuser',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
