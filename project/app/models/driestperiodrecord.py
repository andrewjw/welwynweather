from django.db import models

class DriestPeriodRecord(models.Model):
    start_date = models.DateTimeField(primary_key=True)
    end_date = models.DateTimeField()

    current = models.BooleanField()

    length = models.IntegerField()

    class Meta:
        app_label = "app"
