from django.db import models

class HeaviestRainRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    rain = models.FloatField()

    @staticmethod
    def update(row):
        if row.rain == 0:
            return

        hour = HeaviestRainRecord.objects.filter(date=row.date)
        if len(hour) > 0:
            if hour[0].rain < row.rain:
                hour[0].rain = row.rain
                hour[0].save()
        elif HeaviestRainRecord.objects.all().count() < 5:
            HeaviestRainRecord(date=row.date, rain=row.rain).save()
        else:
            record = HeaviestRainRecord.objects.all().order_by("rain")[0]

            if row.rain > record.rain:
                HeaviestRainRecord(date=row.date, rain=row.rain).save()
                [r.delete() for r in HeaviestRainRecord.objects.all()[5:]]

    class Meta:
        app_label = "app"
        ordering = ["-rain"]
