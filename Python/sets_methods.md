# SET METHODS


---


№ |             Method            |                                     Description                                     |
--|:-----------------------------:|:-----------------------------------------------------------------------------------:|
01| add()                         | Adds an element to the    set                                                       |
02| clear()                       | Removes all the    elements from the set                                            |
03| copy()                        | Returns a copy of the set                                                           |
04| difference()                  | Returns a set      containing the difference between two or more sets               |
05| difference_update()           | Removes the      items in this set that are also included in another, specified set |
06| discard()                     | Remove the specified    item                                                        |
07| intersection()                | Returns a set,      that is the intersection of two or more sets                    |
08| intersection_update()         |    Removes the items in this set that are not present in other, specified set(s)    |
09| isdisjoint()                  | Returns whether      two sets have a intersection or not                            |
10| issubset()                    | Returns whether      another set contains this set or not                           |
11| issuperset()                  | Returns whether    this set contains another set or not                             |
12| pop()                         | Removes an element from the    set                                                  |
13| remove()                      | Removes the specified element                                                       |
14| symmetric_difference()        | Returns      a set with the symmetric differences of two sets                       |
15| symmetric_difference_update() |    inserts the symmetric differences from this set and another                      |
16| union()                       | Return a set containing      the union of sets                                      |
17| update()                      | Update the set with    another set, or any other iterable                           |


---


## 1. ADD( )

The `add()` method adds an element to the set.

If the element already exists, the add() method does not add the element.


` set_add_syntax = set.add(elmnt) `


| Parameter |               Description               |
|:---------:|:---------------------------------------:|
| elmnt     | Required. The element to add to the set |


```python
nums = {1, 2, 3, 4, 5, 6, 7}
nums.add(-7)
print(nums)
```
```
> {1, 2, 3, 4, 5, 6, 7, -7}
```


---


## 12. POP( )

The pop() method removes a random item from the set.

This method returns the removed item.


` set_pop_syntax = set.pop() `    # No parameter values.


```python
nums = {1, 2, 3, 4, 5, 6, 7}
nums.pop()
nums.pop()
print(nums)
```
```
> {3, 4, 5, 6, 7}
```


---


## 13. REMOVE( )

The remove() method removes the specified element from the set.

This method is different from the discard() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.


` set_syntax = set.remove(item) `


| Parameter |                  Description                 |
|:---------:|:--------------------------------------------:|
| item      | Required. The item to search for, and remove |


```python
nums = {1, 2, 3, 4, 5, 6, 7}
nums.remove(1)
print(nums)
```
```
> {2, 3, 4, 5, 6, 7}
```


---
