# CLASSES MAGIC METHODS / DUNDERS


---


## LINKS

[A guide to use Python magic methods](https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15)
[Data model python official documentation](https://docs.python.org/3/reference/datamodel.html)


---


## Initialization dunders

Methods to help and change the class initialization behavior.

| #   | Method                 | Operation | Description                                           |
|-----|------------------------|-----------|-------------------------------------------------------|
| 1.1 | x.__new__(cls[,...])   | a = x()   | Called to create a new instance of class cls          |
| 1.2 | x.__init__(self[,...]) | a = x()   | Called after the instance has been created by __new__ |
| 1.3 | x.__del__(self)        | del x     | Called when instance is about to be destroyed         |

Remarks:
- The return of `__new__` should be an instance of the class. If nothing is returned, the new instance’s `__init__` is not called.
- No value should be returned by `__init__`. A TypeError is raised if anything than None is returned.
- The operation `del x` does not directly call `x.__del__`. It decrements the reference count of `x` and only when it is zero that it is really called.
- Any exception that occurs during `__del__` is ignored and a warning is printed to `sys.stderr` instead.


---


# Representation

Useful to get a string that represents the class instance.

| #   | Method                  | Operation       | Description                                         |
|-----|-------------------------|-----------------|-----------------------------------------------------|
| 2.1 | x.__format__(self,spec) | format(x, spec) | Called to compute the formatted string of `x`       |
| 2.2 | x.__bytes__(self)       | bytes(x)        | Called to compute byte-string representation of `x` |
| 2.3 | x.__str__(self)         | str(x)          | Called to show informal representation of `x`       |
| 2.4 | x.__repr__(self)        | repr(x)         | Called to show an official representation of `x`    |

Remarks:
- If a class declares `__repr__` but not `__str__`, then `__repr__` is also used as “informal” representation, that is, is called by `str()`.
- The `spec` argument is a string that contains a description of format options desired and is up to the class to interpret it. Most of the time, the class will either delegate to one of the built-in types or follow a similar syntax.
- The major difference between `__repr__` and `__str__` is the intended audience. The `__repr__` function is intended to produce an output that is machine-readable (it can be even a Python expression), while `__str__` is more a human-readable output (it must be a string).


---


## Attribute access

Can customize the meaning of access to an attribute (use, assignment or deletion).

| #   | Method                           | Operation  | Description                                                                     |
|-----|----------------------------------|------------|---------------------------------------------------------------------------------|
| 3.1 | x.__getattr__(self, name)        | v = x.name | Called when the default attribute access falls with an `AttributeError`           |
| 3.2 | x.__getattribute__(self, name)   | v = x.name | Called unconditionally to implement attribute access for instances of the class |
| 3.3 | x.__setattr__(self, name, value) | x.name = v | Called when attribute assignment is attempted                                   |
| 3.4 | x.__delattr__(self, name)        | del x.name | Like `__setattr__()` but for attribute deletion instead of assignment           |
| 3.5 | x.__dir__(self)                  | dir(x)     | A sequence must be returned                                                     |

Remarks:
- If the method is found through normal mechanism, `__getattr__` is never called.
- If the class defines both `__getattr__` and `__getattribute__`, `__getattr__` is only called if `__getattribute__` raises an `AttributeError` or explicitly calls it.
- If `__setattr__` wants to assign to an instance attribute, it should call the base class method with the same name, for example, `object.__setattr__(self, name, value)` or `self.__dict__[name]=value`.


---


## Descriptors

Descriptors are classes which, when accessed through either getting, setting, or deleting, can also alter other objects. Here the descriptor is a class that declares one or many of theses methods and appears in one attribute of the owner class.

| # | Method                               | Operation          | Observation                                                                                                                           |
|---|--------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|
|4.1| x.__set_name_(self, owner, name)     |                    | Called at the time the owning class owner is created. The descriptor has been assigned to name.                                       |
|4.2| x.__delete__(self, instance)         | del instance.x     | Called to delete the attribute on an instance instance of the owner class.                                                            |
|4.3| x.__get__(self instance, owner=None) | v = instance.x     | Called  to get the attribute of the owner class (class attribute access) or of  an instance of that class (instance attribute access) |
|4.4| x.__set__(self, instance, value)     | instance.x = value | Called to set the attribute on an instance instance of the owner class to a new value, value.                                         |

Remarks
- Descriptors aren’t meant to stand alone; rather, they’re meant to be held by an owner class. Descriptors can be useful when building object-oriented databases or classes that have attributes whose values are dependent on each other
- To be a descriptor, a class must have at least one of `__get__`, `__set__`, and `__delete__` implemented
- The same behavior can be achieved by using `property` decorator.


---


## Container methods

The following methods can be defined to implement container objects. Containers usually are `sequences` (such as lists or tuples) or `mappings` (like dictionaries), but can represent other containers as well.

| #   | Method                     | Operation   | Observation                                                                |
|-----|----------------------------|-------------|----------------------------------------------------------------------------|
| 5.1 | x.__missing__(self, key)   | v = x[key]  | Called by `dict` subclasses to get value when key is not in the dictionary |
| 5.2 | x.__contains__(self, item) | item in x   | Called to check if item is in the container                                |
| 5.3 | x.__setitem__(self,key)    | x[key] = v  | Called to implement assignment to value at the index key                   |
| 5.4 | x. __delitem__(self,key)   | del x[key]  | Called to implement deletion of the item in key                            |
| 5.5 | x.__reversed__(self)       | reversed(x) | Called to implement reverse iteration                                      |
| 5.6 | x.__iter__(self)           | iter(x)     | Should return an iterator for the container                                |
| 5.7 | x.__len__((self)           | len(x)      | Should return the length of the object, an integer >= 0                    |
| 5.8 | x.__getitem__(self,key)    | v = x[key]  | Should return the object with at index key                                 |

Remarks:
For methods __getitem__, __setitem__ and __delitem__:
- If `key` is of an inappropriate type, it should raise `TypeError`.
- If `key` is a value outside the set of indexes (for sequences type), it should raise `IndexError`.
- If `key` is missing (for mapping types), it should raise `KeyError`.


---


## Context Managers

Context managers allow setup and cleanup actions to be executed when wrapped by `with` statements or called directly. This can be used to save and restore states, lock and unlock resources, or close files and connections.

|  #  | Method                                      | Operation       | Observation                             |
|:---:|---------------------------------------------|-----------------|-----------------------------------------|
| 6.1 | x.__enter__(self)                           | with x as obj:  | Enter the runtime context related to x  |
| 6.2 | x.__exit__(self, exc, exc_value, traceback) | with x as obj:  | Exit the runtime context related to x   |

Remarks:
- If the context was exited without any exception, all three parameters `exc`, `exc_value` and traceback will be `None`.
- If an exception is supplied, the method should return `True` to suppress it. Otherwise, it will continue normally upon exit from this method.


---


## Callable Objects

Allows an instance of an object to be have like a function, that is, you can “call” them.

|  #  | Method                     | Operation           | Observation                                         |
|:---:|----------------------------|---------------------|-----------------------------------------------------|
| 7.1 | x.__call__(self[,args...]) | x([arg1, arg2...])  | Called when the instance is "called" as a function  |

Remarks:
- The `__call__` method can be declare as any other function, as you can declare as many arguments as you want.
- It is useful when the instance must change its current state a lot, like in class that represents a point in plane.


---


## Emulating numeric types (objects): Binary arithmetic operations

These methods are called to implement the binary arithmetic operations

| #    |            Method            | Operator     |
|------|:----------------------------:|:------------:|
| 8.1  | x.__add__(self, y)           | x + y        |
| 8.2  | x.__sub__(self, y)           | x - y        |
| 8.3  | x.__mul__(self, y)           | x * y        |
| 8.4  | x.__matmul__(self, y)        | x @ y        |
| 8.5  | x.__truediv__(self, y)       | x / y        |
| 8.6  | x.__floordiv__(self, y)      | x // y       |
| 8.7  | x.__mod__(self, y)           | x % y        |
| 8.8  | x.__divmod__(self, y)        | divmod(x, y) |
| 8.9  | x.__pow__(self, y[, modulo]) | x**y         |
| 8.10 | x.__lshift__(self, y)        | x << y       |
| 8.11 | x.__rshift__(self, y)        | x >> y       |
| 8.12 | x.__and__(self, y)           | x & y        |
| 8.13 | x.__xor__(self, y)           | x ^ y        |
| 8.14 | x.__or__(self, y)            | x \| y       |


---


## Emulating numeric types (objects): Binary arithmetic operations with reflected (swapped) operands.

| #    | Method                    | Operation          |
|------|---------------------------|--------------------|
| 9.1  | x.__radd__(self, y)       | y + x              |
| 9.2  | x.__rsub__(self, y)       | у - х              |
| 9.3  | x.__rmul__(self, y)       | y * x              |
| 9.4  | x.__rmatmul__(self, y)    | y @ x              |
| 9.5  | x.__rtruediv__(self, y)   | y / x              |
| 9.6  | x.__rfloordiv__(self, y)  | y // x             |
| 9.7  | x.__rmod__(self, y)       | у % х              |
| 9.8  | x.__rdivmod__(self, y)    | divmod(y, x)       |
| 9.9  | x.__rpow__(self, y)       | **A                |
| 9.10 | x.__rlshift__(self, y)    | y << x             |
| 9.11 | x.__rrshift__(self, y)    | y >> x             |
| 9.12 | x.__rand__(self, y)       | y & x              |
| 9.13 | x.__rxor__(self,y)        | y ^ x              |
| 9.14 | x.__ror__(self, y)        | y \| x             |


---


## Implement the augmented arithmetic assignments :

| #     |             Method            |  Operator  |
|-------|:-----------------------------:|:----------:|
| 10.1  | x.__iadd__(self, y)           | x += y     |
| 10.2  | x.__isub__(self, y)           | x -= y     |
| 10.3  | x.__imul__(self, y)           | x *= y     |
| 10.4  | x.__imatmul__(self, y)          | x @= y     |
| 10.5  | x.__itruediv__(self, y)         | x/= y      |
| 10.6  | x.__ifloordiv__(self, y)      | x //= y    |
| 10.7  | x.__imod__(self, y)           | x %= y     |
| 10.8  | x.__ipow__(self, y[, modulo]) | x **= y !! |
| 10.9  | x.__ilshift__(self, y)        | x <<= y    |
| 10.10 | x.__irshift__(self, y)        | x >>= y    |
| 10.11 | x.__iand__(self, y)           | x &= y     |
| 10.12 | x.__ixor__(self, y)           | x ^= y     |
| 10.13 | x.__ior__(self, y)            | x \|= y    |


---


## Emulating numeric types: Unary arithmetic operations:

| #    |        Method       |  Operator  |
|------|:-------------------:|:----------:|
| 11.1 | x.__neg__(self)     | -x         |
| 11.2 | x.__pos__(self)     | +x         |
| 11.3 | x.__abs__(self)     | abs(x)     |
| 11.4 | x.__invert__(self)  | ~          |


---


## Implementing the built-in math functions

| #     |        Method          |  Operator  |
|-------|:----------------------:|:----------:|
| 12.1  | x.__complex__(self)    | complex(x) |
| 12.2  | x.__int__(self)        | int(x)     |
| 12.3  | x.__float__(self)      | float(x)   |
| 12.4  | x.__round__(self[,n])  | round(x)   |
| 12.5  | x.__trunc__(self)      | trunc(x)   |
| 12.6  | x.__floor__(self)      | floor(x)   |
| 12.7  | x.__ceil__(self)       | ceil(x)    |

---


## Implementing `operator.index()`

Called to implement `operator.index()`, and whenever Python needs to losslessly convert the numeric object to an integer object (such as in slicing, or in the built-in `bin()`, `hex()` and `oct()` functions). Presence of this method indicates that the numeric object is an integer type. Must return an integer.

| #     |        Method       |  Operator          |
|-------|:-------------------:|:------------------:|
| 13.1  | x.__index__(self)   | operator.index(x)  |


---


## Rich Comparison Operators:

Some methods to enable a class to behave like built-in types and implement intuitive comparison between objects using operators.

| #     |         Method        | Operator |                         Description                                |
|-------|:---------------------:|:--------:|:------------------------------------------------------------------:|
| 14.1  | x.__lt__(self, other) | <        |                                                                    |
| 14.2  | x.__le__(self, other) | <=       |                                                                    |
| 14.3  | x.__eq__(self, other) | ==       |                                                                    |
| 14.4  | x.__ne__(self, other) | !=       | If `__ne__` is not implemented, it returns the opposite of __eq__. |
| 14.5  | x.__ge__(self, other) | >=       |                                                                    |
| 14.6  | x.__gt__(self, other) | >        |                                                                    |
| 14.7  | x.__bool__(self)      | bool(x)  | Called to implement truth value testing                            |
| 14.8  | x.__hash__(self)      | hash(x)  | Objects that compare equal should have the same hash value         |

Remarks:
- It may return `NotImplemented` error if does not implement the operation for the given pair of arguments.
- By convention, it should returns `False` and `True`. But these methods can return any value, and if it is used in a Boolean context (such as `if` statement) Python will call `bool()` on the value to determine if it is true or false.
- If `__bool__` is not defined, Python calls `__len__`, and the object is defined true if its result is different than zero.
- If a class does not define `__eq__` then it should not define `__hash__` either.
- A class that defines `__eq__` but does not define `__hash__` will have its `__hash__` implicitly set to `None`. In this case, it is not possible to use them in hashable collections such as `set`.
`__hash__` should return an integer. And `a == b` means that `hash(a) == hash(b)`.


---


## Other

| #     |         Method       | Operator | Description     |
|-------|:--------------------:|:--------:|:---------------:|
| 15.1  | x.__idiv__(self, y)  | /=       |                 |
| 15.2  | x.__long__(self)     | long(x)  |                 |
| 15.3  | x.__oct__(self)      | oct(x)   |                 |
| 15.4  | x.__hex__(self       | hex(x)   |                 |


---


## Callable types: User-defined methods:

A user-defined function object is created by a function definition (see section Function definitions). It should be called with an argument list containing the same number of items as the function’s formal parameter list.

| #     |    Attribute    |                                                                      Meaning                                                                     |           |
|-------|:---------------:|:------------------------------------------------------------------------------------------------------------------------------------------------:|:---------:|
| 16.1  | __doc__         | The function’s documentation string, or None if unavailable; not inherited by subclasses.                                                        | Writable  |
| 16.2  | __name__        | The function’s name.                                                                                                                             | Writable  |
| 16.3  | __qualname__    | The function’s qualified name.     New in version 3.3.                                                                                           | Writable  |
| 16.4  | __module__      | The name of the module the function was defined in, or None if unavailable.                                                                      | Writable  |
| 16.5  | __defaults__    | A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value.                 | Writable  |
| 16.6  | __code__        | The code object representing the compiled function body.                                                                                         | Writable  |
| 16.7  | __globals__     | A reference to the dictionary that holds the function’s global variables — the global namespace of the module in which the function was defined. | Read-only |
| 16.8  | __dict__        | The namespace supporting arbitrary function attributes.                                                                                          | Writable  |
| 16.9  | __closure__     | None or a tuple of cells that contain bindings for the function’s free variables. See below for information on the cell_contents attribute.      | Read-only |
| 16.10 | __annotations__ | A dict containing annotations of parameters.  The keys of the dict are the parameter names, and 'return' for the return annotation, if provided. | Writable  |
| 16.11 | __kwdefaults__  | A dict containing defaults for keyword-only parameters.                                                                                          | Writable  |

Remarks:
- Function objects also support getting and setting arbitrary attributes, which can be used, for example, to attach metadata to functions. Regular attribute dot-notation is used to get and set such attributes.
---


## 1.1 - 1.3

```python
class A:
  def __new__(cls):
    print('Creation of A')
    instance = super().__new__(cls)
    return instance

  def __init__(self):
    print('Initialization')

  def __del__(self):
    print('Delete')

a = A()
del a
```


---


## 2.1 - 2.4

```python
class B:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'B ({self.a})'

    def __str__(self):
        return f'B with {self.a}'

    def __bytes__(self):
        return self.a.to_bytes(4, byteorder='big')

    def __format__(self, spec):
        if spec == 'f':
            return str(self.a)
        return str(self)

b = B(10)
print(repr(b))
print(str(b))
print(bytes(b))
print(format(b, 'f'))
```
```
> B (10)
> B with 10
> b'\x00\x00\x00\n'
> 10
```


---


## 3.1 - 3.5

```python
class D:
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''
    def __init__(self, val):
        super().__setattr__('counter', 0)
        super().__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super().__setattr__('counter', self.counter + 1)
        super().__delattr__(name)

d = D(10)
print(d.value, d.counter)
d.value = 11
print(d.value, d.counter)
```


---


## 4.1 - 4.4

```python
class Celsius:
    '''Descriptor for celsius value.'''
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    '''Descriptor for farenheit value.'''
    def __get__(self, instance, owner):
        return (instance.celsius * 9 / 5) + 32.0

    def __set__(self, instance, value):
        instance.celsius = (value - 32) * 5 / 9


class Temperature:
    celsius = Celsius()
    fahrenheit = Fahrenheit()

e = Temperature()
e.celsius = 10
print(f'{e.celsius} ºC = {e.fahrenheit} ºF')
e.fahrenheit = 45
print(f'{e.celsius} ºC = {e.fahrenheit} ºF')
```


---


## 5.1 - 5.8

```python
class FunctionalList:
    '''A class wrapping a list with some extra functional magic'''
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def head(self, n):
        return self.values[:n]

    def tail(self, n):
        return self.values[n:]

    def first(self):
        return self.values[0]

    def last(self):
        return self.values[-1]

a = FunctionalList([1, 2, 3, 4])
print(a.head(2))
print(a[0])
```


---


## 6.1 - 6.2

```python
class H:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.fp = open(self.name)
        return self.fp

    def __exit__(self, exc, exc_value, traceback):
        print(f'Exception: {exc_value}')
        self.fp.close()
        self.fp = None


h = H('test.txt')
with h as v:
    print(v.read())
```


---


## 7.1

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

p = Point(1, 2)
print(p)
p(4, 5)
print(p)
```


---


## 8.1 - 8.14

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


---


## 14.1 - 14.8

```python
class C:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __hash__(self):
        return hash(self.age)

    def __bool__(self):
        return self.age > 0

alice = C(15)
bob = C(30)
rel = 'younger' if alice < bob else 'older'
print(f'Alice is {rel} than Bob')
print(hash(alice))
```
```
> Alice is younger than Bob
> 15
```
