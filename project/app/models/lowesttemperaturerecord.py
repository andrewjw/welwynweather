from django.db import models

from app.models import DayRow

class LowestTemperatureRecord(models.Model):
    date = models.DateField(db_index=True)

    indoor = models.BooleanField()

    temperature = models.FloatField(db_index=True)

    @staticmethod
    def update():
        LowestTemperatureRecord.objects.all().delete()

        for day in DayRow.objects.filter(min_temp_in__isnull=False).order_by("min_temp_in")[:5]:
            LowestTemperatureRecord(date=day.date, indoor=True, temperature=day.min_temp_in).save()

        for day in DayRow.objects.filter(min_temp_out__isnull=False).order_by("min_temp_out")[:5]:
            LowestTemperatureRecord(date=day.date, indoor=False, temperature=day.min_temp_out).save()

    class Meta:
        app_label = "app"
        ordering = ["temperature"]
