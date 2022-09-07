# Collatz conjecture
#Rules:
# 1. Pick any number
# if the number is even x:2
# if the number is odd x*3+1
# the result will be a loop of 1>4>2

# Enter a range of numbers for which the iterations should be calculated
# Example from 5 to 500
# Print the number with the biggest amount of iterations and a number of iterations
# Print x, x_max_super, x_iterations

# Input check
while True:
    while True:
        x1 = int(input("Please Enter lowest Number : "))
        if type(x1)==int:
            break
    while True:
        x2 = int(input("Please Enter highest Number : "))
        if type(x2)==int:
            break
    if x2 > x1:
        break

def collatz_conjecture(x):

    x_iterations = 0
    x_peak = x1

    while True:
        if (x%2==0):
            x=int(x/2)
        else:
            x = int(x*3+1)

        if x > x_peak:
            x_peak = x

        x_iterations += 1

        if x==1:
            break
    return x_peak, x_iterations

x_peak_all = 0
x_iterations_all = 0
x_peak_x = 0
x_iterations_x = 0

for i in range(x1, x2+1):
    if result[0] > x_peak_all: # x_peak > x_peak_all
        x_peak_all = result[0] # x_peak_all = x_peak
        x_peak_x = i # x_peak_x = i
    if result[1] > x_iterations_all:
        x_iterations_all = result[1]
        x_iterations_x = i

print(f"\nHighest peak {x_peak_all} was for {x_peak_x}.")
print(f"The most {x_iterations_all} was for {x_iterations_x}")
print(f"Overall amount of iterations for all x is {all_quantity}.\n")
