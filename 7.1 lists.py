# LISTS

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
thislist = ["apple", "banana", "cherry"]    # order [[0],[1],[2]], [[-3],[-2],[-1]]
thislist = ["apple", "apple", "apple"]      # Items can be the same
thislist = list(range(10))                  # generates a list containing all of the integers, 0 to 9.
print(thislist)

# NESTED LISTS
# Lists inside lists
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2])         # Prints ['cc', 'dd', ['eee', 'fff']]
print(L[2])         # Prints ['cc', 'dd', ['eee', 'fff']]
print(L[2][2])      # Prints ['eee', 'fff']
print(L[2][2][0])   # Prints eee

# NESTED LISTS 2D GRIDS, MATRICES
m = [
    [1,2,3],
    [4,5,6]
    ]
print(m[1][2])

# LIST PROPERTIES - OPERATIONS==================================================

# CONCATENATE LISTS -----------------------------------------------------------
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 # adds lists together, list2 is added at the end
print(list3)
print(list1 + [4, 5, 6])    # returns a,b,c,4,5,6
print(nums * 3)             # returns abcabcabc
# See also 'append' & "extend' method

# ACCESS ITEMS - ORDER --------------------------------------------------------
thislist = ["apple", "banana", "cherry"]    # indexing order [[0],[1],[2]]
thislist = ["apple", "banana", "cherry"]    # negative indexing [[-3],[-2],[-1]]
print(thislist[1])  # returns banana

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    # [0], [1], [2], [3], [4], [5], [6]
print(thislist[2:5])   # returns cherry, orange, kiwi
print(thislist[:4])    # returns [0], [1], [2], [3];  number [4] is not included
print(thislist[2:])    # returns from [2] to the end
print(thislist[-4:-1]) # returns from "orange" to "mango", "mango" is not included

# IN/NOT OPERATORS --- CHECK IF ITEM IN LIST ----------------------------------
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print("banana" in thislist) # returns True
print(not apple in thislist)    # retruns False
print(not potato in thislist)    # retruns True

# REASSIGN INDEXES - CHANGE ITEM VALUE
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"                    # Change one value
nums[2] = 5                                     # certain index in a list can be reassigned.
nums[0] = nums[1] - 5
thislist[1:3] = ["blackcurrant", "watermelon"]  # Change two values with two values
thislist[1:2] = ["blackcurrant", "watermelon"]  # Replace one value with two values
thislist[1:3] = ["watermelon"]                  # Replace two values with only one value
print(thislist)

# DELETE LIST OR LIST ITEM
# del keyword deletes item or variable
my_list = ["a", "b", "c"]
del my_list         # deletes the list
del my_list[3:5]    # deletes items in the list

# PYTHON BUILT-IN FUNCTIONS ===================================================

# len() FUNCTION - LIST LENGTH
# len is written before the list it is being called on, without a dot.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))                        # returns 3

# type() - LIST ITEMS DATA TYPES
# ------------------------------
# Python built-in function
# List items can be of any data type:
list1 = ["abc", 34, True, 40, "male"]   # A list with strings, integers and boolean values:
print(type(mylist)) # Shows the type of the list
# From Python's perspective, lists are defined as objects with the data type 'list':

# list() CONSTRUCTOR - Python built-in function
# ---------------------------------------------
thislist = list(("apple", "banana", "cherry")) # tuple made into a list
print(thislist) # returns a list
#
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) # Make a copy of a list with the list()
print(mylist)

# KEYWORDS ====================================================================
# del - DELETE LIST OR LIST ITEM
my_list = ["a", "b", "c"]
del my_list         # deletes the list
del my_list[3:5]    # deletes items in the list
