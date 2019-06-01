#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import RPi.GPIO as gpio
import webgpio, settings, requests, time

# set up the pins that light toggle the button lights
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(settings.buttonOneLightPin, gpio.OUT)
gpio.setup(settings.buttonTwoLightPin, gpio.OUT)

# begin watching the power hub to turn on and off devices
relayOne = False
relayTwo = False
while True:
    relayOneCheck = webgpio.getRelayValue(settings.flagOne)
    if relayOne != relayOneCheck:
        if relayOneCheck:
            webgpio.setPinHigh(settings.buttonOneLightPin)
        else:
            webgpio.setPinLow(settings.buttonOneLightPin)
        relayOne = relayOneCheck

    relayTwoCheck = webgpio.getRelayValue(settings.flagTwo)
    if relayTwo != relayTwoCheck:
        if relayTwoCheck:
            webgpio.setPinHigh(settings.buttonTwoLightPin)
        else:
            webgpio.setPinLow(settings.buttonTwoLightPin)
        relayOne = relayTwoCheck
    time.sleep(2)
