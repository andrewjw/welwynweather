import datetime

from django.db import models

from dayrow import DayRow

class MonthRow(models.Model):
    date = models.DateTimeField(primary_key=True)
    timestamp = models.IntegerField(),
    delay = models.IntegerField(null=True, blank=True)

    avg_temp_in = models.FloatField()
    avg_max_temp_in = models.FloatField()
    avg_min_temp_in = models.FloatField()

    max_hum_in = models.FloatField()
    min_hum_in = models.FloatField()
    max_temp_in = models.FloatField()
    min_temp_in = models.FloatField()

    avg_temp_out = models.FloatField()
    avg_max_temp_out = models.FloatField()
    avg_min_temp_out = models.FloatField()

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
        date = d.date.replace(day=1)
        try:
            m = MonthRow.objects.get(date=date)
        except MonthRow.DoesNotExist:
            m = MonthRow(date=date)

        next_month = date
        while next_month.month == d.date.month:
            next_month += datetime.timedelta(days=1)

        rows = WeatherRow.objects.filter(date__gte=date, date__lt=next_month)
        days = DayRow.objects.filter(date__gte=date, date__lt=next_month)

        m.max_hum_in = max([d.max_hum_in for d in days])
        m.min_hum_in = min([d.min_hum_in for d in days])
        m.max_temp_in = max([d.max_temp_in for d in days])
        m.min_temp_in = min([d.min_temp_in for d in days])

        m.avg_temp_in = sum([row.temp_in for row in rows])/len(rows)
        m.avg_max_temp_in = sum([d.max_temp_in for d in days])/len(days)
        m.avg_min_temp_in = sum([d.min_temp_in for d in days])/len(days)

        if len([d.max_hum_out for d in days if d.max_hum_out is not None]) > 0:
            m.max_hum_out = max([d.max_hum_out for d in days if d.max_hum_out is not None])
            m.min_hum_out = min([d.min_hum_out for d in days if d.min_hum_out is not None])
            m.max_temp_out = max([d.max_temp_out for d in days if d.max_temp_out is not None])
            m.min_temp_out = min([d.min_temp_out for d in days if d.min_temp_out is not None])

            m.avg_temp_out = sum([row.temp_out for row in rows if row.contact])/len([r for r in rows if r.contact])
            m.avg_max_temp_out = sum([d.max_temp_out for d in days if d.max_temp_out is not None])/len(days)
            m.avg_min_temp_out = sum([d.min_temp_out for d in days if d.min_temp_out is not None])/len(days)

            m.max_wind_gust = max([d.max_wind_gust for d in days])

            m.rain = sum([d.rain for d in days])

            m.hot_days = len([d for d in days if d.max_temp_out > 27])
            m.cold_days = len([d for d in days if d.min_temp_out is not None and d.min_temp_out < 0])
            m.rain_days = len([d for d in days if d.rain > 0])

        m.save()

        ClimateByMonth.update(d)
        YearRow.update(d)

    class Meta:
        app_label = "app"

from weatherrow import WeatherRow
from yearrow import YearRow
from climatebymonth import ClimateByMonth
