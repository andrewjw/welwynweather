from datetime import timedelta

from django.db import models

class ClimateByMonth(models.Model):
    month = models.IntegerField(primary_key=True)

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
    highest_low_temp_out_record = models.FloatField()
    lowest_high_temp_out_record = models.FloatField()
    highest_low_temp_out_average = models.FloatField()
    lowest_high_temp_out_average = models.FloatField()
    avg_max_temp_out_record = models.FloatField()
    avg_min_temp_out_record = models.FloatField()
    avg_max_temp_out_average = models.FloatField()
    avg_min_temp_out_average = models.FloatField()

    wind_gust_record = models.FloatField(null=True, blank=True)
    wind_gust_average = models.FloatField(null=True, blank=True)

    rain_record = models.FloatField()
    rain_average = models.FloatField()

    cold_days_record = models.IntegerField()
    cold_days_average = models.FloatField()
    hot_days_record = models.IntegerField()
    hot_days_average = models.FloatField()
    days_of_rain_record = models.IntegerField()
    days_of_rain_average = models.FloatField()

    @staticmethod
    def update(d):
        try:
            month = ClimateByMonth.objects.get(month=d.date.month)
        except ClimateByMonth.DoesNotExist:
            month = ClimateByMonth(month=d.date.month)

        months = MonthRow.objects.filter(date__month=month.month)
        if len(months) == 0:
            return

        month.avg_temp_in_record = max([m.avg_temp_in for m in months])
        month.avg_temp_in_average = sum([m.avg_temp_in for m in months])/len(months)
        month.avg_temp_out_record = max([m.avg_temp_out for m in months])
        month.avg_temp_out_average = sum([m.avg_temp_out for m in months])/len(months)

        month.max_temp_in_record = max([m.max_temp_in for m in months])
        month.min_temp_in_record = min([m.min_temp_in for m in months])
        month.max_temp_in_average = sum([m.max_temp_in for m in months])/len(months)
        month.min_temp_in_average = sum([m.min_temp_in for m in months])/len(months)

        month.avg_max_temp_in_record = max([m.avg_max_temp_in for m in months])
        month.avg_min_temp_in_record = min([m.avg_min_temp_in for m in months])
        month.avg_max_temp_in_average = sum([m.avg_max_temp_in for m in months])/len(months)
        month.avg_min_temp_in_average = sum([m.avg_min_temp_in for m in months])/len(months)

        month.max_temp_out_record = max([m.max_temp_out for m in months])
        month.min_temp_out_record = min([m.min_temp_out for m in months])
        month.max_temp_out_average = sum([m.max_temp_out for m in months])/len(months)
        month.min_temp_out_average = sum([m.min_temp_out for m in months])/len(months)

        month.highest_low_temp_out_record = max([m.highest_low_temp_out for m in months])
        month.lowest_high_temp_out_record = min([m.lowest_high_temp_out for m in months])
        month.highest_low_temp_out_average = sum([m.highest_low_temp_out for m in months])/len(months)
        month.lowest_high_temp_out_average = sum([m.lowest_high_temp_out for m in months])/len(months)

        month.avg_max_temp_out_record = max([m.avg_max_temp_out for m in months])
        month.avg_min_temp_out_record = min([m.avg_min_temp_out for m in months])
        month.avg_max_temp_out_average = sum([m.avg_max_temp_out for m in months])/len(months)
        month.avg_min_temp_out_average = sum([m.avg_min_temp_out for m in months])/len(months)

        month.wind_gust_record = max([m.max_wind_gust for m in months])
        month.wind_gust_average = sum([m.max_wind_gust for m in months])/len(months)

        month.rain_record = max([m.rain for m in months])
        month.rain_average = sum([m.rain for m in months])/len(months)

        month.cold_days_average = sum([m.cold_days for m in months])/float(len(months))
        month.cold_days_record = max([m.cold_days for m in months])
        month.hot_days_average = sum([m.hot_days for m in months])/float(len(months))
        month.hot_days_record = max([m.hot_days for m in months])
        month.days_of_rain_average = sum([m.rain_days for m in months])/float(len(months))
        month.days_of_rain_record = max([m.rain_days for m in months])

        month.save()

    class Meta:
        app_label = "app"

from monthrow import MonthRow
