'''
Power of two: 128 64 32 16 8 4 2 1
Required output: e.g. 17

Using 8-bit binary system to analyze input.
Input: 0
Input: 0
Input: 0
Input: 1
Input: 0
Input: 0
Input: 0
Input: 1

Output binary: 00010001
Output decimal: 17
'''

from signal import pause
from time import sleep
from gpiozero import LED, Button

# Binary as a string = ' '
binary_as_string = ' '

button1 = Button(2)
button2 = Button(3)

# function
def func_act0()



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
