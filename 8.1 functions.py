# FUNCTIONS
# ----------------------------

# You can create your own functions by using the def statement.

def my_func(): # Here’s an example of a function named my_func.
   print("spam") # It takes no arguments, and prints "spam" 1 time.

# So once you’ve defined a function, you can call it multiple times in your code.
# The function needs to be defined before it can be called. Calling a function before its definition will cause an error.
my_func() # call it first time
my_func() # call it second time

# Functions can take arguments, which can be used to generate the function output.
def exclamation(word): # variable word = "spam"
   print(word + "!") # returns: spam!

exclamation("spam")

# You can call the same function with different arguments.
def exclamation(word):
   print(word + "!")
# returns: spam!
# returns: eggs!
exclamation("spam")
exclamation("eggs")

# You can define functions with more than one argument; separate them with commas. Like this:
# Arguments can be used as variables inside the function.
def print_sum_twice(x, y):
   print(x + y) # returns 5 + 8 = 13
print_sum_twice(5, 8)

# Function smay return value or a variable or an expression
def square(x):
    return x**2 #returns x squared

# We can use a function inside an if statement and other
def square(x):
    return x**2 #returns x squared
if (square(2) < 10):
    print (x)

# Any code placed after the return statement won’t be executed.
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

 # A function can only return once, thus, if you need to return multiple values, you can use a list.
 def double(a, b):
   return [a*2, b*2]
