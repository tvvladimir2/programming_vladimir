# LIST METHODS


---


|№ |  Method   | Description                                                                  |
|--|-----------|------------------------------------------------------------------------------|
|1 | append()	 | Adds an element at the end of the list                                       |
|2 | clear()	 | Removes all the elements from the list                                       |
|3 | copy()	   | Returns a copy of the list                                                   |
|4 | count()	 | Returns the number of elements with the specified value                      |
|5 | extend()	 | Add the elements of a list (or any iterable), to the end of the current list |
|6 | index()	 | Returns the index of the first element with the specified value              |
|7 | insert()  | Adds an element at the specified position                                    |
|8 | pop()	   | Removes the element at the specified position                                |
|9 | remove()	 | Removes the item with the specified value                                    |
|10| reverse() | Reverses the order of the list                                              |
|11| sort()	   | Sorts the list                                                               |


---


## 1. APPEND()

To add an item to the end of the list, use the append() method:

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")    # Inserts at the end
print(thislist)
```


---


## 2. CLEAR( )

Clear the list

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()    # The clear() method empties the list.
print(thislist)
```


---


# 3. COPY( )

You cannot copy a list simply by typing list2 = list1, because:
- list2 will only be a reference to list1,
- and changes made in list1 will automatically also be made in list2.

```python
oldlist = ["apple", "banana", "cherry"]
newlist = oldlist.copy()    # Make a copy of a list with the copy() method:
print(newlist)
```


---


## 4. COUNT()

Count how many times the element appears in a list

```python
numbers = [2, 3, 5, 2, 11, 2, 7]
print(number.count(numbers(2))) # returns 3 times number 2 is in a list
```


---


## 5. EXTEND ( )

Add lists
To append elements from another list to the current list, use the extend() method.

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", True, 5]
thislist.extend(tropical) # add the elements of tropical to thislist at the end
print(thislist)
```


---


## 6. INDEX( )
# ----------------------------------------------------------------------------
# The index method finds the first occurrence of a list item and returns its index.
# If the item isn't in the list, it raises a ValueError.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))   # returns 2


---


## 7. INSERT( )
Insert items to a specified index
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")    # Insert "watermelon" as the third item:
print(thislist) # returns ['apple', 'banana', 'watermelon', 'cherry']
```


---


## 8. POP( )

Remove specified index

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)     # The pop() method removes the specified index.
del thislist[1]     # Same as pop
thislist.pop()      # Removes the last item.
print(thislist)
```


---


## 9.REMOVE( )

Remove itmes froma list

```python
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")   # removes banana [1], removes only 1 item
print(thislist) # returns "apple", "cherry", "banana"
```


---


## 10. REVERSE( )

Reverse order of the list

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()  # Reverse the order of the list items:
print(thislist)
```


---


## 11. SORT( )

Sort the list

**Example 1**:
```python
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
```


**Example 2**: Customize sort function
```python
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=False, key=criteria)
# key=str.lower # from Upper case to lower case sorting
print(thislist)
```


---
