from datetime import timedelta

from django.db import models

class ClimateMonth(models.Model):
    month = models.IntegerField(primary_key=True)

    max_temp_in_record = models.FloatField()
    min_temp_in_record = models.FloatField()
    max_temp_in_average = models.FloatField()
    min_temp_in_average = models.FloatField()

    max_temp_out_record = models.FloatField()
    min_temp_out_record = models.FloatField()
    max_temp_out_average = models.FloatField()
    min_temp_out_average = models.FloatField()

    wind_ave_record = models.FloatField(null=True, blank=True)
    wind_gust_record = models.FloatField(null=True, blank=True)
    wind_ave_average = models.FloatField(null=True, blank=True)
    wind_gust_average = models.FloatField(null=True, blank=True)

    rain_record = models.FloatField()
    rain_average = models.FloatField()

    @staticmethod
    def update(d):
        try:
            month = ClimateMonth.objects.get(month=d.date.month)
        except ClimateMonth.DoesNotExist:
            month = ClimateMonth(month=d.date.month)

        days = DayRow.objects.filter(date__month=month.month)

        max_temp_in = [d.max_temp_in for d in days]
        min_temp_in = [d.min_temp_in for d in days]
        max_temp_out = [d.max_temp_out for d in days if d.max_temp_out is not None]
        min_temp_out = [d.min_temp_out for d in days if d.max_temp_out is not None]

        wind_ave = [d.wind_ave for d in days if d.wind_ave is not None]
        wind_gust = [d.max_wind_gust for d in days if d.max_wind_gust is not None]

        rain = [d.rain for d in days]

        month.max_temp_in_record = max(max_temp_in)
        month.min_temp_in_record = min(min_temp_in)
        month.max_temp_in_average = sum(max_temp_in)/len(max_temp_in)
        month.min_temp_in_average = sum(min_temp_in)/len(min_temp_in)

        month.max_temp_out_record = max(max_temp_out)
        month.min_temp_out_record = min(min_temp_out)
        month.max_temp_out_average = sum(max_temp_out)/len(max_temp_out)
        month.min_temp_out_average = sum(min_temp_out)/len(min_temp_out)

        month.wind_ave_record = max(wind_ave)
        month.wind_gust_record = max(wind_gust)
        month.wind_ave_average = sum(wind_ave)/len(wind_ave)
        month.wind_gust_average = sum(wind_gust)/len(wind_gust)

        month.rain_record = max(rain)
        month.rain_average = sum(rain)/len(rain)
        
        month.save()

    class Meta:
        app_label = "app"

from dayrow import DayRow
