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


##
