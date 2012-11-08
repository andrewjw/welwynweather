from django.db import models

class LowestPressureRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    pressure = models.FloatField()

    class Meta:
        app_label = "app"
