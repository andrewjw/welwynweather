import datetime

from django.db import models

from monthrow import MonthRow

class YearRow(models.Model):
    date = models.DateField(primary_key=True)

    avg_temp_in = models.FloatField()
    avg_temp_out = models.FloatField()

    avg_max_temp_in = models.FloatField()
    avg_min_temp_in = models.FloatField()
    avg_max_temp_out = models.FloatField()
    avg_min_temp_out = models.FloatField()

    max_hum_in = models.FloatField()
    min_hum_in = models.FloatField()
    max_temp_in = models.FloatField()
    min_temp_in = models.FloatField()

    max_hum_out = models.FloatField(null=True, blank=True)
    min_hum_out = models.FloatField(null=True, blank=True)
    max_temp_out = models.FloatField(null=True, blank=True)
    min_temp_out = models.FloatField(null=True, blank=True)

    max_wind_gust = models.FloatField(null=True, blank=True)

    rain = models.FloatField()

    hot_days = models.IntegerField()
    cold_days = models.IntegerField()
    rain_days = models.IntegerField()

    data_quality = models.FloatField()

    @staticmethod
    def update(d):
        date = d.date.replace(day=1, month=1)
        try:
            y = YearRow.objects.get(date=date)
        except YearRow.DoesNotExist:
            y = YearRow(date=date)

        next_year = date.replace(year=date.year+1)

        days = DayRow.objects.filter(date__gte=date, date__lt=next_year)
        months = MonthRow.objects.filter(date__gte=date, date__lt=next_year)

        y.avg_temp_in = sum([d.avg_temp_in for d in days])/len(days)
        y.avg_temp_out = sum([d.avg_temp_out for d in days])/len(days)
        y.avg_max_temp_in = sum([d.max_temp_in for d in days])/len(days)
        y.avg_min_temp_in = sum([d.min_temp_in for d in days])/len(days)
        y.avg_max_temp_out = sum([d.max_temp_out for d in days if d.max_temp_out is not None])/len(days)
        y.avg_min_temp_out = sum([d.min_temp_out for d in days if d.max_temp_out is not None])/len(days)

        y.max_hum_in = max([m.max_hum_in for m in months])
        y.min_hum_in = min([m.min_hum_in for m in months])
        y.max_temp_in = max([m.max_temp_in for m in months])
        y.min_temp_in = min([m.min_temp_in for m in months])

        y.max_hum_out = max([m.max_hum_out for m in months])
        y.min_hum_out = min([m.min_hum_out for m in months])
        y.max_temp_out = max([m.max_temp_out for m in months])
        y.min_temp_out = min([m.min_temp_out for m in months])

        y.max_wind_gust = max([m.max_wind_gust for d in months])

        y.rain = sum([m.rain for m in months if m.rain is not None])

        y.hot_days = sum([m.hot_days for m in months])
        y.cold_days = sum([m.cold_days for m in months])
        y.rain_days = sum([m.rain_days for m in months])

        good = sum([d.good_rows for d in days])
        bad = sum([d.bad_rows for d in days])

        y.data_quality = 100.0 * good/(good + bad)

        y.save()

    class Meta:
        app_label = "app"

from climatebyyear import ClimateByYear
from weatherrow import WeatherRow
from dayrow import DayRow
