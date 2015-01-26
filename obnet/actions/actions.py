#!/usr/bin/env python3
#Filename: actions.py
import requests
import time
import hmac
import hashlib

def OrderCreate( api_key, api_secret, user_id, ticker, price, qty, buy, token ):
    "Create an Order: Buy=1 means Create a Buy order, Buy=0 means Create a Sell order. Suggestion: Use the OrderBuy and OrderSell instead"
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()
       
    url="https://api.icbit.se/api/orders/create?ticker=" + ticker + "&key=" + api_key + "&signature=" + signature + "&nonce=" + nonce + "&price=" + price + "&qty=" + qty + "&buy=" + buy + "&token=" + token
    data= requests.get(url).json()
    
    #Just one item expected in the Dictionary.
    for item in data:    
        try:
            oid = item.get('oid')
            return oid
        except AttributeError:
            error = data['error']
            return error
   
def OrderBuy( api_key, api_secret, user_id, ticker, price, qty, token ):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()
    
    url="https://api.icbit.se/api/orders/create?ticker=" + ticker + "&key=" + api_key + "&signature=" + signature + "&nonce=" + nonce + "&price=" + price + "&qty=" + qty + "&buy=1" + "&token=" + token
    data= requests.get(url).json()
    
    #Just one item expected in the Dictionary.
    for item in data:
        try:
            oid= item.get('oid')
            return oid
        except AttributeError:
            error = data['error']
            return error

def OrderSell( api_key, api_secret, user_id, ticker, price, qty, token ):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()
  
    url="https://api.icbit.se/api/orders/create?ticker=" + ticker + "&key=" + api_key + "&signature=" + signature + "&nonce=" + nonce + "&price=" + price + "&qty=" + qty + "&buy=0" + "&token=" + token
    data= requests.get(url).json()
    
    #Just one item expected in the Dictionary.
    for item in data:
        try:
            oid = item.get('oid')
            return oid
        except AttributeError:
            error = data['error']
            return error

def OrderCancel( api_key, api_secret, user_id, oid):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()   

    url="https://api.icbit.se/api/orders/cancel?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce + "&id=" + oid
    data= requests.get(url).json()
    
    #Just one item expected in the Dictionary.
    for item in data:
        try:
            oid = item.get('oid')
            return oid
        except AttributeError:
            error = data['error']
            return error
