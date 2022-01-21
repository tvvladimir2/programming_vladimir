# LISTS COMPREHENSION
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# is the same as:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)



thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    #A short hand 'for' loop that will print all items in a list:
'''
L = [mapping-expression for element in source-list if filter-expression]
returns:
apple
banana
cherry
'''
