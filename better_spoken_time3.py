#!/usr/bin/python
import time


#print suffixed

days_in_words =  {1:'first', 2:'second', 3:'third', 4:'fourth',
 5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth',
 9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth',
 13:'thirteenth', 14:'fouteenth', 15:'fifteenth', 16:'sixteenth',
 17:'seventeeth', 18:'eighteenth', 19:'nineteenth', 20:'twentieth',
 21:'twentyfirst', 22:'twentysecond', 23:'twentythird', 24:'twentyfourth',
 25:'twentyfifth', 26:'twentysixth', 27:'twentyseventh', 28:'twentyeigth',
 29:'twentyninth', 30:'thirtieth', 31:'thirtyfirst'}

day = int(time.strftime("%d"))
suffixed = days_in_words[day]

now = time.strftime("%A %B ") + suffixed + ',' + time.strftime(" %I %M %p")
# print now


if int(time.strftime("%H")) < 12:
  period = ' morning '
if int(time.strftime("%H")) >= 12:
  period = ' afternoon '
if int(time.strftime("%H")) >= 17:
  period = ' evening '

#print time.strftime("%H")
#print period

# reads out good morning + my name
gmt = 'Good' + period + ','

# reads date and time (sorry for the no apostrophe in it's)
day = ' its ' + now + '.  '
