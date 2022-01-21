# LISTS

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
thislist = ["apple", "banana", "cherry"]    # order [[0],[1],[2]], [[-3],[-2],[-1]]
thislist = ["apple", "apple", "apple"]      # Items can be the same
print(thislist)

# PYTHON COLLECTIONS (ARRAYS)
# There are four collection data types in the Python programming language:
thislist = ["apple", "banana", "cherry"] # - List is a collection which is ordered and changeable. Allows duplicate members.
mytuple = ("apple", "banana", "cherry")  # - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
myset = {"apple", "banana", "cherry"}    # - Set is a collection which is unordered and unindexed. No duplicate members.
thisdictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}                                        # - Dictionary is a collection which is ordered* and changeable. No duplicate members.

# LIST LENGTH
thislist = ["apple", "banana", "cherry"]
print(len(thislist))                        # returns 3

# LIST ITEMS DATA TYPES
# List items can be of any data type:
list1 = ["abc", 34, True, 40, "male"]   # A list with strings, integers and boolean values:
print(type(mylist)) # Shows the type of the list
# From Python's perspective, lists are defined as objects with the data type 'list':
<class 'list'>

# list() CONSTRUCTOR
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# ACCESS ITEMS - ORDER
thislist = ["apple", "banana", "cherry"]    # indexing order [[0],[1],[2]]
thislist = ["apple", "banana", "cherry"]    # negative indexing [[-3],[-2],[-1]]
print(thislist[1])  # returns banana

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    # [0], [1], [2], [3], [4], [5], [6]
print(thislist[2:5])   # returns cherry, orange, kiwi
print(thislist[:4])    # returns [0], [1], [2], [3];  number [4] is not included
print(thislist[2:])    # returns from [2] to the end
print(thislist[-4:-1]) # returns from "orange" to "mango", "mango" is not included

# CHECK IF ITEM EXISTS
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# CHENGE ITEM VALUE
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"                    # Change one value
thislist[1:3] = ["blackcurrant", "watermelon"]  # Change two values with two values
thislist[1:2] = ["blackcurrant", "watermelon"]  # Replace one value with two values
thislist[1:3] = ["watermelon"]                  # Replace two values with only one value
print(thislist)

# DELETE LIST OR LIST ITEM
# del keyword deletes item or variable
my_list = ["a", "b", "c"]
del my_list         # deletes the list
del my_list[3:5]    # deletes items in the list

# LOOP THROUGH THE LIST
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:  # loops 3 times
  print(x)  # returns the value of each item
# apple
# banana
# cherry

# LOOP THROUGH THE INDEX NUMBERS
# - You can also loop through the list items by referring to their index number.
# - Use the range() and len() functions to create a suitable iterable.
# - Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len  (thislist)):
    print(i)
    print(thislist[i]) # returns:
# 0
# apple
# 1
# banana
# 2
# cherry

# LOOP THROUGH THE INDEX NUMBERS MATHEMATICALLY
colors = ["red", "yellow", "blue", "green"]
for x in range(1500):
    y = colors[x%4] # Loops through the list, 0,1,2,3,0,1,2,3,0
    print(y, x, x%4)
    # red    0 0
    # yellow 1 1 остаток само число 1 т.к. 1 / 4 не делится без остатка
    # blue   2 2
    # green  3 3
    # red    4 0
    # yellow 5 1
    # blue   6 2
    # green  7 3
    # red    8 0


# METHODS
# =============================================================================

# INSERT ITEMS
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")    # Insert "watermelon" as the third item:
print(thislist) # returns ['apple', 'banana', 'watermelon', 'cherry']

# ADD ITEMS TO LIST
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")    # Inserts at the end
print(thislist)

# REMOVE SPECIFIED ITEM FROM LIST
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")   # removes banana [1], removes only 1 item, first item
print(thislist) # returns "apple", "cherry", "banana"

# MAX ITEM IN A LIST
data = [7, 5, 6.9, 1, 8, 42, 33]
print(max(data)) # prints 42
print(min(data)) # prints 1
data.remove(max(data)) # removes 42
data.remove(min(data)) # removes 1

# EXTEND LIST - ADD LISTS
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", True, 5]
thislist.extend(tropical) # add the elements of tropical to thislist at the end
print(thislist)

# REMOVE SPECIFIED INDEX
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)     # The pop() method removes the specified index.
del thislist[1]     # Same as pop
thislist.pop()      # Removes the last item.
print(thislist)

# CLEAR THE LIST
thislist = ["apple", "banana", "cherry"]
thislist.clear()    # The clear() method empties the list.
print(thislist)

# COUNT NUMBER OF TIMES THE ITEM IS IN A LIST
numbers = [2, 3, 5, 2, 11, 2, 7]
print(number.count(numbers(2))) # returns 3 times number 2 is in a list
