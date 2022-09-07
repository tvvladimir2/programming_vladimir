import turtle

turtle.setup(1000,1000)                   #Determine the window size
window = turtle.Screen()                #Get a reference to the window
window.title("Handling keypresses!")    # Change the window title
window.bgcolor("lightgreen")            # Set the background color
t = turtle.Turtle()                        # Create our favorite turtle
t.speed(0)

# # METHOD2
# x_zero = 0
# y_zero = 0

# The next four functions are our "event handlers".
def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def crazy():
    colors = ["red", "yellow", "blue", "green"]
    for x in range(50):
        t.pencolor(colors[x%4])
        t.circle(x)
        t.left(91)
        print(x)

def quit():
    window.bye() # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down") # first function name, then button
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(quit, "q")
turtle.onkey(pen_up, "u")
turtle.onkey(pen_down, "d")
turtle.onkey(crazy, "c")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
window.listen()
turtle.mainloop()  # This will make sure the program continues to run
