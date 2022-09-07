import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
colors = ["red", "yellow", "blue", "green"]
sides = int(turtle.numinput("How many sides", "How many sides do you want(1-8)?", 4, 1, 8))

for x in range(500):
    t.pencolor(colors[x%sides])
    t.circle(sides)
    t.left(91)
    print(x)
