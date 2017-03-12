from django.db import models

from app.models import DayRow

class WettestDayRecord(models.Model):
    date = models.DateField(primary_key=True)

    rain = models.FloatField()

    @staticmethod
    def update():
        records = DayRow.objects.all().order_by("-rain")[:5]

        WettestDayRecord.objects.all().delete()

        [WettestDayRecord(date=d.date, rain=d.rain).save() for d in records]

    class Meta:
        app_label = "app"
        ordering = ["-rain"]
