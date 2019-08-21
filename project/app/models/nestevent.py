from datetime import timedelta

from django.db import models

class NestEvent(models.Model):
    date = models.DateTimeField(primary_key=True)

    duration = models.IntegerField()

    target = models.FloatField()

    class Meta:
        app_label = "app"

from monthrow import MonthRow
