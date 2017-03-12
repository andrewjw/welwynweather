from datetime import datetime

from django.db import models
from django.utils.timezone import utc

from app.models.dayrow import DayRow

class HighestPressureRecord(models.Model):
    date = models.DateField(primary_key=True)

    pressure = models.FloatField()

    @staticmethod
    def update():
        records = DayRow.objects.all().order_by("-abs_pressure")[:5]

        HighestPressureRecord.objects.all().delete()

        [HighestPressureRecord(date=d.date, pressure=d.abs_pressure).save() for d in records]


    class Meta:
        app_label = "app"
        ordering = ["-pressure"]
