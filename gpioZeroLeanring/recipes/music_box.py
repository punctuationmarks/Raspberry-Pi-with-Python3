# simple beatbox machine with buttons and a single led light
# concept taken and expanded from RPi foundation tutorials

import gpiozero
from gpiozero import Button
from gpiozero import LED
import pygame
from pygame.mixer import Sound
from signal import pause
import os 

pygame.init()

btn1 = Button("GPIO18")
btn2 = Button("GPIO23")
btn3 = Button("GPIO25")
btn4 = Button("GPIO16")


led4 = LED("GPIO4")

blip = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/elec_blip.wav")
bass = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/glitch_bass_g.wav")
snare = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/elec_snare.wav")
glitch = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/glitch_perc5.wav")



def activate_blip():
	print("Blip and light!")
	led4.on()
	blip.play()

def activate_bass():
	print("Bass and light!")
	led4.on()
	bass.play()

def activate_snare():
	print("Snare and light")
	led4.on()
	snare.play()

def activate_glitch():
	print("Glitch and Light!")
	led4.on()
	glitch.play()


btn1.when_pressed = activate_blip
btn1.when_released = led4.off

btn2.when_pressed = activate_bass
btn2.when_released = led4.off

btn3.when_pressed = activate_snare
btn3.when_released = led4.off

btn4.when_pressed = activate_glitch
btn4.when_released = led4.off

pause()




