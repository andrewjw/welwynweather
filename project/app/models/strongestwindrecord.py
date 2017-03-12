from django.db import models

from app.models.dayrow import DayRow

class StrongestWindRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    speed = models.FloatField()

    @staticmethod
    def update():
        records = DayRow.objects.all().order_by("-max_wind_ave")[:5]

        StrongestWindRecord.objects.all().delete()

        [StrongestWindRecord(date=d.max_wind_ave_at, speed=d.max_wind_ave).save() for d in records]

    class Meta:
        app_label = "app"
        ordering = ["-speed"]
