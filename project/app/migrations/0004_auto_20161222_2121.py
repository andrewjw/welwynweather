# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161222_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearrow',
            name='max_hum_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yearrow',
            name='max_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yearrow',
            name='max_wind_gust',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yearrow',
            name='min_hum_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yearrow',
            name='min_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
