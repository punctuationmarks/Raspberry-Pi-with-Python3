import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# GPIO22
ledPin = 26
# GPIO5
# buttonPin = 5
buttonPin = 27

# keeping track of the count
# so the program doesn't run indefinitely, 
# and stops after "x" amount of button presses
totalBlinkCount = 3
currentButtonCount = 0


GPIO.setup(ledPin, GPIO.OUT)

# intializing the button
# it's an input, and specifying the current state
# this button is "open contact" when you press it "closes contact"
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# keeping track of button state, 
# True == up state aka open 
buttonPressState = True
# False == off state
ledState = False


try:
	while currentButtonCount < totalBlinkCount:
		print("waiting for the button to be pressed")
		# once pressed, the buttonPressState will go false
		# (or be flipped by the GPIO button pin input)
		buttonPressState = GPIO.input(buttonPin)

		if buttonPressState == False and ledState == False:
			# updating the gpio to send power to led
			GPIO.output(ledPin, True)
			# just a debugging printer
			print("LED on")
			# updating the state (for our tracking)
			ledState = True
			# sleeping 
			sleep(2)

		# if button is pressed while led is on
		elif buttonPressState == False and ledState == True:
			# turning off power to the LED
			GPIO.output(ledPin, False)
			print("LED off")
			ledState = False
			currentButtonCount += 1
			sleep(0.5)
		# just for debugging:
		if buttonPressState == False:
                        sleep(0.1)
                        print("button pressed")
		if ledState == True:
			print("LED on")



		# this sleep timer is set here so the RPi doesn't obsessively 
		# check to see if the button has been pressed 
		# -NOTE: without this the RPi will use all of its resources checking
		# to see if the button has been pressed yet, which might lead to 
		# killing the raspberry pi :( 
		sleep(0.8)

finally:
	# turning the led off, no matter what before cleaning up
	# this is due to the state being stored somewhere in memory
	# which *might* put the LED on when the program is rerun
	GPIO.output(ledPin, False)
	GPIO.cleanup()
	print("GPIO.cleanup()")
	
