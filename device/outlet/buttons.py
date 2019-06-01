#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import sys
sys.path.append("..")
import RPi.GPIO as gpio
import webgpio, settings, requests, time
from gpiozero import Button

# setup the buttons
buttonOne = Button(settings.buttonOneClickPin)
buttonTwo = Button(settings.buttonTwoClickPin)

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

# begin the button listener
while True:
    try:
        buttonOne.when_pressed = relayButtonPressed(settings.flagOne, 1)
        buttonTwo.when_pressed = relayButtonPressed(settings.flagTwo, 2)
        time.sleep(0.1)
    except (Exception):
        time.sleep(1)
