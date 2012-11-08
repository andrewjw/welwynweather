from django.db import models

class StrongestGustRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    speed = models.FloatField()

    class Meta:
        app_label = "app"
