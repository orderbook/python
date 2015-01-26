#!/usr/bin/env python3
#Filename: SearchOrders.py
import requests
import time
import hmac
import hashlib

def SearchOrdersByTicker( api_key, api_secret, user_id, ticker):
    "Orders placed in a specific Ticker"
    nonce = str(int(round(time.time() * 1000)))
    message = str(nonce) + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()

    oticker = [] 
    for item in data:
        if item.get('ticker')== ticker:
            oticker.append(item)
    return oticker

def SearchOrdersByStatus( api_key, api_secret, user_id, status):
    "Orders with a specific status"
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()
    ostatus = []
    for item in data:
        if item.get('status') == int(status):
            ostatus.append(item)
    return ostatus

def SearchOrdersActive( api_key, api_secret, user_id):
    "Your New Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "0")

def SearchOrdersPartFilled( api_key, api_secret, user_id):
    "Your Partially Filled Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "1")

def SearchOrdersFilled( api_key, api_secret, user_id):
    "Your Filled Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "2")

def SearchOrdersDoneForToday( api_key, api_secret, user_id):
    "Your Canceled Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "3")

def SearchOrdersCanceled( api_key, api_secret, user_id):
    "Your Canceled Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "4")

def SearchOrdersRejected( api_key, api_secret, user_id):
    "Your Rejected Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "5")

def SearchOrdersPendCancel( api_key, api_secret, user_id):
    "Your Active Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "6")

def SearchOrdersPendNew( api_key, api_secret, user_id):
    "Your Active Orders"
    return SearchOrdersByStatus( api_key, api_secret, user_id, "10")

def SearchOrders( api_key, api_secret, user_id, status, ticker, info, otype, price, token , oid):
    "Orders with a specific set of params"
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url = "https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data = requests.get(url).json()
    
    osearch = []
    for item in data:
        if ((not status ) or (item.get('status') == int(status))) and ((not ticker) or (item.get('ticker') == ticker)) and ((not otype)
            or (item.get('type') == int(otype))) and ((not token) or (item.get('token') == token)) and ((not oid)
            or (item.get('oid') == oid)) and ((not price) or (item.get('price') == int(price))) and ((not info) or (item.get('info') == int(info))):
            osearch.append(item)
                  
    return osearch

