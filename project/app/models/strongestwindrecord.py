from django.db import models

class StrongestWindRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    speed = models.FloatField()

    @staticmethod
    def update(row):
        hour = StrongestWindRecord.objects.filter(date__year=row.date.year, date__month=row.date.month, date__day=row.date.day)
        if len(hour) > 0:
            if hour[0].speed < row.wind_ave:
                hour[0].delete()
                hour[0].date = row.date
                hour[0].speed = row.wind_ave
                hour[0].save()
        elif StrongestWindRecord.objects.all().count() < 5:
            StrongestWindRecord(date=row.date, speed=row.wind_ave).save()
        else:
            record = StrongestWindRecord.objects.all().order_by("speed")[0]

            if row.wind_ave > record.speed:
                StrongestWindRecord(date=row.date, speed=row.wind_ave).save()
                [r.delete() for r in StrongestWindRecord.objects.all()[5:]]
    
    class Meta:
        app_label = "app"
        ordering = ["-speed"]
