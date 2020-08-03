#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import RPi.GPIO as gpio
import settings, time, json

# python 2 vs 3 import
try: 
    from urllib.request import urlopen
except:
    from urllib2 import urlopen

def getRelayValue(flagKey):
    """get relay value for given key"""
    URL = settings.powerHubAPIURL + "flag/" + flagKey
    f = urlopen(URL)
    data = json.loads(f.read().decode('utf-8'))
    return int(data['message']) == 1
    
def setPinHigh(pin):
    """set a current GPIO pin to positive"""
    gpio.output(pin, gpio.HIGH)

def setPinLow(pin):
    """set a current GPIO pin to negative"""
    gpio.output(pin, gpio.LOW)

