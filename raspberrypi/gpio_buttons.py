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

button0 = Button(2)
button1 = Button(3)

def func_act0():
    # Your code
    print('Button0 pressed')
    z = '0'
    main_func(z)
    sleep(1)

def func_act1():
    # Your code
    print('Button1 pressed')
    z = '1'
    main_func(z)
    sleep(1)
    
def main_func(z):
    global binary_as_string
    binary_as_string += z
    print(binary_as_string)
    if len(binary_as_string) == 8:
        print('Output binary: ', binary_as_string)
        print('Output decimal: ne znayu kak vvesti', )
        binary_as_string = ''

try:     
    button0.when_pressed = func_act0
    button1.when_pressed = func_act1
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
