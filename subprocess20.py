# -*- coding: utf-8 -*-

import subprocess
import time
import textwrap
from better_spoken_time3 import gmt, day

from get_url_news8 import news
print(day)
print(subprocess.call('echo starting speak', shell=True))

from gtts import gTTS
from weather import Weather

count = 1

# your name goes here:
name = 'Joyce '
area = 'Perth'
# end
end = 'Thats all for now.  Have a nice day and enjoy your music  '

# Turn all of the parts into a single string

# Weather
w = Weather(area)
weather = w.weather_condition() + w.weather_low_high()

wad = (gmt + name + day + weather + news + end)

# strip any quotation marks
wad = wad.replace('"', '').strip()
wad = wad.replace("'", '').strip()



# Send shorts to Google and return mp3s
tts = gTTS(text=wad, lang="en")
tts.save("todays.mp3")
print("PRINTING OUTPUT")
print(wad)

# Play the mp3s returned
print(subprocess.call ('mpg123 *.mp3', shell=True))
