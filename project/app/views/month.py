from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response
from django.utils import timezone

from app.models import HourRow, DayRow, MonthRow, ClimateByMonth

def month(req, year, month):
    try:
        date = datetime(int(year), int(month), 1).replace(tzinfo=timezone.utc)
    except ValueError:
        raise Http404

    next_month = date
    while next_month.month == date.month:
        next_month += timedelta(days=1)

    dayrows = DayRow.objects.filter(date__gte=date, date__lt=next_month)
    rows = HourRow.objects.filter(date__gte=date, date__lt=next_month)

    if len(rows) == 0:
        raise Http404

    prev_month = date - timedelta(days=1)
    if DayRow.objects.filter(date__year=prev_month.year, date__month=prev_month.month).count() == 0:
        prev_month = None

    next_month = date + timedelta(days=1)
    while next_month.month == date.month:
        next_month = next_month + timedelta(days=1)
    if DayRow.objects.filter(date__year=next_month.year, date__month=next_month.month).count() == 0:
        next_month = None

    wind_dir = {}
    for row in rows:
        for (key, value) in eval(row.wind_dir).items():
            wind_dir[key] = wind_dir.get(key, 0) + value

    day = date
    days = []
    while day.month == date.month and DayRow.objects.filter(date=day).count() > 0:
        days.append(day)

        day += timedelta(days=1)

    monthobj = MonthRow.objects.get(date=date)

    context = {
            "rows": rows,
            "date": date, "days": days,
            "total_rain": sum([row.rain for row in rows]),
            "prev_month": prev_month, "next_month": next_month,
            "max_temp_in": max([row.temp_in for row in rows]), "min_temp_in": min([row.temp_in for row in rows]),
            "max_temp_out": max([row.temp_out for row in rows if row.temp_out is not None]),
            "min_temp_out": min([row.temp_out for row in rows if row.temp_out is not None]),
            "max_hum_in": max([row.hum_in for row in rows]), "min_hum_in": min([row.hum_in for row in rows]),
            "max_hum_out": max([row.hum_out for row in rows if row.hum_out is not None]),
            "min_hum_out": min([row.hum_out for row in rows if row.hum_out is not None]),
            "avg_temp_in": monthobj.avg_temp_in,
            "avg_temp_out": monthobj.avg_temp_out,
            "avg_max_temp_in": monthobj.avg_max_temp_in,
            "avg_max_temp_out": monthobj.avg_max_temp_out,
            "avg_min_temp_in": monthobj.avg_min_temp_in,
            "avg_min_temp_out": monthobj.avg_min_temp_out,
            "wind_dir_list": [wind_dir.get(key, 0) for key in range(0, 16, 2)],
            "today": datetime.today(),
            "climate": ClimateByMonth.objects.get(month=int(month)),
            "month": monthobj,
            "months": MonthRow.objects.filter(date__lte=date, date__month=int(month))[::-1]
        }

    return render_to_response("html/month.html", context)
