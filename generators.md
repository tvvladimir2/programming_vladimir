# GENERATORS


---


## LINKS

[Generators at Realpython ](https://realpython.com/introduction-to-python-generators/)


---


## DESCRIPTION

Generators are a type of iterable, like lists or tuples. These are objects that you can loop over like a list.
However, unlike lists, lazy iterators do not store their contents in memory.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

Using generators results in `improved performance`, which is the result of the lazy (on demand) generation of values, which translates to `lower memory usage`.
Furthermore, we do not need to wait until all the elements have been generated before we start to use them.

- Don't allow indexing
- Can be iterate through
- Created using functions and the yield statement.
- Can be finite & infinite
- Finite generator can be converted to a list.
- Improve performance
- Can start using them immediately
- Using yield will result in a generator object.


--


## CREATE

The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.

**Example**: Create using a function & the yield statement.
```python
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

print(countdown())

for i in countdown():
    print(i)

test_list = list(countdown())
print(test_list)
```
```
> <generator object countdown at 0x7f483c3933c0>

> 5
> 4
> 3
> 2
> 1

> [5, 4, 3, 2, 1]
```


---


## INFINITE GENERATOR

Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
In fact, they can be infinite!

```python
def infinite_sevens():
  while True:
    yield 7

for i in infinite_sevens():
  print(i)
```
```
> 7
> 7
> 7
> 7
> ...
```


---


## CONVERT a GENERATOR to a LIST

Finite generators can be converted into lists by passing them as arguments to the list function.

```python
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
```
```
> [0, 2, 4, 6, 8, 10]
```

---


## GENRATORS vs LIST COMPREHENSION

Trying to create a list in a very extensive `range` will result in a MemoryError when using `list comprehension`.
This code shows an example where the list comprehension runs out of memory.

```python
even = [2*i for i in range(10**100)]    # List comprehension
```
```
> MemoryError
```


---


## Why Generators?
Before we learn about generators, let's see an example of an iterator implemented in Python.

```python
class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration
numbers = Even(10)
print(next(numbers))
print(next(numbers))
print(next(numbers))
```
```
> 2
> 4
> 6
```

This code generates a sequence of even numbers. For this we have created a custom iterator.

For an object to be iterator it should implement:
- The  `__iter__()` method - To return an iterator object
- The  `__next__()` method - To return the next element in the stream & possibly raise `StopIteration` exception when
there are no values to be returned.

As you can see, the process of creating iterators is both lengthy and counterintuitive. Generators come to the rescue in such situations.


---


## Python Generators

Now, let's implement the same iterator from previous section using a generator.
A generator is simply a function but with slight modification. In generator function, we use the `yield` keyword to get the next item of the iterator.

```python
def even_generator():
    n = 0

    n += 2
    yield n
    n += 2
    yield n

    n += 2
    yield n
numbers = even_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))
```
```
> 2
> 4
> 6
```

First, we have created a generator function that has three yield statements. When we call this generator, it returns an iterator object.

Then, we have called the `__next__()` method to retrieve elements from this iterator. The first `yield` returns the value of `n = 2`.

The difference between `return` and `yield` is that the `return` statement terminates the function completely while the `yield` statement pauses the function saving all its states for next successive calls.

So, when we call `yield` for the second and third time, we get `4` and `6` respectively.

Let's make this generator return even numbers till a certain `max` number:


```python
def even_generator(max):
    n = 2

    while n <= max:
        yield n
        n += 2
numbers = even_generator(4)
print(next(numbers))
print(next(numbers))
print(next(numbers))
```
```
> 2
> 4
> Traceback (most recent call last):
> File "<string>", line 12, in <module>
> StopIteration
```


In this case, our generator could generate even numbers only till `4`. So, using `next()` function for the third time raised a `StopIteration` exception.

Notice how we have never explicitly defined the `__iter__()` method, `__next__()` method, or raised a `StopIteration` exception. They are handled implicitly by generators making our program much simpler and easier to understand.


---


## Infinite Stream of Data with Generators

Iterators and generators are generally used to handle a large stream of data--theoretically even an infinite stream of data. These large streams of data cannot be stored in memory at once. To handle this, we can use generators to handle only one item at a time.

Now, let's build a generator to produce an infinite stream of fibonacci numbers. The fibonacci series is a series where the next element is the sum of the last two elements.

```
> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,.....
```

```python
def generate_fibonacci():
    n1 = 0
    yield n1

    n2 = 1
    yield n2

    while True:
        n1, n2 = n2, n1 + n2
        yield n2

seq = generate_fibonacci()
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
```
```
> 0
> 1
> 1
> 2
> 3
```

If we had used a for loop and a list to store this infinite series, we would have run out of memory.

However, with generators, we can keep accessing these items for as long as we want. It is because we are just dealing with one item at a time.


---


## READING A FILE

Useful for reading large files, espcially if the file is larger than the available memory.

**Example 1**: Open a file, loop through each line, yields each row, instead of returning it.
```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

csv_reader(text.txt)
```


**Example**: Generator expression (generator comprehension)

```python
csv_gen = (row for row in open(file_name))
```

---
