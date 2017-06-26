from django.db import models

from app.models import DayRow

class HighestTemperatureRecord(models.Model):
    date = models.DateField(db_index=True)

    indoor = models.BooleanField()

    lowest = models.BooleanField(default=False)

    temperature = models.FloatField(db_index=True)

    @staticmethod
    def update():
        HighestTemperatureRecord.objects.all().delete()

        for day in DayRow.objects.order_by("-max_temp_in")[:5]:
            HighestTemperatureRecord(date=day.date, indoor=True, temperature=day.max_temp_in).save()

        for day in DayRow.objects.filter(max_temp_out__isnull=False, data_quality__gt=50).order_by("-max_temp_out")[:5]:
            HighestTemperatureRecord(date=day.date, indoor=False, temperature=day.max_temp_out).save()

        for day in DayRow.objects.filter(max_temp_out__isnull=False, data_quality__gt=50).order_by("max_temp_out")[:5]:
            HighestTemperatureRecord(date=day.date, indoor=False, temperature=day.max_temp_out, lowest=True).save()

    class Meta:
        app_label = "app"
        ordering = ["-temperature"]
