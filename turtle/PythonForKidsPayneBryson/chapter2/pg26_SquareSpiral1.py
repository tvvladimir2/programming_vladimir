import turtle

p = turtle.Turtle()

# for x in range(1000):
#     t.forward(x)
#     t.left(90)

p.penup()
p.goto(1,300)
p.pendown()
p.left(90)

# рисуем забор
while True:
    p.forward(50)
    p.right(45)
    p.forward(10)
    p.right(45)
    p.forward(10)
    p.right(45)
    p.forward(10)
    p.right(45)
    p.forward(50)
    p.left(90)
    p.forward(25)
    p.left(90)
