# Fibonacci sequence
# 0 1 1 2 3 5 8 13 21 34

a = 0
b = 1
print(a)
print(b)
while b < 1000000000: # Terminate on condition, or it will run forever and get stuck
    c = a + b
    print(c)
    a = b
    b = c
