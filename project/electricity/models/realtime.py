from django.db import models

class RealTime(models.Model):
    date = models.DateTimeField(primary_key=True)

    temperature = models.FloatField()

    watts = models.IntegerField()

    def __str__(self):
        return "<Realtime %s>" % (self.date, )

    class Meta:
        app_label = "electricity"
