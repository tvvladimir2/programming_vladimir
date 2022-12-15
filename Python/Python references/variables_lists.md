# LISTS


---


# DESCRIPTION
- Lists are used to store multiple items in a single variable.
- Lists are created using square brackets:
- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

When to use lists:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.


---


## LIST STRUCTURE, SYNTAX
```
list_name = [element1, element2, element3, value4, value5, value6]
list_name_forward_indexing = [0, 1, 2, 3, 4]
list_name_backward_indexing = [-5, -4, -3, -2, -1]
```


---


## CREATE LIST
```python
# 1:
my_empty_list = []
print('1', my_empty_list)

# 2:
mylist = ["apple", "banana", "cherry"]    # order [[0],[1],[2]], [[-3],[-2],[-1]]
print('2', mylist)

# 3:
same_item_list = ["apple", "apple", "apple"]      # Items can be the `same`
print('3', same_item_list)

# 4:
different_element_type_list = ["abc", 34, True]
print('4', different_element_type_list)

# 5:
generated_list = list(range(10))                  # generates a list containing all of the integers, 0 to 9.
print('5', generated_list)

# 6:
my_nested_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print('6', my_nested_list)

# 7:
list_comprehension = [i**3 for i in range(5)]
print('7', list_comprehension)
```
```
> 1 []
> 2 ['apple', 'banana', 'cherry']
> 3 ['apple', 'apple', 'apple']
> 4 ['abc', 34, True]
> 5 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
> 6 ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
> 7 [0, 1, 8, 27, 64]
```


---


## NESTED LISTS
**Example 1**: LISTS INSIDE LISTS
```python
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2])         # Prints ['cc', 'dd', ['eee', 'fff']]
print(L[2])         # Prints ['cc', 'dd', ['eee', 'fff']]
print(L[2][2])      # Prints ['eee', 'fff']
print(L[2][2][0])   # Prints eee
```
```
> ['cc', 'dd', ['eee', 'fff']]
> ['cc', 'dd', ['eee', 'fff']]
> ['eee', 'fff']
eee
```

**Example 2**: NESTED LISTS 2D GRIDS, MATRICES
```python
m = [
    [1,2,3],
    [4,5,6]
    ]
print(m[1][2])
```


---


# LIST PROPERTIES - OPERATIONS==================================================


---


## CONCATENATE LISTS (ADD LISTS)
```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2       # adds lists together, list2 is added at the end
print(list3)
print(list1 + [4, 5, 6])    # returns a,b,c,4,5,6
print(nums * 3)             # returns abcabcabc
```
```
> ['a', 'b', 'c', 1, 2, 3]
> ['a', 'b', 'c', 4, 5, 6]
> ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
```


---


## ACCESS ITEMS
**Example 1**: Access single index
```python
thislist = ["apple", "banana", "cherry"]    # indexing order [[0],[1],[2]]
thislist = ["apple", "banana", "cherry"]    # negative indexing [[-3],[-2],[-1]]
print(thislist[1])
```
```
> banana
```


---

**Example 2**: Access range of indexes, list slices
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]    # [0], [1], [2], [3], [4], [5], [6]
print('1', thislist[2:5])
print('2', thislist[:4])       # returns [0], [1], [2], [3];  number [4] is not included
print('3', thislist[2:])       # returns from [2] to the end
print('4', thislist[2:5:2])    # step is 2
print('5', thislist[-4:-1])
```
```
> 1 ['cherry', 'orange', 'kiwi']
> 2 ['apple', 'banana', 'cherry', 'orange']
> 3 ['cherry', 'orange', 'kiwi', 'melon', 'mango']
> 4 ['apple', 'cherry', 'kiwi']
> 5 ['orange', 'kiwi', 'melon']
```


---


## IN/NOT OPERATORS
Check if item is in a list:
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print("banana" in thislist) # returns True
print(not apple in thislist)    # retruns False
print(not potato in thislist)    # retruns True
```
```
> Yes, 'apple' is in the fruits list
> True
> False
> True
> True
```


---


## REASSIGN INDEXES
**Example 1**: Change item's value
```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"                    # Change one value
print(thislist)
```
```
> ['apple', 'blackcurrant', 'cherry']
```

**Example 2**: Replace a range of values
```python
thislist = ["apple", "banana", "cherry", "tomato"]
thislist[0:3] = ["blackcurrant", "watermelon"]    # Replace a range of values
print(thislist)
thislist[1:3] = ["watermelon"]                    # Replace two values with only one value
print(thislist)
```
```
> ['blackcurrant', 'watermelon', 'tomato']
> ['blackcurrant', 'watermelon']
```


---


## `DEL` KEYWORD

Delete list or list element

`del` keyword deletes item or variable
```python
my_list = ["a", "b", "c"]
del my_list         # deletes the list
del my_list[3:5]    # deletes items in the list
```


---
