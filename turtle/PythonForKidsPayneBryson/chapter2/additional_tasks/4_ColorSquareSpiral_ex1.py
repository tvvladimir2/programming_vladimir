import turtle
import random
# Random color each square

# t = turtle.Pen()
# t.speed(0)
# colors = ["red", "yellow", "blue", "green"]
# for x in range(1500):
#     t.pencolor(random.choice(colors))
#     t.forward(x)
#     t.left(93)
#     t.forward(x)
#     t.left(93)
#     t.forward(x)
#     t.left(93)
#     t.forward(x)
#     t.left(93)
#     print(x)

t = turtle.Pen()
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(200):
    t.pencolor(random.choice(colors))
    for y in range(4):
        t.forward(x)
        t.left(93)

    print(x)
