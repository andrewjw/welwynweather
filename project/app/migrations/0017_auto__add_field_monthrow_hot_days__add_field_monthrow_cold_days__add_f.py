# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MonthRow.hot_days'
        db.add_column('app_monthrow', 'hot_days',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'MonthRow.cold_days'
        db.add_column('app_monthrow', 'cold_days',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'MonthRow.rain_days'
        db.add_column('app_monthrow', 'rain_days',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MonthRow.hot_days'
        db.delete_column('app_monthrow', 'hot_days')

        # Deleting field 'MonthRow.cold_days'
        db.delete_column('app_monthrow', 'cold_days')

        # Deleting field 'MonthRow.rain_days'
        db.delete_column('app_monthrow', 'rain_days')


    models = {
        'app.climatemonth': {
            'Meta': {'object_name': 'ClimateMonth'},
            'cold_days_average': ('django.db.models.fields.IntegerField', [], {}),
            'cold_days_record': ('django.db.models.fields.IntegerField', [], {}),
            'days_of_rain_average': ('django.db.models.fields.IntegerField', [], {}),
            'days_of_rain_record': ('django.db.models.fields.IntegerField', [], {}),
            'hot_days_average': ('django.db.models.fields.IntegerField', [], {}),
            'hot_days_record': ('django.db.models.fields.IntegerField', [], {}),
            'max_temp_in_average': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_in_record': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out_average': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out_record': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_in_average': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_in_record': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out_average': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out_record': ('django.db.models.fields.FloatField', [], {}),
            'month': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'month_rain_average': ('django.db.models.fields.FloatField', [], {}),
            'month_rain_record': ('django.db.models.fields.FloatField', [], {}),
            'rain_average': ('django.db.models.fields.FloatField', [], {}),
            'rain_record': ('django.db.models.fields.FloatField', [], {}),
            'wind_ave_average': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_ave_record': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_gust_average': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_gust_record': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'app.coldestperiodrecord': {
            'Meta': {'ordering': "['-length']", 'object_name': 'ColdestPeriodRecord'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        },
        'app.dayrow': {
            'Meta': {'ordering': "['date']", 'object_name': 'DayRow'},
            'abs_pressure': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'max_hum_in': ('django.db.models.fields.FloatField', [], {}),
            'max_hum_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_temp_in': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_wind_gust': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_hum_in': ('django.db.models.fields.FloatField', [], {}),
            'min_hum_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_temp_in': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rain': ('django.db.models.fields.FloatField', [], {}),
            'rained': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'wind_ave': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_dir': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        },
        'app.driestperiodrecord': {
            'Meta': {'ordering': "['-length']", 'object_name': 'DriestPeriodRecord'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        },
        'app.heaviestrainrecord': {
            'Meta': {'ordering': "['-rain']", 'object_name': 'HeaviestRainRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'rain': ('django.db.models.fields.FloatField', [], {})
        },
        'app.highestpressurerecord': {
            'Meta': {'ordering': "['-pressure']", 'object_name': 'HighestPressureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {})
        },
        'app.highesttemperaturerecord': {
            'Meta': {'ordering': "['-temperature']", 'object_name': 'HighestTemperatureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'db_index': 'True'})
        },
        'app.hourrow': {
            'Meta': {'ordering': "['date']", 'object_name': 'HourRow'},
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
            'Meta': {'ordering': "['pressure']", 'object_name': 'LowestPressureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'pressure': ('django.db.models.fields.FloatField', [], {})
        },
        'app.lowesttemperaturerecord': {
            'Meta': {'ordering': "['temperature']", 'object_name': 'LowestTemperatureRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indoor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'temperature': ('django.db.models.fields.FloatField', [], {'db_index': 'True'})
        },
        'app.monthrow': {
            'Meta': {'object_name': 'MonthRow'},
            'cold_days': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'delay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hot_days': ('django.db.models.fields.IntegerField', [], {}),
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
            'rain_days': ('django.db.models.fields.IntegerField', [], {})
        },
        'app.strongestgustrecord': {
            'Meta': {'ordering': "['-speed']", 'object_name': 'StrongestGustRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        'app.strongestwindrecord': {
            'Meta': {'ordering': "['-speed']", 'object_name': 'StrongestWindRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        'app.warmestperiodrecord': {
            'Meta': {'ordering': "['-length']", 'object_name': 'WarmestPeriodRecord'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        },
        'app.weatherrow': {
            'Meta': {'ordering': "['date']", 'object_name': 'WeatherRow'},
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
            'Meta': {'ordering': "['-rain']", 'object_name': 'WettestDayRecord'},
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
            'rain': ('django.db.models.fields.FloatField', [], {})
        },
        'app.wettestperiodrecord': {
            'Meta': {'ordering': "['-length']", 'object_name': 'WettestPeriodRecord'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['app']