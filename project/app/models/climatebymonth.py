from datetime import timedelta

from django.db import models

class ClimateByMonth(models.Model):
    month = models.IntegerField(primary_key=True)

    max_temp_in_record = models.FloatField()
    min_temp_in_record = models.FloatField()
    max_temp_in_average = models.FloatField()
    min_temp_in_average = models.FloatField()

    max_temp_out_record = models.FloatField()
    min_temp_out_record = models.FloatField()
    max_temp_out_average = models.FloatField()
    min_temp_out_average = models.FloatField()

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
            month = ClimateByMonth.objects.get(month=d.date.month)
        except ClimateByMonth.DoesNotExist:
            month = ClimateByMonth(month=d.date.month)

        months = MonthRow.objects.filter(date__month=month.month)

        month.max_temp_in_record = max([m.max_temp_in for m in months])
        month.min_temp_in_record = min([m.min_temp_in for m in months])
        month.max_temp_in_average = sum([m.max_temp_in for m in months])/len(months)
        month.min_temp_in_average = sum([m.min_temp_in for m in months])/len(months)

        month.max_temp_out_record = max([m.max_temp_out for m in months])
        month.min_temp_out_record = min([m.min_temp_out for m in months])
        month.max_temp_out_average = sum([m.max_temp_out for m in months])/len(months)
        month.min_temp_out_average = sum([m.min_temp_out for m in months])/len(months)

        month.wind_gust_record = max([m.max_wind_gust for m in months])
        month.wind_gust_average = sum([m.max_wind_gust for m in months])/len(months)

        month.rain_record = max([m.rain for m in months])
        month.rain_average = sum([m.rain for m in months])/len(months)

        month.cold_days_average = sum([m.cold_days for m in months])/len(months)
        month.cold_days_record = max([m.cold_days for m in months])
        month.hot_days_average = sum([m.hot_days for m in months])/len(months)
        month.hot_days_record = max([m.hot_days for m in months])
        month.days_of_rain_average = sum([m.rain_days for m in months])/len(months)
        month.days_of_rain_record = max([m.rain_days for m in months])

        month.save()

    class Meta:
        app_label = "app"

from monthrow import MonthRow
