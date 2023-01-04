# CLASSES: CLASS MEMBER: METHODS


---



## CONSTRUCTOR

A constructor is a `special type of method` which will be called automatically when you create an instance of a class. A constructor is defined by using an access modifier and class name <access-modifier> <class-name>(){ }.

Example: **Constructor**
```cs
class Student
{
    // <access-modifier> <class-name>(){ }
    public Student()    // it has the same name as a class, hence gets called
    {
        //constructor
    }
}
```

- A constructor name must be the same as a class name.
- A constructor can be `public`, `private`, or `protected`.
- The constructor `cannot return any value` so cannot have a return type.
- A class can have multiple constructors with different parameters but can only have one parameterless constructor.
- If no constructor is defined, the C# compiler would create it internally.



---