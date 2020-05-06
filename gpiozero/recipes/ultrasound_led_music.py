import gpiozero
from gpiozero import (Button, DistanceSensor, LED)
import pygame
from pygame.mixer import Sound
from time import sleep
from signal import pause
import os 

pygame.init()

sensor = DistanceSensor(echo=17, trigger=18)
led = LED(12)

sound = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/glitch_perc5.wav")


def activate_light_sound():
    led.on()
    sound.play()
    print("LED on and sound playing!")


while True:
    cm = sensor.distance * 100
    inches = cm / 2.5
    print(inches)
    sleep(0.25)

    if inches >= 8.0:
        distance_too_far = inches - 8
        print("f{distance_too_far} inches too far, come closer")
    if inches < 2.0:
        distance_too_close = inches - 8
        print("f{distance_too_close} inches too close, move back!")
    else:
        activate_light_sound()
            
    
            