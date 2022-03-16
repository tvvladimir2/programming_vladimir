# RECURSIONS


---


## DESCRIPTION

Python also accepts function recursion, which means a defined function can call itself.
Self-reference = functions calling themselves.

Features:
- Can be infinite.
- Can be indirect.

Benefits:
- You can loop through data to reach a result.
- Used to solve problems that can be broken up into easier sub-problems of the same type.

Cons:
- A function which never terminates can use an excess amounts of memory or processor power.


---


## SYNTAX STRUCTURE

```python
def recurse():
  ...
  recurse()             # Recursive call
  ...

recurse()               # Call the function
```


---


## SIMPLE EXAMPLE

```python
i = 0

def greet():
  print('Hello' + i)
  i += 1
  greet()

greet()
```
```
> 0
> 1
> 2
> ...
> 996
> RecursionError: maximum recursion depth exceeded while calling a Python object
```


---


## MAX NUMBER OF RECURSIONS

```python
import sys

sys.setrecursionlimit(2000)       # Increase number of recursions

print(sys.setrecursionlimit())    # By default returns > 1000
```
```
> 2000
```


---


## INDIRECT RECURSIONS

Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.

```python
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))
```
```
> True
> False
```


---


## OTHER EXAMPLES

**Example**: Calculate the sum of all numbers in a list

```python
def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0] + calc(list[1:])   # return list[0] + list[0] + list[0] + list[0] + list[0]
                                          # list[0] is iterating through a list
list = [1, 3, 4, 2, 5]
x = calc(list)        
print(x)
```

**Example**:

```python
def fib(x):
  if x==0 or x==1:
    return 1
  else:
    return fib(x-1)+fib(x-2)    # return fib(3) + fib(2)
                                # return fib(2) + fib(1) + fib(1) + fib(0)
                                # return fib(1) + fib(0) + fib(1) + fib(1) + fib(0)
                                # return 1+1+1+1+1
print(fib(4))
```
```
> 5
```


---
