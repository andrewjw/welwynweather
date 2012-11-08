# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DayRow.delay'
        db.delete_column('app_dayrow', 'delay')


        # Changing field 'DayRow.wind_dir'
        db.alter_column('app_dayrow', 'wind_dir', self.gf('django.db.models.fields.TextField')(max_length=255))
        # Deleting field 'HourRow.is_raining'
        db.delete_column('app_hourrow', 'is_raining')

        # Adding field 'HourRow.rained'
        db.add_column('app_hourrow', 'rained',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DayRow.delay'
        db.add_column('app_dayrow', 'delay',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'DayRow.wind_dir'
        db.alter_column('app_dayrow', 'wind_dir', self.gf('django.db.models.fields.IntegerField')())
        # Adding field 'HourRow.is_raining'
        db.add_column('app_hourrow', 'is_raining',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'HourRow.rained'
        db.delete_column('app_hourrow', 'rained')


    models = {
        'app.dayrow': {
            'Meta': {'object_name': 'DayRow'},
            'abs_pressure': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'max_hum_in': ('django.db.models.fields.FloatField', [], {}),
            'max_hum_out': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_in': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out': ('django.db.models.fields.FloatField', [], {}),
            'max_wind_gust': ('django.db.models.fields.FloatField', [], {}),
            'min_hum_in': ('django.db.models.fields.FloatField', [], {}),
            'min_hum_out': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_in': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out': ('django.db.models.fields.FloatField', [], {}),
            'rain': ('django.db.models.fields.FloatField', [], {}),
            'rained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'wind_ave': ('django.db.models.fields.FloatField', [], {}),
            'wind_dir': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        'app.driestperiodrecord': {
            'Meta': {'object_name': 'DriestPeriodRecord'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        },
        'app.heaviestrainrecord': {
            'Meta': {'object_name': 'HeaviestRainRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'rain': ('django.db.models.fields.FloatField', [], {})
        },
        'app.highestpressurerecord': {
            'Meta': {'object_name': 'HighestPressureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {})
        },
        'app.highesttemperaturerecord': {
            'Meta': {'object_name': 'HighestTemperatureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'temperature': ('django.db.models.fields.FloatField', [], {})
        },
        'app.hourrow': {
            'Meta': {'object_name': 'HourRow'},
            'abs_pressure': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'hum_in': ('django.db.models.fields.FloatField', [], {}),
            'hum_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rain': ('django.db.models.fields.FloatField', [], {}),
            'rained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'temp_in': ('django.db.models.fields.FloatField', [], {}),
            'temp_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_ave': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_dir': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'wind_gust': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'app.lowestpressurerecord': {
            'Meta': {'object_name': 'LowestPressureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {})
        },
        'app.lowesttemperaturerecord': {
            'Meta': {'object_name': 'LowestTemperatureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'temperature': ('django.db.models.fields.FloatField', [], {})
        },
        'app.monthrow': {
            'Meta': {'object_name': 'MonthRow'},
            'abs_pressure': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'delay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_hum_in': ('django.db.models.fields.FloatField', [], {}),
            'max_hum_out': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_in': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out': ('django.db.models.fields.FloatField', [], {}),
            'max_wind_gust': ('django.db.models.fields.FloatField', [], {}),
            'min_hum_in': ('django.db.models.fields.FloatField', [], {}),
            'min_hum_out': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_in': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out': ('django.db.models.fields.FloatField', [], {}),
            'rain': ('django.db.models.fields.FloatField', [], {}),
            'rained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'wind_ave': ('django.db.models.fields.FloatField', [], {}),
            'wind_dir': ('django.db.models.fields.IntegerField', [], {})
        },
        'app.strongestgustrecord': {
            'Meta': {'object_name': 'StrongestGustRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        'app.strongestwindrecord': {
            'Meta': {'object_name': 'StrongestWindRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        'app.weatherrow': {
            'Meta': {'object_name': 'WeatherRow'},
            'abs_pressure': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'delay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hum_in': ('django.db.models.fields.FloatField', [], {}),
            'hum_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'is_raining': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rain': ('django.db.models.fields.FloatField', [], {}),
            'raw_rain': ('django.db.models.fields.FloatField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'temp_in': ('django.db.models.fields.FloatField', [], {}),
            'temp_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_ave': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wind_gust': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'app.wettestdayrecord': {
            'Meta': {'object_name': 'WettestDayRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'rain': ('django.db.models.fields.FloatField', [], {})
        },
        'app.wettestperiodrecord': {
            'Meta': {'object_name': 'WettestPeriodRecord'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']