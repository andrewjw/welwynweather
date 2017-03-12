from django.db import models

from app.models import HourRow

class HeaviestRainRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    rain = models.FloatField()

    @staticmethod
    def update():
        HeaviestRainRecord.objects.all().delete()

        for hour in HourRow.objects.order_by("-rain")[:5]:
            HeaviestRainRecord(date=hour.date, rain=hour.rain).save()

    class Meta:
        app_label = "app"
        ordering = ["-rain"]
