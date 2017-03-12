# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_yearrow_data_quality'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayrow',
            name='bad_rows',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayrow',
            name='good_rows',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthrow',
            name='bad_rows',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthrow',
            name='good_rows',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
