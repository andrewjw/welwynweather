from datetime import timedelta

from django.db import models

class NestSensors(models.Model):
    date = models.DateTimeField(primary_key=True)

    avg_temp = models.FloatField()
    avg_humidity = models.FloatField()
    max_pir = models.FloatField()
    max_nearPir = models.FloatField(null=True, blank=True)

    min_ch1 = models.FloatField(null=True, blank=True)
    max_ch1 = models.FloatField(null=True, blank=True)
    min_ch2 = models.FloatField(null=True, blank=True)
    max_ch2 = models.FloatField(null=True, blank=True)
    min_als = models.FloatField()
    max_als = models.FloatField()

    min_tp0 = models.FloatField()
    max_tp0 = models.FloatField()
    min_tp1 = models.FloatField()
    max_tp1 = models.FloatField()
    min_tp2 = models.FloatField()
    max_tp2 = models.FloatField()
    min_tp3 = models.FloatField()
    max_tp3 = models.FloatField()

    @property
    def time(self):
        if self.date.hour % 2 == 0 and self.date.minute == 0:
            return "%i:%02i" % (self.date.hour, self.date.minute)
        else:
            return ""

    class Meta:
        app_label = "app"

from monthrow import MonthRow
