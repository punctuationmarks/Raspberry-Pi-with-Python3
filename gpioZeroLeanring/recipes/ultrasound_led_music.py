import gpiozero
from gpiozero import (Button, DistanceSensor, LED)
import pygame
from pygame.mixer import Sound
from time import sleep
from signal import pause
import os 

# need to in initialized the pygame to have the music play, with pygame.mixer
pygame.init()

# Having two ultrasonic sensors
sensor_1 = DistanceSensor(echo=18, trigger=17)
sensor_2 = DistanceSensor(echo=14, trigger=4)

# having two LEDs
led_1 = LED(24)
led_2 = LED(13)
# starting the LEDs the off position, 
# this is to be explicit but also because this is safer for the RPi
led_1.off()
led_2.off()

sound_1 = Sound("../audioFiles/glitch_perc5.wav")
sound_2 = Sound("../audioFiles/elec_blip.wav")


def activateSoundAndLight(led, sound):
    led.on()
    sound.play()
    sleep(0.2)
    print(f"{led} on and {sound} sound playing!")
    led.off()

while True:
    cm_1 = sensor_1.distance * 100
    cm_2 = sensor_2.distance * 100
    inches_1 = cm_1 / 2.5
    inches_2 = cm_2 / 2.5
    # print(inches_1)
    # print(inches_2)
    sleep(0.1)

    if inches_1 >= 8.0:
        distance_too_far = inches_1 - 8
        print(f"{distance_too_far} inches_1 too far, come closer")
    elif inches_1 < 2.0:
        distance_too_close = inches_1
        print(f"{distance_too_close} inches_1 too close, move back!")
    elif (2.0 < inches_1 <= 8.0):
        activateSoundAndLight(led_1, sound_1)
        sleep(0.1)

    elif inches_2 >= 8.0:
        distance_too_far = inches_2 - 8
        print(f"{distance_too_far} inches_2 too far, come closer")
    elif inches_2 < 2.0:
        distance_too_close = inches_2
        print(f"{distance_too_close} inches_2 too close, move back!")
    elif (2.0 < inches_2 <= 8.0):
        activateSoundAndLight(led_2, sound_2)
        sleep(0.1)        