#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0
import RPi.GPIO as gpio
import webgpio, settings, requests, time

# set up the pins to control relay one and two
gpio.setmode(gpio.BCM)
gpio.setup(settings.relayOnePin, gpio.OUT)
gpio.setup(settings.relayTwoPin, gpio.OUT)

# begin watching the power hub to turn on and off devices
relayOne = False
relayTwo = False
while True:
    relayOneCheck = getRelayValue(settings.flagOne)
    if relayOne != relayOneCheck:
        if relayOneCheck:
            setPinHigh(settings.relayOnePin)
        else:
            setPinLow(settings.relayOnePin)
        relayOne = relayOneCheck

    relayTwoCheck = getRelayValue(settings.flagTwo)
    if relayTwo != relayTwoCheck:
        if relayTwoCheck:
            setPinHigh(settings.relayTwoPin)
        else:
            setPinLow(settings.relayTwoPin)
        relayOne = relayTwoCheck
    time.sleep(2)
