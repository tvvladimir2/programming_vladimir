# FUNCTIONS
# ----------------------------

# You can create your own functions by using the def statement.

# SYNTAX STRUCTURE
def name(arguments):    # function name = indentifier (parentheses = function call) # creates your own function
    """This function prints
       message on the screen""" # Docstring for a documentation
    statement           # /(function body), executed each time the function is called
    statement           # must be indented
    ...
    return(value)       # Nothing is executed after a return statement. Returns None if not specified.
    return a+b, a-b     # return multiple values as a tuple.
# So once you’ve defined a function, you can call it multiple times in your code.
# The function needs to be defined before it can be called. Calling a function before its definition will cause an error.
my_func(arguments) # call it first time
# you can pass as many arhuments as you like
my_func('Bob', var, 10) # call it second time and pass three agruments


# NESTED FUNCTIONS
# A function defined within other function.
# They are useful when performing complex task multiple times within another function, to avoid loops or code duplication.
# A nested function can act as a closure.
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
result = outer(2, 4)
print(result)   # Prints 6


# FUNCTION ARGUMENT CANNOT BE REFERENCED OUTSIDE THE FUNCTION
def function(variable):
    variable += 1
    print(variable)
function(7)             # Prints 8
print(variable)         # NameError: name 'variable' is not defined


# RECURSION
# A function calls itself and repeats its behavior until some condition is met to return a result.
def countdown(num):
    if num <= 0:
        print('Stop')
    else:
        print(num)
        countdown(num-1)
countdown(5)    # Prints 5, 4, 3, 2, 1, Stop


# DOCSTRING
def func():
    '''documentation
    is here'''
print(func.__doc__)    # prints the docstring of a function
help(func)             # uses help() function to print the function docstring


# UNPACK RETURNED TUPLE
def func(a,b)
    return a+b, a*b
add, multiply = func(3, 2)   # add = a+b; multiply=a*b


# EXAMPLE
# Functions can take arguments, which can be used to generate the function output.
def exclamation(word): # variable word = "spam"
   print(word + "!") # returns: spam!
exclamation("spam") # call function


# CALL SAME FUNCTION WITH DIFFERENT ARGUMENTS
def exclamation(word):
   print(word + "!")
# returns: spam!
# returns: eggs!
exclamation("spam")
exclamation("eggs")


# ASSIGNING FUNCTIONS TO VARIABLES
#------------------------------------------------------------------------------
def hello():
    print('Hello, World!')
hi = hello  # Assign a different name to function and call through the new name.
hi()    # Prints Hello, World!
#
# JUMP TABLE USING ABOVE METHOD
#------------------------------
def findSquare(x):
    return x ** 2
def findCube(x):
    return x ** 3
exponent = {'square': findSquare, 'cube': findCube} # Create a dictionary of functions
print(exponent['square'](3))    # passes 3 as an argument # Prints 9
print(exponent['cube'](3))  # Prints 27


# PYTHON FUNCTION EXECUTES AT RUNTIME
# Because Python treats def as an executable statement, it can appear anywhere a normal statement can.
x = 0
if x:
    def hello():                    # nest a function inside an if statement to select between alternative definitions.
        print('Hello, World!')
else:
    def hello():
        print('Hello, Universe!')
hello()                             # Prints Hello, Universe!


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


# FUNCTION AS AN ARGUMENT
#------------------------------------------------------------------------------
def add(x, y):
    return x + y
def do_twice(func, x, y):   # func = add
    return func(func(x, y), func(x, y)) # executes add from here x3 times
# > return func (15, 15)
# > return 30
a = 5
b = 10
print(do_twice(add, a, b))  # prints 30
