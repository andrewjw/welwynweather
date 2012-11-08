from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response

from app.models import WeatherRow, DayRow

def day(req, year, month, day):
    try:
        date = datetime(int(year), int(month), int(day))
    except ValueError:
        raise Http404

    rows = WeatherRow.objects.filter(date__gte=date, date__lt=date + timedelta(days=1))

    if len(rows) == 0:
        raise Http404

    yesterday = date - timedelta(days=1)
    tomorrow = date + timedelta(days=1)

    context = {
            "rows": rows,
            "total_rain": sum([row.rain for row in rows]),
            "yesterday": yesterday if DayRow.objects.filter(date=yesterday).count() > 0 else None,
            "tomorrow": tomorrow if DayRow.objects.filter(date=tomorrow).count() > 0 else None,
            "date": rows[0].date,
            "day": rows[0].get_day()
        }

    return render_to_response("html/day.html", context)
