# PYTHON TUPLES


---


## DESCRIPTION

Tuples are used to store multiple items in a single variable.

**Ordered**: Maintain the order of the data insertion.
**Unchangeable**: Tuples are immutable, can not modify items.
**Heterogeneous**: Can contain a data of types.
**Contains duplicate**: Allows duplicate data.

The only difference between lists and tuples is that lists are mutable (elements of a list can be changed), whereas tuples are immutable (elements of a tuple cannot be changed).


---


## STURCTURE - SYNTAX

` tuple_syntax = (item1, item2, float, string, tuple(), list(), bool, complex_number, ) `


---


## CREATE A TUPLE

To create a tuple, we need to wrap items inside parentheses `()` and separate items by a comma.

**Example 1**:

```python
# 1
tuple1 = 21, -5, 6, 9      # can be created without the parentheses
tuple2 = (1, 2, 'Name', tuple(), (42, 'hi'), (3+3j), [3,4])
empty_tuple = ()
tuple_item_types = ("True", "5", "3.00001")        # Can have any data types
single_item_tuple = ("apple",)  # To create a tuple with one item use ','
```
```
> (21, -5, 6, 9)
> (21, -5, 6, 9)
> ()                            # same as `None`
> ('True', '5', '3.00001')
> ('apple',)
```


**Example 2**: Like lists and dictionaries, tuples can be nested within each other.

```python
print(21, -5, 6, 9)
print(21, (21, -5, 6, 9), 6, 9)
print(21, (21, -5, 6, (21, -5, 6, 9)), 6, 9)
```
```
> 21 -5 6 9
> 21 (21, -5, 6, 9) 6 9
> 21 (21, -5, 6, (21, -5, 6, 9)) 6 9
```


**Example3**: use `tuple()` constructor method to create a tuple

```python
this_tuple = tuple(("apple", "banana", "cherry")) # Tuple to Tuple
my_tuple = tuple(["apple", "banana", "cherry"]) # List to Tuple
print(this_tuple)
print(my_tuple)
```
```
> ('apple', 'banana', 'cherry')
> ('apple', 'banana', 'cherry')
```


---


## SLICE (SLICING)

We can access elements from a tuple using indexes in a similar way to lists.

` tuple = (item[0], item[1], item[2], (item[3][0], item[3][1]), item[4]) `
` tuple = (item[-5], item[-4], item[-3], (item[-2][-2], item[-2][-1]), item[-1]) `

```python
numbers = (1, 5, 6, 3)
print(numbers[2])
print(numbers[1:4])
```
```
> 6
> > (5, 6, 3)
```


---


# LOOP THROUGH A TUPLE
We can loop through a tuple using a `for` loop:

```python
numbers = (1, 5, 6, 3)
for number in numbers:
   print(number)
```
```
> 1
> 5
> 6
> 3
```


---


## Python Tuple vs List

The difference between tuple and list is that a list can be changed but tuple cannot be changed.

**Example**: Let's try changing an item of a tuple:

```python
languages_tuple = ("Python", "JavaScript", "C++", "Kotlin")
languages_tuple[0] = "Java"
print(languages_tuple)
```
```
> Traceback (most recent call last):
>  File "<string>", line 2, in <module>
>TypeError: 'tuple' object does not support item assignment
```


---


## Programming Task

**Can you guess the output of this program?**

```python
mixed_list = ["Hello", -34, "Java", True]
print("1.", mixed_list[-1])
mixed_list[1] = "Hi"
print("2.", mixed_list)
mixed_tuple = (1, 3, 4, 5)
mixed_tuple[1] = 100
print("3.", mixed_tuple)
```
```
> 1. True
> 2. ['Hello', 'Hi', 'Java', True]
> Traceback (most recent call last):
> File "<string>", line 10, in <module>
> TypeError: 'tuple' object does not support item assignment
```


---
