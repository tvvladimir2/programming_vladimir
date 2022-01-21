# VARIABLES

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# Legal varible names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
myVariableName = "John"     # Camel case - each word, except first, starts with capital letter
MyVariableName = "John"     # Pascal case - each word starts with capital letter
my_variable_name = "John"   # Each word is separated by an underscore character:

# Integers, e.g. 1, 2, 3, 4, 5
x = 4           # x is of type int
x = int(3)      # x will be 3
print(type(x))  # Get type of the variable

# Float, e.g. 1.0, 2,456, 0.000001
y = float(3)  # z will be 3.0
y = float(input("write a number"))

# Strings
z = "Sally" # x is now of type str
# is the same as
x = 'Sally'
x = str(3)    # x will be '3'
print(x)

# Tuple
x = ["apple", "banana", "cherry"]

# Boolean
x = True

#CASTING
# Specify a type on to a variable:
x = int(1)   # x will be 1

# ASSIGN MULTIPLE VARIABLES
x, y, z = "Orange", "Banana", "Cherry"  # multiple variables in one line
x = y = z = "Orange"                    # same value to multiple variables

# UNPACK VARIABLES
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# DELETE VARIABLES
x = 5
my_list = ["a", "b", "c"]
del x               # deletes the variable
del my_list         # deletes the list
del my_list[3:5]    # deletes items in the list

# GLOBAL VARIABLES
# - Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# - Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
    x = "fantastic"     # Create a variable inside a function, with the same name as the global variable
    # use the global keyword if you want to change a global variable inside a function.
    y = global("cool")  # use the global keyword, the variable belongs to the global scope
  print("Python is " + x)

myfunc()
print(x)
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
