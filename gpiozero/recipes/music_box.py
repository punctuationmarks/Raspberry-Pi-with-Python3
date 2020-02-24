import gpiozero
from gpiozero import Button
from gpiozero import LED

import pygame
from pygame.mixer import Sound

from signal import pause

pygame.init()


btn1 = Button("GPIO18")
btn2 = Button("GPIO23")
btn3 = Button("GPIO25")
btn4 = Button("GPIO12")


led = LED("GPIO4")

tick = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/elec_tick.wav")
bass = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/glitch_bass_g.wav")
snare = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/elec_snare.wav")
bd_klub = Sound("/home/pi/Raspberry-Pi-with-Python3/music_files_from_sonic_pi/samples/bd_klub.wav")



btn_sounds = {btn1: tick,
		btn2: bass,
		btn3: snare,
		btn4: bd_klub}




for btn, sound in btn_sounds.items():
	btn.when_pressed = sound.play
	btn.when_pressed = led.on
	btn.when_released = led.off

pause()




