from django.db import models

class LowestTemperatureRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    indoor = models.BooleanField()

    temperature = models.FloatField()

    class Meta:
        app_label = "app"
