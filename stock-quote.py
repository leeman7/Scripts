#!/usr/bin/env python3
import sys
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def stockQuote(watchlist):
    # default url for a stock quote search
    url="https://markets.businessinsider.com/stocks/"
    data=[] # create a temp list to stuff each url content into
    # iterate over our watchlist extracting html data
    for stock in watchlist:
        temp=urlopen(url+stock+"-stock")
        bs = BeautifulSoup(temp.read(), 'html.parser')
        data.append(bs)
    
    counter=0
    # iterate over our stock html data to pull out the closing price
    for stock in data:
        nameList=stock.findAll('div', {'class':'col-md-3 col-xs-6 text-right bold black'})
        price=nameList[0].get_text()
        print(watchlist[counter] + " " + price.strip())
        counter+=1

        
stockQuote(["MSFT","GOOGL","T"])