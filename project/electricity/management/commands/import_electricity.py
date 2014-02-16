import csv
import datetime
import glob
import os
import sys
import time

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc

from electricity.models import RealTime, Hourly, Daily, Monthly, Minute

class Command(BaseCommand):
    def handle(self, **options):
        do_import("/home/andrew/cc128/data/")

def do_import(data_dir):
    all_years = [x for x in sorted(glob.glob(data_dir + os.sep + "*")) if "." not in x]

    last_update = get_last_update()

    [import_year(data_dir, last_update, y.split("/")[-1]) for y in sorted(all_years) if int(y.split("/")[-1]) >= last_update.year]

def import_year(data_dir, last_update, year):
    print year
    all_months = sorted(glob.glob(data_dir + os.sep + year + os.sep + "*"))

    if int(year) == last_update.year:
        months = [m.split("/")[-1] for m in all_months if ".csv" not in m and int(m.split("/")[-1].split("-")[1]) >= last_update.month]
    else:
        months = [m.split("/")[-1] for m in all_months]

    [import_month(data_dir, last_update, m.split("-")[0], m.split("-")[1]) for m in months if ".csv" not in m]

def import_month(data_dir, last_update, year, month):
    print year, month
    all_days = sorted(glob.glob(data_dir + os.sep + year + os.sep + year + "-" + month + os.sep + "*"))

    print "/home/andrew/cc128/data/%s.csv" % (year, )
    fp = csv.reader(open("/home/andrew/cc128/data/%s.csv" % (year, )))
    for row in fp:
        db, create = Monthly.objects.get_or_create(date=getdate(row[0]), defaults={ "kwh": float(row[1]) })
        db.kwh = float(row[1])
        db.save()
        if create:
            Minute.update(db)

    print "/home/andrew/cc128/data/%s/%s-%s.csv" % (year, year, month)
    fp = csv.reader(open("/home/andrew/cc128/data/%s/%s-%s.csv" % (year, year, month)))
    for row in fp:
        db, create = Daily.objects.get_or_create(date=getdate(row[0]), defaults={ "kwh": float(row[1]) })
        db.kwh = float(row[1])
        db.save()
        if create:
            Minute.update(db)

    if int(year) == last_update.year and int(month) == last_update.month:
        days = [d for d in all_days if d.split("/")[-1] >= last_update.strftime("%Y-%m-%d")]
    else:
        days = all_days

    [import_day(filename, last_update) for filename in days]

def import_day(filename, last_update):
    print filename

    if "_hourly" in filename:
        fp = csv.reader(open(filename, "r"))

        for row in fp:
            db, create = Hourly.objects.get_or_create(date=getdate(row[0]), defaults={ "kwh": float(row[1]) })
            db.kwh = float(row[1])
            db.save()
            if create:
                Minute.update(db)
    else:
        fp = csv.reader(open(filename, "r"))

        for row in fp:
            date = getdate(row[0])
            if date < last_update:
                continue
            db, create = RealTime.objects.get_or_create(date=getdate(row[0]), defaults={ "temperature": float(row[2]), "watts": int(row[3]) })
            db.temperature = float(row[2])
            db.watts = int(row[3])
            db.save()
            if create:
                Minute.update(db)

def get_last_update():
    try:
        return RealTime.objects.all().order_by("-date")[0].date
    except IndexError:
        return datetime.datetime(1900, 1, 1, tzinfo=utc)

def get_last_rain(date):
    last_update = WeatherRow.objects.filter(date__lt=date).order_by("-date")
    
    if last_update.count() == 0:
        return None
        
    return last_update[0].raw_rain

def totimestamp(dt):
    return time.mktime(dt.timetuple())

def getdate(string):
    return datetime.datetime.strptime(string.split(".")[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=utc)
