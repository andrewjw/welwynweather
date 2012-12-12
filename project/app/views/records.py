from datetime import date

from django.shortcuts import render_to_response

from app.models import HighestTemperatureRecord, LowestTemperatureRecord
from app.models import HighestPressureRecord, LowestPressureRecord
from app.models import HeaviestRainRecord, StrongestGustRecord, StrongestWindRecord
from app.models import DriestPeriodRecord, WettestPeriodRecord, WettestDayRecord
from app.models import WarmestPeriodRecord, ColdestPeriodRecord

def records(req):
    context = {
            "today": date.today(),
            "highest_temp_in": HighestTemperatureRecord.objects.filter(indoor=True),
            "highest_temp_out": HighestTemperatureRecord.objects.filter(indoor=False),
            "lowest_temp_in": LowestTemperatureRecord.objects.filter(indoor=True),
            "lowest_temp_out": LowestTemperatureRecord.objects.filter(indoor=False),
            "highest_pressure": HighestPressureRecord.objects.all(),
            "lowest_pressure": LowestPressureRecord.objects.all(),
            "heaviest_rain": HeaviestRainRecord.objects.all(),
            "strongest_gust": StrongestGustRecord.objects.all(),
            "strongest_wind": StrongestWindRecord.objects.all(),
            "driest_period": DriestPeriodRecord.objects.all(),
            "wettest_period": WettestPeriodRecord.objects.all(),
            "wettest_day": WettestDayRecord.objects.all(),
            "warmest_period": WarmestPeriodRecord.objects.all(),
            "coldest_period": ColdestPeriodRecord.objects.all()
        }

    return render_to_response("html/records.html", context)
