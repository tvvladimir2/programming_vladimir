# Define a function
def shout(word):
  """
  This function prints a word with an
  exclamation mark following it.
  """
  # Above is a doctring comment, it must be the first line in a fucntion. Can not use simple comments.
  print(word + "!")
  print(shout.__doc__) # will print the Docstring

# Call a function 'shout'
shout("spam")