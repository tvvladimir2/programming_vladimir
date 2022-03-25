from signal import pause
from time import sleep
from gpiozero import LED, Button



# function
def go_zero():
    i = 1

def go_one():
    i = 0

button1 = Button(21)
button2 = Button(19)

try:
    button1.when_pressed = go_zero           # Use function name as a callback
    button2.when_pressed = go_one           # Use function name as a callback
    pause()
finally:
    pass








'''
gpiozero documentation:
button class:
https://gpiozero.readthedocs.io/en/stable/api_input.html?highlight=button#gpiozero.Button

class gpiozero.Button(pin, *,
                      pull_up=True,
                      active_state=None,
                      bounce_time=None,
                      hold_time=1,
                      hold_repeat=False,
                      pin_factory=None)

'''
