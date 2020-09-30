# Installing
GPIOzero is built ontop of other GPIO libraries, you have to have one of the following installed:
	- RPi.GPIO (prefered)
	- RPIO.GPIO
	- pigpio

```
pip3 install rpi.gpio
pip3 install gpiozero
```


# Physical GPIO referencing in GPIOzero
With GPIOzero the GPIOs are fixed and can not be altered. 
Meaning, if you're counting 1 through 40 of the GPIO pins, 
you can't customize where the code references the 
actual GPIO pin's location (if you need to do that, 
check out [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)).
But you can reference the actual board's pins as well as the 
GPIO layout, plus many other reference points depending on where
you're coming from. 

- Different ways of referencing GPIO pins
```
# these all reference the same GPIO pin
led = LED(17)
led = LED("GPIO17")
led = LED("BCM17")
led = LED("WPIO")
led = LED("BOARD11")
led  LED("J8:11")
```

- the GPIO once referenced has a good deal of information
```
$ python
>>> import gpiozero
>>> led = gpiozero.LED("BOARD11")
>>> 
>>> led
<gpiozero.LED object on pin GPIO17, active_high=True, is_active=False>
>>> led.active_high
True
>>> led.is_active
False
>>> 

``` 

This the GPIO vs board pin layout of the RPi.


[//]: # (Testing out comments in Markdown. This should display an image below)

![GPIO pins of RPi](http://gpiozero.readthedocs.io/en/stable/_images/pin_layout.svg "GPIO pin of RaspberryPi")





