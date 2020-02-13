# Basic "Recipes"
import gpiozero
from gpiozero import Button
from gpiozero import LED


led =  LED(17)
# led = LED("GPIO17")
# led = LED("BOARD11")



# making an led blink

def blinkingLED(gpio=""):
	from time import sleep
	led = LED(gpio)
	time = 5
	while time > 0:
		time -= 1
		print(time)
		led.on()
		sleep(0.5)
		led.off()
		sleep(0.5)


# blinkingLED("BOARD13")

# LED also has a blink method
# from signal import pause
# led = LED(gpio)
# led.blink()
# pause()



def ledWithVaryingBrightness(gpio=""):
	from gpiozero import PWMLED
	from time import sleep
	led = PWMLED(gpio)
	
	time = 5
	while time > 0:
		led.value = 0 # off
		sleep(1)
		led.value = 0.5 # half brightness
		sleep(1)
		led.value = 1 #full brightness
		sleep(1)

# ledWithVaryingBrightness("BOARD13")

# PWMLED also has built in pulse method
# led = PWMLED(x)
# led.pulse() 






# these are all the same GPIO pin
# button = Button(22)
# button = Button("GPIO22")
buttonPin22 = Button("BOARD15")


# print(button)
# <gpiozero.Button object on pin GPIO22, pull_up=True, is_active=False>

# print(type(button))
# <class 'gpiozero.input_devices.Button'>

# print(button.is_pressed)
# False

# print(type(button.is_pressed))
# <class 'bool'>

# GPIOzero's Button.is_pressed
def button_pressed_funct(button):
	if button.is_pressed:
		print("Button has been pressed\nBoolean=1")
	else:
		print("Button has not been pressed\nBoolean=0")

# button_pressed_funct(buttonPin22)




# GPIOzero's Button.wait_for_press()
def button_pressed_with_pause_until_press(gpio=""):
	from gpiozero import Button
	# note how this method is called
	# vs how the is_pressed method
	button = Button(gpio)
	button.wait_for_press()
	print("This only runs once the button has been pressed")
	print("Should be very valuable for have a series of steps with buttons\nstarting or stopping the code")



# GPIOzero's Button.when_pressed
def print_something():
	print("when called, this prints")

def button_pressed_calls_functions(gpio=""):
	from gpiozero import Button
	from signal import pause

	button = Button(gpio)
	'''
	Note: when calling a function with button.when_pressed, the function
	does not have parentheses () on the function
	Check the docs for explanation, but will not run right with ()
	'''
	button.when_pressed = print_something
	pause()


 
