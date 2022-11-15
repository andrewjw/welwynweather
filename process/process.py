#!/usr/bin/python3

import csv
import datetime
import glob
import json
import os.path
from statistics import mean
import sys
from zoneinfo import ZoneInfo

def needs_update(srcfn, destfn):
    if not os.path.exists(destfn):
        return True
    src_mtime = os.path.getmtime(srcfn) if srcfn is not None else os.path.getmtime(destfn)
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

    day_string = day.split("/")[-1].split(".")[0]
    summary = {
        "date": day_string,
        "link": f"/%s/%s/%s" % tuple(day_string.split("-")),
        "max_temp_in": max([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "min_temp_in": min([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "avg_temp_in": mean([d["temp_in"] for d in data if d["temp_in"] is not None]),
        "max_temp_out": max([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "min_temp_out": min([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "avg_temp_out": mean([d["temp_out"] for d in data if d["temp_out"] is not None]) if has_outside_data else None,
        "rain": sum(d["rain"] for d in data),
        "end_rain": prev_rain
    }

    json.dump({ "summary": summary, "data": data }, open(destfn, "w"))

    return prev_rain

def generate_month(year, month, day_files, destfn):
    hours = []
    temp_in, temp_out = [], []
    last_hour = None
    rain = 0
    for day_file in sorted(glob.glob(os.path.join(day_files, "*.json"))):
        for row in json.load(open(day_file))["data"]:
            if row["temp_in"] is not None:
                temp_in.append(row["temp_in"])
            if row["temp_out"] is not None:
                temp_out.append(row["temp_out"])
            if last_hour is None or last_hour != parse_date(row["timestamp"]).hour:
                last_hour = parse_date(row["timestamp"]).hour

                row["rain"] += rain

                hours.append(row)
            else:
                rain += row["rain"]

    summary = {
        "month": f"%s %s" % (month, year),
        "max_temp_in": max(temp_in),
        "min_temp_in": min(temp_in),
        "avg_temp_in": mean(temp_in),
        "max_temp_out": max(temp_out),
        "min_temp_out": min(temp_out),
        "avg_temp_out": mean(temp_out),
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
        "avg_temp_in": mean([d["avg_temp_in"] for d in days if d["avg_temp_in"] is not None]),
        "max_temp_out": max([d["max_temp_out"] for d in days if d["max_temp_out"] is not None]),
        "min_temp_out": min([d["min_temp_out"] for d in days if d["min_temp_out"] is not None]),
        "avg_temp_out": mean([d["avg_temp_out"] for d in days if d["avg_temp_out"] is not None]),
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

def guess_year_avg(dest, year):
    d = datetime.date(year, 1, 1)
    temp_out = []
    while d.year == year:
        dayfn = os.path.join(dest, str(d.year), "%02i" % (d.month, ), "%02i.json" % (d.day, ))
        if os.path.exists(dayfn):
            temp_out.append(json.load(open(dayfn))["summary"]["avg_temp_out"])
        else:
            past_temp_out = []
            for past_year in range(2011, d.year):
                pastdayfn = os.path.join(dest, str(past_year), "%02i" % (d.month, ), "%02i.json" % (d.day, ))
                if os.path.exists(pastdayfn):
                    past_temp_out.append(json.load(open(pastdayfn))["summary"]["avg_temp_out"])
            temp_out.append(mean([t for t in past_temp_out if t is not None]))

        d += datetime.timedelta(days=1)
    return mean(temp_out)

def generate_climate(dest, destfn):
    years, months = [], []
    for year in sorted(glob.glob(os.path.join(dest, "2*.json"))):
        year_num = year.split("/")[-1].split(".")[0]
        if year_num != "2021":
            years.append({ "year": year_num, "avg_temp_out": json.load(open(year))["summary"]["avg_temp_out"]})
        else:
            years.append({ "year": "2021", "avg_temp_out": guess_year_avg(dest, 2021)})

        avg_temp_out = []
        months.append({ "year": year_num, "avg_temp_out": avg_temp_out})
        for month in sorted(glob.glob(os.path.join(dest, year_num, "*.json"))):
            avg_temp_out.append(json.load(open(month))["summary"]["avg_temp_out"])

    json.dump({ "years": years, "months": months }, open(destfn, "w"))

class TopFive:
    def __init__(self, reverse=False):
        self.reverse = reverse
        self.values = []

    def add(self, value, link, link_text):
        if value is None:
            return
        self.values.append({ "value": value, "link": link, "link_text": link_text })
        self.values.sort(key=lambda v: v["value"], reverse=self.reverse)

        values = []
        text = set()
        for v in self.values:
            if v["link_text"] not in text:
                values.append(v)
                text.add(v["link_text"])

        self.values = values[:5]

def generate_records(dest, destfn):
    max_temp_out = TopFive(True)
    min_temp_out = TopFive()

    for year in sorted(glob.glob(os.path.join(dest, "2*.json"))):
        year_num = year.split("/")[-1].split(".")[0]
        for month in sorted(glob.glob(os.path.join(dest, year_num, "*.json"))):
            month_num = month.split("/")[-1].split(".")[0]
            for day in sorted(glob.glob(os.path.join(dest, year_num, month_num, "*.json"))):
                day_json = json.load(open(day))
                for row in day_json["data"]:
                    if row["temp_out"] is not None:
                        max_temp_out.add(row["temp_out"], day_json["summary"]["link"], day_json["summary"]["date"])
                        min_temp_out.add(row["temp_out"], day_json["summary"]["link"], day_json["summary"]["date"])
    
    json.dump({ "max_temp_out": max_temp_out.values, "min_temp_out": min_temp_out.values}, open(destfn, "w"))

def parse_date(d):
    return datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").replace(tzinfo=ZoneInfo("UTC"))

def main():
    source = sys.argv[1]
    dest = sys.argv[2]

    last_day = None
    new_day = False
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

                new_day = new_day or not os.path.exists(destfn)

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

    climatefn = os.path.join(dest, "climate.json")
    if needs_update(None, climatefn) or new_day:
        generate_climate(dest, climatefn)

    recordsfn = os.path.join(dest, "records.json")
    if needs_update(None, recordsfn) or new_day:
        generate_records(dest, recordsfn)

if __name__ == "__main__":
    main()
