#! /usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0

# powerhub website to sync relays with internet based on/off value
powerHubAPIURL = 'http://www.my-powerhub.com'
secretAPIKey = 'PASSWORD HERE'

# remote flag values to use from central power hub
flagOne = '1';
flagTwo = '2';

# relay GPIO trigger pins
relayOnePin = 17
relayTwoPin = 18

# button click GPIO pins
buttonOneClickPin = 22
buttonTwoClickPin = 23

# button light GPIO pins
buttonOneLightPin = 24
buttonTwoLightPin = 25

# motion detector GPIO pin
motionDetectorPin = 11

# which flags the motion detector turns on
motionDetectorPin = ['1', '2']
