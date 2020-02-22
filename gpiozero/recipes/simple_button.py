from gpiozero import LED, Button
from signal import pause

led = LED(26)
btn = Button(4)


print("led: ", led)
print("btn: ", btn)
# led:  <gpiozero.LED object on pin GPIO26, active_high=True, is_active=False>
# btn:  <gpiozero.Button object on pin GPIO4, pull_up=True, is_active=False>


btn.when_pressed = led.on
btn.when_released = led.off


pause()
