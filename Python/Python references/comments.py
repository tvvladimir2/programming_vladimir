# COMMENTS
#This is a comment
#Use Ctrl+/ to comments lines in Atom
print("Hello, World!") #This is a comment
# print("Hello, World!")
# '#' is an octothorpe, a number sign or hash symbol

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


# DOCSTRINGS (documentation strings)
# Similar to comments, designed to explain code. But, they’re more specific and have a different syntax.
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
#
# READ DOCSTRINGS OF MODULES AND THEIR FUNCTION
import math
print(math.__doc__)     # show math module docstring, documentation
print("-------------")
print(math.pi.__doc__)  # show pi function docstring
