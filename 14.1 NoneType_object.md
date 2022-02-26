# NoneType Object


---


## USEFUL LINKS

[Null in Python](https://realpython.com/null-in-python/)


---


## DESCRIPTION
`None` is a keyword. Defines `null` objects and variables.
`None` is not defined to be 0 or any other value. In Python, `None` is an object and a first-class citizen!


---


## PRINT ( ) function
`None` by itself has no output, but printing it displays None to the console.
```python
print(None)                     # returns `None`
print()                         # returns `None`
```


---


## FUNCTION RETURN
When you call `f()`, there’s no output for you to see. When you print a call to it, however, you’ll see the hidden `None` it returns.

```python
def f():
  pass

print(has_no_return())          # returns `None`
```


---


## MISSING OR DEFAULT PARAMETERS
`None` also often used as a signal for missing or default parameters. For instance, `None` appears twice in the docs for `list.sort`.
Here `None` is a `default parameter` and a `type hint`.

```python
help(list.sort)
```
```
>> Help on method_descriptor:
>>
>> sort(...)
>>    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
```


---


# IF COMPARISON
Use `None` as part of a comparison.

**Example 1:**
```python
import re
# Check if 'Goodbye' is in 'Hello, Worlds!'
match = re.match(r"Goodbye", "Hello, World!")   #  re.match(pattern, string, flags=0)
if match is None:
  print("It doesn't match.")
```
```
>> It doesn't match.
```


**Example 2:**
Use the identity operators `is` and `is not`.
Do not use the equality operators `==` and `!=`.
```python
class BrokenComparison:
  def __eq__(self, other):
    return True

b = BrokenComparison()

print(b)          # returns `<__main__.BrokenComparison object at 0x0000029846E13C10>`
print(b == None)  # Equality operator returns a wrong answer `True`
print(b is None)  # Identity operator can't be fooled, can not override it, and it returns `False`
```


**Example 3:**
`None` `is` `falsy`, which means `not None` `is` `True`.

```python
some_result = None          # prints `False`
print(bool(some_result))
if some_result:             # same as `some_result` is True
  print("Got a result!")
else:
  print("No result.")       # prints `No result.`
```


---


## FALSY OBJECTS

```python
mylist[]              # empty lists
mydictionary = {}     # empty dictionary
x = set()             # empty set
x = ''                # empty string
x = 0                 # empty variable
x = False             # `False bool variable`
```


---


## DECLARING VS ASSIGNING NULL VARIABLES
Can not `declare` a variable without `assigning statement` like in some languages:

```python
print(bar)          # 'bar' is not defined
```
```
>> Traceback (most recent call last):
>>  File "<stdin>", line 1, in <module>
>> NameError: name 'bar' is not defined
```

> A variable with the value `None` is different from an `undefined` variable.

In Python variables come to life from `assignment statements`.
A variable will only start life as null in Python if you assign None to it.
```python
bar = None
print(bar)            # returns `None`
```


---


## Using None as a Default Parameter (stopped here)
