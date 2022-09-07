# Swap variables
a = int(input("Input a: "))
b = int(input("Input b: "))
print("a = ", a)
print("b = ", b)

# Method 1
# a2 = a
# b2 = b
# a = b2
# b = a2

#Method 2
# a = a + b # a = 13
# b = a - b # b = 3
# a = a - b

# Method 3
a, b = b, a

print("a = ", a)
print("b = ", b)

x=1
y=2
z=3
w=4
x, y, z, w = y, x, w, z
print(f"{x},{y},{z},{w}")
