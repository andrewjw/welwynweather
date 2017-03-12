from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response
from django.utils.timezone import utc

from app.models import WeatherRow, DayRow, HourRow, ClimateMonth

def day(req, year, month, day):
    try:
        date = datetime(int(year), int(month), int(day), tzinfo=utc)
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
            "day": rows[0].get_day(),
            "today": datetime.today(),
            "hourly_data": HourRow.objects.filter(date__gte=date, date__lt=date + timedelta(days=1)),
            "climate": ClimateMonth.objects.get(month=date.month),
            "on_this_day": DayRow.objects.filter(date__day=date.day, date__month=date.month).order_by("-date")[:5]
        }

    return render_to_response("html/day.html", context)
