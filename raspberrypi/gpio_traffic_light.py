'''
Traffic lights + buzzer + button
Component   GPIO pin
Button      21
Red LED     25
Amber LED   8
Green LED   7
Buzzer      15
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

