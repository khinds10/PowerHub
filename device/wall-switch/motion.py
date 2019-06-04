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

# set up the pins that light toggle the button lights
gpio.setup(settings.buttonOneLightPin, gpio.OUT)
gpio.setup(settings.buttonTwoLightPin, gpio.OUT)


# HAVE THE MOTION DETECTOR WORKING

# -- IT SHOULD BE CONFIGURED TO RUN AT STARTUP AND TURN ONE OR BOTH OF THE FLAGS ON

# -- IF YOU MANUALLY PRESS A BUTTON IT SHOULD WAIT 2 HOURS BEFORE DETECTING MOTION AGAIN


def setFlags(value):
    pass

while True:







    #  @TODO -- this should only fire??! once and awhile, or remember that it was previously used
    # 2 hour timeout on this
    
    checkForMotion = GPIO.input(motionDetectorPin)
    setFlags(str(checkForMotion))

            
            











#    relayOneCheck = webgpio.getRelayValue(settings.flagOne)
#    if relayOne != relayOneCheck:
#        if relayOneCheck:
#            webgpio.setPinLow(settings.relayOnePin)
#            webgpio.setPinHigh(settings.buttonOneLightPin)
#        else:
#            webgpio.setPinHigh(settings.relayOnePin)
#            webgpio.setPinLow(settings.buttonOneLightPin)
#        relayOne = relayOneCheck

#    relayTwoCheck = webgpio.getRelayValue(settings.flagTwo)
#    if relayTwo != relayTwoCheck:
#        if relayTwoCheck:
#            webgpio.setPinLow(settings.relayTwoPin)
#            webgpio.setPinHigh(settings.buttonTwoLightPin)
#        else:
#            webgpio.setPinHigh(settings.relayTwoPin)
#            webgpio.setPinLow(settings.buttonTwoLightPin)
#        relayOne = relayTwoCheck
    time.sleep(1)






































    
        
