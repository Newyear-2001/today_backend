# f1d3a0e580be2a7585d984b4ad33fae4
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
#from sqlalchemy import create_engine
import MySQLdb
#import pymysql
import time 
from urllib.request import Request, urlopen 
from urllib.parse import urlencode, quote_plus

# https://api.openweathermap.org/data/2.5/onecall?lat=37.7491361111111&lon=128.878497222222&exclude=minutely,alerts&units=metric&appid=f1d3a0e580be2a7585d984b4ad33fae4
class Api_load:

    def __init__(self, si_gu=None, lon=None, lat=None):
        self.api_key = 'f1d3a0e580be2a7585d984b4ad33fae4'
        self.si_gu = si_gu
        self.lon = lon
        self.lat = lat
        #si_gun

    def lon_lat_load(self):
        city_csv = pd.read_csv("/Users/choeseyeon/Documents/GitHub/today_backend/weather/weather_api/korea_latitude_longitude_list.csv", encoding='utf-8')       
        find_city = city_csv.loc[(city_csv['city'] == self.si_gu)].values.tolist()
        self.lon = find_city[0][3]
        self.lat = find_city[0][4]
        return self.lon, self.lat

    def api_load(self):
        self.lon, self.lat = self.lon_lat_load()
        url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,alerts&units=metric&appid={API_key}".format(self.lon, self.lat, self.api_key)
        # url = "https://api.openweathermap.org/data/2.5/onecall?lat=37.7491361111111&lon=128.878497222222&exclude=minutely,alerts&units=metric&appid=f1d3a0e580be2a7585d984b4ad33fae4"

        res = urlopen(url)
        json_data = res.read().decode("utf-8")
        
# if __name__=="__main__":
#     Api_load.api_load()