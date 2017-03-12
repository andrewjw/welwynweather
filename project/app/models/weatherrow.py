from datetime import datetime, date

from django.db import models
from django.utils.timezone import utc

class WeatherRow(models.Model):
    date = models.DateTimeField(primary_key=True)
    timestamp = models.IntegerField(),
    delay = models.IntegerField(null=True, blank=True)

    hum_in = models.FloatField()
    temp_in = models.FloatField()

    hum_out = models.FloatField(null=True, blank=True)
    temp_out = models.FloatField(null=True, blank=True)

    abs_pressure = models.FloatField()
    wind_ave = models.FloatField(null=True, blank=True)
    wind_gust = models.FloatField(null=True, blank=True)
    wind_dir = models.IntegerField(null=True, blank=True)

    rain = models.FloatField()
    raw_rain = models.FloatField()

    is_raining = models.BooleanField()

    status = models.IntegerField()

    @property
    def time(self):
        return "%i:%02i" % (self.date.hour, self.date.minute)

    @property
    def contact(self):
        return self.status & 64 == 0 and self.temp_out is not None

    def get_hour(self):
        try:
            return HourRow.objects.get(date=self.get_hour_time())
        except HourRow.DoesNotExist:
            return HourRow(date=self.get_hour_time())

    def get_hour_time(self):
        return datetime(self.date.year, self.date.month, self.date.day, self.date.hour, tzinfo=utc)

    def get_day(self):
        try:
            return DayRow.objects.get(date=datetime(self.date.year, self.date.month, self.date.day, tzinfo=utc))
        except DayRow.DoesNotExist:
            return DayRow(date=datetime(self.date.year, self.date.month, self.date.day, tzinfo=utc))

    def get_month(self):
        try:
            return MonthRow.objects.get(date=datetime(self.date.year, self.date.month, 1, tzinfo=utc))
        except MonthRow.DoesNotExist:
            return MonthRow(date=datetime(self.date.year, self.date.month, 1, tzinfo=utc))

    class Meta:
        app_label = "app"
        ordering = ["date"]

from hourrow import HourRow
from dayrow import DayRow
from monthrow import MonthRow
