from django.core.management.base import BaseCommand, CommandError

from app.models import *

class Command(BaseCommand):
    def handle(self, **options):
        WeatherRow.objects.all().delete()
        HourRow.objects.all().delete()
        DayRow.objects.all().delete()

        HighestTemperatureRecord.objects.all().delete()
        LowestTemperatureRecord.objects.all().delete()

        HighestPressureRecord.objects.all().delete()
        LowestPressureRecord.objects.all().delete()

        HeaviestRainRecord.objects.all().delete()

        StrongestGustRecord.objects.all().delete()
        StrongestWindRecord.objects.all().delete()

        DriestPeriodRecord.objects.all().delete()
        WettestPeriodRecord.objects.all().delete()
        WettestDayRecord.objects.all().delete()

        ColdestPeriodRecord.objects.all().delete()
        WarmestPeriodRecord.objects.all().delete()
        
        ClimateMonth.objects.all().delete()
