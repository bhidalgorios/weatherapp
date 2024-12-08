# Generated by Django 5.1.3 on 2024-12-07 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('observation_time', models.CharField(max_length=50)),
                ('isDaytime', models.CharField(max_length=50)),
                ('temperature', models.IntegerField()),
                ('temperatureUnit', models.CharField(max_length=50)),
                ('windSpeed', models.CharField(max_length=50)),
                ('windDirection', models.CharField(max_length=50)),
                ('icon_url', models.URLField()),
                ('shortForecast', models.CharField(max_length=50)),
                ('detailedForecast', models.CharField(max_length=150)),
            ],
        ),
    ]
