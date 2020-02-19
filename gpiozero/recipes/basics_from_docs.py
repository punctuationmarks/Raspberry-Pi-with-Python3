'''
Note, this will not be able to run or even be imported
on a linux machine that isn't a Raspberry pi, 
this is due to not having GPIO pins 
(it fails at library import)
'''


# Basic "Recipes" via GPIOzero's docs
# import gpiozero
# from gpiozero import Button
# from gpiozero import LED


# led =  LED(26)
# led = LED("GPIO16")
# led = LED("BOARD37")


# making an led blink
def blinkingLED(gpio=""):
    from time import sleep
    led = LED(gpio)
    time = 5
    while time > 0:
        time -= 1
        print(time)
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)


# blinkingLED("BOARD27")

# LED also has a blink method
# from signal import pause
# led = LED(gpio)
# led.blink()
# pause()


def ledWithVaryingBrightness(gpio=""):
    from gpiozero import PWMLED
    from time import sleep
    led = PWMLED(gpio)

    time = 5
    while time > 0:
        led.value = 0  # off
        sleep(1)
        led.value = 0.5  # half brightness
        sleep(1)
        led.value = 1  # full brightness
        sleep(1)

# ledWithVaryingBrightness("BOARD13")

# PWMLED also has built in pulse method
# led = PWMLED(x)
# led.pulse()


# these are all the same GPIO pin
# button = Button(27)
# button = Button("GPIO27")
# button = Button("BOARD13")


# print(button)
# <gpiozero.Button object on pin GPIO22, pull_up=True, is_active=False>

# print(type(button))
# <class 'gpiozero.input_devices.Button'>

# print(button.is_pressed)
# False

# print(type(button.is_pressed))
# <class 'bool'>

# GPIOzero's Button.is_pressed
def button_pressed_funct(button):
    if button.is_pressed:
        print("Button has been pressed\nBoolean=1")
    else:
        print("Button has not been pressed\nBoolean=0")

# button_pressed_funct(buttonPin22)


# GPIOzero's Button.wait_for_press()
def button_pressed_with_pause_until_press(gpio=""):
    from gpiozero import Button
    # note how this method is called
    # vs how the is_pressed method
    button = Button(gpio)
    button.wait_for_press()
    print("This only runs once the button has been pressed")
    print("Should be very valuable for have a series of steps with buttons\nstarting or stopping the code")


# GPIOzero's Button.when_pressed
def print_something_on_button_press():
    print("when called, this prints")


def button_pressed_calls_functions(gpio=""):
    from gpiozero import Button
    from signal import pause

    button = Button(gpio)
    '''
	Note: when calling a function with button.when_pressed, the function
	does not have parentheses () on the function
	Check the docs for explanation, but will not run right with ()
	'''
    button.when_pressed = print_something_on_button_press
    pause()


# from GPIO docs on how to play music with pygame
def music_player(gpio_pins=None):
    from gpiozero import Button
    import pygame.mixer
    from pygame.mixer import Sound
    from signal import pause

    # initializing
    pygame.mixer.init()

    button_sounds = {
        # note, pygame needs .wav files to make this useful
        # so convert as needed
        Button(gpio_pins[0]): Sound("./music_files_from_sonic_pi/samples/ambi_choir.wav"),
        Button(gpio_pins[1]): Sound("./music_files_from_sonic_pi/samples/ambi_dark_woosh.wav"),
        Button(gpio_pins[2]): Sound("./music_files_from_sonic_pi/samples/ambi_drone.wav"),
        Button(gpio_pins[3]): Sound("./music_files_from_sonic_pi/samples/ambi_glass_hum.wav")
    }

    # looping over the dictionary and allowing the buttons to call the sound
    # upon any press
    for button, sound, in button_sounds.items():
        button.when_pressed = sound.play

	# having the pause allows the button to stop when 
	# no longer being pressed?
    pause()


'''
So this is the same structure as above, testing the concept with print 
statements, since this is something I might actually need to use to build the
light show project
'''


def testing_list_to_dict_printing(some_list=None):
    x = {
        some_list[0]: "value_1",
        some_list[1]: "value_2",
        some_list[2]: "value_3"
    }
    for key, value in x.items():
        print(key, " : ", value)

# z = [0, 1, 2]
# f(z)


# another option for yusing a button to play music
# with hardcoded buttons and music wav files
def music_player_from_Rpi_projects():

    from gpiozero import Button
    import pygame
    # initializing pygame
    pygame.init()

    # grabbing each sound you want to use
    drum = pygame.mixer.Sound("./music_files_from_sonic_pi/samples/drum_tom_mid_hard.wav")
    cymbal = pygame.mixer.Sound("./music_files_from_sonic_pi/samples/drum_cymbal_hard.wav")
    snare = pygame.mixer.Sound("./music_files_from_sonic_pi/samples/drum_snare_hard.wav")
    cow_bell = pygame.mixer.Sound("./music_files_from_sonic_pi/samples/drum_cowbell.wav")
    # you can play the individual sound by calling play()
    # drum.play()

    # initializng the GPIO buttons
    btn_drum = Button(4)
    btn_cymbal = Button(17)
    btn_snare = Button(27)
    btn_cow_bell = Button(10)
    # calling the play() function on the sound
    # you want when button is pressed
    # NOTE: remember the syntax is functionName without the parenthesis
    btn_drum.when_pressed = drum.play
    btn_cymbal.when_pressed = cymbal.play
    btn_snare.when_pressed = snare.play
    btn_cow_bell.when_pressed = cow_bell.play
