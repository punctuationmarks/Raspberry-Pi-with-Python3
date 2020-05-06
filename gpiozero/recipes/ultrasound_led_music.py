import gpiozero
from gpiozero import (Button, DistanceSensor, LED)
import pygame
from pygame.mixer import Sound
from time import sleep
from signal import pause
import os 

pygame.init()

sensor_1 = DistanceSensor(echo=18, trigger=17)
sensor_2 = DistanceSensor(echo=14, trigger=4)

led_1 = LED(12)
led_2 = LED(13)
led_1.off()
led_2.off()

sound = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/glitch_perc5.wav")


def activate_light_sound_1():
    led_1.on()
    sound.play()
    print("led_1 on and sound playing!")


def activate_light_sound_2():
    led_2.on()
    sound.play()
    print("led_2 on and sound playing!")


while True:
    cm_1 = sensor_1.distance * 100
    cm_2 = sensor_2.distance * 100
    inches_1 = cm_1 / 2.5
    inches_2 = cm_2 / 2.5
    print(inches_1)
    print(inches_2)
    sleep(0.25)

    if inches_1 >= 8.0:
        distance_too_far = inches_1 - 8
        print("f{distance_too_far} inches_1 too far, come closer")
    if inches_1 < 2.0:
        distance_too_close = inches_1
        print("f{distance_too_close} inches_1 too close, move back!")
    else:
        activate_light_sound_1()
            
    
    if inches_2 >= 8.0:
        distance_too_far = inches_2 - 8
        print("f{distance_too_far} inches_2 too far, come closer")
    if inches_2 < 2.0:
        distance_too_close = inches_2
        print("f{distance_too_close} inches_2 too close, move back!")
    else:
        activate_light_sound_2()
            
            