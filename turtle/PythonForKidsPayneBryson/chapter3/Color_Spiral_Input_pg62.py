import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
sides = int(turtle.numinput("How many sides",
                "How many sides do you want(1-8)?", 4, 1, 8))

for x in range(360):
    t.pencolor(color[sides%x])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x*sides / 200)
