from django.db import models

class Monthly(models.Model):
    date = models.DateTimeField(primary_key=True)

    kwh = models.FloatField()

    def __str__(self):
        return "<Monthly %s>" % (self.date, )

    class Meta:
        app_label = "electricity"
