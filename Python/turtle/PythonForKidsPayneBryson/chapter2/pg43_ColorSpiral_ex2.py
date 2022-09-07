import turtle

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
# sides = int(input("Type number of sides:"))
sides = eval(input("Type number of sides(Maximum 10 sides):"))

colors = ["red", "yellow", "blue", "orange", "green",
"purple", "pink", "white","brown", "black"]

for x in range(360):
    t.pencolor(colors[x%10])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    print(x)
