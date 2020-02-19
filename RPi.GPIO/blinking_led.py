import RPi.GPIO as GPIO
from time import sleep

# initializing the GPIO pins by setting the board's "mode"
# you can set it up as "BOARD" which is actual pin numbering 
# (i.e. starting at the top left corner as pin 1 then rigth is 2
# then 3 (in left side second to top) then right is 4)
# or use BCM which is used for a gpio extension board for 
# breadboard programming

GPIO.setmode(GPIO.BCM)


totalBlinkCount = 5
currentCount = 0
# where the led is connected to
# getting its powersource
LEDPin = 22

# setting up the led pin, 
# have to specify if it's an output (e.g. giving signal)
# or if it's an input (i.e. button)
GPIO.setup(LEDPin, GPIO.OUT)

'''
This is wrapped in a try statement, because we don't want this
to get stuck running (e.g. in case of program crash)
and using "finally" to clean up the GPIO pins (i.e. setting 
them back to a neutral state, instead of any electricity flowing to them 
in a low or high state, unknowingly)

which is best practices, and your program will actually 
give an error code if you don't clean up the GPIO pins

example error if run without clean up on second run:
	RuntimeWarning: This channel is already in use, continuing anyway.  
	Use GPIO.setwarnings(False) to disable warnings.
'''
try:
	while currentCount < totalBlinkCount:
		# giving power to the led, 
		GPIO.output(LEDPin, True)
		print("LED on")
		sleep(2)
		# turning off the led power source
		GPIO.output(LEDPin, False)
		print("LED off")
		sleep(1)
		currentCount += 1
finally:
	GPIO.cleanup()
	print("GPIO.cleanup() ran")

