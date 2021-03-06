# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthrow',
            name='avg_max_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthrow',
            name='avg_min_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthrow',
            name='avg_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthrow',
            name='max_hum_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthrow',
            name='max_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthrow',
            name='min_hum_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthrow',
            name='min_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
