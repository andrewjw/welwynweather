from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import render_to_response
from django.utils import timezone

from electricity.models import RealTime, Hourly, Daily, Monthly, Minute

def day(req, year, month, day):
    start = timezone.make_aware(datetime(int(year), int(month), int(day)), timezone.get_current_timezone())
    end = timezone.make_aware(datetime(int(year), int(month), int(day)) + timedelta(days=1), timezone.get_current_timezone())

    minutes = Minute.objects.filter(date__gte=start, date__lt=end)

    context = {
        "watts": minutes
    }

    return render_to_response("ehtml/day.html", context)
