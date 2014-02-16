# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RealTime'
        db.create_table('electricity_realtime', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')()),
            ('watts', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('electricity', ['RealTime'])

        # Adding model 'Monthly'
        db.create_table('electricity_monthly', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('kwh', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('electricity', ['Monthly'])

        # Adding model 'Hourly'
        db.create_table('electricity_hourly', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('kwh', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('electricity', ['Hourly'])

        # Adding model 'Daily'
        db.create_table('electricity_daily', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('kwh', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('electricity', ['Daily'])


    def backwards(self, orm):
        # Deleting model 'RealTime'
        db.delete_table('electricity_realtime')

        # Deleting model 'Monthly'
        db.delete_table('electricity_monthly')

        # Deleting model 'Hourly'
        db.delete_table('electricity_hourly')

        # Deleting model 'Daily'
        db.delete_table('electricity_daily')


    models = {
        'electricity.daily': {
            'Meta': {'object_name': 'Daily'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'kwh': ('django.db.models.fields.FloatField', [], {})
        },
        'electricity.hourly': {
            'Meta': {'object_name': 'Hourly'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'kwh': ('django.db.models.fields.FloatField', [], {})
        },
        'electricity.monthly': {
            'Meta': {'object_name': 'Monthly'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'kwh': ('django.db.models.fields.FloatField', [], {})
        },
        'electricity.realtime': {
            'Meta': {'object_name': 'RealTime'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'temperature': ('django.db.models.fields.FloatField', [], {}),
            'watts': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['electricity']