from gpiozero import Button

# Create button class
button = Button(2)

# Get button input and control it
while true:
    button.wait_for_press()
    print('Button pressed')
    # Поставить режим ожидания чтобы ждать следующего нажатия
    time.sleep(1)
