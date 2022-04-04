# gpiozero.LED()


---


## LINKS

[gpiozero.LED() documentation](https://gpiozero.readthedocs.io/en/stable/recipes.html#led)


---


# ON / OFF

**Example**: Repeatedly.
```python
from gpiozero import LED
from time import sleep


my_led = LED(17)

while True:
    my_led.on()
    sleep(1)
    my_led.off()
    sleep(1)
```

**Example**: Once
```python
from gpiozero import LED
from signal import pause

red = LED(17)

red.blink()

pause()
```

---


# BRIGHTNESS

```python
from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.5  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)
```

```python
from gpiozero import PWMLED
from signal import pause

led = PWMLED(17)

led.pulse()

pause()
```
