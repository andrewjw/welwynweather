from django.db import models

from app.models import DayRow

class WettestPeriodRecord(models.Model):
    start_date = models.DateField(primary_key=True)
    end_date = models.DateField()

    current = models.BooleanField()

    length = models.IntegerField()

    @staticmethod
    def update():
        periods = []

        period = None

        for day in DayRow.objects.order_by("date"):
            if not day.rained and period is not None:
                periods.append(period)
                periods.sort(key=lambda p: -p.length)
                periods = periods[:5]
                period = None

            if day.rained and period is None:
                period = WettestPeriodRecord(start_date=day.date, end_date=day.date, current=False, length=1)
            elif day.rained:
                period.end_date = day.date
                period.length += 1

        if period is not None:
            periods.append(period)
        periods.sort(key=lambda p: -p.length)
        [p.save() for p in periods[:5]]

    class Meta:
        app_label = "app"
        ordering = ["-length"]
