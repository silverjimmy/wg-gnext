# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-07 09:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0022_schedulestep_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulestep',
            name='duration',
            field=models.IntegerField(default=4, help_text='The duration in weeks', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(52)], verbose_name='Duration'),
        ),
    ]