# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-07 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0024_schedulestep_use_periodization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulestep',
            name='use_periodization',
            field=models.BooleanField(default=False, help_text='If checked your workout duration will be categorized based on available cycles'),
        ),
    ]