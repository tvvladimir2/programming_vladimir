import turtle

window = turtle.Screen()
t = turtle.Pen()
t.speed(0)

# METHOD2
x_zero = -450
y_zero = 130
number_houses = 7
house_rows = 3

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
