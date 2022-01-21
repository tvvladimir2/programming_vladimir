import math_calc

x = int(input(">")) # main number variable

while True:
    print("please type in one of these functions:=,+,-,/,*")
    job = input(f"{x}") # that means these all are functions you can use
    if job == "+":
        x = math_calc.func_add(x) #math_calc.func_add(x)
    if job == "-":
        x = math_calc.func_min(x)
    if job == "*":
        x = math_calc.func_mult(x)
    if job == "/":
        x = math_calc.func_div(x)
    print(f"{x}")
