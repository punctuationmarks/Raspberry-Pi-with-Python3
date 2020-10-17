# PIR is a motion sensor that is a "passive infrared sensor" meaning it detects heat, but is slow at the process
# these sensors are good for things like turning on the lights when someone walks into a room

from gpiozero import LED
from gpiozero import MotionSensor
import time


led = LED(4)
pir = MotionSensor(23)
print(pir)

led.off()


while True:
        pir.wait_for_motion()
        print("There's motion!")
        led.on()
#       time.sleep(1)
        pir.wait_for_no_motion()
        time.sleep(1)
        led.off()
        print("No motion!")

