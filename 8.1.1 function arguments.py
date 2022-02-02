# FUNCTION ARGUMENTS

# TYPES OF ARGUMENTS (see sub chapter)
# Supports such arguments:
# - Positional Arguments
# - Keyword Arguments
# - Default Arguments
# - Variable Length Positional Arguments (*args)
# - Variable Length Keyword Arguments (**kwargs)

# POSITIONAL ARGUMENTS
#------------------------------------------------------------------------------
# Values are copied to their corresponding parameters in order.
# You need to pass arguments in the order in which they are defined.
def func(name, job):
    print(name, 'is a', job)
func('Bob', 'developer')    # Prints Bob is a developer


# KEYWORD ARGUMENTS
#------------------------------------------------------------------------------
# Pass arguments using the names of their corresponding parameters.
# The order of the arguments no longer matters
def func(name, job):
    print(name, 'is a', job)
func(job='developer', name='Bob')   # Prints Bob is a developer


# KEYWORD + POSITIONAL ARGUMENTS
#------------------------------------------------------------------------------
# combine positional and keyword arguments in a single call.
# Specify the positional arguments before keyword arguments.
def func(var1, var2, name, job):
    print(name, 'is a', job)
func(40, 36, job='developer', name='Bob')   # Prints Bob is a developer


# DEFAULT ARGUMENTS
#------------------------------------------------------------------------------
# Specify default values for arguments when defining a function.
# Makes selected arguments optional.
# Set default value 'developer' to a 'job' parameter
def func(name, job='developer'):
    print(name, 'is a', job)
func('Bob', 'manager')  # Prints Bob is a manager
func('Bob')             # Prints Bob is a developer


# VARIABLE LENGTH ARGUMENTS (*args and **kwargs) (var-args)
#------------------------------------------------------------------------------
# For creating functions that take unlimited number of arguments
# Unknow number of arguments before passing them to your function.
# *args
#--------------------
# A parameter prefixed with an asterisk * collects all the unmatched positional arguments into a tuple.
# It is a normal tuple >> perform any operation that a tuple supports, like indexing, iteration etc.
def print_arguments(*args):
    print(args)
print_arguments(1, 54, 60, 8, 98, 12)   # Prints (1, 54, 60, 8, 98, 12)
