#!/usr/bin/env python3
#Filename: orderbook.py
import requests
import time
import hmac
import hashlib

""" Ticker methods """
def TickerBuy( ticker ):
    "Show all the Buy contracts and its prices"

    url="https://api.icbit.se/api/orders/book?ticker=" + ticker
    data= requests.get(url).json()

    buy = data['buy'];

    return buy

def TickerSell( ticker ):
    "Show the Buy contracts and its prices"

    url="https://api.icbit.se/api/orders/book?ticker=" + ticker
    data= requests.get(url).json()

    sell= data['sell'];
   
    return  sell

def TickerTimeStamp( ticker ):
    "Show the timestamp of the latest modified"
    url="https://api.icbit.se/api/orders/book?ticker=" + ticker
    data= requests.get(url).json()
    
    seconds = data['ts'];
    
    return seconds
 
""" Order methods """
