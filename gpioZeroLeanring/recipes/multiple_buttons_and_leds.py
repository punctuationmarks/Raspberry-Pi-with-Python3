from gpiozero import LED, Button
from signal import pause

# two leds
led = LED(26)
led2 = LED(21)

# four buttons
btn1 = Button(4)
btn2 = Button(17)
btn3 = Button(27)
btn4 = Button(22)

# having two sources to control the button
led.source = btn1
led.source = btn2
led2.source = btn3
led2.source = btn4


pause()
