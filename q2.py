import requests
import json
from datetime import date

def give_quote(category="love"):
    """
    Uses API instead of web scrapping
    Returns a JSON containing quote information
    use as qod[<variable>]
    author - string
    title - string
    tags - list
    length - int
    background - url
    quote - string
    category - string
    date - year-month-day
    """
    url = "http://quotes.rest/qod.json?category={}".format(category)
    r = requests.get(url)
    qod = r.json()

    qod = qod['contents']['quotes'][0]
    return qod

def check_date(year_month_day):
    """
    Checks if the date is the same as today
    """
    #year_month_day = j_now

    j_now = year_month_day.split('-')

    y,m,d = int(j_now[0]) ,int(j_now[1]), int(j_now[2])
    j_now = date(y,m,d)
    now = date.today()
    if j_now == now:
        return True
    else:
        return False



def quotes():
    #categories = ["inspre", "management", "sports",
    #              "life", "funny", "love", "art"]
    categories = ["love","art"]
    json = {}
    for c in categories:

        quote = {
            "quote": "Don’t count the days; make the days count.",
            "length": '',
            "author": "Mohamad Ali",
            "tags": [
                "inspire",
                "life",
                "productive"
            ],
            "category": "inspire",
            "date": "2016-08-19",
            "title": "Inspiring Quote of the day",
            "background": "https://theysaidso.com/img/bgs/man_on_the_mountain.jpg",
            "id": "zdTLGFsZSu3_FtmJw7XbxQeF"
        }
        quote = give_quote(c)
        json[quote['category']] = {
                        "quote": quote['quote'],
                        "author": quote['author']
                            }
    return json

def write_json():
    a = {}
    today = date.today()
    print(today)
    today = "{}-{}-{}".format(today.year, today.month, today.day)
    return {"date":today, "categories": quotes()}

def check_json_file(filename):
    with open(filename, 'r') as f:
        j = json.loads(f.read())

    j_now = j["date"]
    if check_date(j_now):
        return(print("already have quotes"))

    with open(filename, 'w') as f:
        j = json.dumps(write_json())
        f.write(j)
        print("success")
    print(write_json())
    json.dumps(write_json())
#check_json_file("categories.json")

check_json_file("categories.json")
