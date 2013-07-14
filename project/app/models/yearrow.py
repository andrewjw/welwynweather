import datetime

from django.db import models

from monthrow import MonthRow

class YearRow(models.Model):
    date = models.DateTimeField(primary_key=True)

    max_hum_in = models.FloatField()
    min_hum_in = models.FloatField()
    max_temp_in = models.FloatField()
    min_temp_in = models.FloatField()

    max_hum_out = models.FloatField()
    min_hum_out = models.FloatField()
    max_temp_out = models.FloatField()
    min_temp_out = models.FloatField()

    max_wind_gust = models.FloatField()

    rain = models.FloatField()

    hot_days = models.IntegerField()
    cold_days = models.IntegerField()
    rain_days = models.IntegerField()

    @staticmethod
    def update(d):
        date = d.date.replace(day=1, month=1)
        try:
            y = YearRow.objects.get(date=date)
        except YearRow.DoesNotExist:
            y = YearRow(date=date)

        next_year = date.replace(year=date.year+1)

        months = MonthRow.objects.filter(date__gte=date, date__lt=next_year)

        y.max_hum_in = max([m.max_hum_in for m in months])
        y.min_hum_in = min([m.min_hum_in for m in months])
        y.max_temp_in = max([m.max_temp_in for m in months])
        y.min_temp_in = min([m.min_temp_in for m in months])

        y.max_hum_out = max([m.max_hum_out for m in months])
        y.min_hum_out = min([m.min_hum_out for m in months])
        y.max_temp_out = max([m.max_temp_out for m in months])
        y.min_temp_out = min([m.min_temp_out for m in months])

        y.max_wind_gust = max([m.max_wind_gust for d in months])

        y.rain = sum([m.rain for m in months])

        y.hot_days = sum([m.hot_days for m in months])
        y.cold_days = sum([m.cold_days for m in months])
        y.rain_days = sum([m.rain_days for m in months])

        y.save()

        ClimateByYear.update(d)

    class Meta:
        app_label = "app"

from climatebyyear import ClimateByYear
