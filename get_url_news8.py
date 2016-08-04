#!/usr/bin/env python

import feedparser
def news():
    try:
        url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
        #url = 'https://news.google.com/news?pz=1&cf=all&ned=en_ph&hl=en&topic=snc&output=rss'
        rss = feedparser.parse(url)
        #rss = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
        #rss = feedparser.parse('http://news.feedzilla.com/en_us/headlines/oddly-enough/top-stories.rss')

        newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  '

    # print newsfeed

    # Today's news from BBC
        news = 'And now, The latest stories from the World section of the BBC News.  ' + newsfeed

    except rss.bozo:
        news = 'Failed to reach BBC News'

    # print news
    return news
