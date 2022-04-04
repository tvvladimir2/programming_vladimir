# CLASSES


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
class Student:
  # Class variables
  school_name = 'ABC school'            

  # Constructor
  def __init__(self, name, age):        # Constructor for initialize instance variables (data members)
    self.name = name
    self.age = age

  # Behavior (instance methods)
  def show(self):
      print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

  # Class method:
  @classmethod
  def change_school(cls, name):         # `cls` refers to the Class
    print(Student.school_name)          # Access class variables
    Student.school_name = name          # Modify class variables

# Create object of a class
jessa = Student('Jessa', 14)

# Call class method
Student.change_school('ZYZ School')

# Access instance variables
print('Student:', jessa.name, jessa.age)

# Modify instance variables
jessa.name = 'Veronika'
s1.age = 16
print('Student:', jessa.name, jessa.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)

# Call methods
jessa.show()
```


---


## `__init__` method

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
