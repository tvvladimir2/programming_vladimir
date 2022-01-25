#This is a comment
#Use Ctrl+/ to comments lines in Atom
print("Hello, World!") #This is a comment
# print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
# is the same as:
'''
This is a comment
written in
more than just one line
'''

# Output
x = "awesome"
y = "game"
z = 5
print("Python is " + x) # print statement is often used to output variables.
print(x + y)            # + character works as a mathematical operator
print(x+ z) # !!!   > gives arror combing string and number.

# Docstrings (documentation strings) are similar to comments, in that they’re designed to explain code. But, they’re more specific and have a different syntax.
# They’re created by putting a multiline string containing an explanation of the function below the function's first line. Like this:
# Docstrings act as documentation for other developers who use your function.
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  # Above is a doctring, it is must be the first line in a fucntion. Can not use simple comments.
  print(word + "!")
  print(shout.__doc__) # will print the Docstring

shout("spam")

# Read docstrings of modules and their functions
import math
print(math.__doc__)     # show math module docstring, documentation
print("-------------")
print(math.pi.__doc__)  # show pi function docstring
