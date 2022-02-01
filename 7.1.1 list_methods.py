# LIST METHODS
# ----------------------------------------------------------------------------
# Method 	Description
append()	# Adds an element at the end of the list
clear()	    # Removes all the elements from the list
copy()	    # Returns a copy of the list
count()	    # Returns the number of elements with the specified value
extend()	# Add the elements of a list (or any iterable), to the end of the current list
index()	    # Returns the index of the first element with the specified value
insert()	# Adds an element at the specified position
pop()	    # Removes the element at the specified position
remove()	# Removes the item with the specified value
reverse()	# Reverses the order of the list
sort()	    # Sorts the list

# EXAMPLE
list = [1,2]
list.append[4]  # The dot before append is there because it is a method of the list class.

# MAX ITEM IN A LIST
# outputs the max number in a list
data = [7, 5, 6.9, 1, 8, 42, 33]
print(max(data)) # prints 42
print(min(data)) # prints 1
data.remove(max(data)) # removes 42
data.remove(min(data)) # removes 1

# COUNT()
# ----------------------------------------------------------------------------
# Count how many times the element appears in a list
numbers = [2, 3, 5, 2, 11, 2, 7]
print(number.count(numbers(2))) # returns 3 times number 2 is in a list

# INSERT()
# ----------------------------------------------------------------------------
# Insert items to a specified index
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")    # Insert "watermelon" as the third item:
print(thislist) # returns ['apple', 'banana', 'watermelon', 'cherry']

# INDEX()
# ----------------------------------------------------------------------------
# The index method finds the first occurrence of a list item and returns its index.
# If the item isn't in the list, it raises a ValueError.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))   # returns 2

# APPEND()
# ----------------------------------------------------------------------------
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")    # Inserts at the end
print(thislist)

# REMOVE()
# ----------------------------------------------------------------------------
# Remove itmes froma list
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")   # removes banana [1], removes only 1 item
print(thislist) # returns "apple", "cherry", "banana"

# EXTEND ()
# ----------------------------------------------------------------------------
# Add lists
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", True, 5]
thislist.extend(tropical) # add the elements of tropical to thislist at the end
print(thislist)

# POP()
# ----------------------------------------------------------------------------
# Remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)     # The pop() method removes the specified index.
del thislist[1]     # Same as pop
thislist.pop()      # Removes the last item.
print(thislist)

# CLEAR()
# ----------------------------------------------------------------------------
# Clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()    # The clear() method empties the list.
print(thislist)

# SORT()
# ----------------------------------------------------------------------------
# Sort the list
thislist1 = ["apple", "banana", "cherry"]
thislist2 = [100, 50, 65, 82, 23]
city_list3 = [['Omaha', 'Lincoln', 'Norfolk'],
             ['LA', 'San Diego', 'San Francisco'],
             ['Las Vegas', 'Carson City', 'Laughlin']]  # List of lists
thislist1.sort()                # Sorts the list from A to Z
thislist1.sort(reverse = True)  # Sorts the list reversely from Z to A
thislist2.sort()                # Sorts the list numerically
thislist2.sort(reverse = True)  # Sorts the list descending
city_list3.sort()               # Sorted based on what the first item of every list is
print(thislist)

# Customize sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=False, key=criteria)
# key=str.lower # from Upper case to lower case sorting
print(thislist)

# REVERSE()
# ----------------------------------------------------------------------------
# Reverse order of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()  # Reverse the order of the list items:
print(thislist)

# COPY()
# ----------------------------------------------------------------------------
# You cannot copy a list simply by typing list2 = list1, because:
# list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
oldlist = ["apple", "banana", "cherry"]
newlist = oldlist.copy()    # Make a copy of a list with the copy() method:
print(newlist)
