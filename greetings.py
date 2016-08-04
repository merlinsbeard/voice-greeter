# -*- coding: utf-8 -*-

import subprocess
import time
import textwrap
import sys, getopt
import argparse
from os import listdir, makedirs
from better_spoken_time3 import gmt, day
from gtts import gTTS
from weather import Weather
from get_url_news8 import news



class Morning:

    def __init__(self,openner, name, today, area, weather,news=''):
        self.openner = openner
        self.name = name
        self.area = area
        self.today = today
        self.news = news
        self.weather = weather
        self.end = 'Thats all for now.  Have a nice day and enjoy your music  '
        self.greeting = ''

    def create_greeting(self):
        greet = self.openner + self.name + self.today + self.weather + self.news + self.end
        greet = greet.replace('""', '').strip()
        greet = greet.replace("'", '').strip()
        self.greeting = greet
        return(greet)

    def create_mp3(self, greeting):
        try:
            pages = len(listdir("Sounds"))
        except FileNotFoundError:
            makedirs("Sounds")
            pages = 0
        count = pages + 1
        tts = gTTS(text=greeting, lang="en")
        tts.save("Sounds/{}.mp3".format(count))

    def create_filename():
        pass

    def output(self):
        self.create_mp3(self.create_greeting(), "t1.mp3")

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("name", type=str,
                        help="Your Name")
    parser.add_argument("area", type=str,
                        help="Area where you live")
    parser.add_argument("-n","--news", action="store_true",
                        help="")

    args = parser.parse_args()
    name = args.name
    area = args.area
    print(day)
    w = Weather(area)

    if args.news:
        morning = Morning(gmt, name, day, area, w.weather_combine(), news=news())
    else:
        morning = Morning(gmt, name, day, area, w.weather_combine())

    print(subprocess.call('echo Creating MP3 ...', shell=True))
    morning.create_mp3(morning.create_greeting())
    print(morning.greeting)

if __name__ == '__main__':
    main()
