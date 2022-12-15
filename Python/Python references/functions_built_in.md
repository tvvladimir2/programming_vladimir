# BUILT-IN FUNCTIONS

| №  |    Function    |                                          Description                                          |
|----|:--------------:|:---------------------------------------------------------------------------------------------:|
| 1  | abs()          | Returns the absolute value of a number                                                        |
| 2  | all()          | Returns True if all items in an iterable object are true                                      |
| 3  | any()          | Returns True if any item in an iterable object is true                                        |
| 4  | ascii()        | Returns a readable version of an object. Replaces none-ASCII characters with escape character |
| 5  | bin()          | Returns the binary version of a number                                                        |
| 6  | bool()         | Returns the boolean value of the specified object                                             |
| 7  | bytearray()    | Returns an array of bytes                                                                     |
| 8  | bytes()        | Returns a bytes object                                                                        |
| 9  | callable()     | Returns True if the specified object is callable, otherwise False                             |
| 10 | chr()          | Returns a character from the specified    Unicode code.                                       |
| 11 | classmethod()  | Converts a method into a class method                                                         |
| 12 | compile()      | Returns the specified source as an object, ready to be executed                               |
| 13 | complex()      | Returns a complex number                                                                      |
| 14 | delattr()      | Deletes the specified attribute (property or method) from the specified object                |
| 15 | dict()         | Returns a dictionary (Array)                                                                  |
| 16 | dir()          | Returns a list of the specified object's properties and methods                               |
| 17 | divmod()       | Returns the quotient and the remainder when argument1 is divided by argument2                 |
| 18 | enumerate()    | Takes a collection (e.g. a tuple) and returns it as an enumerate object                       |
| 19 | eval()         | Evaluates and executes an expression                                                          |
| 20 | exec()         | Executes the specified code (or object)                                                       |
| 21 | filter()       | Use a filter function to exclude items in an iterable object                                  |
| 22 | float()        | Returns a floating point number                                                               |
| 23 | format()       | Formats a specified value                                                                     |
| 24 | frozenset()    | Returns a frozenset object                                                                    |
| 25 | getattr()      | Returns the value of the specified attribute (property or method)                             |
| 26 | globals()      | Returns the current global symbol table as a dictionary                                       |
| 27 | hasattr()      | Returns True if the specified object has the specified attribute (property/method)            |
| 28 | hash()         | Returns the hash value of a specified object                                                  |
| 29 | help()         | Executes the built-in help system                                                             |
| 30 | hex()          | Converts a number into a hexadecimal value                                                    |
| 31 | id()           | Returns the id of an object                                                                   |
| 32 | input()        | Allowing user input                                                                           |
| 33 | int()          | Returns an integer number                                                                     |
| 34 | isinstance()   | Returns True if a specified object is an instance of a specified object                       |
| 35 | issubclass()   | Returns True if a specified class is a subclass of a specified object                         |
| 36 | iter()         | Returns an iterator object                                                                    |
| 37 | len()          | Returns the length of an object                                                               |
| 38 | list()         | Returns a list                                                                                |
| 39 | locals()       | Returns an updated dictionary of the current local symbol table                               |
| 40 | map()          | Returns the specified iterator with the specified function applied to each item               |
| 41 | max()          | Returns the largest item in an iterable                                                       |
| 42 | memoryview()   | Returns a memory view object                                                                  |
| 43 | min()          | Returns the smallest item in an iterable                                                      |
| 44 | next()         | Returns the next item in an iterable                                                          |
| 45 | object()       | Returns a new object                                                                          |
| 46 | oct()          | Converts a number into an octal                                                               |
| 47 | open()         | Opens a file and returns a file object                                                        |
| 48 | ord()          | Convert an integer    representing the Unicode of the specified character                     |
| 49 | pow()          | Returns the value of x to the power of y                                                      |
| 50 | print()        | Prints to the standard output device                                                          |
| 51 | property()     | Gets, sets, deletes a property                                                                |
| 52 | range()        | Returns a sequence of numbers, starting from 0 and increments by 1 (by default)               |
| 53 | repr()         | Returns a readable version of an object                                                       |
| 54 | reversed()     | Returns a reversed iterator                                                                   |
| 55 | round()        | Rounds a numbers                                                                              |
| 56 | set()          | Returns a new set object                                                                      |
| 57 | setattr()      | Sets an attribute (property/method) of an object                                              |
| 58 | slice()        | Returns a slice object                                                                        |
| 59 | sorted()       | Returns a sorted list                                                                         |
| 60 | staticmethod() | Converts a method into a static method                                                        |
| 61 | str()          | Returns a string object                                                                       |
| 62 | sum()          | Sums the items of an iterator                                                                 |
| 63 | super()        | Returns an object that represents the parent class                                            |
| 64 | tuple()        | Returns a tuple                                                                               |
| 65 | type()         | Returns the type of an object                                                                 |
| 66 | vars()         | Returns the __dict__ property of an object                                                    |
| 67 | zip()          | Returns an iterator, from two or more iterators                                               |


