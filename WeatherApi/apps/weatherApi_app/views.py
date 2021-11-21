# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

# Create your views here.

from .forms import GetCityForm
from .models import CityWeatherModel

import requests
from .serializers import WeatherSerializer

def index(req):
    print "in index"
    if req.method == 'POST':
        print "in Post"
        form = GetCityForm(req.POST)
        if form.is_valid():
            print 'Valid Form'
            city = form.cleaned_data['city']
            print city
            print settings.APIKEY
            url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + city + "&units=imperial&cnt=5" + settings.APIKEY
            # params = {'house' : city}
            # params = {'city': city}
            # r = requests.get(url, params=params)
            r = requests.get(url)
            json = r.json()
            print json
            # print json['name']

            serializer = WeatherSerializer(data=json)
            if serializer.is_valid():
                print 'Valid Serializer'
                # print serializer.data
                # print serializer['name']  Works !!!
                # print serializer['main']['temp']  Works!!
                # weather = serializer.save()
            #     print weather
            #     weather_list = {'weather':weather['name']}
                context = {
                    'weather_list' : serializer['name']
                }

                return render(req, 'weatherApi_app/weather.html', context) #HTTP Call
            else:
                print serializer.errors
        else:
            print "In Else"
            context = {
                'getCityForm' : form
            }
            return render(req, 'weatherApi_app/index.html', context)
    else:
        context = {
            'getCityForm' : GetCityForm()
        }
        return render(req, 'weatherApi_app/index.html', context)
