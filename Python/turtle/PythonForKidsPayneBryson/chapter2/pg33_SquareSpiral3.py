import turtle

t = turtle.Pen()
t.pencolor("green")
t.speed(0)
sides = 3
colors = ["red", "yellow", "blue", "green"]
for x in range(1500):
    t.forward(x)
    t.left(60)
