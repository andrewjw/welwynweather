from django.db import models

class StrongestGustRecord(models.Model):
    date = models.DateTimeField(primary_key=True)

    speed = models.FloatField()

    @staticmethod
    def update(row):
        hour = StrongestGustRecord.objects.filter(date__year=row.date.year, date__month=row.date.month, date__day=row.date.day)
        if len(hour) > 0:
            if hour[0].speed < row.wind_gust:
                hour[0].delete()
                hour[0].date = row.date
                hour[0].speed = row.wind_gust
                hour[0].save()
        elif StrongestGustRecord.objects.all().count() < 5:
            StrongestGustRecord(date=row.date, speed=row.wind_gust).save()
        else:
            record = StrongestGustRecord.objects.all().order_by("speed")[0]

            if row.wind_gust > record.speed:
                StrongestGustRecord(date=row.date, speed=row.wind_gust).save()
                [r.delete() for r in StrongestGustRecord.objects.all()[5:]]
    
    class Meta:
        app_label = "app"
        ordering = ["-speed"]
