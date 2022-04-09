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
from timeit import default_timer


timer = default_timer()
button = Button(21)
led_red = LED(25)
led_yellow = LED(8)
led_green = LED(7)
buzzer = Buzzer(15)


led_red.off()
led_yellow.off()
led_green.off()
buzzer.off()


timer = True


def timer_func():
    global timer
    for x in range(5):
        print('You can press the button in: ', (5-x) )
        buzzer.on()
        buzzer.beep()
        buzzer.off()
        sleep(1)
    timer = True
    print('You can press the button')



def main_func():
    global timer
    led_green.on()
    if timer == False:
        timer_func()


def button_func():
    global timer
    print('Cannot trespass')
    buzzer.value = 0.05
    buzzer.beep(0.8, 0.8)
    sleep(3)
    led_green.off()
    led_yellow.on()
    led_yellow.blink(0.5, 0.5)
    sleep(1.5)
    led_yellow.off()
    led_red.on()
    print('Can trespass')
    buzzer.beep(0.2, 0.2)
    sleep(5)
    led_red.off()
    led_yellow.on()
    led_yellow.blink(0.5, 0.5)
    sleep(1.5)
    led_yellow.off()
    buzzer.off()
    print('Cannot trespass')
    led_green.on()
    timer = False
    main_func()


main_func()


try:
    while True:
        if button.is_pressed:
                button_func()


finally:
    pass


# print('Button pressed')
# led_red.on()
# led_red.blink(2,2)
# led_orange.on()
# led_orange.blink(2,2)
# led_green.on()
# led_green.blink(2,2)
# #led_red.off()
# buzzer.on()
# buzzer.beep()
# #buzzer.off()
# sleep(1)
# led.value = 0  off
# sleep(1)
# led.value = 0.5  half brightness
# sleep(1)
# led.value = 1   full brightness

