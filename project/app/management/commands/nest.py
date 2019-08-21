import cProfile
import csv
import datetime
import glob
import os
import sys
import time
import pytz
import zipfile

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import utc
from django.conf import settings

from app.models import NestSensors

class Command(BaseCommand):
    def handle(self, *args, **options):
        do_import(options["path"])

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str, default=None)

def do_import(fp):
    z = zipfile.ZipFile(fp)

    for info in z.infolist():
        if "NEST_DATA/Nest/thermostats/" in info.filename:
            if "-sensors.csv" in info.filename:
                import_sensors(csv.reader(z.open(info.filename)))
            elif "-summary.json" in info.filename:
                print info.filename

def import_sensors(fp):
    fp.next() # skip header
    for row in fp:
        year, month, day = map(int, row[0].split("-"))
        hour, minute = map(int, row[1].split(":"))
        d = datetime.datetime(year, month, day, hour, minute, tzinfo=pytz.utc)

        if len(NestSensors.objects.filter(date=d)) > 0:
            dbrow = NestSensors.objects.filter(date=d)[0]
        else:
            dbrow = NestSensors(date=d)

        dbrow.avg_temp = float(row[2])
        dbrow.avg_humidity = float(row[3])
        dbrow.max_pir = float(row[4])
        dbrow.max_nearPir = float(row[5]) if len(row[5]) > 0 else None

        dbrow.min_ch1 = float(row[6]) if len(row[6]) > 0 else None
        dbrow.max_ch1 = float(row[7]) if len(row[7]) > 0 else None
        dbrow.min_ch2 = float(row[8]) if len(row[8]) > 0 else None
        dbrow.max_ch2 = float(row[9]) if len(row[9]) > 0 else None
        dbrow.min_als = float(row[10])
        dbrow.max_als = float(row[11])

        dbrow.min_tp0 = float(row[12])
        dbrow.max_tp0 = float(row[13])
        dbrow.min_tp1 = float(row[14])
        dbrow.max_tp1 = float(row[15])
        dbrow.min_tp2 = float(row[16])
        dbrow.max_tp2 = float(row[17])
        dbrow.min_tp3 = float(row[18])
        dbrow.max_tp3 = float(row[19])

        dbrow.save()
