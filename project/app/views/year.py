from datetime import date, timedelta

from django.http import Http404
from django.shortcuts import render_to_response
from django.utils import timezone
from django.utils.timezone import utc

from app.models import DayRow, YearRow, ClimateByYear

def year(req, year):
    try:
        d = date(int(year), 1, 1)
    except ValueError:
        raise Http404

    next_year = date(int(year)+1, 1, 1)

    rows = DayRow.objects.filter(date__gte=d, date__lt=next_year)

    if len(rows) == 0:
        raise Http404

    prev_year = d - timedelta(days=1)

    wind_dir = {}
    for row in rows:
        for (key, value) in eval(row.wind_dir).items():
            wind_dir[key] = wind_dir.get(key, 0) + value

    month = d
    months = []
    while month.year == d.year:
        if DayRow.objects.filter(date__year=month.year, date__month=month.month).count() > 0:
            months.append(month)

        next_month = month
        while next_month.month == month.month:
            next_month += timedelta(days=1)
        month = next_month

    years = YearRow.objects.filter(date__lte=d, date__gte=date(2012, 1, 1))
    for yearobj in years:
        if yearobj.date.year == date.today().year:
            days_in_year = (datetime(int(year), 12, 31) - datetime(int(year), 1, 1)).days
            days_so_far = (datetime.now() - datetime(int(year), 1, 1)).days
            yearobj.predicted_rain = (days_in_year*yearobj.rain)/days_so_far

    if len([y for y in years if y.date==d]) == 0:
        raise Http404
    year = [y for y in years if y.date==d][0]

    context = {
            "rows": rows,
            "date": d, "months": months,
            "total_rain": sum([row.rain for row in rows]),
            "prev_year": prev_year if DayRow.objects.filter(date__year=prev_year.year).count() else None,
            "next_year": next_year if DayRow.objects.filter(date__year=next_year.year).count() else None,
            "max_temp_in": max([row.max_temp_in for row in rows]), "min_temp_in": min([row.min_temp_in for row in rows]),
            "max_temp_out": max([row.max_temp_out for row in rows if row.max_temp_out is not None]),
            "min_temp_out": min([row.min_temp_out for row in rows if row.min_temp_out is not None]),
            "avg_temp_out": year.avg_temp_out,
            "avg_temp_in": year.avg_temp_in,
            "wind_dir_list": [wind_dir.get(key, 0) for key in range(0, 16, 2)],
            "today": date.today(),
            "climate": ClimateByYear.objects.get(),
            "year": year,
            "years": years[::-1]
        }

    return render_to_response("html/year.html", context)
