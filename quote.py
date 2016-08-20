import requests
from quote_crawl import save_quotes

def give_quote(category="love"):
    quotes = save_quotes()
    return quotes['categories'][category]


def give_quote2(category="love"):
    """
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
