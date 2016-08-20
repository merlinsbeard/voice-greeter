import requests
from bs4 import BeautifulSoup
import json
from datetime import date

def check_date(year_month_day):
    """
    Checks if the date is the same as today
    """
    j_now = year_month_day.split('-')
    y,m,d = int(j_now[0]) ,int(j_now[1]), int(j_now[2])
    j_now = date(y,m,d)
    now = date.today()
    if j_now == now:
        return True
    else:
        return False


def quotes():
    url = "https://theysaidso.com/qod"
    url = requests.get(url)

    soup = BeautifulSoup(url.text, 'html.parser')
    cats = ['love', 'inspiring','art', 'funny', 'sports', 'life', 'management']
    j = {}
    for q in soup.find_all('div', attrs={'class': 'carousel-caption'}):
        data = q.find_all('span')
        cat = q.find('a').string.lower()
        category = ''
        for c in cats:
            if c in cat:
                category = c
        quote = data[0].string
        author = data[1].string
        #print('Category: {}'.format(category.title()))
        #print('Quote: {}'.format(quote.title()))
        #print('Author: {}'.format(author.title()))
        #print('==================')
        #j[category] = [quote, author]
        j[category] = {
                        "quote": quote,
                        "author": author
                            }
    return j


def write_json():
    a = {}
    today = date.today()
    print(today)
    today = "{}-{}-{}".format(today.year, today.month, today.day)
    return {"date":today, "categories": quotes()}

def save_quotes(filename='categories.json'):
    """
    Saves the scrapped quotes in categories.json file
    and returns the scrapped quotes in json format
    """
    a = write_json()
    with open('categories.json', 'w') as f:
        f.write(json.dumps(a))
    return a


if __name__ == '__main__':
    save_quotes()
