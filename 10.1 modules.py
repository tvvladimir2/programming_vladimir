'''
Built-in modules in Python are written in C and interpreted using the Python interpreter.
Pieces of code written by someone else.
'''


# LIST INSTALLED MODULES
#------------------------------------------------------------------------------
print (help('modules') ) # list all modules installed in Python


# STRUCTURE SYNTAX
from module_name import var1, var2, function1, function2
x = module_name.function1()
y = var1


# IMPORT & ACCESS VALUES, USE FUNCTIONS
#------------------------------------------------------------------------------
import the                              # import module with all functions and values
from math import pi                     # Import a certain function.
from math import pi, sqrt               # Import multiple objects using ','
from math import sqrt as square_root    # import an object under a different name using 'as' keyword
import math as m                        # import a module under a different name using 'as' keyword
x = math.sqrt(9)                        # module.function() >> random.randint()
