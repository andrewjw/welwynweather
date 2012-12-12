from django.db import models

class WettestDayRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    rain = models.FloatField()

    @staticmethod
    def update(row):
        if not row.rained:
            return

        if WettestDayRecord.objects.all().count() < 5:
            WettestDayRecord(date=row.date, rain=row.rain).save()
        else:
            record = WettestDayRecord.objects.order_by("rain")[0]

            if row.rain > record.rain:
                WettestDayRecord(date=row.date, rain=row.rain).save()
                [r.delete() for r in WettestDayRecord.objects.all()[5:]]

    class Meta:
        app_label = "app"
        ordering = ["-rain"]
