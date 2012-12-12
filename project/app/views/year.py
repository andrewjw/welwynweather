from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response

from app.models import DayRow

def year(req, year):
    try:
        date = datetime(int(year), 1, 1)
    except ValueError:
        raise Http404

    next_year = datetime(int(year)+1, 1, 1)

    rows = DayRow.objects.filter(date__gte=date, date__lt=next_year)

    if len(rows) == 0:
        raise Http404

    prev_year = date - timedelta(days=1)

    wind_dir = {}
    for row in rows:
        for (key, value) in eval(row.wind_dir).items():
            wind_dir[key] = wind_dir.get(key, 0) + value

    month = date
    months = []
    while month.year == date.year:
        if DayRow.objects.filter(date__year=month.year, date__month=month.month).count() > 0:
            months.append(month)

        next_month = month
        while next_month.month == month.month:
            next_month += timedelta(days=1)
        month = next_month

    context = {
            "rows": rows,
            "date": date, "months": months,
            "total_rain": sum([row.rain for row in rows]),
            "prev_year": prev_year if DayRow.objects.filter(date__year=prev_year.year).count() else None,
            "next_year": next_year if DayRow.objects.filter(date__year=next_year.year).count() else None,
            "max_temp_in": max([row.max_temp_in for row in rows]), "min_temp_in": min([row.min_temp_in for row in rows]),
            "max_temp_out": max([row.max_temp_out for row in rows if row.max_temp_out is not None]),
            "min_temp_out": min([row.min_temp_out for row in rows if row.min_temp_out is not None]),
            "wind_dir_list": [wind_dir.get(key, 0) for key in range(0, 16, 2)],
            "today": datetime.today()
        }

    return render_to_response("html/year.html", context)
