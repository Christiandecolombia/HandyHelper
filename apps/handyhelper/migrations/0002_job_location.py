# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-19 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handyhelper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
