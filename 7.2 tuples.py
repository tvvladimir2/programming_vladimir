# TUPPLES
# - Tuples are used to store multiple items in a single variable.
# - Tuple is one of 4 built-in data types in Python used to store collections of
#   data, the other 3 are List, Set, and Dictionary, all with different
#   qualities and usage.
# - Tuples are unchangeable, meaning that we cannot change, add or remove items
#   after the tuple has been created.



thistuple = ("apple", "banana", "cherry")   # written in round brackets
thistuple = ("apple", "banana", "cherry")   # are ordered: [0], [1], [2]
thistuple = ("apple", "apple", "apple")     # allow duplicate values.
thistuple = ("True", "5", "3.00001")        # Can have any data types
thistuple = ("apple",)  # To create a tuple with one item use ','
print(thistuple)W

# PYTHON BUILT-IN FUNCTIONS ==================================================

# len() - MEASURE LENGTH OF TUPLE --------------------------------------------
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))   # Shows the lengths of the Tuple, returns 3
DW
# type() - SHOW DATATYPE -----------------------------------------------------
<class 'tuple'> # - From Python's perspective, tuples are defined as objects
                #   with the data type 'tuple'.
# E.g.:
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# tuple() - CONSTRUCTOR TO MAKE TUPLE ----------------------------------------
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # Tuple to Tuple
thistuple = tuple([(]"apple", "banana", "cherry"]) # List to Tuple
print(thistuple)
