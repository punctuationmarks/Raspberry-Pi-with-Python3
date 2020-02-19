from gpiozero import Button
import RPi.GPIO as GPIO

btn = Button(27)

def hello():
	print("Hello")

while True:
	try:
		btn.when_pressed = hello

	finally:
		GPIO.cleanup()
