# Collatz conjecture
#Rules:
# 1. Pick any number
# if the number is even x:2
# if the number is odd x*3+1
# the result will be a loop of 1>4>2

x = int(input("Please Enter a Number : "))
iterations = 0
x_max = x

print(x)
while True:
    if (x%2==0):
        x=int(x/2)
    else:
        x = int(x*3+1)

    if x > x_max:
        x_max = x
    iterations += 1
    print(x)

    if x==1:
        break

print("this number is collatz")
print(f"Number of iterations:{iterations}")
print(f"Biggest number:{x_max}")
