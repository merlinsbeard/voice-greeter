from better_spoken_time3 import gmt, day
from weather import Weather
from quote import give_quote
from gtts import gTTS
from os import listdir, makedirs

import requests
import time
import unipath
import soundcloud
import argparse


class Hello:


    def __init__(self, name,
            area, category='life'):

        self.name = name
        self.area = area
        self.category = category


    def get_greeting(self):
        self.greeting ='{} {} {}'.format(
                gmt, self.name, day)
        return self.greeting


    def get_weather(self):
        weather = Weather(self.area)
        self.weather = weather.weather_combine()
        return self.weather


    def get_quote(self):
        quote = give_quote(self.category)
        quote_of_day = "Todays quote of the day. {} by {}. ".format(
                            quote['quote'], quote['author'])
        self.quote = quote_of_day
        return self.quote


    def get_whole_greeting(self):
        end = 'Thats all for now.  Have a nice day and enjoy your music  '
        greet = '{} {}.  {} {}'.format(
                self.get_greeting(), self.get_weather(),
                self.get_quote(), end)
        greet = greet.replace('""', '').strip()
        greet = greet.replace("'", '').strip()

        self.whole_greeting = greet
        return self.whole_greeting

    def create_mp3(self):
        self.get_whole_greeting()
        try:
            pages = len(listdir("Sounds"))
        except FileNotFoundError:
            makedirs("Sounds")
            pages = 0
        count = pages + 1
        tts = gTTS(text=self.whole_greeting, lang="en")
        date_string = time.strftime("%Y-%m-%d-%H%M")
        save_file = "greeting-{}-{}.mp3".format(
                                count, date_string)
        print(save_file)
        tts.save("Sounds/{}".format(save_file))
        print('saving file')
        self.file = save_file
        return self.file


    def get_soundcloud(self):

        client = soundcloud.Client(
                client_id=env('SOUNDCLOUD_CLIENT_ID'))
        track = client.post('/tracks', track={

            'title': self.file,
            'asset_data': open(
                'Sounds/{}'.format('self.file'),'rb')

            })

        self.url = track.permalink_url
        return self.url


def sample_run():
    """
    for testing purposes
    """
    a = Hello('bj','manila','life')
    a.get_whole_greeting()
    print(a.create_mp3())
    #print(a.get_whole_greeting())
    print('+++++++++++++++')
    print(a.file)


def greet(name, area, category='life'):
    hello = Hello(name, area, category)
    #print(hello.get_whole_greeting())
    hello.create_mp3()
    print('success')
    print(hello.whole_greeting)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("name", type=str,
                        help="Your Name")
    parser.add_argument("area", type=str,
                        help="Area where you live")

    cat_help = 'love, inspiring, art, funny, sports, life, management'
    parser.add_argument("-c", "--category", action="store",
                        help=cat_help)


    args = parser.parse_args()
    name = args.name
    area = args.area

    if args.category:
        category = args.category
        greet(name, area, category)
    else:
        greet(name, area)


if __name__ == '__main__':
    main()
