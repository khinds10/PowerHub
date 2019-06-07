#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import sys
sys.path.append("..")
import RPi.GPIO as gpio
import webgpio, settings, requests, time

# set up the pins to control relay one and two
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(settings.relayOnePin, gpio.OUT)
gpio.setup(settings.relayTwoPin, gpio.OUT)

# set up the pins that light toggle the button lights
gpio.setup(settings.buttonOneLightPin, gpio.OUT)
gpio.setup(settings.buttonTwoLightPin, gpio.OUT)

# begin watching the power hub to turn on and off devices
relayOne = False
relayTwo = False
relayOneCheck = False
relayTwoCheck = False
while True:
    try:
        relayOneCheck = webgpio.getRelayValue(settings.flagOne)
        if relayOne != relayOneCheck:
            if relayOneCheck:
                webgpio.setPinLow(settings.relayOnePin)
                webgpio.setPinHigh(settings.buttonOneLightPin)
            else:
                webgpio.setPinHigh(settings.relayOnePin)
                webgpio.setPinLow(settings.buttonOneLightPin)
            relayOne = relayOneCheck

        relayTwoCheck = webgpio.getRelayValue(settings.flagTwo)
        if relayTwo != relayTwoCheck:
            if relayTwoCheck:
                webgpio.setPinLow(settings.relayTwoPin)
                webgpio.setPinHigh(settings.buttonTwoLightPin)
            else:
                webgpio.setPinHigh(settings.relayTwoPin)
                webgpio.setPinLow(settings.buttonTwoLightPin)
            relayTwo = relayTwoCheck
        time.sleep(1)
    except (Exception):
        time.sleep(1)
