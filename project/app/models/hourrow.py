from datetime import timedelta

from django.db import models
from django.conf import settings

dir_text_map = { 0: "North", 1: "NNE", 2: "North East", 3: "ENE",
    4: "East", 5: "ESE", 6: "South East", 7: "SSE", 8: "South",
    9: "SSW", 10: "South West", 11: "WSW", 12: "West", 13: "WNW", 14: "North West", 15: "NNW" }

class HourRow(models.Model):
    date = models.DateTimeField(primary_key=True)

    hum_in = models.FloatField()
    temp_in = models.FloatField()

    hum_out = models.FloatField(null=True, blank=True)
    temp_out = models.FloatField(null=True, blank=True)

    abs_pressure = models.FloatField()
    wind_ave = models.FloatField(null=True, blank=True)
    wind_gust = models.FloatField(null=True, blank=True)
    wind_dir = models.TextField(max_length=255)

    rain = models.FloatField()

    rained = models.BooleanField()

    status = models.IntegerField()

    @property
    def time(self):
        return self.date.strftime("%a %d, %I %p")

    @property
    def dir_text(self):
        items = eval(self.wind_dir).items()
        if len(items) == 0:
            return "N/A"
        items.sort(key=lambda x: -x[1])
        try:
            return dir_text_map[items[0][0]]
        except KeyError:
            return "N/A"

    def update(self):
        in_count, out_count = 0, 0

        hum_in, temp_in, hum_out, temp_out, abs_pressure, wind_ave, wind_gust, rain, status = 0, 0, 0, 0, 0, 0, 0, 0, 0
        wind_dir = {}
        for row in WeatherRow.objects.filter(date__gte=self.date, date__lt=self.date + timedelta(seconds=60*60)):
            in_count += 1
            hum_in += row.hum_in
            temp_in += row.temp_in
            abs_pressure += row.abs_pressure

            if row.temp_out is not None:
                out_count += 1
                temp_out += row.temp_out

                wind_gust = max(wind_gust, row.wind_gust)
                wind_ave += row.wind_ave
                wind_dir[row.wind_dir] = wind_dir.get(row.wind_dir, 0) + 1

                rain += row.rain

            if row.hum_out is not None:
                hum_out += row.hum_out

            status = max(status, row.status)

        self.hum_in = hum_in / in_count
        self.temp_in = temp_in / in_count
        self.abs_pressure = abs_pressure / in_count

        if out_count == 0:
            self.temp_out, self.hum_out, self.wind_gust, self.wind_ave = None, None, None, None
            self.wind_dir = "{}"
            self.rain = 0
        else:
            self.temp_out = temp_out / out_count
            self.hum_out = hum_out / out_count
            self.wind_gust = wind_gust
            self.wind_ave = wind_ave / out_count
            self.wind_dir = str(wind_dir)
            self.rain = rain

        self.rained = self.rain > 0

        self.status = status

        for update in settings.HOUR_ROW:
            if self.date >= update["start"] and self.date < update["end"]:
                update["func"](self)

        self.save()

    class Meta:
        app_label = "app"
        ordering = ["date"]

from weatherrow import WeatherRow
