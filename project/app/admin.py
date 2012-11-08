from django.contrib import admin
from app.models import WeatherRow, HourRow, DayRow

class WeatherRowAdmin(admin.ModelAdmin):
    date_hierarchy="date"
    list_display=["date", "temp_in", "temp_out", "hum_in", "hum_out", "wind_gust", "rain"]
admin.site.register(WeatherRow, WeatherRowAdmin)

class HourRowAdmin(admin.ModelAdmin):
    date_hierarchy="date"
    list_display=["date", "temp_in", "temp_out", "hum_in", "hum_out", "wind_gust", "rain"]
admin.site.register(HourRow, HourRowAdmin)

class DayRowAdmin(admin.ModelAdmin):
    date_hierarchy="date"
    list_display=["date", "max_temp_in", "max_temp_out", "max_hum_in", "max_hum_out", "max_wind_gust", "rain"]
admin.site.register(DayRow, DayRowAdmin)