from datetime import timedelta

from django.db import models

class DayRow(models.Model):
    date = models.DateTimeField(primary_key=True)

    avg_temp_in = models.FloatField()
    avg_temp_out = models.FloatField()

    max_hum_in = models.FloatField()
    min_hum_in = models.FloatField()
    max_temp_in = models.FloatField()
    min_temp_in = models.FloatField()

    max_hum_out = models.FloatField(null=True, blank=True)
    min_hum_out = models.FloatField(null=True, blank=True)
    max_temp_out = models.FloatField(null=True, blank=True)
    min_temp_out = models.FloatField(null=True, blank=True)

    abs_pressure = models.FloatField()
    wind_ave = models.FloatField(null=True, blank=True)
    max_wind_gust = models.FloatField(null=True, blank=True)
    wind_dir = models.TextField(max_length=255)

    rain = models.FloatField()

    rained = models.BooleanField()

    status = models.IntegerField()

    @property
    def wind_dir_list(self):
        obj = eval(self.wind_dir)
        return [obj.get(key, 0) for key in range(0, 16, 2)]

    @property
    def time(self):
        return self.date.strftime("%b %d")

    def prev_day(self):
        try:
            return DayRow.objects.get(date=self.date - timedelta(days=1))
        except DayRow.DoesNotExist:
            return None

    def update(self):
        first_in, first_out = True, True
        pressure = []
        wind_ave = []
        wind_dir = {}
        temp_in = 0
        temp_out = 0
        self.rain = 0
        self.status = 0

        count = 0
        for row in WeatherRow.objects.filter(date__gte=self.date, date__lt=self.date + timedelta(seconds=24*60*60)):
            count += 1
            if first_in:
                self.max_hum_in, self.min_hum_in = row.hum_in, row.hum_in
                self.max_temp_in, self.min_temp_in = row.temp_in, row.temp_in
                temp_in = row.temp_in
                first_in = False
            else:
                self.max_hum_in = max(self.max_hum_in, row.hum_in)
                self.min_hum_in = min(self.min_hum_in, row.hum_in)
                self.max_temp_in = max(self.max_temp_in, row.temp_in)
                self.min_temp_in = min(self.min_temp_in, row.temp_in)
                temp_in += row.temp_in

            if row.contact and first_out:
                self.max_hum_out, self.min_hum_out = row.hum_out, row.hum_out
                self.max_temp_out, self.min_temp_out = row.temp_out, row.temp_out
                self.max_wind_gust = row.wind_gust
                temp_out = row.temp_out
                first_out = False
            elif row.contact:
                self.max_hum_out = max(self.max_hum_out, row.hum_out)
                self.min_hum_out = min(self.min_hum_out, row.hum_out)
                self.max_temp_out = max(self.max_temp_out, row.temp_out)
                self.min_temp_out = min(self.min_temp_out, row.temp_out)
                self.max_wind_gust = max(self.max_wind_gust, row.wind_gust)
                temp_out += row.temp_out

            pressure.append(row.abs_pressure)
            if row.contact:
                wind_ave.append(row.wind_ave)
                wind_dir[row.wind_dir] = wind_dir.get(row.wind_dir, 0) + 1
                self.rain += row.rain

            self.status = max(self.status, row.status)

        self.avg_temp_in = temp_in / count
        self.avg_temp_out = temp_out / count

        self.abs_pressure = sum(pressure) / len(pressure)
        if len(wind_ave) > 0:
            self.wind_ave = sum(wind_ave) / len(wind_ave)
        else:
            self.wind_ave = None
        self.wind_dir = str(wind_dir)
        self.rained = self.rain > 0

        self.save()

        MonthRow.update(self)

    class Meta:
        app_label = "app"
        ordering = ["date"]

from weatherrow import WeatherRow
from monthrow import MonthRow
