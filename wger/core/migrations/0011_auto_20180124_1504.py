# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-24 12:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180124_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
