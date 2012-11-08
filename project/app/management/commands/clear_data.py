from django.core.management.base import BaseCommand, CommandError

from app.models import WeatherRow, HourRow, DayRow

class Command(BaseCommand):
    def handle(self, **options):
        WeatherRow.objects.all().delete()
        HourRow.objects.all().delete()
        DayRow.objects.all().delete()
