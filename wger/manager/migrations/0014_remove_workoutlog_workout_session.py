# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-30 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20180130_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutlog',
            name='workout_session',
        ),
    ]