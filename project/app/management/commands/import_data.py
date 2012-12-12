import csv
import datetime
import glob
import os
import sys
import time

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc

from app.models import WeatherRow, HighestTemperatureRecord, LowestTemperatureRecord
from app.models import DriestPeriodRecord, WettestPeriodRecord, WettestDayRecord
from app.models import ColdestPeriodRecord, WarmestPeriodRecord
from app.models import ClimateMonth

class Command(BaseCommand):
    def handle(self, **options):
        do_import("/home/andrew/weather/data/raw/")

def do_import(data_dir):
    all_years = sorted(glob.glob(data_dir + os.sep + "*"))

    last_update = get_last_update()

    [import_year(data_dir, last_update, y.split("/")[-1]) for y in sorted(all_years) if int(y.split("/")[-1]) >= last_update.year]

def import_year(data_dir, last_update, year):
    all_months = sorted(glob.glob(data_dir + os.sep + year + os.sep + "*"))

    if int(year) == last_update.year:
        months = [m.split("/")[-1] for m in all_months if int(m.split("/")[-1].split("-")[1]) >= last_update.month]
    else:
        months = [m.split("/")[-1] for m in all_months]

    [import_month(data_dir, last_update, m.split("-")[0], m.split("-")[1]) for m in months]

def import_month(data_dir, last_update, year, month):
    all_days = sorted(glob.glob(data_dir + os.sep + year + os.sep + year + "-" + month + os.sep + "*"))

    if int(year) == last_update.year and int(month) == last_update.month:
        days = [d for d in all_days if d.split("/")[-1] >= last_update.strftime("%Y-%m-%d.txt")]
    else:
        days = all_days

    [import_day(filename, last_update) for filename in days]

def import_day(filename, last_update):
    fp = csv.reader(open(filename, "r"))

    first_day = True

    print filename
    for row in fp:
        update = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
        if update <= last_update:
            continue

        prev_rain = get_last_rain(update)
        if prev_rain is not None:
            rain = float(row[10]) - prev_rain if row[10] != '' else 0
            raw_rain = float(row[10]) if row[10] != '' else 0
        else:
            rain = 0
            raw_rain = 0

        if rain is not None and (rain < 0 or rain > 10):
            rain = 0

        try:
            obj = WeatherRow.objects.get(date=update)
        except WeatherRow.DoesNotExist:
            obj = WeatherRow(date=update)
        
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
        obj.status = int(row[11]) if row[11] else None
        obj.raw_rain = raw_rain

        obj.save()
        
        if first_day:
            d = obj.get_day().prev_day()
            if d != None:
                HighestTemperatureRecord.update(d)
                LowestTemperatureRecord.update(d)
                DriestPeriodRecord.update(d)
                WettestPeriodRecord.update(d)
                WettestDayRecord.update(d)
                ColdestPeriodRecord.update(d)
                WarmestPeriodRecord.update(d)
                ClimateMonth.update(d)

def get_last_update():
    try:
        return WeatherRow.objects.all().order_by("-date")[0].date
    except IndexError:
        return datetime.datetime(1900, 1, 1, tzinfo=utc)

def get_last_rain(date):
    last_update = WeatherRow.objects.filter(date__lt=date).order_by("-date")
    
    if last_update.count() == 0:
        return None
        
    return last_update[0].raw_rain

def totimestamp(dt):
    return time.mktime(dt.timetuple())
