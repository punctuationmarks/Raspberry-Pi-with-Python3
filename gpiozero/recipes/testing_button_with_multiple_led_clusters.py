# Basic "Recipes" via GPIOzero's docs
import gpiozero
from gpiozero import Button
from gpiozero import LED
from gpiozero import PWMLED
from time import sleep
from signal import pause

# used for sound
import pygame
from pygame.mixer import Sound
pygame.mixer.init()

# led =  LED(26)
# led = LED("GPIO16")
# led = LED("BOARD37")

#ledCluster = LED(26)

# making an led blink
def blinkingLED(gpio="GPIO18"):
    led = LED(gpio)
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

# this GPIO is a custer of 4 LEDs each with their own resistors
# This will run first and then run down to the next LED  function
#blinkingLED("GPIO26")


def button_press_causes_individual_light(gpio=""):
    button = Button(gpio)
    # this will use the default LED since I can't pass a variable to the function
    # (as far as I know)
    button.when_pressed = blinkingLED
    # button.when_pressed = sound.play
    pause()




button_press_causes_individual_light("GPIO12")



def ledWithVaryingBrightness(gpio="GPIO26"):\
    # PWM (pulse-width-modulation)
	led = PWMLED(gpio)
	led.value = 0.5  # half brightness
	sleep(1)
	led.value = 1  # full brightness
	sleep(1)
	led.value = 0  # off
	sleep(1)





# sound = Sound("../../music_files_from_ sonic_pi/samples/bass_voxy_c.wav")

def button_press_causes_light_(gpio=""):
    button = Button(gpio)
    # this will use the default LED since I can't pass a variable to the function
    # (as far as I know)
    button.when_pressed = ledWithVaryingBrightness
    # button.when_pressed = sound.play
    pause()


# calling the button in the function
button_press_causes_light_("GPIO21")

