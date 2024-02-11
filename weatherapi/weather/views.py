from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import WeatherData
import requests

def get_weather(request):

    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=CIDADE&appid=MINHA_API')
    data = response.json()


    temperature = data['main']['temp']
    humidity = data['main']['humidity']


    weather_data = WeatherData(temperature=temperature, humidity=humidity)
    weather_data.save()


    return JsonResponse({'temperature': weather_data.temperature, 'humidity': weather_data.humidity})