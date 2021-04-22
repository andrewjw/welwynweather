from datetime import timedelta

from django.db import models

from app.models import WeatherRow

class FastestChange(models.Model):
    date = models.DateTimeField(db_index=True)

    temperature = models.BooleanField(default=True)

    positive = models.BooleanField(default=True)

    value = models.FloatField(db_index=True)

    end = models.DateTimeField()

    @staticmethod
    def update():
        temp_positives, temp_negatives = [], []
        pressure_positives, pressure_negatives = [], []
        last_temp_positive, last_temp_negative = None, None
        last_pressure_positive, last_pressure_negative = None, None

        history = []
        row_count = WeatherRow.objects.count()
        print "Loading", row_count, "rows"
        for offset in range(0, row_count, 1000):
            for row in WeatherRow.objects.all()[offset:offset+1000]:
                history.append(row)
                while history[0].date < row.date - timedelta(hours=1):
                    del history[0]

                first_temp_out = None
                for h in history:
                    if h.temp_out is not None:
                        first_temp_out = h
                        break

                last_temp_out = None
                for h in history[::-1]:
                    if h.temp_out is not None:
                        last_temp_out = h
                        break

                if last_temp_out is not None and first_temp_out.temp_out < last_temp_out.temp_out:
                    if last_temp_negative is not None:
                        temp_negatives.append(last_temp_negative)
                        last_temp_negative = None

                    if last_temp_positive is None or (last_temp_out.temp_out - first_temp_out.temp_out) > last_temp_positive.value:
                        last_temp_positive = FastestChange(date=FastestChange.get_date(history[0]), temperature=True, positive=True, value=last_temp_out.temp_out - first_temp_out.temp_out, end=history[-1].date)
                elif last_temp_out is not None and first_temp_out.temp_out > last_temp_out.temp_out:
                    if last_temp_positive is not None:
                        temp_positives.append(last_temp_positive)
                        last_temp_positive = None

                    if last_temp_negative is None or (last_temp_out.temp_out - first_temp_out.temp_out) < last_temp_negative.value:
                        last_temp_negative = FastestChange(date=FastestChange.get_date(history[0]), temperature=True, positive=False, value=last_temp_out.temp_out - first_temp_out.temp_out, end=history[-1].date)

                if history[0].abs_pressure < history[-1].abs_pressure:
                    if last_pressure_negative is not None:
                        pressure_negatives.append(last_pressure_negative)
                        last_pressure_negative = None

                    if last_pressure_positive is None or (history[-1].abs_pressure - history[0].abs_pressure) > last_pressure_positive.value:
                        last_pressure_positive = FastestChange(date=FastestChange.get_date(history[0]), temperature=False, positive=True, value=history[-1].abs_pressure - history[0].abs_pressure, end=history[-1].date)
                elif history[0].abs_pressure > history[-1].abs_pressure:
                    if last_pressure_positive is not None:
                        pressure_positives.append(last_pressure_positive)
                        last_pressure_positive = None

                    if last_pressure_negative is None or (history[-1].abs_pressure - history[0].abs_pressure) < last_pressure_negative.value:
                        last_pressure_negative = FastestChange(date=FastestChange.get_date(history[0]), temperature=False, positive=False, value=history[-1].abs_pressure - history[0].abs_pressure, end=history[-1].date)

        if last_temp_negative is not None:
            temp_negatives.append(last_temp_negative)
        if last_temp_positive is not None:
            temp_positives.append(last_temp_positive)
        if last_pressure_negative is not None:
            pressure_negatives.append(last_pressure_negative)
        if last_pressure_positive is not None:
            pressure_positives.append(last_pressure_positive)

        FastestChange.objects.all().delete()

        print len(temp_positives)
        print len(temp_negatives)
        print len(pressure_positives)
        print len(pressure_negatives)
        temp_positives.sort(key=lambda x: -x.value)
        [x.save() for x in temp_positives[:5]]
        temp_negatives.sort(key=lambda x: x.value)
        [x.save() for x in temp_negatives[:5]]
        pressure_positives.sort(key=lambda x: -x.value)
        [x.save() for x in pressure_positives[:5]]
        pressure_negatives.sort(key=lambda x: x.value)
        for fc in pressure_negatives[:5]:
            print fc.date, fc.temperature, fc.positive, fc.value, fc.end
        [x.save() for x in pressure_negatives[:5]]

    @staticmethod
    def get_date(history):
        if history.date.minute == 0:
            return history
        else:
            return history.date.replace(minute=0) + timedelta(hours=1)

    class Meta:
        app_label = "app"
        ordering = ["value"]
