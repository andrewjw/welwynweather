from day import day

from app.models import DayRow

def index(req):
    row = DayRow.objects.all().order_by("-date")[0]

    return day(req, row.date.year, row.date.month, row.date.day)
