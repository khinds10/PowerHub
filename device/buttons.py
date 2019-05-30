#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import RPi.GPIO as gpio
import webgpio, settings, requests, time
from gpiozero import Button

# setup the buttons
relayButtonOne = Button(settings.buttonOneClickPin)
relayButtonTwo = Button(settings.buttonTwoClickPin)

# set up the pins that light toggle the button lights
gpio.setmode(gpio.BCM)
gpio.setup(settings.buttonOneLightPin, gpio.OUT)
gpio.setup(settings.buttonTwoLightPin, gpio.OUT)

# setup the secret to pass with the "write" requests
secretKey = hashlib.md5()
secretKey.update(settings.secretAPIKey)
secretKeyValue = secretKey.hexdigest()

def relayButtonPressed(flagKey, buttonNumber):
    """set the remote flag based on current status"""
    action = '/unset'
    if webgpio.getRelayValue(flagKey):
        action = '/set'
    URL = settings.powerHubAPIURL + "flag/" + flagKey + action
    r = requests.get(url = URL, headers={"api-key":secretKeyValue})
    data = r.json()
    
    if flagKey == settings.flagOne:
        if action == '/unset':
            webgpio.setPinLow(settings.buttonOneLightPin)
        else:
            webgpio.setPinHigh(settings.buttonOneLightPin)
            
    if flagKey == settings.flagTwo:
        if action == '/unset':
            webgpio.setPinLow(settings.buttonTwoLightPin)
        else:
            webgpio.setPinHigh(settings.buttonTwoLightPin)

# start up by checking if the buttons should be illuminated or not
if webgpio.getRelayValue(settings.flagOne):
    webgpio.setPinHigh(settings.relayOnePin)

if webgpio.getRelayValue(settings.flagTwo):
    webgpio.setPinHigh(settings.relayTwoPin)

# begin the button listener
while True:
    try:
        relayButtonOne.when_pressed = relayButtonPressed(settings.flagOne, 1)
        relayButtonTwo.when_pressed = relayButtonPressed(settings.flagTwo, 2)
        time.sleep(0.1)
    except (Exception):
        time.sleep(1)
