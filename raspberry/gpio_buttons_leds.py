from signal import pause
from time import sleep
from gpiozero import LED, Button

# Control LED
# blink_on = False
#
# def go_blink():
#     global blink_on
#
#     if blink_on:
#         led1.off()
#         led2.off()
#     else:
#         led1.blink(0.5, 0.5)
#         sleep(0.5)
#         led2.blink(0.5, 0.5)
#
#     blink_on = not blink_on
#
# led1 = LED(26)
# led2 = LED(19)

button1 = Button(21)
button2 = Button(19)

try:
    # button1.when_pressed = go_blink           # Use function name as a callback
    # button.when_pressed = led1.on
    # button.when_pressed = led1.blink
    # button.when_pressed = led1.blink(0.5, 0.5)

    pause()
finally:
    pass
