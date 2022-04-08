'''
Useful link. How to us gpiozero.LED() class.
https://gpiozero.readthedocs.io/en/stable/recipes.html#led
'''

'''
Traffic lights + buzzer + button
Component   GPIO pin
Button      21
Red LED     25
Amber LED   8
Green LED   7
Buzzer      15
'''

'''
Условия задачки:
Traffic light is always green in normal mode.
Normal mode is indefinite.

If button is pressed, the traffic light goes to tresspassing mode.
Using German traffic light system:
- Buzzer starts to beep slowly. Green goes Off. Yellow blinks three times. Then yellow goes Off.
- Red goes On. Wait for 5 seconds. Buzzer is beeping fast.
- Red is still on. Yellow blinks three times. Buzzer is beeping slow.
- Both, yellow and red go off.
- Normal mode is activated.
- Pressing a button in tresspassing mode does nothing.
- Normal mode has a timer of 10 seconds. If you press the button before 10 seconds: Buzzer beeps slow. Once the timer is over 10 seconds, Normal mode is activated.
'''

#from signal import pause
from time import sleep
# import time as t
from gpiozero import LED, Button, Buzzer


# Hardware assignment
button = Button(21)
led_red = LED(25)
led_orange = LED(8)
led_green = LED(7)
buzzer = Buzzer(15)


# Set initial state of hardware
led_red.off()
led_orange.off()
led_green.off()
buzzer.off()


# Timer
timer = True


def timer_func():
    global timer
    for i in range(5):
        print('Can press a button in: ', (5-i))
        buzzer.on()
        buzzer.beep()
        buzzer.off()
        sleep(1)
    timer = True
    print('You can now press the button') 


# Always green
def main_func():
    led_green.on()
    if timer == False:
        timer_func()
    
    
# Red light
def func_button():
    global timer
    # Check if button is pressed
    print('Button pressed')
    if timer == True:
        timer = False

        # Switch green light
        led_green.off()
        
        # Orange
        print('Wait for it')
        led_orange.on()
        buzzer.beep()
        sleep(5)
        led_orange.off()
        
        # Red
        led_red.on()
        print('GO')
        buzzer.beep(0.2,0.2)
        sleep(7)
        buzzer.off()
        
        # Red + Orange
        led_orange.blink(0.5, 0.5)
        print('STOP')
        sleep(5)
        led_orange.off()
        led_red.off()
        # Run main func
        main_func()
        

main_func()

try:
    button.when_pressed = func_button

finally:
    pass
