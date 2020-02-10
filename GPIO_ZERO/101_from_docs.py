# Basic "Recipes"
import gpiozero
from gpiozero import Button
from gpiozero import LED

# these are all the same GPIO pin
# button = Button(22)
# button = Button("GPIO22")
button = Button("BOARD15")


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
