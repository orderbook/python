#!/usr/bin/env python3
#Filename: Orders.py
import requests
import time
import hmac
import hashlib

def OrdersAll( api_key, api_secret, user_id):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()
    return data

def OrderStatus( api_key, api_secret, user_id, oid):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()
    return data

def OrderToken( api_key, api_secret, user_id, oid):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()
    return data

def OrderPrice( api_key, api_secret, user_id, oid):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()
    return data

def OrderTicker( api_key, api_secret, user_id, oid):
    nonce = str(int(round(time.time() * 1000)))
    message = nonce + user_id + api_key
    signature = hmac.new(api_secret.encode(), msg=message.encode(), digestmod=hashlib.sha256).hexdigest().upper()

    url="https://api.icbit.se/api/orders/all?key=" + api_key + "&signature=" + signature + "&nonce=" + nonce 
    data= requests.get(url).json()
    return data