---


## 1. ABS( )

The abs() function returns the absolute value of the specified number.
Absolute value of 3 is 3.
Absolute value of −3 is also 3.
Absolute number of 0 is 0.
The absolute value of a number may be thought of as its distance from zero.

`function_syntax = abs(n)`

| Parameter |     Description    |
|:---------:|:------------------:|
| n         | Required. A number |

```python
print(abs(3))
print(abs(-3))
print(abs(0))
```
```
> 3
> -3
> 0
```


---


## 2. ALL( )

The `all()` function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the `all()` function also returns True.

`all_function = all(iterable)`

| Parameter |                  Description                 |
|:---------:|----------------------------------------------|
| iterable  | An iterable object (list, tuple, dictionary) |

**Example**:
```python
mydict = {1 : "Apple", 1 : "Orange"}
print(all(mydict))

mytuple = (0, True, False)
x = all(mytuple)
```
```
> True
> False
```


---


## 3. ANY( )

The `any()` function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the `any()` function will return False.

`any_function = any(iterable)`

| Parameter |                  Description                 |
|:---------:|----------------------------------------------|
| iterable  | An iterable object (list, tuple, dictionary) |

**Example**: Check if any item in a tuple is True:
```python
mydict = {0 : "Apple", 1 : "Orange"}
print(any(mydict))

mytuple = (0, 1, False)
print(any(mytuple))
```
```
> True
> True
```


---


## 18. ENUMERATE( )

The `enumerate()` function takes a collection (e.g. a tuple) and returns it as an enumerate object.
The `enumerate()` function adds a counter as the key of the enumerate object.

`enumerate_function = enumerate(iterable, start)`

| Parameter |                               Description                              |
|:---------:|------------------------------------------------------------------------|
| iterable  | An iterable object                                                     |
| start     | A Number. Defining the start number of the enumerate object. Default 0 |

**Example**: Convert a tuple into an enumerate object:
```python
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))
```
```
> [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```


---


## 21. FILTER( )


The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
- higher-order functions that operates on lists (or similar objects called iterables)
- similiar to anonymous functions (lambdas)
- a function that returns a Boolean
- the result has to be explicitly converted to a list if you want to print it.


` function_filter_syntax = filter(function, iterable) `


| Parameter |                     Description                    |
|:---------:|:--------------------------------------------------:|
| function  | A Function to be run for each item in the iterable |
| iterable  | The iterable to be filtered                        |


**Example 1**: Filter the array, and return a new array with only the values equal to or above 18:

```python
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

print(adults)
print(type(adults))
# print(list(adults))   # returns [18, 24, 32]

for x in adults:
  print(x)

```
```
<filter object at 0x000001DEBF8C8FA0>
<class 'filter'>
> 18
> 24
> 32
```


**Example 2**: Fill in the blanks to extract all items that are less than 5 from the list.

```python
nums = [1, 2, 5, 8, 3, 0, 7]

y = list( filter(lambda x: x < 5, nums))

print(y)
```
```
> [1, 2, 3, 0]
```


---


## 37. LEN( )

The len() function returns the number of items in an object.
When the object is a string, the `len()` function returns the number of characters in the string.

`len_syntax = len(object) = len(sequence or a collection)`

```python
print(len("Hello"))
```
```
> 5
```


---


## 40. MAP( )

The `map()` function executes a specified function for each item in an iterable. The item is sent to the function as a `parameter`.
The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.
- higher-order functions that operates on lists (or similar objects called iterables)
- similiar to anonymous functions (lambdas)
- the result has to be explicitly converted to a list if you want to print it.


