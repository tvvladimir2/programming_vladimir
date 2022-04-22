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


## DESCRIPTION

Objects are created using classes, which are actually the focal point of OOP.
It is a part of `object-oriented programming (OOP) paradigm`.
The class describes what the object will be, but is separate from the object itself.
In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the `keyword class` and an `indented block`, which contains `class methods` (which are functions).

**Example**: Simple class and its objects.
```python
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
```

The code above defines a class named `Cat`, which has two attributes: `color` and `legs`.
Then the class is used to `create 3 separate objects` of that class.


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
In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.

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
