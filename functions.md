# FUNCTIONS


---


You can create your own functions by using the `def` statement.

## SYNTAX STRUCTURE

```python
# The function needs to be defined before it can be called. Calling a function before its definition will cause an error.
def name(argument1, argument2):   # function name = indentifier (parentheses = function call) # creates your own function
    """This function prints
       message on the screen"""   # Docstring for a documentation
    statement                     # /(function body), executed each time the function is called
    statement                     # must be indented
    ...
    return(value1, value2, ...)   # Nothing is executed after a return statement. Returns None if not specified.

# Once you’ve defined a function, you can call it multiple times in your code.
my_func(argument1)                # call it first time
# you can pass as many arhuments as you like
my_func('Bob', var, 10)           # call it second time and pass three agruments
```


---


## NESTED FUNCTIONS

A function defined within other function.
They are useful when performing complex task multiple times within another function, to avoid loops or code duplication.
A nested function can act as a closure.

```python
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)
result = outer(2, 4)
print(result)
```
```
> 6
```

---


# FUNCTION ARGUMENT CANNOT BE REFERENCED OUTSIDE THE FUNCTION

```python
def function(variable):
    variable += 1
    print(variable)

function(7)             # Prints 8

print(variable)
```
```
> 8
> NameError: name 'variable' is not defined
```


---


## DECLARE A GLOBAL VARIABLE INSIDE A FUNCTION

```python
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)
```


---


# RECURSION

A function calls itself and repeats its behavior until some condition is met to return a result.

```python
def countdown(num):
    if num <= 0:
        print('Stop')
    else:
        print(num)
        countdown(num-1)
countdown(5)    # Prints 5, 4, 3, 2, 1, Stop
```
```
> 5
> 4
> 3
> 2
> 1
> Stop
```


---


# DOCSTRING

**Example 1**: using `__dic__` docstring

```python
def func():
    '''documentation
    is here'''
print(func.__doc__)    # prints the docstring of a function
```
```
> documentation
>     is here
```


**Example 2**: using `help()` function

```python
def func():
    '''documentation
    is here'''
help(func)             # uses help() function to print the function docstring
```
```
> Help on function func in module __main__:
>
> func()
>     documentation
>     is here
```


---


## UNPACK RETURNED TUPLE

```python
def func(a,b):
  return (a+b, a*b)
add, multiply = func(3, 2)   # add = a+b; multiply=a*b
result = func(3, 2)
print(add)
print(multiply)
print(result)
```
```
> 5
> 6
> (5, 6)
```


---


# CALL SAME FUNCTION WITH DIFFERENT ARGUMENTS

```python
def exclamation(word):
   print(word + "!")

print(exclamation("spam"))
print('')
print(exclamation("eggs"))
```
```
spam!
None

eggs!
None
```


---


# ASSIGNING FUNCTIONS TO VARIABLES

```python
def hello():
    print('Hello, World!')

hi = hello  # Assign a different name to function and call through the new name.
hi()        # Prints Hello, World!
```
```
Hello, World!
```


---


## JUMP CALL TABLE

```python
def findSquare(x):
    return x ** 2
def findCube(x):
    return x ** 3
exponent = {'square': findSquare, 'cube': findCube} # Create a dictionary of functions
print(exponent['square'](3))    # passes 3 as an argument # Prints 9
print(exponent['cube'](3))  # Prints 27
```
```
> 9
> 27
```


---


## PYTHON FUNCTION EXECUTES AT RUNTIME

Because Python treats `def` as an executable statement, it can appear anywhere a normal statement can.

```python
x = 0
if x:
    def hello():                    # nest a function inside an if statement to select between alternative definitions.
        print('Hello, World!')
else:
    def hello():
        print('Hello, Universe!')
hello()                             # Prints Hello, Universe!
```
```
> Hello, Universe!
```


---


## RETURN VALUE or VARIABLE or EXPRESSION

Functions may return value or a variable or an expression

```python
def square(x):
    return (x**2, 4, x+2)
```


---


# `DEF` INSIDE AN `IF` STATEMENT

We can use a function inside an if statement and other

```python
def square(x):
    return x**2 #returns x squared
if (square(2) < 10):
    print (x)
```


---


# AFTER `RETURN` STATEMENT

**Example 1**: Any code placed after the return statement won’t be executed.
```python
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(1,2))`
```
```
> 3
```

**Example 2**: Use list to return multiple values
```python
def double(a, b):
     return [a*2, b*2]
print(double(1,2))
```
```
> [2, 4]
```


---


## FUNCTION AS AN ARGUMENT

```python
def add(x, y):
    return x + y
def do_twice(func, x, y):   # func = add
    return func(func(x, y), func(x, y)) # executes add from here x3 times
# > return func (15, 15)
# > return 30
a = 5
b = 10
print(do_twice(add, a, b))
```
```
> 30
```


---
