import os
os.system('cls') # Clear the screen on Windows
# 0 1 1 2 3 5 8 13 21 34 55 89

def fib(x,y,z):
    a = x
    b = y
    print("\n" * 5)
    print(f"Starting fibonacci sequence. First number is {a}, second number is {b}. Number of iterrations is {z}.")
    print(a)
    print(b)
    for i in range (z):
        c = a + b
        print(c)
        a = b
        b = c

# x = 0 # First number
x = int(input("Please type the first number of Fibonacci sequence:"))

# y = 1 # Second number
y = int(input("Second: "))
# z = 20 # Number of iteractions
z = int(input("Number of iteractions:"))
fib(x,y,z)

# for loops are traditionally used when you have a block
# of code which you want to repeat a fixed number of times.
# The Python for statement iterates over the members of a sequence in order,
# executing the block each time.
# Contrast the for statement with the ''while'' loop,
# used when a condition needs to be checked each iteration,
# or to repeat a block of code forever.
# for i in range (0, 10):
# a = 10
# for i in range (11):
#     print(a)
#     a += 1