` function_map_syntax = map(function, iterables) `


| Parameter |                                                                                   Description                                                                                  |
|:---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| function  | Required. The function to execute for each item                                                                                                                                |
| iterable  | Required. A sequence, collection or an iterator object. You can send as      many iterables as you like, just make sure the function has one parameter      for each iterable. |


**Example 1**: Calculate the length of each word in the tuple:

```python
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
print(type(x))

#convert the map into a list, for readability:
print(list(x))
```
```
> <map object at 0x0000025317575460>
> <class 'map'>
> [5, 6, 6]
```


**Example 2**: Using `map()` with `Lambda`. Multiply each item in a list by 2.

```python
nums = [33,45,65,32,44]

a = list(map(lambda x: x*2, nums))
print(a)
```
```
> [66, 90, 130, 64, 88]
```


---


## 41. MAX( )

The `max()` function returns the item with the highest value, or the item with the highest value in an iterable.
If the values are strings, an alphabetically comparison is done.

`function_max = max(n1, n2, n3, ...) = max(iterable)`

|    Parameter                |          Description                                                               |
|:---------------------------:|------------------------------------------------------------------------------------|
| n1, n2, n3, ... or iterable | `One or more items to compare` or `An iterable, with one or more items to compare` |

**Example 1**: Return the name with the highest value, ordered alphabetically:
```python
print(max("Abb", "Bcc", "Cdd"))
```
```
> Cdd
```

**Example 2**: Return the item in a tuple with the highest value:
```python
print(max(1, 5, 3, 9))
```
```
> 9
```


---


## 43. MIN( )

The `min()` function returns the item with the lowest value, or the item with the lowest value in an iterable.
If the values are strings, an alphabetically comparison is done.

`min_function = min(n1, n2, n3, ...) = min(iterable) `

| Parameter                   | Description                                                                        |
|:---------------------------:|------------------------------------------------------------------------------------|
| n1, n2, n3, ... or Iterable | `One or more items to compare` or 'An iterable, with one or more items to compare' |

**Example 1**: Return the name with the lowest value, ordered alphabetically:
```python
print(min("Abb", "Bcc", "Cdd"))
```
```
> Abb
```


**Example 2**: Return the item in a tuple with the lowest value:
```python
a = (1, 5, 3, 9)
prin(min(a))
```
```
> 1
```


---


## 52. RANGE( )

The `range()` function returns a sequence of numbers.
By default, it starts from 0, increments by 1 and stops before the specified number.

`range_syntax = range(start, stop, step)`

| Parameter | Description                                                                      |
|:---------:|:--------------------------------------------------------------------------------:|
| start     | Optional. An integer number specifying at which position to start. Default is 0  |
| stop      | Required. An integer number specifying at which position to stop (not included). |
| step      | Optional. An integer number specifying the incrementation. Default is 1          |

```python
mylist = list(range(10))        # generates a list containing all of the integers, 0 to 9.
print(mylist)
mylist = list(range(3, 8))      # generates a list from 3 to 7
print(mylist)
mylist = list(range(5, 11, 2))  # third argument determines the interval of the sequence produced, also called the step. # returns 5,7,9
print(mylist)
```
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7]
[5, 7, 9]
```


---


## 55. ROUND( )

The `round()` function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
The default number of decimals is 0, meaning that the function will return the nearest integer.

`round_function = round(number, digits)`

| Parameter |                                     Description                                |
|:---------:|--------------------------------------------------------------------------------|
| number    | Required. The number to be rounded                                             |
| digits    | Optional. The number of decimals to use when rounding the number. Default is 0 |

```python
print(round(5.76543))
print(round(5.76543, 1))
```
```
> 5.77
> 5.8
```


---


## 62. SUM( )

The `sum()` function returns a number, the sum of all items in an iterable.

`function_sum = sum(iterable, start)`

| Parameter |                     Description                     |
|:---------:|-----------------------------------------------------|
| iterable  | Required. The sequence to sum                       |
| start     | Optional. A value that is added to the return value |

```python
a = (1, 2, 3, 4, 5)     # sums is 15
x = sum(a, 7)           # sums is 15 + 7 = 22
print(x)
```
```
> 22
```
