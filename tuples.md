# PYTHON TUPLES


---


## DESCRIPTION

A tuple in Python is similar to a list. It is also an ordered collection of items.

The only difference between the two is that lists are mutable (elements of a list can be changed), whereas tuples are immutable (elements of a tuple cannot be changed).


---


## CRETA A TUPLE

To create a tuple, we need to wrap items inside parentheses `()` and separate items by a comma.
**Example 1**:
```python
tuple1 = 21, -5, 6, 9      # can be created without the parentheses
tuple2 = (21, -5, 6, 9)
empty_tuple = ()
print(numbers)
```
```
> (21, -5, 6, 9)
> (21, -5, 6, 9)
> ()                # same as `None`
```

**Example 2**:
Like lists and dictionaries, tuples can be nested within each other.
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


---


## ACCESS ELEMENTS IN A TUPLE

We can access elements from a tuple in a similar way to lists.

```python
numbers = (1, 5, 6, 3)
print(numbers[2])
```
```
> 6
```


---


## SLICING TUPLES

We can also perform slicing similar to lists.

```python
numbers = (1, 5, 6, 3)
print(numbers[1:4])
```
```
> (5, 6, 3)
```


---


# LOOP THROUGHA TUPLE
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
