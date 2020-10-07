from gpiozero import DistanceSensor 
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
while True:
    cm = sensor.distance * 100
    inch = cm / 2.5
    print(f"cm={cm}\ninches={inch}")
    sleep(0.5)