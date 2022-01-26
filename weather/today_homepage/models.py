from django.db import models

        
# 도시 별 온도 DB 
"""
도시 이름, 현재 시간, 
최고 온도, 최저 온도,
체감 온도, 습도량  
"""
class WeatherInfo(models.Model):
    city_name = models.CharField(max_length=30, primary_key=True, null=False)   
    pub_data = models.DateField(auto_now_add=True, null=False)                 
    max_temperature = models.FloatField(null=False)
    min_temperature = models.FloatField(null=False)
    feel_temperature = models.FloatField(null=False)
    average_temp = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    
    class Meta:
        db_table = "weather_information"
        
    
    def __str__(self) -> str:
        return self.city_name

# dress code 
class Dress(models.Model):
    average_temp = models.OneToOneField(WeatherInfo, primary_key=True, on_delete=models.CASCADE)
    dress1 = models.TextField()
    dress2 = models.TextField()
    dress3 = models.TextField()
    dress4 = models.TextField()
    dress5 = models.TextField()
    dress6 = models.TextField()
    
    class Meta:
        db_table = "dress"
           
           
    def __str__(self):
        return self.average_temp


# 도시 별 풍속 DB {온도DB(도시이름) 외래키 지정}
"""
도시 이름(온도 DB 외래키 지정), 현재 시간,
풍속, 풍향, 바람세기
"""
class WeatherWindInfo(models.Model):
    city_name = models.ForeignKey(WeatherInfo, on_delete=models.CASCADE)
    pub_data = models.DateField(auto_now_add=True, null=False)
    wind_speed = models.IntegerField(null=False)
    wind_deg = models.IntegerField(null=False)
    wind_gust = models.FloatField(null=False)

    class Meta:
        db_table = "wind_information"
      
      
    def __str__(self) -> str:
        return self.cityname

# User table 
class Users(models.Model):
    nickname = models.CharField(max_length=10)
    content = models.CharField(max_length=50)
    password =  models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=10)
    
    class Meta:
        db_table = "user_information"
           
           
    def __str__(self):
        return self.city