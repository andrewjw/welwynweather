from datetime import datetime

from electricity.models import Minute
from electricity.views import day

def index(req):
    last = Minute.objects.all().order_by("-date")[0]
    return day.day(req, last.date.year, last.date.month, last.date.day)
