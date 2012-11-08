# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LowestPressureRecord'
        db.create_table('app_lowestpressurerecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('pressure', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['LowestPressureRecord'])

        # Adding model 'HighestPressureRecord'
        db.create_table('app_highestpressurerecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('pressure', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['HighestPressureRecord'])

        # Adding model 'StrongestGustRecord'
        db.create_table('app_strongestgustrecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['StrongestGustRecord'])

        # Adding model 'DayRow'
        db.create_table('app_dayrow', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('delay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max_hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('min_hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('max_hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('min_hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('abs_pressure', self.gf('django.db.models.fields.FloatField')()),
            ('wind_ave', self.gf('django.db.models.fields.FloatField')()),
            ('max_wind_gust', self.gf('django.db.models.fields.FloatField')()),
            ('wind_dir', self.gf('django.db.models.fields.IntegerField')()),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
            ('rained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['DayRow'])

        # Adding model 'WettestPeriodRecord'
        db.create_table('app_wettestperiodrecord', (
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['WettestPeriodRecord'])

        # Adding model 'MonthRow'
        db.create_table('app_monthrow', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('delay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max_hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('min_hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('max_hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('min_hum_out', self.gf('django.db.models.fields.FloatField')()),
            ('max_temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('min_temp_out', self.gf('django.db.models.fields.FloatField')()),
            ('abs_pressure', self.gf('django.db.models.fields.FloatField')()),
            ('wind_ave', self.gf('django.db.models.fields.FloatField')()),
            ('max_wind_gust', self.gf('django.db.models.fields.FloatField')()),
            ('wind_dir', self.gf('django.db.models.fields.IntegerField')()),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
            ('rained', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['MonthRow'])

        # Adding model 'HourRow'
        db.create_table('app_hourrow', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('delay', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hum_in', self.gf('django.db.models.fields.FloatField')()),
            ('temp_in', self.gf('django.db.models.fields.FloatField')()),
            ('hum_out', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temp_out', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('abs_pressure', self.gf('django.db.models.fields.FloatField')()),
            ('wind_ave', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wind_gust', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('wind_dir', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
            ('raw_rain', self.gf('django.db.models.fields.FloatField')()),
            ('is_raining', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['HourRow'])

        # Adding model 'HighestTemperatureRecord'
        db.create_table('app_highesttemperaturerecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('indoor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('temperature', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['HighestTemperatureRecord'])

        # Adding model 'LowestTemperatureRecord'
        db.create_table('app_lowesttemperaturerecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('indoor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('temperature', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['LowestTemperatureRecord'])

        # Adding model 'StrongestWindRecord'
        db.create_table('app_strongestwindrecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['StrongestWindRecord'])

        # Adding model 'DriestPeriodRecord'
        db.create_table('app_driestperiodrecord', (
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('length', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('app', ['DriestPeriodRecord'])

        # Adding model 'HeaviestRainRecord'
        db.create_table('app_heaviestrainrecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['HeaviestRainRecord'])

        # Adding model 'WettestDayRecord'
        db.create_table('app_wettestdayrecord', (
            ('date', self.gf('django.db.models.fields.DateTimeField')(primary_key=True)),
            ('rain', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('app', ['WettestDayRecord'])

        # Adding field 'WeatherRow.is_raining'
        db.add_column('app_weatherrow', 'is_raining',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'WeatherRow.status'
        db.alter_column('app_weatherrow', 'status', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'WeatherRow.hum_out'
        db.alter_column('app_weatherrow', 'hum_out', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'WeatherRow.wind_gust'
        db.alter_column('app_weatherrow', 'wind_gust', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'WeatherRow.wind_ave'
        db.alter_column('app_weatherrow', 'wind_ave', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'WeatherRow.temp_out'
        db.alter_column('app_weatherrow', 'temp_out', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'WeatherRow.wind_dir'
        db.alter_column('app_weatherrow', 'wind_dir', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting model 'LowestPressureRecord'
        db.delete_table('app_lowestpressurerecord')

        # Deleting model 'HighestPressureRecord'
        db.delete_table('app_highestpressurerecord')

        # Deleting model 'StrongestGustRecord'
        db.delete_table('app_strongestgustrecord')

        # Deleting model 'DayRow'
        db.delete_table('app_dayrow')

        # Deleting model 'WettestPeriodRecord'
        db.delete_table('app_wettestperiodrecord')

        # Deleting model 'MonthRow'
        db.delete_table('app_monthrow')

        # Deleting model 'HourRow'
        db.delete_table('app_hourrow')

        # Deleting model 'HighestTemperatureRecord'
        db.delete_table('app_highesttemperaturerecord')

        # Deleting model 'LowestTemperatureRecord'
        db.delete_table('app_lowesttemperaturerecord')

        # Deleting model 'StrongestWindRecord'
        db.delete_table('app_strongestwindrecord')

        # Deleting model 'DriestPeriodRecord'
        db.delete_table('app_driestperiodrecord')

        # Deleting model 'HeaviestRainRecord'
        db.delete_table('app_heaviestrainrecord')

        # Deleting model 'WettestDayRecord'
        db.delete_table('app_wettestdayrecord')

        # Deleting field 'WeatherRow.is_raining'
        db.delete_column('app_weatherrow', 'is_raining')


        # Changing field 'WeatherRow.status'
        db.alter_column('app_weatherrow', 'status', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'WeatherRow.hum_out'
        db.alter_column('app_weatherrow', 'hum_out', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'WeatherRow.wind_gust'
        db.alter_column('app_weatherrow', 'wind_gust', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'WeatherRow.wind_ave'
        db.alter_column('app_weatherrow', 'wind_ave', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'WeatherRow.temp_out'
        db.alter_column('app_weatherrow', 'temp_out', self.gf('django.db.models.fields.FloatField')(default=0))

        # Changing field 'WeatherRow.wind_dir'
        db.alter_column('app_weatherrow', 'wind_dir', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        'app.dayrow': {
            'Meta': {'object_name': 'DayRow'},
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