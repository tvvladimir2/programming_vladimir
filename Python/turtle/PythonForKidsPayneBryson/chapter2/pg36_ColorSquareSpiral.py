import turtle
import random

t = turtle.Pen()
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
turtle.bgcolor("black")
for x in range(200):
    # t.pencolor(random.choice(colors))
    t.pencolor(colors[x%4]) # Remainder: Mathimatically switch the item in a list, 0,1,2,3,0,1,2,3,0
    t.forward(x)
    t.left(91)
    print(x, x%4, colors[x%4])
