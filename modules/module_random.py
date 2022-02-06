# Import the random module, and display a random number between 1 and 9:
import random

# random.randrange(start, stop, step)
#------------------------------------------------------------------------------
print(random.randrange(1, 10))

# RANDOM LIST ITEM
#------------------------------------------------------------------------------
colors = ['a', 'b', 'c', 'd', 'e']
print(random.choice(colors))


# EXAMPLE
#------------------------------------------------------------------------------
import random               # import module
random.seed(int(input()))   # initializes the pseudorandom number generator and, in this case, ensures functionality of test cases.
print(random.randint(1,6))  # generate random values in the range of 1 to 6
