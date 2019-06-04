#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import sys
sys.path.append("..")
import RPi.GPIO as gpio
import webgpio, settings, requests, time, hashlib
from gpiozero import Button

# setup the buttons
buttonOne = Button(settings.buttonOneClickPin)
buttonTwo = Button(settings.buttonTwoClickPin)

# setup the secret to pass with the "write" requests
secretKey = hashlib.md5()
secretKey.update(settings.secretAPIKey)
secretKeyValue = secretKey.hexdigest()

def relayButtonPressed(flagKey):
    """set the remote flag based on current status"""
    action = '/set'
    isSet = webgpio.getRelayValue(flagKey)
    if isSet:
        action = '/unset'
    URL = settings.powerHubAPIURL + "flag/" + flagKey + action
    requests.get(url = URL, headers={"api-key":secretKeyValue})
    
def relayButtonOnePressed():
    relayButtonPressed(settings.flagOne)

def relayButtonTwoPressed():
    relayButtonPressed(settings.flagTwo)

# begin the button listener
while True:
    try:
        buttonOne.when_pressed = relayButtonOnePressed
        buttonTwo.when_pressed = relayButtonTwoPressed
        time.sleep(0.1)
    except (Exception):
        time.sleep(1)
