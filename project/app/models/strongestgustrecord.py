from django.db import models

from app.models.dayrow import DayRow

class StrongestGustRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    speed = models.FloatField()

    @staticmethod
    def update():
        records = DayRow.objects.all().order_by("-max_wind_gust")[:5]

        StrongestGustRecord.objects.all().delete()

        [StrongestGustRecord(date=d.max_wind_gust_at, speed=d.max_wind_gust).save() for d in records]


    class Meta:
        app_label = "app"
        ordering = ["-speed"]
