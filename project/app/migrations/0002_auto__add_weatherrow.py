# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WeatherRow'
        db.create_table('app_weatherrow', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('delay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('abs_pressure', self.gf('django.db.models.fields.FloatField')()),
            ('wind_ave', self.gf('django.db.models.fields.FloatField')()),
            ('wind_gust', self.gf('django.db.models.fields.FloatField')()),
            ('wind_dir', self.gf('django.db.models.fields.IntegerField')()),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
            ('raw_rain', self.gf('django.db.models.fields.FloatField')()),
            ('status', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['WeatherRow'])


    def backwards(self, orm):
        # Deleting model 'WeatherRow'
        db.delete_table('app_weatherrow')


    models = {
        'app.weatherrow': {
            'Meta': {'object_name': 'WeatherRow'},
            'abs_pressure': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'delay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hum_in': ('django.db.models.fields.FloatField', [], {}),
            'hum_out': ('django.db.models.fields.FloatField', [], {}),
            'rain': ('django.db.models.fields.FloatField', [], {}),
            'raw_rain': ('django.db.models.fields.FloatField', [], {}),
            'status': ('django.db.models.fields.FloatField', [], {}),
            'temp_in': ('django.db.models.fields.FloatField', [], {}),
            'temp_out': ('django.db.models.fields.FloatField', [], {}),
            'wind_ave': ('django.db.models.fields.FloatField', [], {}),
            'wind_dir': ('django.db.models.fields.IntegerField', [], {}),
            'wind_gust': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['app']