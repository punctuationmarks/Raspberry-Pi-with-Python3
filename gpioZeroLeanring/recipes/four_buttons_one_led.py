from gpiozero import LED, Button
from signal import pause

led = LED(26)
led2 = LED(21)

btn1 = Button(4)
btn2 = Button(17)
btn3 = Button(27)
btn4 = Button(22)

led.source = btn1
led.source = btn2
led2.source = btn3
led2.source = btn4



pause()
