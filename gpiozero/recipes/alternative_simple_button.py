from gpiozero import LED, Button
from signal import pause

led = LED(26)
btn = Button(4)

led.source = btn

print(led.source)
# <generator object ValuesMixin.values at 0xb6452f30>


pause()
