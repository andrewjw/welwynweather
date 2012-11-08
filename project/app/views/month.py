from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response

from app.models import WeatherRow, DayRow

def month(req, year, month, day):
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
            "yesterday_link": "/%i/%i/%i" % (yesterday.year, yesterday.month, yesterday.day) if DayRow.objects.filter(date=yesterday).count() > 0 else None,
            "tomorrow_link": "/%i/%i/%i" % (tomorrow.year, tomorrow.month, tomorrow.day) if DayRow.objects.filter(date=tomorrow).count() > 0 else None,
            "weekday": rows[0].date.strftime("%A"),
            "month": rows[0].date.strftime("%B"),
            "day": rows[0].date.day,
            "year": rows[0].date.year
        }

    return render_to_response("html/day.html", context)
