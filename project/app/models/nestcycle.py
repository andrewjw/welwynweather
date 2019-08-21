from datetime import timedelta

from django.db import models

class NestCycle(models.Model):
    date = models.DateTimeField(primary_key=True)

    duration = models.IntegerField()

    class Meta:
        app_label = "app"

from monthrow import MonthRow
