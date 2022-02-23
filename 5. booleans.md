# BOOLEANS


---


## Create a Boolean
```python
my_boolean = True           # Set a variable to a False boolean
my_boolean = False          # Set a variable to a False boolean
print(2 == 3)               # Created by comparing variables # returns False
print(2 != 10)              # returns True
print("hello" == "hello")   # Created by comparing strings # returns True
print("eleven" != "seven")  # returns True
print(7 <= 8)               # returns True
```


---


### Convert to Boolean
The None object is used to represent the absence of a value.
`None` object returns `False` when converted to a Boolean.

**1. None object to Booolean**
```python
None == None
print(None)   # returns empty string: None
```

**2. Integer, float, list, string to Boolean**
```python
x = 0         # False
x = []        # False
x = ''        # False
y = bool(x)   # returns `False`
```

**3. Function with `None return`**
The None object is returned by any function that doesn't explicitly return anything else.
```python
def some_func():
  print("Hi!")

var = some_func()
print(var)
```
```
>> Hi!
>> None
```


---


### BOOLEANS IN `IF` STATEMENTS
Booleans represent one of two values: True or False.
```python
a = 200
b = 33
if b > a:   # If this is True
  print("b is greater than a")
else:
  print("b is not greater than a")
```


---


### BOOLEAN NOT
The result of not True is False, and not False goes to True
```python
my_boolean = not True      # not only takes one argument, and inverts it.
```


---


### EVALUATE VALUE AND VARIABLE
- Almost any value is evaluated to True if it has some sort of content.
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

```python
x = "Hello"
print(bool(x))      # returns True
```
```
def myFunction() :
  return True       # returns True
```


---


## Insistance ( )
Check if an object is an integer or not:

```python
x = 200
print(isinstance(x, int))   # Returns True
```
```
# return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```


---


## Return here after I study classes !!!
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a `__len__` function that returns 0 or False:
```python
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
```


---


## PRECEDENCE OF BOOLEANS

Example:
```python
if a > b or b < c and b >a:   # What comes first? `or` or `and`?
```
See precedence table in the file operators.py or operators.md
