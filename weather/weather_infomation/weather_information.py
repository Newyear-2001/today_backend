import requests
import pandas as pd 
import django
import json
import os, time, sys
sys.path.append('.')


# django setting 
from django.conf import settings
settings.configure(DEBUG=True)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
django.setup()

# DB 불러오기 
from today_homepage.models import WeatherInfo, WeatherWindInfo

class WeatherKorea:
    # API KEY 
    def __init__(self):
        self.url = 'http://api.openweathermap.org/data/2.5/weather?units=Metric&q='
        self.api_key = 'fbdfba381de815ce5e3da814c81eb70f'
    
    # json 형식 반환 
    def weather_city(self, city):
        weather_get = requests.get(f'{self.url}{city}&APPID={self.api_key}').text
        return weather_get

    # 메인 정보
    def city_weather_information(self):
        city_table = pd.read_csv("/home/imsky/문서/today_project/today_backend/weather/weather_infomation/city_table.csv", encoding='utf-8', engine='python')
        for city in city_table["City"]:
            time.sleep(1)
            info = self.weather_city(city)
            result = json.loads(info)
            temp_info = result.get("main")
            wind_info = result.get("wind")
            average_score = (float(temp_info["temp_max"]) + float(temp_info["temp_min"])) / 2
            print(average_score, type(average_score))
            
            # DB 저장
            WeatherInfo(city_name=city, max_temperature=float(temp_info["temp_max"]), 
                        min_temperature=float(temp_info['temp_min']), feel_temperature=float(temp_info['feels_like']), 
                        average_temp = average_score, humidity=float(temp_info["humidity"])).save()
            WeatherWindInfo(city_name=city, wind_speed=wind_info["speed"], wind_deg=wind_info["deg"], wind_gust=wind_info["gust"]).save()


if __name__ == "__main__":
    s = WeatherKorea().city_weather_information()
    print(s)