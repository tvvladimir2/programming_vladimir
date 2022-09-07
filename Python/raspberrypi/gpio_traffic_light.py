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
from gpiozero import LED, Button, Buzzer

button = Button(21)
led_red = LED(25)
led_orange = LED(8)
led_green = LED(7)
buzzer = Buzzer(15)

def func_button():
    print('Button pressed')
    led_red.on()
    led_red.blink(2,2)
    led_orange.on()
    led_orange.blink(2,2)
    led_green.on()
    led_green.blink(2,2)
    #led_red.off()
    buzzer.on()
    buzzer.beep()
    #buzzer.off()
    sleep(1)

try:
    button.when_pressed = func_button

finally:
    pass
