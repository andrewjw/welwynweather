#!/usr/bin/python3

import csv
import datetime
import glob
import json
import os.path
import sys
from zoneinfo import ZoneInfo

def needs_update(srcfn, destfn):
    if not os.path.exists(destfn):
        return True
    src_mtime = os.path.getmtime(srcfn)
    dest_mtime = os.path.getmtime(destfn)
    this_mtime = os.path.getmtime(__file__)

    return dest_mtime < src_mtime or dest_mtime < this_mtime

def generate_day(day, destfn, prev_rain):
    data = []
    print(day)
    for row in csv.reader(open(day)):
        data_row = {
            "timestamp": row[0],
            "delay":  int(row[1]) if row[1] != '' else None,
            "hum_in": float(row[2]) if row[2] != '' else None,
            "temp_in": float(row[3]) if row[3] != '' else None,
            "hum_out": float(row[4]) if row[4] != '' else None,
            "temp_out": float(row[5]) if row[5] != '' else None,
            "abs_pressure": float(row[6]) if row[6] != '' else None,
            "wind_ave": float(row[7]) if row[7] != '' else None,
            "wind_gust": float(row[8]) if row[8] != '' else None,
            "wind_dir": int(row[9]) if row[9] != '' else None,
            "rain": min(float(row[10]) - prev_rain, 0) if row[10] != '' else 0,
            "status": int(row[11]) if row[11] else None,
        }

        prev_rain = float(row[10])
        data.append(data_row)

    has_outside_data = len([d["temp_out"] for d in data if d["temp_out"] is not None]) > 0

    summary = {
        "date": day.split("/")[-1].split(".")[0],
        "max_temp_in": max([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "min_temp_in": min([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "max_temp_out": max([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "min_temp_out": min([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "rain": sum(d["rain"] for d in data),
        "end_rain": prev_rain
    }

    json.dump({ "summary": summary, "data": data }, open(destfn, "w"))

    return prev_rain

def generate_month(year, month, day_files, destfn):
    hours = []
    last_hour = None
    rain = 0
    for day_file in sorted(glob.glob(os.path.join(day_files, "*.json"))):
        for row in json.load(open(day_file))["data"]:
            if last_hour is None or last_hour != parse_date(row["timestamp"]).hour:
                last_hour = parse_date(row["timestamp"]).hour

                row["rain"] += rain

                hours.append(row)
            else:
                rain += row["rain"]

    summary = {
        "month": f"%s %s" % (month, year)
    }

    json.dump({ "summary": summary, "data": hours}, open(destfn, "w"))

def generate_year(year, day_files, destfn):
    days = []
    for day_file in sorted(glob.glob(os.path.join(day_files, "*", "*.json"))):
        days.append(json.load(open(day_file))["summary"])

    summary = {
        "year": str(year),
        "max_temp_in": max([d["max_temp_in"] for d in days if d["max_temp_in"] is not None]),
        "min_temp_in": min([d["min_temp_in"] for d in days if d["min_temp_in"] is not None]),
        "max_temp_out": max([d["max_temp_out"] for d in days if d["max_temp_out"] is not None]),
        "min_temp_out": min([d["min_temp_out"] for d in days if d["min_temp_out"] is not None]),
    }

    links = {}

    if int(year) > 2011:
        links["prev"] = f"/{ int(year) - 1}"
        links["prev_text"] = f"{ int(year) - 1}"
    if int(year) < datetime.date.today().year:
        links["next"] = f"/{ int(year) + 1}"
        links["next_text"] = f"{ int(year) + 1}"

    json.dump({ "summary": summary, "data": days, "links": links}, open(destfn, "w"))

def generate_recent(dest, destfn, last_day):
    last_day = datetime.date(int(last_day.split("-")[0]), int(last_day.split("-")[1]), int(last_day.split("-")[2]))
    last_day -= datetime.timedelta(days=1)

    data = json.load(open(os.path.join(dest, str(last_day.year), "%02i" % (last_day.month,), "%02i.json" % (last_day.day, ))))["data"]

    last_day += datetime.timedelta(days=1)
    data.extend(json.load(open(os.path.join(dest, str(last_day.year), "%02i" % (last_day.month,), "%02i.json" % (last_day.day, ))))["data"])

    last_time = parse_date(data[-1]["timestamp"])

    data = [row for row in data if parse_date(row["timestamp"]) > last_time - datetime.timedelta(days=1)]

    has_outside_data = len([d["temp_out"] for d in data if d["temp_out"] is not None]) > 0

    summary = {
        "max_temp_in": max([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "min_temp_in": min([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "max_temp_out": max([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "min_temp_out": min([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "rain": sum(d["rain"] for d in data),
    }

    json.dump({ "summary": summary, "data": data }, open(destfn, "w"))


def parse_date(d):
    return datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").replace(tzinfo=ZoneInfo("UTC"))

def main():
    source = sys.argv[1]
    dest = sys.argv[2]

    last_day = None
    prev_rain = 0
    print(os.path.join(source, "raw/*"))
    for year in sorted(glob.glob(os.path.join(source, "raw/*"))):
        year_needs_update = False
        for month in sorted(glob.glob(f"{year}/*")):
            month_needs_update = False
            for day in sorted(glob.glob(f"{month}/2*")):
                last_day = day
                if not os.path.exists(os.path.join(dest, year.split("/")[-1])):
                    os.mkdir(os.path.join(dest, year.split("/")[-1]))
                if not os.path.exists(os.path.join(dest, year.split("/")[-1], month.split("-")[-1])):
                    os.mkdir(os.path.join(dest, year.split("/")[-1], month.split("-")[-1]))
                destfn = os.path.join(dest, year.split("/")[-1], month.split("-")[-1], day.split("-")[-1].split(".")[0] + ".json")

                if needs_update(day, destfn):
                    prev_rain = generate_day(day, destfn, prev_rain)
                    year_needs_update = month_needs_update = True
                else:
                    prev_rain = json.load(open(destfn))["summary"]["end_rain"]

            if month_needs_update:
                destfn = os.path.join(dest, year.split("/")[-1], month.split("-")[-1] + ".json")
                generate_month(year.split("/")[-1], month.split("-")[-1], os.path.join(dest, year.split("/")[-1], month.split("-")[-1]), destfn)

        if year_needs_update:
            destfn = os.path.join(dest, year.split("/")[-1] + ".json")
            generate_year(year.split("/")[-1], os.path.join(dest, year.split("/")[-1]), destfn)

    if last_day is not None:
        open(os.path.join(dest, "today.json"), "w").write(last_day.split("/")[-1].split(".")[0])

    generate_recent(dest, os.path.join(dest, "recent.json"), last_day.split("/")[-1].split(".")[0])

if __name__ == "__main__":
    main()
