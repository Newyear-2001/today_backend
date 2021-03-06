# Generated by Django 3.2 on 2022-01-26 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user_information',
            },
        ),
        migrations.CreateModel(
            name='WeatherInfo',
            fields=[
                ('city_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pub_data', models.DateField(auto_now_add=True)),
                ('max_temperature', models.FloatField()),
                ('min_temperature', models.FloatField()),
                ('feel_temperature', models.FloatField()),
                ('average_temp', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
            options={
                'db_table': 'weather_information',
            },
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('average_temp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='today_homepage.weatherinfo')),
                ('dress1', models.TextField()),
                ('dress2', models.TextField()),
                ('dress3', models.TextField()),
                ('dress4', models.TextField()),
                ('dress5', models.TextField()),
                ('dress6', models.TextField()),
            ],
            options={
                'db_table': 'dress',
            },
        ),
        migrations.CreateModel(
            name='WeatherWindInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_data', models.DateField(auto_now_add=True)),
                ('wind_speed', models.IntegerField()),
                ('wind_deg', models.IntegerField()),
                ('wind_gust', models.FloatField()),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='today_homepage.weatherinfo')),
            ],
            options={
                'db_table': 'wind_information',
            },
        ),
    ]
