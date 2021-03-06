# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-08-21 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170613_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='NestSensors',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('avg_temp', models.FloatField()),
                ('avg_humidity', models.FloatField()),
                ('max_pir', models.FloatField()),
                ('max_nearPir', models.FloatField(blank=True, null=True)),
                ('min_ch1', models.FloatField(blank=True, null=True)),
                ('max_ch1', models.FloatField(blank=True, null=True)),
                ('min_ch2', models.FloatField(blank=True, null=True)),
                ('max_ch2', models.FloatField(blank=True, null=True)),
                ('min_als', models.FloatField()),
                ('max_als', models.FloatField()),
                ('min_tp0', models.FloatField()),
                ('max_tp0', models.FloatField()),
                ('min_tp1', models.FloatField()),
                ('max_tp1', models.FloatField()),
                ('min_tp2', models.FloatField()),
                ('max_tp2', models.FloatField()),
                ('min_tp3', models.FloatField()),
                ('max_tp3', models.FloatField()),
            ],
        ),
    ]
