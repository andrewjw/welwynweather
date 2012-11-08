from django.db import models

class HeaviestRainRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    rain = models.FloatField()

    class Meta:
        app_label = "app"
