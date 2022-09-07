print("How many turtles?")
turtle_number = int(input("> "))

import turtle
import random

x_screen = 1000
y_screen = 1000

turtle.setup(x_screen, y_screen)           # Determine the window size
window = turtle.Screen()          # Get a reference to the window
window.title("Turtle race!")      # Change the window title
window.bgcolor("white")           # Set the background color

colors = ['orange', 'red', 'blue', 'green', 'black']

t1 = turtle.Turtle()
t1.pencolor(colors[0])
t1.speed(5)

t2 = turtle.Turtle()
t2.pencolor(colors[1])
t2.speed(5)

if turtle_number > 2:
    t3 = turtle.Turtle()
    t3.pencolor(colors[2])
    t3.speed(5)
if turtle_number > 3:
    t4 = turtle.Turtle()
    t3.pencolor(colors[3])
    t4.speed(5)
if turtle_number > 4:
    t5 = turtle.Turtle()
    t5.pencolor(colors[4])
    t5.speed(5)

# The next four functions are our "event handlers".
def forward():
    t1.speed(random.randrange(1, 5))
    t1.forward(800)
    t2.speed(random.randrange(1, 5))
    t2.forward(800)
    if turtle_number > 2:
        t3.speed(random.randrange(1, 5))
        t3.forward(800)
    if turtle_number > 3:
        t4.speed(random.randrange(1, 5))
        t4.forward(800)
    if turtle_number > 4:
        t5.speed(random.randrange(1, 5))
        t5.forward(800)
    window.ontimer(forward, 250)

# for x in range

# These lines "wire up" keypresses to the handlers we've defined.

t1.penup()
t1.goto((-x_screen/2)+(x_screen/(turtle_number+1))*1, -400)
t1.left(90)
t1.pendown()
t2.penup()
t2.goto((-x_screen/2)+(x_screen/(turtle_number+1))*2, -400)
t2.left(90)
t2.pendown()
if turtle_number > 2:
    t3.penup()
    t3.goto((-x_screen/2)+(x_screen/(turtle_number+1))*3, -400)
    t3.left(90)
    t3.pendown()
if turtle_number > 3:
    t4.penup()
    t4.goto((-x_screen/2)+(x_screen/(turtle_number+1))*4, -400)
    t4.left(90)
    t4.pendown()
if turtle_number > 4:
    t5.penup()
    t5.goto((-x_screen/2)+(x_screen/(turtle_number+1))*5, -400)
    t5.left(90)
    t5.pendown()
# turtle.ontimer(forward, 250)
window.ontimer(forward, 250)
turtle.onkey(forward, "Up")
window.update()
window.listen()
turtle.mainloop()  # This will make sure the program continues to run

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
