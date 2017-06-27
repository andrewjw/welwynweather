# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-13 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20170410_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='climatebymonth',
            name='highest_low_temp_out_average',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebymonth',
            name='highest_low_temp_out_record',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebymonth',
            name='lowest_high_temp_out_average',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebymonth',
            name='lowest_high_temp_out_record',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebyyear',
            name='highest_low_temp_out_average',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebyyear',
            name='highest_low_temp_out_record',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebyyear',
            name='lowest_high_temp_out_average',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatebyyear',
            name='lowest_high_temp_out_record',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthrow',
            name='highest_low_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='monthrow',
            name='lowest_high_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yearrow',
            name='highest_low_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yearrow',
            name='lowest_high_temp_out',
            field=models.FloatField(blank=True, null=True),
        ),
    ]