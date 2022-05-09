# CLASSES


---


## LINKS

[O'Reilly - Python Beyond the Basics - Object-Oriented Programming](https://www.oreilly.com/library/view/python-beyond-the/9781771373609/)


---


## CHAPTER ORDER

- Classes, Instances, Attributes And Methods
- Defining A Class
- Instance Methods
- Instance Attributes
- Encapsulation
- `Init` Constructor
- Class Attributes
- Working With Class And Instance Data
- Assignment 1
- Assignment 1 - Solution

---


## OBJECT-ORIENTED PYTHON

- Everything is an object in Python, even numbers.
- Other languages employ primitives (non-object data)
- An object is a unit of data (having one or more `attributes`), of a particular `class` or `type`, with associated functionality (`methods`).

**Example**: Every entity in Python is an object of a particular type.
```python
# my_integer is of type 'int'
# my_integer is of class 'int'
my_integer = 5
my_string = 'hello'
my_list = ['a', 'b', 'c']
my_bool = True
my_none = None

def my_function():
  print('Hello')

# Take the type of the list and assign it to a variable.
# Then we checked the type of that object.
# The type of an object has a type.
my_type = type(my_list)

print(type(my_integer))
print(type(my_string))
print(type(my_list))
print(type(my_bool))
print(type(my_none))
print(type(my_function))
print(type(my_type))
```
```
>>> <class 'int'>
>>> <class 'str'>
>>> <class 'list'>
>>> <class 'bool'>
>>> <class 'NoneType'>
>>> <class 'function'>
>>> <class 'type'>
```

The `object` or `class` has `attributes`, some of which are methods.

**Example**: Find attributes associated with the integer.
```python
var = 5
print(dir(var))         # List of integer attributes
print(var.numerator)    # Attribute that returns the value that is
print(var.real)
print(var.bit_length)   # Attribute which is a method which returns the bit length of the integer.
```
```
>>> ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__',
    '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__',
    '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__',
    '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__',
    '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
    '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
    '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
    '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
    '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
    '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio',
    'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 5
>>> 5
>>> 3
```


---


## OOP DESCRIPTION

| Term      | Description                                                                | Car example                                           |
|:---------:|:--------------------------------------------------------------------------:|:-----------------------------------------------------:|
| Class     | A blueprint for an instance.                                               | Provides the blueprint for a car object.              |
| Instance  | A constructed object of the class.                                         | Car as a class object. Holds data. Unit of data.      |
| Type      | Indicates the class the instance belongs to.                               |                                                       |
| Attribute | Any object value: `object.attribute`. Not every attribute is a method.     | Each instance of a car has its own state (attributes) |
| Method    | a `callable attribute` defined in the class. Every method is an attribute. | Each instance of a car does the same thing (methods)  |

Objects are created using classes, which are actually the focal point of OOP.
It is a part of `object-oriented programming (OOP) paradigm`.
The class describes what the object will be, but is separate from the object itself.
In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the `keyword class` and an `indented block`, which contains `class methods` (which are functions).
All classes begin with an upper-case letter, that's a standard Python convention.


**Example**: Create an empty class
`__main__` is a namespace.
`0x000001CC906C7F70` is a Hex code, address of memory where the object is stored. The identity.

```python
class MyClass(object):
  pass

this_object = MyClass()
print (this_object)
```
```
>>> <__main__.MyClass object at 0x000001CC906C7F70>
```

**Example**: Attributes
Variables defined in a class are available in the instances though object attribute syntax.
Attribute is not located in the instance. It's located in the class. The instance looks for this attribute in the class variables.
```python
class MyClass(object):
  var = 10

this_object = MyClass()
print (this_object.var)
```
```
>>> 10
```


**Example**: Simple class and its objects.

- `self` is the object/instance upon which the method is called
- `self` = felix, rover, stumpy

```python
class MyClass:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = MyClass("ginger", 4)
rover = MyClass("dog-colored", 4)
stumpy = MyClass("brown", 3)
```

The code above defines a class named `MyClass`, which has two attributes: `color` and `legs`.
Then the class is used to `create 3 separate objects` of that class.


---


## INSTANCE METHODS

- Instance methods are variables defined in a class.
- They are accessed through the instance: `instance.method()`
- When called through the instance, the instance is automatically passed as 1st argument of the method.
- Because of this automatic passing of the instance, instance methods are known as "bound" methods, i.e. bound to the instance upon which it is called.
- An instance of a class knows what class it's from
- Vars defined in the class are available to the instance
- A method on an instance passes instance as the first argument to the method (named `self` in the method)
- Instances have their own data, called instance attributes
- Variables defined in the class are called `class attributes`
- When we read an attribute, Python looks for it first in the instance, and then the class

**Example**: Incorrect instance method:

When we call a method on an instance, the instance gets passed as the implicit first argument to the method automatically.

```python
class Joe(object):
  def callme():         # `self` is deleted
    print('calling "callme" method with an instance:   ')

thisjoe = Joe()

# Passes an argument when calling the function, but nothing in the parenthesis.
thisjoe.callme()    
```
```
>>> TypeError: callme() takes 0 positional arguments but 1 was given
```


**Example**: Correct instance method:

```python
class Joe(object):
  def callme(self):         # `self` is present
    print('calling "callme" method with an instance:   ')
    print(self)             # Gives the ID of an instance

thisjoe = Joe()

# Passes an argument when calling the function, but nothing in the parenthesis.
thisjoe.callme()            # Passes the instance directly

# Prove that `thisjoe` and `self` are really the same object
print(thisjoe)              # Gives the ID of an instance
```
```
>>> calling "callme" method with an instance:
>>> <__main__.Joe object at 0x000001AC805D5490>
>>> <__main__.Joe object at 0x000001AC805D5490>  
```


---


## Instance attributes

- Instance values are stored right in the instance using the instance's attributes.
- `instance.attribute = value` sets the instance's attributes
- Instance can access variables defined in the class
- An instance can also get and set values in itself
- Because these values change according to what happens to the object, we call these values `state`
- Instance data takes the form of instance attribute values, set and accessed through `object.attribute` syntax

```python
import random

class MyClass(object):
  def do_this_function(self):
    # Set the value of the attribute `rand_val` in the instance itself
    self.rand_val = random.randint(1,10)

my_instance = MyClass()
my_instance.do_this_function()

# `rand_val` is stored in the instance
print(my_instance.rand_val)
```
```
>>> 2
```


---


## THREE PILLARS

- Encapsulation
- Inheritance
- Polymorphism


---


## ENCAPSULATION

- Why write a whole method to set and get the value?
- It provides a gateway for any operations having to do with the instance's state.
- In this gateway we can insure the integrity of the instance's attributes.
- By using these methods we are `Encapsulating` the instance and ensuring the integrity of it's data.

- Encapsulation: the first of the three pillars of OOP.
- Encapsulation refers to the safe storage of data (as attributes) in an instance.
- Data should be accessed only through instance methods.
- Data should be validated as correct (depending on the requirement set in the class methods).
- Data should be safe from changes by external processes.
- Although normally set in a setter method, instance attributes values can be set anywhere.
- Encapsulation in Python is a voluntary restriction.
- Python does not implement data hiding, as does other languages.

```python
class MyClass(object):
  def set_val(self, val):
    self.value = val

  def get_val(self):
    return self.value

a = MyClass()
b = MyClass()

# Using class methods.
a.set_val(10)
b.set_val(100)

print(a.get_val())
print(b.get_val())

# Setting the value of the attribute directly in the instance.
a.value = 'hello'
print(a.value)
print(a.get_val())
```
```
>>> 10
>>> 100

>>> hello
>>> hello
```



```python
class MyInteger(object):
  def set_val(self, val):
    # We attempt to convert whatever is passed to the method to the integer.
    try:
      val = int(val)
    # If it can not set the value to integer, the value will simply return without setting it up.
    except ValueError:
      return
    self.value = val

  def get_val(self):
    return self.value

  def increment_val(self):
    self.val = self.val + 1

i = MyInteger()

# Set the value of the attribute using methods.
i.set_val(9)
print(i.get_val())

i.set_val('hi')
print(i.get_val())


# Setting the value of the attribute directly in the instance.
i.val = 'hi'
# TypeError: can only concatenate str (not "int") to str
print(i.increment_val())
```
```
>>> 9
>>> 9
```


---


## __INIT__ CONSTRUCTOR METHOD

- `__init__` is a keyword variable: it must be named `init`.
- `__init__` is a magic method because it is a method automatically called when a new instance is constructed.
- It it is not present, it is not called.
- The `self` argument is the first appearance of the instance.
- `__init__` offers the opportunity to initialize attributes in the instance at the time of construction.


The `__init__` magic method is the most important method in a class.
This is called when an `instance (object)` of the class is created, using the class name as a function.

All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the `self` argument to the list for you;
You do not need to include it when you call the methods. Within a method definition, `self` refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, `MyClass` instance has attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.
In an `__init__` method, `self.attribute` can therefore be used to set the initial value of an instance's attributes.


**Example**:

```python
class MyClass:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = MyClass("ginger", 4)
print(felix.color)
```


**Example**:
```python
class MyClass(object):
  def __init__(self):
    print('calling __init')
    # Sets an integer value in the instance
    self.val = 0

  def increment(self):
    self.val += 1

# We are not calling the method `__init__` directly.
# We are just constructing a new instance.
my_object = MyClass()
my_object.increment()
my_object.increment()
print(my_object.val)
```
```
>>> 2
```
```python
class MyClass(object):
  def __init__(self, value):
    print('calling __init')
    # Sets an integer value in the instance
    self.val = value

  def increment(self):
    self.val += 1

# Because `__init__` is passed automatically, we can pass an argument too.
my_object = MyClass(5)
my_object.increment()
my_object.increment()
print(my_object.val)
```
```
>>> 7
```


---


## CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES

- The instance has access to both `class attributes` & `instance attributes`.
- Attributes / variables in the class are accessible through the instance.
- Instance attributes are also accessible by the instance.
- When we use the syntax `object.attribute`, we're asking Python to look up the attribute:
  - Attribute lookup order:
  - First in the instance.
  - Then in the class.
- Method calls through the instance follow this lookup.
- An instance of the class know what class it's from.
- Vars defined in the class are available to the instance.
- A method on an instance passes instance as the first argument to the method (named `self` in the method)
- Variables defined in the class are class attributes.
- When we read an attribute, Python looks for it first in the instance, and then in the class.

**Example**: Class attribute vs Instance attribute.
```python
class MyClass(object):
  classy = 10               # Class attribute / variable.

  def set_val(self):
    self.insty = 100        # Instance attribute.

my_object = MyClass()

my_object.set_val()

print(my_object.classy)
print(my_object.insty)
```
```
>>> 10
>>> 100
```


**Example**: Prove attribute lookup order.
```python
class MyClass(object):
  classy = 10               # Class attribute / variable.

my_object = MyClass()
# Reads from the class
print(my_object.classy)

my_object = 20
# Read from the instance
print(my_object.classy)

# Delete from the instance
del. my_object.classy
# Read from the class
print(my_object.classy)
```
```
>>> 10
>>> 20
>>> 10
```


---


## WORKING WITH CLASS AND INSTANCE DATA

- Class data is intended to be shared among instances.
-

```python
class InstanceCounter(object):
  # Counts how many instances are created.
  # All instances have access to this attribute.
  # Class variable and attribute.
  count = 0

  def __init__(self, val, name):
    # Each instance has access to this attributes, but no other.
    self.val = val
    self.name = name
    # Why do we have to qualify `count` variable with the class name `InstanceCounter` if we are inside the class itself right now?
    # Because `count` variable is outside the function `__init__`. It is not global. So we need direction where to take it from.
    InstanceCounter.count +=1

  def set_val(self, newval):
    self.val = newval

  def get_val(self):
    return self.val

  def get_count(self):
    return InstanceCounter.count

a = InstanceCounter (5, 'a')
b = InstanceCounter (13, 'b')
c = InstanceCounter (17, 'c')

for i in (a, b, c):
  print('val of object', i.name, '= %s' % (i.get_val()))
  print('count: %s' % (i.get_count()))
```
```
>>> val of object a = 5
>>> count: 3
>>> val of object b = 13
>>> count: 3
>>> val of object c = 17
>>> count: 3
```


---


## Assignment

Create a class to output given output.

```python
# Write your class here:
class MaxSizeList(object):

  def __init__(self, val_range):
    self.val_range = int(val_range)
    self.val_list = []

  def push(self, newval):
    self.val_list.append(newval)

  def get_list(self):
    return self.val_list[0: self.val_range]

# Given piece of code
a = MaxSizeList (3)
b = MaxSizeList (1)

a.push('hey')
a.push('hi')
a.push('let\'s')
a.push('go')

b.push('hey')
b.push('hi')
b.push('let\'s')
b.push('go')

print(a.get_list())
print(b.get_list())
```
```
>>> ['hey', 'hi', "let's"]
>>> ['hey']
```


---


# INHERITANCE AND POLYMORPHISM


---


## INHERITING ATTRIBUTES (SUPERCLASS)

- Inheritance the second pillar of OOP
- Inheritance provides a way to share functionality between classes.
- One class can inherit from another:
  - The class' attributes are inherited
  - In particular, its methods are inherited
  - This means that instances of an inheriting (child) class can access attributes of the inherited (parent) class
- This is simply another level of attribute lookup: instance, then class, then inherited classes
- The child class can access the attributes of all parent (grandparent, etc.) classes.
- Inheritance promotes code collaboration and reuse. E.g. Server class > Application class >> Image class.
- 'No code should appear twice'

- Classes can be organized into an inheritance hierarchy.
- `object.attribute` lookup hierarchy:
  - The instance
  - The class
  - Any class from which this class inherits

- An inheriting class `class MyClass(YourClass)` can be known as:
  - Child class
  - Derived class
  - Subclass
- An inherited class `class YourClass(object)` can be known as:
  - Parent classy
  - Base classy
  - Superclass

**Example**: Explaining theory
```python
class Date(object):               # inherits from the `object' class`
  def get_date(self):
    return '2014-10-13'

# Place `Date` class name in the arguments list of `Time` class definition.
# Allows to call a `get_date` method on a `Time` object.
class Time(Date):                 # inherits from the `Date` class
  def get_time(self):
    return '08:13:07'

my_date = Date()
print(my_date.get_date())

my_time = Time()
print(my_time.get_time())
print(my_time.get_date())         # found this method in the `Date` class
```
```
>>> 2014-10-13
>>> 08:13:07
>>> 2014-10-13
```

**Example**: Dog & Cat differences.
```python
# Define a SuperClass
class Animal(object):         # Class `Animal` enhirits from `object`. `object` is a built-in superclass from which all news style class inherit from.
  # `Animal` has two method attributes. They are inherited by `Dog` & `Cat`.
  def __init__(self, name):   # `self` for `Dog` class is equal to `Dog`.
    self.name = name
  # All animals eat.
  def eat(self, food):
    print ('%s is eating %s' % (self.name, food))

# Subclass. `Dog` class inherits from a SuperClass `Animal`.
class Dog(Animal):        # `Dog` & `Cat` both inherit from `Animal`.
  # This class has only one method attribute.
  # 'fetch' method is exclusive to `Dog` class
  def fetch(self, thing):
    print ('%s goes after %s' % (self.name, thing))

# Subclass. `Cat` class inherits from a SuperClass `Animal`.
class Cat(Animal):        # `Dog` & `Cat` both inherit from `Animal`
  # This class has only one method attribute.
  # 'catch_string' method is exclusive to `Cat` class
  def catch_string(self):
    print('%s shreds the string!' % (self.name))


d = Dog('Rover')
c = Cat('Katja')

d.fetch('paper')  # Rover goes after the paper!
c.catch_string()    # Katja shreds the string!
d.eat('dog food') # Rover is eating dog food.
c.eat('cat food') # Katja is eating cat food.
d.catch_string()    # AtrributeError: 'Dog' object has no attribute 'catch_string'
```
```
>>> Rover goes after paper
>>> Katja shreds the string!
>>> Rover is eating dog food
>>> Rover is eating cat food
>>> AttributeError: 'Dog' object has no attribute 'catch_string'
```


**Syntax**:
```python
# Superclass
class Parent():
  def __init__(self, atr1, atr2):
      self.atr1 = atr1
      self.atr2 = atr2

# Subclass
class Child(Parent):
  def child_func(self):
      print("Child_func!")

obj = Child(atr1, atr2)
```


**Example**: Method inheritance 1
```python
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()    # 2
A().method()    # 1

b = B()
a = A()

b.method()      # 2
a.method()      # 1
```


**Example**: Method inheritance 2
```python
class A:
  def a(self):
    print(1)

class B(A):
  def a(self):
    print(2)

class C(B):
  def c(self):
    print(3)

c = C()
c.a()
```
```
> 2
```


**Example**: Indirect inheritance from a third party. Circular inheritance is not possible.
```python
class A:
    def method(self):
        print("A method")

class B(A):
    def second_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.second_method()
c.third_method()
```
```
> A method
> B method
> C method
```


**Example**: `super` is a useful `inheritance-related function` that refers to the `parent class`.
```python
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()    # calls the spam() method of the superclass.

B().spam()
```
```
> 2
> 1
```


---


#  POLYMORPHISM

- The third pillar of OOP
- Two classes with same interface (i.e., method name). We call this 'Common Interface'.
- The methods are often different, but conceptually similar.
- Allows for expressiveness in design: we can say that this group of related classes implement the same action.
- Allows to design a family of classes that do the same thing, possibly differently.
- `Duck typing` refers to reading an object's attributes to decide whether it is of a proper type, rather than checking the type itself.
- `Duck typing` = Handle errors using exception handling.
- If it walks like a `duck`, talks like a `duck`, it must be a `duck`. We are going to do the thing that we expect this object to do.
- Checking the `type` of instance ahead of time is considered `UnPythonic`

**Example**: Dog & Cat differences.
```python
# A Superclass
class Animal(object):
  def __init__(self, name):
    self.name = name
  def eat(self, food):
    print ('%s is eating %s' % (self.name, food))

class Dog(Animal):
  def fetch(self, thing):
    print ('%s goes after %s' % (self.name, thing))
  # A child class has a method with the same name as other child class.
  def show_affection(self):
    print('{0} wags tail'.format(self.name))

class Cat(Animal):
  def catch_string(self):
    print('%s shreds the string!' % (self.name))
  # A child class has a method with the same name as other child class.
  def show_affection(self):
    print('{0} purrs'.format(self.name))

for i in (Dog('Rover'), Cat('Katja'), Cat('Precious'), Dog('Scout')):
  # Child classes have the same interface for `show_affection`.
  # Each `show_affection` methods are different for each child class.
  i.show_affection()
```
```
>>> Rover wags tail
>>> Katja purrs
>>> Precious purrs
>>> Scout wags tail
```


**Example**: Python itself has classes that are polymorphic.
E.g. `len()` can be used with different variable types.

```python
# Create a string variable.
var = 'hello'
# Use built-in Python method.
print(len(var))
# Call `len()` instance method `__len__`.
print(var.__len__())
# Show string methods
print(dir(var))

# `len()` works on all types because this method is included in all instance types.
print(len([1,2,3]))
print(len(('a', 'b', 'c')))
print(len({'a': 1, 'b': 2}))

# `len()` is included in list and other instance types. So these types are polymorphic.
print(([1,2,3]))
```
```
>>> 5
>>> 5
>>> ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> 3
>>> 3
>>> 2

>>> ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```


---


## Inheriting The Constructor

[https://www.programiz.com/python-programming/methods/built-in/super](Python 'super' at Programiz)

- `__init__` is like any other method; it can be inherited.
- If a class does not have an `__init__` constructor, Python will check its parant class to see if it can find one.
- As soon as it finds one, Python calls it and stops looking.
- We can use the `super()` function to call methods in the  parent class.
- We may want to initialize in the parent as well as our own class.


**Example**: From Programiz.com
```python
class Animal(object):
  def __init__(self, animal_type):
    print('Animal Type:', animal_type)

class Mammal(Animal):
  def __init__(self):
    # call superclass
    # Instead of:
    # Animal.__init__(self, 'Mammal')
    super().__init__('Mammal')
    print('Mammals give birth directly')

dog = Mammal()
```
```
>>> Animal Type: Mammal
>>> Mammals give birth directly
````

**Example**: From O'Reilly - Python Beyond the Basics - Object-Oriented Programming - 0404
```python
import random

class Animal(object):
  def __init__(self, name):
    self.name = name

class Dog(Animal):

  # Now 'Dog' has it's own `__init__`.
  def __init__(self, name):
    # `super` is a built-in function designed to relate a class to it's `super class` (parent class).
    # `super` says: get the `super` class of `Dog` and pass the `Dog` instance to whatever method we state here (here's `__init__` now).
    # We are calling `Animal.__init__(self, var)` with 'Dog' object
    # `super` allows to keep things modular.
    # Allows to separate common functionality from more specific functionality.
    # We could write instead:
    # Animal.__init__(name)
    # Instead of:
    # Animal.__init__(self, name)
    super(Dog, self).__init__(name)
    self.breed = random.choice(['Shiu Tzu', 'Beagle', 'Mutt'])

  def fetch(self, thing):
    print ('%s goes after the %s' % (self.name, thing))

d = Dog('dogname')

print(d.name)
print(d.breed)
```
```
>>> dogname
>>> Mutt
```





























## SYNTAX

```python
class Student:                  # `Student` instance.

  # Class variables (class attributes). Shared by all instances of the class.
  school_name = 'ABC school'            

  # 'Class constructor' method for instance variables (data members) initialization.
  # Call __init__ method to create an instance (object) of the class, using the class name as a function.
  # __init__ method takes two arguments and assigns them to the object's attributes
  def __init__(self, name, age):        # `Self` is a must, it refers to the instance calling the method.
    self.name = name                    # `self.attribute` used to set the initial value of an instance's attributes.
    self.age = age

  # Behavior (instance methods) add additional functionality. Accesses using 'jessa.show()'.
  def show(self):
      print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

  # Class method:
  @classmethod
  def change_school(cls, name):         # `cls` refers to the Class
    print(Student.school_name)          # Access class variables
    Student.school_name = name          # Modify class variables

# Create object of a class
jessa = Student('Jessa', 14)
mikey = Student('Mikky', 15)

# Call class method
Student.change_school('ZYZ School')

# Access instance variables
print('Student:', jessa.name, jessa.age)

# Modify instance variables
jessa.name = 'Veronika'
s1.age = 16
print('Student:', jessa.name, jessa.age)

# Modify class variables (class attributes)
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)
print('School name:', jessa.school_name)

# Call methods
jessa.show()
```


---


# OBJECT LIFE-CYCLE

Stages:

- Creation
  - Definition of the class to which it belongs
  - Instantiation of an instance, when `__init__` is called. Memory is allocated to store the instance. Just before this occurs, the `__new__` method of the class is called. This is usually overridden only in special cases.

- Manipulation
  - Other code can then interact with the object, by calling functions on it and accessing its attributes.

- Destruction
  - When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes. Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object. If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted. In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well. The `del` statement reduces the reference count of an object by one, and this often leads to its deletion. The magic method for the `del` statement is `__del__`. The process of deleting objects when they are no longer needed is called garbage collection.
