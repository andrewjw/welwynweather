from django.db import models

class MonthRow(models.Model):
    date = models.DateTimeField(primary_key=True)
    timestamp = models.IntegerField(),
    delay = models.IntegerField(null=True, blank=True)

    max_hum_in = models.FloatField()
    min_hum_in = models.FloatField()
    max_temp_in = models.FloatField()
    min_temp_in = models.FloatField()

    max_hum_out = models.FloatField()
    min_hum_out = models.FloatField()
    max_temp_out = models.FloatField()
    min_temp_out = models.FloatField()

    abs_pressure = models.FloatField()
    wind_ave = models.FloatField()
    max_wind_gust = models.FloatField()
    wind_dir = models.IntegerField()

    rain = models.FloatField()

    rained = models.BooleanField()

    status = models.IntegerField()

    def update(self):
        return
    
    class Meta:
        app_label = "app"
