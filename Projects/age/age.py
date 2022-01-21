age1 = int(input("type in person1 age"))
age2 = int(input("type in person2 age"))
print(age1)
print(age2)
age3 = age2 - age1
age4 = age1 - age2
if age1 < age2:
    print(age3)
    print("age2 is bigger")
elif age2 == age1:
    print(0)
    print("none is bigger")
else:
    print(age4)
    print("age1 is bigger")
