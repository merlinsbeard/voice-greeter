# -*- coding: utf-8 -*-

import subprocess
import time
import textwrap
import sys
import getopt
import argparse
from os import listdir, makedirs
from better_spoken_time3 import gmt, day
from gtts import gTTS
from weather import Weather
from get_url_news8 import news
from quote import give_quote


class Morning:

    def __init__(self, name, area, weather, quote_of_day,
                 openner=gmt, today=day, news=''):
        self.openner = gmt
        self.name = name
        self.area = area
        self.today = day
        self.news = news
        self.weather = weather
        self.end = 'Thats all for now.  Have a nice day and enjoy your music  '
        self.greeting = ''
        self.quote_of_day = quote_of_day

    def create_greeting(self):
        greet = self.openner + self.name + \
                self.today + self.weather + \
                self.news + self.quote_of_day + self.end

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
        date_string = time.strftime("%Y-%m-%d-%H%M")
        save_file = "greeting-{}-{}".format(count, date_string)
        tts.save("Sounds/{}.mp3".format(save_file))

    def sound_file_path(self):
        sound_path = 'Sounds/'
        return sound_path

    def output(self):
        self.create_mp3(self.create_greeting(), "t1.mp3")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,
                        help="Your Name")
    parser.add_argument("area", type=str,
                        help="Area where you live")
    parser.add_argument("-n", "--news", action="store_true",
                        help="")
    cat_help = 'love, inspiring, art, funny, sports, life, management'
    parser.add_argument("-c", "--category", action="store",
                        help=cat_help)

    args = parser.parse_args()
    name = args.name
    area = args.area
    print(day)
    w = Weather(area)

    if args.news:
        n2 = news()
    else:
        n2 = ''

    if args.category:
        a = vars(args)
        quote_of_day = give_quote(a['category'])

    else:
        quote_of_day = give_quote()

    quote_of_day = "Todays quote of the day. {} by {}. ".format(
                        quote_of_day['quote'], quote_of_day['author'])

    morning = Morning(name,
                      area, w.weather_combine(), quote_of_day, news=n2)

    print(subprocess.call('echo Creating MP3 ...', shell=True))
    morning.create_mp3(morning.create_greeting())
    print(morning.greeting)

if __name__ == '__main__':
    main()
