from datetime import date

from django.shortcuts import render_to_response

from app.models import HighestTemperatureRecord, LowestTemperatureRecord
from app.models import HighestPressureRecord, LowestPressureRecord
from app.models import HeaviestRainRecord, StrongestGustRecord, StrongestWindRecord
from app.models import DriestPeriodRecord, WettestPeriodRecord, WettestDayRecord
from app.models import WarmestPeriodRecord, ColdestPeriodRecord, FastestChange

def records(req):
    context = {
            "today": date.today(),
            "highest_temp_in": HighestTemperatureRecord.objects.filter(indoor=True),
            "highest_temp_out": HighestTemperatureRecord.objects.filter(indoor=False, lowest=False),
            "lowest_high_temp_out": HighestTemperatureRecord.objects.filter(indoor=False, lowest=True).order_by("temperature"),
            "lowest_temp_in": LowestTemperatureRecord.objects.filter(indoor=True),
            "lowest_temp_out": LowestTemperatureRecord.objects.filter(indoor=False, highest=False),
            "highest_low_temp_out": LowestTemperatureRecord.objects.filter(indoor=False, highest=True).order_by("-temperature"),
            "highest_pressure": HighestPressureRecord.objects.all(),
            "lowest_pressure": LowestPressureRecord.objects.all(),
            "heaviest_rain": HeaviestRainRecord.objects.all(),
            "strongest_gust": StrongestGustRecord.objects.all(),
            "strongest_wind": StrongestWindRecord.objects.all(),
            "driest_period": DriestPeriodRecord.objects.all(),
            "wettest_period": WettestPeriodRecord.objects.all(),
            "wettest_day": WettestDayRecord.objects.all(),
            "warmest_period": WarmestPeriodRecord.objects.all(),
            "coldest_period": ColdestPeriodRecord.objects.all(),
            "fastest_pos_temperature": FastestChange.objects.filter(temperature=True, positive=True).order_by("-value"),
            "fastest_neg_temperature": FastestChange.objects.filter(temperature=True, positive=False).order_by("value"),
            "fastest_pos_pressure": FastestChange.objects.filter(temperature=False, positive=True).order_by("-value"),
            "fastest_neg_pressure": FastestChange.objects.filter(temperature=False, positive=False).order_by("value")
        }

    return render_to_response("html/records.html", context)
