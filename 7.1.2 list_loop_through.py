# LISTS LOOPS

# LOOP THROUGH THE LIST OF ITEMS
# =============================================================================
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:  # loops 3 times
  print(x)  # returns the value of each item
# apple
# banana
# cherry


# LOOP THROUGH THE INDEX NUMBERS
# =============================================================================

# USING FOR LOOP
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

# USING WHILE LOOP
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(i)
    print(thislist[i])
    i = i + 1
# 0
# apple
# 1
# banana
# 2
# cherry
