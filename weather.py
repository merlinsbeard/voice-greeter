import urllib
import urllib.request
import json
import decimal
import requests

class Weather():
    """
    Creates Weather object containing information about Current weather
    """

    def __init__(self, area):
        self.area = area
        self.weather_url = "http://api.openweathermap.org/"
        self.appid = "5be49f19e5f9f928228c830fb67cf008"

    def weather_condition(self):
        """
        returns current weather condition
        """
        weather_api = "{}data/2.5/weather?q={}&units=metric&APPID={}" \
                    .format(self.weather_url, self.area, self.appid)

        r = requests.get(weather_api)

        weather_dict = r.json()
        current = weather_dict['main']['temp']
        current_low = weather_dict['main']['temp_min']
        current_high = weather_dict['main']['temp_max']
        conditions = weather_dict['weather'][0]['description']
        location = weather_dict['name']
        current = str(current).replace(".", " point ")
        weather = "Weather conditions for {} today are {} with a current temperature of {}" \
                    .format(self.area, conditions, current)
        return weather

    def weather_low_high(self):
        """
        returns the highs and lows of current weather
        """
        weather_api = "{}data/2.5/forecast/weather?q={}&units=metric&APPID={}" \
                    .format(self.weather_url, self.area, self.appid)
        r = requests.get(weather_api)
        weather_dict = r.json()

        todays_low = weather_dict['list'][0]['main']['temp_min']
        todays_high = weather_dict['list'][0]['main']['temp_max']


        todays_low = str(round(todays_low,1))
        todays_high = str(round(todays_high,1))

        todays_low = todays_low.replace(".", " point ")
        todays_high = todays_high.replace(".", " point ")

        weather = " with a low of {} and a high of {}.  ".format(todays_low, todays_high)
        return weather

    def weather_combine(self):
        return self.weather_condition() + self.weather_low_high()
