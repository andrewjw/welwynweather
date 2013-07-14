# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClimateByYear'
        db.create_table('app_climatebyyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('max_temp_in_record', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_in_record', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_in_average', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_in_average', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_out_record', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_out_record', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_out_average', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_out_average', self.gf('django.db.models.fields.FloatField')()),
            ('wind_gust_record', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wind_gust_average', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rain_record', self.gf('django.db.models.fields.FloatField')()),
            ('rain_average', self.gf('django.db.models.fields.FloatField')()),
            ('cold_days_record', self.gf('django.db.models.fields.IntegerField')()),
            ('cold_days_average', self.gf('django.db.models.fields.IntegerField')()),
            ('hot_days_record', self.gf('django.db.models.fields.IntegerField')()),
            ('hot_days_average', self.gf('django.db.models.fields.IntegerField')()),
            ('days_of_rain_record', self.gf('django.db.models.fields.IntegerField')()),
            ('days_of_rain_average', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['ClimateByYear'])

        # Adding model 'YearRow'
        db.create_table('app_yearrow', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('max_hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('min_hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('max_hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('min_hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('max_wind_gust', self.gf('django.db.models.fields.FloatField')()),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
            ('hot_days', self.gf('django.db.models.fields.IntegerField')()),
            ('cold_days', self.gf('django.db.models.fields.IntegerField')()),
            ('rain_days', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['YearRow'])


    def backwards(self, orm):
        # Deleting model 'ClimateByYear'
        db.delete_table('app_climatebyyear')

        # Deleting model 'YearRow'
        db.delete_table('app_yearrow')


    models = {
        'app.climatebymonth': {
            'Meta': {'object_name': 'ClimateByMonth'},
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
            'rain_average': ('django.db.models.fields.FloatField', [], {}),
            'rain_record': ('django.db.models.fields.FloatField', [], {}),
            'wind_gust_average': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_gust_record': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'app.climatebyyear': {
            'Meta': {'object_name': 'ClimateByYear'},
            'cold_days_average': ('django.db.models.fields.IntegerField', [], {}),
            'cold_days_record': ('django.db.models.fields.IntegerField', [], {}),
            'days_of_rain_average': ('django.db.models.fields.IntegerField', [], {}),
            'days_of_rain_record': ('django.db.models.fields.IntegerField', [], {}),
            'hot_days_average': ('django.db.models.fields.IntegerField', [], {}),
            'hot_days_record': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_temp_in_average': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_in_record': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out_average': ('django.db.models.fields.FloatField', [], {}),
            'max_temp_out_record': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_in_average': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_in_record': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out_average': ('django.db.models.fields.FloatField', [], {}),
            'min_temp_out_record': ('django.db.models.fields.FloatField', [], {}),
            'rain_average': ('django.db.models.fields.FloatField', [], {}),
            'rain_record': ('django.db.models.fields.FloatField', [], {}),
            'wind_gust_average': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wind_gust_record': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
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
        },
        'app.yearrow': {
            'Meta': {'object_name': 'YearRow'},
            'cold_days': ('django.db.models.fields.IntegerField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'primary_key': 'True'}),
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
        }
    }

    complete_apps = ['app']