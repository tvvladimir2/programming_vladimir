import turtle

turtle.setup(1000,1000)                   #Determine the window size
window = turtle.Screen()                #Get a reference to the window
window.title("Handling keypresses!")    # Change the window title
window.bgcolor("lightgreen")            # Set the background color
t = turtle.Turtle()                        # Create our favorite turtle
t.speed(10)

# # METHOD2
lead_x = 0
lead_y = 0

# The next four functions are our "event handlers".
def forward():
    t.forward(10)

def stop():
    t.forward(0)

def left():
    t.left(15)

def right():
    t.right(15)

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def crazy():
    colors = ["red", "yellow", "blue", "green"]
    for x in range(40,44):
        t.pencolor(colors[x%4])
        t.circle(x)
        t.left(91)
        print(x)

def house():
    x_zero = -450
    y_zero = 130
    number_houses = 10
    house_rows = 1

    for o in range(house_rows):
        for i in range(number_houses):
            #square
            t.penup()
            t.goto(x_zero,y_zero)
            t.pendown()
            for x in range(4):
                t.left(90)
                t.forward(100)
            #door
            t.goto(x_zero-20,y_zero)
            for x in range(2):
                t.left(90)
                t.forward(40)
                t.left(90)
                t.forward(20)
            #window
            t.penup()
            t.goto(x_zero-60,y_zero+20)
            t.pendown()
            for x in range(4):
                t.left(90)
                t.forward(20)
            t.penup()
            t.goto(x_zero-70,y_zero+30)
            t.pendown()
            for z in range (4):
                t.forward(10)
                t.left(180)
                t.forward(10)
                t.left(90)
            t.penup()
            #roof
            t.goto(x_zero+20,y_zero+100)
            t.pendown()
            #roof_v1
            # for x in range(3):
            #     t.left(120)
            #     t.forward(140)
            # #roof_v2
            t.goto(x_zero-50, y_zero+140)
            t.goto(x_zero-120,y_zero+100)
            t.goto(x_zero+20,y_zero+100)
            t.penup()
            x_zero += 160
            t.goto(x_zero,y_zero)
        y_zero -= 250
        x_zero -= number_houses*160

def quit():
    window.bye() # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
while True:
    turtle.onkey(forward, "Up")
    turtle.onkey(stop, "Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    turtle.onkey(quit, "q")
    turtle.onkey(pen_up, "u")
    turtle.onkey(pen_down, "d")
    turtle.onkey(house, "h")
    turtle.onkey(crazy, "c")
    print(lead_x, lead_y)
    # t.goto(lead_x,lead_y)
    window.listen()
    turtle.mainloop()  # This will make sure the program continues to run

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
