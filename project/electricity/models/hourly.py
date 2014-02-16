from django.db import models

class Hourly(models.Model):
    date = models.DateTimeField(primary_key=True)

    kwh = models.FloatField()

    def __str__(self):
        return "<Hourly %s>" % (self.date, )

    class Meta:
        app_label = "electricity"
