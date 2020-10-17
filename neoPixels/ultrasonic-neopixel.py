# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import gpiozero
from gpiozero import (Button, DistanceSensor, LED)
from time import sleep
from signal import pause
import os


# ultrasonic sensor
sensor = DistanceSensor(echo=23, trigger=17)


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(10):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)




x = 2

while True:
    cm = sensor.distance * 100
    inches = cm / 2.5
    sleep(0.1)
    
    if inches >= 8.0:
        tooFar = inches - 8
        print(f"{tooFar} inches too far")
        pixels.fill((0, 0, 0))
    elif inches < 2.0:
        print("too close")
        pixels.fill((0, 0, 0))
    else:
    # Comment this line out if you have RGBW/GRBW NeoPixels
#        pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
        rainbow_cycle(1)
        pixels.show()
        time.sleep(0.1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
#    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
#    pixels.show()
#    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
#    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
#    pixels.show()
#    time.sleep(1)

#    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
#    x -=1	
#    print(x)
