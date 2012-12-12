from django.db import models

class HighestTemperatureRecord(models.Model):
    date = models.DateTimeField(db_index=True)

    indoor = models.BooleanField()

    temperature = models.FloatField(db_index=True)

    @staticmethod
    def update(row):
        if row.max_temp_in is not None:
            today = HighestTemperatureRecord.objects.filter(indoor=True, date=row.date)
            if len(today) > 0:
                if today[0].temperature < row.max_temp_in:
                    today[0].temperature = row.max_temp_in
                    today[0].save()
            elif HighestTemperatureRecord.objects.filter(indoor=True).count() < 5:
                HighestTemperatureRecord(date=row.date, indoor=True, temperature=row.max_temp_in).save()
            else:
                record = HighestTemperatureRecord.objects.filter(indoor=True).order_by("temperature")[0]

                if row.max_temp_in > record.temperature:
                    HighestTemperatureRecord(date=row.date, indoor=True, temperature=row.max_temp_in).save()
                    [r.delete() for r in HighestTemperatureRecord.objects.filter(indoor=True)[5:]]

        if row.max_temp_out is not None:
            today = HighestTemperatureRecord.objects.filter(indoor=False, date=row.date)
            if len(today) > 0:
                if today[0].temperature < row.max_temp_out:
                    today[0].temperature = row.max_temp_out
                    today[0].save()
            elif HighestTemperatureRecord.objects.filter(indoor=False).count() < 5:
                HighestTemperatureRecord(date=row.date, indoor=False, temperature=row.max_temp_out).save()
            else:
                record = HighestTemperatureRecord.objects.filter(indoor=False).order_by("temperature")[0]

                if row.max_temp_out > record.temperature:
                    HighestTemperatureRecord(date=row.date, indoor=False, temperature=row.max_temp_out).save()
                    [r.delete() for r in HighestTemperatureRecord.objects.filter(indoor=False)[5:]]

    class Meta:
        app_label = "app"
        ordering = ["-temperature"]

