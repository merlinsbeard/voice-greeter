
# -*- coding: utf-8 -*-

import urllib
import urllib.request
import json
import decimal
import requests

appid = "5be49f19e5f9f928228c830fb67cf008"
area = "Manila"

weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Manila&units=metric&APPID=5be49f19e5f9f928228c830fb67cf008"

weather_api = requests.get(weather_url)


response_dictionary = weather_api.json()
current = response_dictionary['main']['temp']
current_low = response_dictionary['main']['temp_min']
current_high = response_dictionary['main']['temp_max']
conditions = response_dictionary['weather'][0]['description']
location = response_dictionary['name']

current = round(current,1)
current_low = round(current_low,1)
current_high = round(current_high,1)

wtr = 'Weather conditions for ' + str(location) +' today are ' + str(conditions) + ' with a current temperature of ' + str(current)

print(wtr)

weather2_url = "http://api.openweathermap.org/data/2.5/forecast/weather?q=Manila&units=metric&APPID=5be49f19e5f9f928228c830fb67cf008"
weather2_api = requests.get(weather2_url)

response_2_dictionary = weather2_api.json()

#todays_low = response_2_dictionary['list'][0]['temp']['night']
#todays_high = response_2_dictionary['list'][0]['temp']['day']

todays_low = response_2_dictionary['list'][0]['main']['temp_min']
todays_high = response_2_dictionary['list'][0]['main']['temp_max']


todays_low = str(round(todays_low,1))
todays_high = str(round(todays_high,1))

todays_low = todays_low.replace(".", " point ")
todays_high = todays_high.replace(".", " point ")

frc = ' with a low of ' + todays_low + ' and a high of ' + todays_high + '.  '
print(frc)
