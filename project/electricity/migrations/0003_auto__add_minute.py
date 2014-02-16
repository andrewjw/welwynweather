# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Minute'
        db.create_table('electricity_minute', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('watts', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('electricity', ['Minute'])


    def backwards(self, orm):
        # Deleting model 'Minute'
        db.delete_table('electricity_minute')


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
        'electricity.minute': {
            'Meta': {'object_name': 'Minute'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'watts': ('django.db.models.fields.IntegerField', [], {})
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