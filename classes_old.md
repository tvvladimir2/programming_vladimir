# CLASSES


---


## CHAPTER ORDER

- Classes (file classes.md)
- Inheritance
- Magic methods & operators
- Object life cycle
- Data hiding
- Class & static methods
- Properties


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

**Example**:

When we call a method on an instance, the instance gets passed as the implicit first argument to the method automatically.

Incorrect version:
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


Correct version:
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


## __INIT__ method

The `__init__` method is the most important method in a class.
This is called when an `instance (object)` of the class is created, using the class name as a function.

All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self argument to the list for you; you do not need to include it when you call the methods. Within a method definition, self refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.
In an `__init__` method, `self.attribute` can therefore be used to set the initial value of an instance's attributes.

```python
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)
```


---


# INHERITANCE (SUPER CLASS)

Inheritance provides a way to share functionality between classes.

**Example**: Classes share attributes, but have different methods or other.
```python
# Define a SuperClass
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Subclass. `Cat` class inherits from a SuperClass `Animal`.
class Cat(Animal):
    # `purr` method is exclusive to `Cat` class
    def purr(self):
        print("Purr...")

# Subclass. `Dog` class inherits from a SuperClass `Animal`.
class Dog(Animal):
    # `bark` method is exclusive to `Dog` class
    def bark(self):
        print("Woof!")

# The attributes are shared between `Dog` & `Cat` classes.
fido = Dog("Fido", "brown")

print(fido.color)
fido.bark()
```
```
> brown
> Woof!
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


# OBJECT LIFE-CYCLE

Stages:

- Creation
  - Definition of the class to which it belongs
  - Instantiation of an instance, when `__init__` is called. Memory is allocated to store the instance. Just before this occurs, the `__new__` method of the class is called. This is usually overridden only in special cases.

- Manipulation
  - Other code can then interact with the object, by calling functions on it and accessing its attributes.

- Destruction
  - When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes. Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object. If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted. In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well. The `del` statement reduces the reference count of an object by one, and this often leads to its deletion. The magic method for the `del` statement is `__del__`. The process of deleting objects when they are no longer needed is called garbage collection.
