# C#: CLASS & OBJECTS


---


## LINKS

[](https://www.tutorialsteacher.com/csharp/csharp-class)
[C# Programming Tutorial (Caleb Curry)](https://www.youtube.com/watch?v=sGvosEfEu0E&list=PL_c9BZzLwBRIXCJGLd4UzqH34uCclOFwC&index=75)



---



## DESCRIPTION

A class is like a blueprint of a specific object that has certain attributes and features. For example, a car should have some attributes such as four wheels, two or more doors, steering, a windshield, etc. It should also have some functionalities like start, stop, run, move, etc. Now, any object that has these attributes and functionalities is a car. Here, the car is a class that defines some specific attributes and functionalities. Each individual car is an object of the car class. You can say that the car you are having is an object of the car class.

Likewise, in object-oriented programming, a class defines some properties, fields, events, methods, etc. A class defines the kinds of data and the functionality their objects will have.



---



## DEFINE A CLASS

A class can be defined by using the `class` keyword. Let's define a class named `Student`.


Example: **Define a Class**
```cs
class Student
{
    
}
```


---



## CREATE MANY CLASSES IN ONE SCRIPT

```cs
using System;
using System.Collections.Generic;

// First class
public class Program
{
	public static void Main()
	{
		var students = new List<Student>() { 
                new Student(){ Id = 1, Name="Bill"},
                new Student(){ Id = 2, Name="Steve"},
                new Student(){ Id = 3, Name="Ram"},
                new Student(){ Id = 4, Name="Abdul"}
            };
	
		Console.WriteLine("No of elelemts: " + students.Count);
	}
}

// Second class
class Student{
	public int Id { get; set; }
	public string Name { get; set; }
}
```
```
> No of elelemts: 4
```


---



## CLASS MEMEBERS

A class can contain one or more `class members`:
1. fields
2. properties
3. constructors
4. methods
5. delegates
6. events.

A class and its members can have `access modifiers` such as:
- public
- private
- protected
- internal (restrict access from other parts of the program)



---



## INCAPSULATION

![](images/encapsulation.png)