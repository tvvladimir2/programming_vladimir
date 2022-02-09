# EXCEPTIONS (ERRORS)
#


# COMMON EXCEPTIONS
#------------------------------------------------------------------------------
''' Different exceptions are raised for different reasons.
- ImportError: an import fails;
- IndexError: a list is indexed with an out-of-range number;
- NameError: an unknown variable is used;
- SyntaxError: the code can not be parsed properly;
- TypeError: a function is called on a value of an inappropriate type;
- ValueError: a function is called on a value of the correct type, but with an inappropriate value.
- ZeroDivisionError:
- OSError:
'''

# SYNTAX STRUCTURE
try:
    statements  # run as a normal side of the program
    ...
except:
    statements  # execute this when exception occurs
    ...
else:
    statements  # execute this only if no exceptions are raised
    ...
finally:        # define clean-up actions that must be executed under all circumstances e.g. closing a file.
    statements  # always execute this
    ...
following_statement


# EXCEPTION HANDLING
# - Exception handling is particularly useful when dealing with user input.
# - Custom exceptions should typically be derived from the Exception class.
#------------------------------------------------------------------------------
try:                                # 'try' block contains code that might throw an exception
    num1 = 7
    num2 = 1
    print (num1 / num2)             # If exception occurs, the code in the try block stops being executed
    print("Done calculation")
    variable = 10
    print(variable + "hello")
except ZeroDivisionError:           # The except statement defines the type of exception to handle (in our case, the ZeroDivisionError).
    print("An error occurred")      # If exception occurs, the code in the except block is run
    print("due to zero division")   # If no error occurs, the code in the except block doesn't run.
    raise ValueError                # raise exceptions
except (ValueError, TypeError):     # 'try' statement can have multiple different except blocks to handle different exceptions.
    print("Error occurred")         # Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
except:                             # An except statement without any exception specified will catch all errors.
    print("An error occurred")      # Can catch unexpected errors and hide programming mistakes.
finally:                            # Code within 'finally' statement always runs after execution of the code in the try, and possibly in the except, blocks.
    print("This code will run no matter what")

# EXAMPLE: - VARIABLE TYPE CHECK
pin = input() # 44aB or 3456 (string or number)
try:
	pin = int(pin)
	print("PIN code is created")   # if pin is a number
except ValueError:
	print("Please enter a number") # if pin is string


# RAISE EXCEPTIONS
#------------------------------------------------------------------------------
# Raise exceptions by using the raise statement.
print(1)
raise ValueError                    # Specify the type of the exception raised.
raise NameError("Invalid name!")    # Raise exception with arguments that give detail about them.
raise                               # raise whatever value error


# ASSERTIONS
#------------------------------------------------------------------------------
# A sanity-check that you can turn on or turn off when you have finished testing the program.
# Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.
# AssertionError exceptions can be caught and handled like any other exception using the try-except statement, but if not handled, this type of exception will terminate the program.
print(1)
assert 2 + 2 == 4   # An expression is tested, and if the result comes up false, an exception is raised.
assert 2 + 1 == 3   # Assert statement
assert "h" != "w"   # returns: True
assert False        # returns: False >> AssertionError
print('1')          # This line does not print because privious line gives AssertionError
assert True         # returns: True >> no error
