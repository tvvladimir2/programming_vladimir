# Method 1
print("Method1")
a = 100
b = 6
print(a)
print(b)
c=b
d=a
a=c
b=d
print(a)
print(b)

# Method 2
print("Method2")
a = int(input("type in amount of a:"))
b = int(input('type in amount of b:'))
print(a)
print(b)
a = a + b  # a = 106
b = a - b  # b = 100
a = a - b  # a = 6
print(a)
print(b)

# Method 3
print("Method3")
a = int(input("type in amount of a:"))
b = int(input('type in amount of b:'))
z = 456
print(a)
print(b)
a,b,z = z,b,a
print(a)
print(b)
print(z)
