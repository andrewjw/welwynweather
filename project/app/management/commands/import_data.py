import cProfile
import csv
import datetime
import glob
import os
import sys
import time

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc
from django.conf import settings

from app.models import WeatherRow, HighestTemperatureRecord, LowestTemperatureRecord
from app.models import DriestPeriodRecord, WettestPeriodRecord, WettestDayRecord
from app.models import ColdestPeriodRecord, WarmestPeriodRecord
from app.models import ClimateMonth, DayRow, HeaviestRainRecord, HourRow
from app.models import StrongestWindRecord, StrongestGustRecord, HighestPressureRecord, LowestPressureRecord
from app.models import MonthRow, ClimateByMonth, YearRow, ClimateByYear
from app.models import FastestChange

class Command(BaseCommand):
    def handle(self, *args, **options):
        #p = cProfile.Profile()
        #p.runcall(do_import, options["path"][0] if options["path"] else "/home/andrew/weather/data/raw/")
        #p.print_stats("cumulative")
        if options["since"] is not None:
            WeatherRow.objects.filter(date__year__gte=options["since"]).delete()
            HourRow.objects.filter(date__year__gte=options["since"]).delete()
            DayRow.objects.filter(date__year__gte=options["since"]).delete()
            MonthRow.objects.filter(date__year__gte=options["since"]).delete()
            YearRow.objects.filter(date__year__gte=options["since"]).delete()

        do_import(options["path"] if options["path"] else "/home/andrew/weather/data/raw/")

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str, default=None)
        parser.add_argument('since', nargs='?', type=int, default=None)

def do_import(data_dir):
    all_years = sorted(glob.glob(data_dir + os.sep + "*"))

    last_update = get_last_update()

    for y in sorted(all_years):
        if int(y.split("/")[-1]) >= last_update.year:
            import_year(data_dir, last_update, y.split("/")[-1])

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

def import_year(data_dir, last_update, year):
    all_months = sorted(glob.glob(data_dir + os.sep + year + os.sep + "*"))

    if int(year) == last_update.year:
        months = [m.split("/")[-1] for m in all_months if int(m.split("/")[-1].split("-")[1]) >= last_update.month]
    else:
        months = [m.split("/")[-1] for m in all_months]

    for m in months:
        last_day = import_month(data_dir, last_update, m.split("-")[0], m.split("-")[1])

    if last_day is not None:
        YearRow.update(last_day)
        ClimateByYear.update(last_day)

def import_month(data_dir, last_update, year, month):
    all_filenames = sorted(glob.glob(data_dir + os.sep + year + os.sep + year + "-" + month + os.sep + "*"))

    if int(year) == last_update.year and int(month) == last_update.month:
        filenames = [d for d in all_filenames if d.split("/")[-1] >= last_update.strftime("%Y-%m-%d.txt")]
    else:
        filenames = all_filenames

    for filename in filenames:
        last_day = import_day(filename, last_update)

    if last_day is not None:
        MonthRow.update(last_day)
        ClimateMonth.update(last_day)
        ClimateByMonth.update(last_day)

    return last_day

def import_day(filename, last_update):
    fp = csv.reader(open(filename, "r"))

    obj, last_obj = None, None
    print filename
    hours = set()

    prev_rain = get_last_rain(last_update)

    for row in fp:
        update = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
        day = update.date()
        if update <= last_update:
            continue

        if prev_rain is not None:
            rain = float(row[10]) - prev_rain if row[10] != '' else 0
        else:
            rain = 0

        raw_rain = float(row[10]) if row[10] != '' else 0
        prev_rain = raw_rain if raw_rain != 0 else prev_rain

        if rain is not None and (rain < 0 or rain > 10):
            rain = 0

        obj = WeatherRow(date=update)

        hours.add(obj.get_hour_time())

        obj.timestamp = totimestamp(update)
        obj.delay = int(row[1]) if row[1] != '' else None
        obj.hum_in = float(row[2]) if row[2] != '' else None
        obj.temp_in = float(row[3]) if row[3] != '' else None
        obj.hum_out = float(row[4]) if row[4] != '' else None
        obj.temp_out = float(row[5]) if row[5] != '' else None
        obj.abs_pressure = float(row[6]) if row[6] != '' else None
        obj.wind_ave = float(row[7]) if row[7] != '' else None
        obj.wind_gust = float(row[8]) if row[8] != '' else None
        obj.wind_dir = int(row[9]) if row[9] != '' else None
        obj.rain = rain
        obj.is_raining = rain > 0
        obj.status = int(row[11]) if row[11] else None
        obj.raw_rain = raw_rain

        for update_spec in settings.RAW_DATA:
            if update >= update_spec["start"] and update < update_spec["end"]:
                r = update_spec["func"](obj)
                if r is None:
                    raise Exception()
                if not r:
                    obj.date = None

        if obj.date is not None:
            obj.save()
            last_obj = obj

    for hour in hours:
        try:
            hourobj = HourRow.objects.get(date=hour)
        except HourRow.DoesNotExist:
            hourobj = HourRow(date=hour)
        hourobj.update()

    return None if last_obj is None else last_obj.get_day().update()

def get_last_update():
    try:
        return WeatherRow.objects.all().order_by("-date")[0].date
    except IndexError:
        return datetime.datetime(1900, 1, 1, tzinfo=utc)

def get_last_rain(date):
    last_update = WeatherRow.objects.filter(date__lte=date).order_by("-date")

    if last_update.count() == 0:
        return None

    return last_update[0].raw_rain

def totimestamp(dt):
    return time.mktime(dt.timetuple())
