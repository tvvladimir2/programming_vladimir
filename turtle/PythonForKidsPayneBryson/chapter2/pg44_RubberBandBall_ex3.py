import turtle
import time

turtle.setup(1000,1000)                   #Determine the window size
window = turtle.Screen()                #Get a reference to the window
window.title("Handling keypresses!")    # Change the window title
window.bgcolor("lightgreen")            # Set the background color

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(3)
sides = 6
colors = ["red", "yellow", "blue", "orange", "green",
"purple", ]

def quit():
    window.bye() # Close down the turtle window

# t.left(36)

for x in range(5):
    t.pencolor(colors[x%sides])
    t.forward(200)
    t.left(144)
    print(x)

t.right(72)
t.circle(210.29/2)
# t.settiltangle(0) # settiltangle(angle)
# time.sleep(1)
# t.settiltangle(45) # settiltangle(angle)
# time.sleep(1)
# t.settiltangle(90) # settiltangle(angle)
# t.forward(215)
# t.penup()
t.setheading(180)
# t.tilt(180) # settiltangle(angle)
# turtle.reset()
t.forward(80)
t.left(90)
t.pendown()
# t.settiltangle(180)
t.circle(370/2)

turtle.onkey(quit, "q")

window.listen()
turtle.mainloop()  # This will make sure the program continues to run
