from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc
from django.conf import settings

from app.models import WeatherRow, HighestTemperatureRecord, LowestTemperatureRecord
from app.models import DriestPeriodRecord, WettestPeriodRecord, WettestDayRecord
from app.models import ColdestPeriodRecord, WarmestPeriodRecord
from app.models import ClimateMonth, DayRow, HeaviestRainRecord, HourRow
from app.models import StrongestWindRecord, StrongestGustRecord, HighestPressureRecord, LowestPressureRecord
from app.models import FastestChange

class Command(BaseCommand):
    def handle(self, *args, **options):
        StrongestWindRecord.update()
        StrongestGustRecord.update()
        HighestPressureRecord.update()
        LowestPressureRecord.update()
        HeaviestRainRecord.update()
        HighestTemperatureRecord.update()
        LowestTemperatureRecord.update()
        DriestPeriodRecord.update()
        WettestPeriodRecord.update()
        WettestDayRecord.update()
        ColdestPeriodRecord.update()
        WarmestPeriodRecord.update()
        FastestChange.update()
