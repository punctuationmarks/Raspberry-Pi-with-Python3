from gpiozero import LED
from gpiozero import MotionSensor
import time


led_cluster = LED(4)
pir = MotionSensor(23)
print(pir)

# led_cluster.on()
# time.sleep(5)
led_cluster.off()


while True:
        pir.wait_for_motion()
        print("There's motion!")
        led_cluster.on()
#       time.sleep(1)
        pir.wait_for_no_motion()
        time.sleep(1)
        led_cluster.off()
        print("No motion!")

