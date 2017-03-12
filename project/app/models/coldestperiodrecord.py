from django.db import models

from app.models import DayRow

class ColdestPeriodRecord(models.Model):
    start_date = models.DateField(primary_key=True)
    end_date = models.DateField()

    current = models.BooleanField()

    length = models.IntegerField()

    def calc_length(self):
        self.length = (self.end_date - self.start_date).days + 1

    @staticmethod
    def update():
        periods = []

        period = None

        for day in DayRow.objects.order_by("date"):
            if day.min_temp_out >= 0 and period is not None:
                periods.append(period)
                periods.sort(key=lambda p: -p.length)
                periods = periods[:5]
                period = None

            if day.min_temp_out < 0 and period is None:
                period = ColdestPeriodRecord(start_date=day.date, end_date=day.date, current=False, length=1)
            elif day.min_temp_out < 0:
                period.end_date = day.date
                period.length += 1

        if period is not None:
            periods.append(period)
        periods.sort(key=lambda p: -p.length)
        [p.save() for p in periods[:5]]

    class Meta:
        app_label = "app"
        ordering = ["-length"]
