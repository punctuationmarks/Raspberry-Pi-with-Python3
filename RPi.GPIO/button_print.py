import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

buttonPin = 27


# intializing the button
# it's an input, and specifying the current state
# this button is "open contact" when you press it "closes contact"
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)



# need to write print statement
