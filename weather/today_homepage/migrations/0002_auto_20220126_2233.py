# Generated by Django 3.2 on 2022-01-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('today_homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherwindinfo',
            name='city_name',
        ),
        migrations.DeleteModel(
            name='Dress',
        ),
        migrations.DeleteModel(
            name='WeatherInfo',
        ),
        migrations.DeleteModel(
            name='WeatherWindInfo',
        ),
    ]
