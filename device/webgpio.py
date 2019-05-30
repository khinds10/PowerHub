#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import RPi.GPIO as gpio
import settings, requests, time

def getRelayValue(flagKey):
    """get relay value for given key"""
    URL = settings.powerHubAPIURL + "flag/" + flagKey
    r = requests.get(url = URL)
    data = r.json()
    return data['message'] == '1'

def setPinHigh(pin):
    """set a current GPIO pin to positive"""
    gpio.output(pin, gpio.HIGH)

def setPinLow(pin):
    """set a current GPIO pin to negative"""
    gpio.output(pin, gpio.LOW)

