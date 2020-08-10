#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as ex:
        print(ex)
        return None
    except URLError as ex:
        print(ex)
        return None
        
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as ex:
        print(ex)
        return None
    else:
        if title == None:
            return None
        else:
            return title
        
title=getTitle('http://www.businessinsider.com')
if title == None:
    print('Title could not be found')
else:
    print(title)

html=urlopen('http://www.businessinsider.com')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList=bs.findAll('a', {'data-analytics-area':'"links"'})
for name in nameList:
    print(name.get_text())