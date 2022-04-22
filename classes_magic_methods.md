# CLASSES MAGIC METHODS / DUNDERS


---


## LINKS

[A guide to use Python magic methods](https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15)


---


## Initialization dunders

Methods to help and change the class initialization behavior.

| # | Operation | Method                | Description                                           |
|---|-----------|-----------------------|-------------------------------------------------------|
|   | a = x()   | x.__new__(cls[,...])  | Called to create a new instance of class cls          |
|   | a = x()   | x._init__(self[,...]) | Called after the instance has been created by __new__ |
|   | del x     | x.__del__(self)       | Called when instance is about to be destroyed         |

Remarks:
- The return of `__new__` should be an instance of the class. If nothing is returned, the new instance’s `__init__` is not called.
- No value should be returned by `__init__`. A TypeError is raised if anything than None is returned.
- The operation `del x` does not directly call `x.__del__`. It decrements the reference count of `x` and only when it is zero that it is really called.
- Any exception that occurs during `__del__` is ignored and a warning is printed to `sys.stderr` instead.


---


## Binary Operator dunders:

| # | Operator |                 Method                |
|---|:--------:|:-------------------------------------:|
|   | +        | object.__add__(self, other)           |
|   | -        | object.__sub__(self, other)           |
|   | *        | object.__mul__(self, other)           |
|   | //       | object.__floordiv__(self, other)      |
|   | /        | object.__truediv__(self, other)       |
|   | %        | object.__mod__(self, other)           |
|   | **       | object.__pow__(self, other[, modulo]) |
|   | <<       | object.__lshift__(self, other)        |
|   | >>       | object.__rshift__(self, other)        |
|   | &        | object.__and__(self, other)           |
|   | ^        | object.__xor__(self, other)           |
|   | \|       | object.__or__(self, other)            |


---


## Extended Assignments:

|   | Operator |                 Method                 |
|---|:--------:|:--------------------------------------:|
|   | +=       | object.__iadd__(self, other)           |
|   | -=       | object.__isub__(self, other)           |
|   | *=       | object.__imul__(self, other)           |
|   | /=       | object.__idiv__(self, other)           |
|   | //=      | object.__ifloordiv__(self, other)      |
|   | %=       | object.__imod__(self, other)           |
|   | **=      | object.__ipow__(self, other[, modulo]) |
|   | <<=      | object.__ilshift__(self, other)        |
|   | >>=      | object.__irshift__(self, other)        |
|   | &=       | object.__iand__(self, other)           |
|   | ^=       | object.__ixor__(self, other)           |
|   | \|=      | object.__ior__(self, other)            |


---


## Unary Operators:

|   |  Operator |          Method          |
|---|:---------:|:------------------------:|
|   | -         | object.__neg__(self)     |
|   | +         | object.__pos__(self)     |
|   | abs()     | object.__abs__(self)     |
|   | ~         | object.__invert__(self)  |
|   | complex() | object.__complex__(self) |
|   | int()     | object.__int__(self)     |
|   | long()    | object.__long__(self)    |
|   | float()   | object.__float__(self)   |
|   | oct()     | object.__oct__(self)     |
|   | hex()     | object.__hex__(self      |


---


## Comparison Operators:

|   | Operator |           Method           |
|---|:--------:|:--------------------------:|
|   | <        | object.__lt__(self, other) |
|   | <=       | object.__le__(self, other) |
|   | ==       | object.__eq__(self, other) |
|   | !=       | object.__ne__(self, other) |
|   | >=       | object.__ge__(self, other) |
|   | >        | object.__gt__(self, other) |


---


## User-defined methods:

|   |    Attribute    |                                                                      Meaning                                                                     |           |
|---|:---------------:|:------------------------------------------------------------------------------------------------------------------------------------------------:|:---------:|
|   | __doc__         | The function’s documentation string, or None if unavailable; not inherited by subclasses.                                                        | Writable  |
|   | __name__        | The function’s name.                                                                                                                             | Writable  |
|   | __qualname__    | The function’s qualified name.     New in version 3.3.                                                                                           | Writable  |
|   | __module__      | The name of the module the function was defined in, or None if unavailable.                                                                      | Writable  |
|   | __defaults__    | A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value.                 | Writable  |
|   | __code__        | The code object representing the compiled function body.                                                                                         | Writable  |
|   | __globals__     | A reference to the dictionary that holds the function’s global variables — the global namespace of the module in which the function was defined. | Read-only |
|   | __dict__        | The namespace supporting arbitrary function attributes.                                                                                          | Writable  |
|   | __closure__     | None or a tuple of cells that contain bindings for the function’s free variables. See below for information on the cell_contents attribute.      | Read-only |
|   | __annotations__ | A dict containing annotations of parameters.  The keys of the dict are the parameter names, and 'return' for the return annotation, if provided. | Writable  |
|   | __kwdefaults__  | A dict containing defaults for keyword-only parameters.                                                                                          | Writable  |

---


## EXAMPLE

Magic methods are `special methods` which have `double underscores` at the beginning and end of their names.
They are also known as `dunders`.
They are used to create functionality that can't be represented as a normal method.

**Example**: Common use of them is `operator overloading`.
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +.
```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
```
```
> 8
> 16
```

The __add__ method allows for the definition of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.
