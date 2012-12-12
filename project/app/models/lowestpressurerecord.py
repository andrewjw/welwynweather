from datetime import datetime

from django.db import models
from django.utils.timezone import utc

class LowestPressureRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    pressure = models.FloatField()

    @staticmethod
    def update(row):
        d = datetime(row.date.year, row.date.month, row.date.day, tzinfo=utc)
        today = LowestPressureRecord.objects.filter(date=d)
        if len(today) > 0:
            if today[0].pressure > row.abs_pressure:
                today[0].pressure = row.abs_pressure
                today[0].save()
        elif LowestPressureRecord.objects.all().count() < 5:
            LowestPressureRecord(date=d, pressure=row.abs_pressure).save()
        else:
            record = LowestPressureRecord.objects.all().order_by("-pressure")[0]

            if row.abs_pressure < record.pressure:
                LowestPressureRecord(date=d, pressure=row.abs_pressure).save()
                [r.delete() for r in LowestPressureRecord.objects.all()[5:]]

    class Meta:
        app_label = "app"
        ordering = ["pressure"]
