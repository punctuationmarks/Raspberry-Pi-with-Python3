from gpiozero import LED, Button
from signal import pause

led1 = LED(21)
led2 = LED(26)
led3 = LED(19)
led4 = LED(13)

#btn1 = Button(4)
#btn2 = Button(8)
#btn3 = Button(23)
#btn4 = Button(17)

led1.source = btn1
led2.source = btn2
led3.source = btn3
led4.source = btn4


pause()
