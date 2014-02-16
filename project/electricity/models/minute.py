from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone

from electricity.models import Daily, Hourly, Monthly, RealTime

class Minute(models.Model):
    date = models.DateTimeField(primary_key=True)

    watts = models.IntegerField()

    def calculate(self):
        enddate = self.date + timedelta(minutes=1)
        realtime = RealTime.objects.filter(date__gte=self.date, date__lt=enddate)

        if len(realtime) > 0:
            self.watts = sum([r.watts for r in realtime])/len(realtime)
            return

        hourly = Hourly.objects.filter(
            date=datetime(self.date.year, self.date.month, self.date.day, self.date.hour).replace(tzinfo=timezone.utc))
        if len(hourly) > 0:
            self.watts = (hourly[0].kwh * 1000)/120
            return

        daily = Daily.objects.filter(
            date=datetime(self.date.year, self.date.month, self.date.day).replace(tzinfo=timezone.utc))
        if len(daily) > 0:
            self.watts = (daily[0].kwh * 1000)/(24*60)
            return

        monthly = Monthly.objects.filter(
            date=datetime(self.date.year, self.date.month, self.date.day).replace(tzinfo=timezone.utc))
        if len(monthly) > 0:
            d = monthly.date
            while d.month == monthly.date.month:
                d = d + timedelta(days=1)
            self.watts = (monthly[0].kwh * 1000) / (24 * 60 * (d - monthly.date).days)
            return

    @staticmethod
    def update(period):
        if isinstance(period, Monthly):
            d = period.date
            enddate = d
            while enddate.month == d.month:
                enddate += timedelta(days=1)
            minutes = dict([(m.date, m) for m in Minute.objects.filter(date__gte=d, date__lt=enddate)])
            while d.month == period.date.month:
                if d in minutes:
                    m = minutes[d]
                else:
                    m = Minute(date=d)
                m.calculate()
                m.save()
                d += timedelta(minutes=1)
        elif isinstance(period, Daily):
            d = period.date
            while d.day == period.date.day:
                m, _ = Minute.objects.get_or_create(date=d, defaults={ "watts": 0 })
                m.calculate()
                m.save()
                d += timedelta(minutes=1)
        elif isinstance(period, Hourly):
            d = period.date
            while d.hour == period.date.hour:
                m, _ = Minute.objects.get_or_create(date=d, defaults={ "watts": 0 })
                m.calculate()
                m.save()
                d += timedelta(minutes=1)
        elif isinstance(period, RealTime):
            m, _ = Minute.objects.get_or_create(date=datetime(period.date.year, period.date.month, period.date.day, period.date.hour, period.date.minute).replace(tzinfo=timezone.utc), defaults={ "watts": 0 })
            m.calculate()
            m.save()

    class Meta:
        app_label = "electricity"
