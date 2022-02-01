# BOOLEANS

# Booleans represent one of two values: True or False.
a = 200
b = 33
if b > a:   # If this is True
  print("b is greater than a")
else:
  print("b is not greater than a")

# Create a Boolean
my_boolean = True          # Set a variable to a boolean
my_boolean = False
print(2 == 3)              # Created by comparing variables # returns False
print(2 != 10)             # returns True
print("hello" == "hello")  # Created by comparing strings # returns True
print("eleven" != "seven") # returns True
print(7 <= 8)              # returns True

# BOOLEAN NOT
# The result of not True is False, and not False goes to True
my_boolean = not True      # not only takes one argument, and inverts it.

# EVALUATE VALUE AND VARIABLE
# - Almost any value is evaluated to True if it has some sort of content.
# - Any string is True, except empty strings.
# - Any number is True, except 0.
# - Any list, tuple, set, and dictionary are True, except empty ones.
x = "Hello"
print(bool(x))      # returns True

def myFunction() :
  return True       # returns True

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))   # Returns True

# return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

<<== Return here after I study classes !!!
# One more value, or object in this case, evaluates to False,
# and that is if you have an object that is made from
# a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# PRECEDENCE
# See file operators.py
