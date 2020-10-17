import gpiozero
from gpiozero import (DistanceSensor, LED)
from time import sleep
from signal import pause
import os


ultrasoni_sensor = DistanceSensor(echo=18, trigger=17)

led = LED(24)

def activateLight():
    led.on()
    sleep(0.2)
    print("led on\n")
    led.off()

while True:
    distance = ultrasoni_sensor.distance
    centimeters = distance * 100

    if centimeters >= 20:
        too_far = centimeters - 5
        print(f"{too_far} centimeters too far, come closer\n")
    elif centimeters < 5:
        too_close = 5- centimeters
        print(f"{too_close} centimeters too close, move back\n")
    else:
        activateLight()
        # sleep(0.1)