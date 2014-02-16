from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone

class ClimateByYear(models.Model):
    avg_temp_in_record = models.FloatField()
    avg_temp_in_average = models.FloatField()

    max_temp_in_record = models.FloatField()
    min_temp_in_record = models.FloatField()
    max_temp_in_average = models.FloatField()
    min_temp_in_average = models.FloatField()
    avg_max_temp_in_record = models.FloatField()
    avg_min_temp_in_record = models.FloatField()
    avg_max_temp_in_average = models.FloatField()
    avg_min_temp_in_average = models.FloatField()

    avg_temp_out_record = models.FloatField()
    avg_temp_out_average = models.FloatField()

    max_temp_out_record = models.FloatField()
    min_temp_out_record = models.FloatField()
    max_temp_out_average = models.FloatField()
    min_temp_out_average = models.FloatField()
    avg_max_temp_out_record = models.FloatField()
    avg_min_temp_out_record = models.FloatField()
    avg_max_temp_out_average = models.FloatField()
    avg_min_temp_out_average = models.FloatField()

    wind_gust_record = models.FloatField(null=True, blank=True)
    wind_gust_average = models.FloatField(null=True, blank=True)

    rain_record = models.FloatField()
    rain_average = models.FloatField()

    cold_days_record = models.IntegerField()
    cold_days_average = models.IntegerField()
    hot_days_record = models.IntegerField()
    hot_days_average = models.IntegerField()
    days_of_rain_record = models.IntegerField()
    days_of_rain_average = models.IntegerField()

    @staticmethod
    def update(d):
        try:
            year = ClimateByYear.objects.get()
        except ClimateByYear.DoesNotExist:
            year = ClimateByYear()

        years = YearRow.objects.filter(date__gte=datetime(2012, 1, 1).replace(tzinfo=timezone.utc))

        if years.count() == 0:
            return

        year.avg_temp_in_record = max([y.avg_temp_in for y in years])
        year.avg_temp_in_average = sum([y.avg_temp_in for y in years])/len(years)
        year.avg_max_temp_in_record = max([y.avg_max_temp_in for y in years])
        year.avg_max_temp_in_average = sum([y.avg_max_temp_in for y in years])/len(years)
        year.avg_min_temp_in_record = max([y.avg_min_temp_in for y in years])
        year.avg_min_temp_in_average = sum([y.avg_min_temp_in for y in years])/len(years)

        year.max_temp_in_record = max([y.max_temp_in for y in years])
        year.min_temp_in_record = min([y.min_temp_in for y in years])
        year.max_temp_in_average = sum([y.max_temp_in for y in years])/len(years)
        year.min_temp_in_average = sum([y.min_temp_in for y in years])/len(years)

        year.avg_temp_out_record = max([y.avg_temp_out for y in years])
        year.avg_temp_out_average = sum([y.avg_temp_out for y in years])/len(years)
        year.avg_max_temp_out_record = max([y.avg_max_temp_out for y in years])
        year.avg_max_temp_out_average = sum([y.avg_max_temp_out for y in years])/len(years)
        year.avg_min_temp_out_record = max([y.avg_min_temp_out for y in years])
        year.avg_min_temp_out_average = sum([y.avg_min_temp_out for y in years])/len(years)

        year.max_temp_out_record = max([y.max_temp_out for y in years])
        year.min_temp_out_record = min([y.min_temp_out for y in years])
        year.max_temp_out_average = sum([y.max_temp_out for y in years])/len(years)
        year.min_temp_out_average = sum([y.min_temp_out for y in years])/len(years)

        year.wind_gust_record = max([y.max_wind_gust for y in years])
        year.wind_gust_average = sum([y.max_wind_gust for y in years])/len(years)

        year.rain_record = max([y.rain for y in years])
        year.rain_average = sum([y.rain for y in years])/len(years)

        year.cold_days_average = sum([y.cold_days for y in years])/len(years)
        year.cold_days_record = max([y.cold_days for y in years])
        year.hot_days_average = sum([y.hot_days for y in years])/len(years)
        year.hot_days_record = max([y.hot_days for y in years])
        year.days_of_rain_average = sum([y.rain_days for y in years])/len(years)
        year.days_of_rain_record = max([y.rain_days for y in years])

        year.save()

    class Meta:
        app_label = "app"

from yearrow import YearRow
