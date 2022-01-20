from django.contrib import admin
from today_homepage.models import WeatherInfo, WeatherWindInfo

# Register your models here.
admin.site.register(WeatherInfo)
admin.site.register(WeatherWindInfo)