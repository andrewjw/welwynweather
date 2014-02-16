from django.db import models

class Daily(models.Model):
    date = models.DateTimeField(primary_key=True)

    kwh = models.FloatField()

    def __str__(self):
        return "<Daily %s>" % (self.date, )

    class Meta:
        app_label = "electricity"
