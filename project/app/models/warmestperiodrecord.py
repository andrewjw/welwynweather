from django.db import models

class WarmestPeriodRecord(models.Model):
    start_date = models.DateTimeField(primary_key=True)
    end_date = models.DateTimeField()

    current = models.BooleanField()

    length = models.IntegerField()

    def calc_length(self):
        self.length = (self.end_date - self.start_date).days + 1

    @staticmethod
    def update(row):
        if row.max_temp_out < 27:
            return

        pd = row.prev_day()
        if pd is not None:
            current = WarmestPeriodRecord.objects.filter(end_date=pd.date)
            if current.count() > 0:
                current[0].end_date = row.date
                current[0].calc_length()
                current[0].save()
                return

        period = WarmestPeriodRecord(start_date=row.date, end_date=row.date)
        d = row.prev_day()
        while d is not None and d.max_temp_out >= 27:
            period.start_date = d.date
            d = d.prev_day()

        period.calc_length()
        
        records = WarmestPeriodRecord.objects.all().order_by("length")
        if records.count() < 5:
            period.save()
        elif period.length > records[0].length:
            period.save()
            [r.delete() for r in WarmestPeriodRecord.objects.all()[5:]]
    
    class Meta:
        app_label = "app"
        ordering = ["-length"]
