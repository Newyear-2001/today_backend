from black import sys
import requests
import pandas as pd 
import django
import os, time

# django setting 
from django.conf import settings
# DB 불러오기 
from today_homepage.models import WeatherInfo, WeatherWindInfo

settings.configure(DEBUG=True)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
django.setup()

class WeatherKorea:
    # API KEY 
    def __init__(self):
        self.url = 'http://api.openweathermap.org/data/2.5/weather?units=Metric&q='
        self.api_key = 'fbdfba381de815ce5e3da814c81eb70f'
    
    # json 형식 반환 
    def weather_city(self, city):
        weather_get = requests.get(f'{self.url}{city}&APPID={self.api_key}').text
        return weather_get


    def city_weather_information(self):
        city_table = pd.read_csv("city_table.csv", encoding='utf-8', engine='python')
        for city in city_table["City"]:
            time.sleep(1)
            info = self.weather_city(city)
            print(info)


