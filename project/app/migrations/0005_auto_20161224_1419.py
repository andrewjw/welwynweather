# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161222_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayrow',
            name='data_quality',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthrow',
            name='data_quality',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]
