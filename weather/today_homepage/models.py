from pyexpat import model
from black import T
from django.db import models
from pandas import notnull


# 도시 별 온도 DB 
"""
도시 이름, 현재 시간, 
최고 온도, 최저 온도,
체감 온도, 습도량  
"""
class WeatherInfo(models.Model):
    city_name = models.CharField(max_length=30, primary_key=True, notnull=True)   
    pub_data = models.DateField(auto_now_add=True, notnull=True)                 
    max_temperature = models.FloatField(notnull=True)
    min_temperature = models.FloatField(notnull=True)
    feel_temperature = models.FloatField(notnull=True)
    humidity = models.FloatField(notnull=True)
    
    def __str__(self) -> str:
        return self.city_name
    
# 도시 별 풍속 DB {온도DB(도시이름 ) 외래키 지정}
"""
도시 이름(온도 DB 외래키 지정), 현재 시간,
풍속, 풍향, 바람세기
"""
class WeatherWindInfo(models.Model):
    cityname = models.ForeignKey(WeatherInfo, on_delete=models.CASCADE)
    pub_data = models.DateField(auto_now_add=True, notnull=True)
    wind_speed = models.IntegerField(notnull=True)
    wind_deg = models.IntegerField(notnull=True)
    wind_gust = models.FloatField(notnull=True)

    def __str__(self) -> str:
        return self.cityname