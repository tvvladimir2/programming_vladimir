# C#: CLASS & OBJECTS


---


## LINKS

[](https://www.tutorialsteacher.com/csharp/csharp-class)



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



### 1. CLASS MEMBER: FIELD CLASS MEMBER

A class can have one or more fields. It is a `class-level variable` that holds a value.

Example: **Field**
```cs
class Student
{
    private int _studentAge;     // Can only be accessed withing this class

    // Not recommended to use. Best to use a property.
    public int studentClass;  // Can be accessed outside this class.
    string studentName;
}
```



---



### 2. CLASS MEMBER: PROPERTIES

A property encapsulates a private field using setter and getter to assign and retrieve underlying field value.
They act like gateways to fields.


Example: **Property**
```cs
class Student
{
    private int id;

    public int StudentId    // Encapsulates a private field
    {
        // Auto implemented property
        get { return id; }
        set { id = value; }
    }

    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```


In the above example, the `id` is a private field that cannot be accessed directly. It will only be accessed using the `StudentId` property. The `get{ }` returns the value of the underlying field and `set{ }` assigns the value to the underlying field `id`.


Example: **Additional logic in get and set**
```cs
class Student
{
    private int id;

    public int StudentId
    {
        get { return id; }

        set {
            if (value > 0)
                id = value;
        }
    }
    
```


From C# 3.0 onwards, property declaration has been made easy if you don't want to apply some logic in getter or setter. Using auto-implemented property, you don't need to declare an underlying private field. C# compiler will automatically create it in IL code.


Example: **Auto-implemented Property**
```cs
class Student
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```

In the above example, backing private field for the FirstName and LastName will be created internally by the compiler. This speed up the development time and code readability.



---



## 3. CLASS MEMBER: CONSTRUCTOR

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



## INSTANTIATE: OBJECTS OF A CLASS

You can create one or more objects of a class. Each object can have different values of properties and field but methods and events behaves the same.

In C#, an object of a class can be created using the `new` keyword and assign that object to a variable of a class type. For example, the following creates an object of the `Student` class and assign it to a variable of the `Student` type.


Example: **Create an Object of a Class**
```cs
Student mystudent = new Student();
```


You can now access public members of a class using the `object.MemberName` notation.


Example: **Access Members of a Class**
```cs
// <Type> <object variable name> = new <Class name / Custom type>
Student mystudent = new Student();  // Instantiate a class: Create an object of a class
mystudent.FirstName = "Steve";  // Create a field class member
mystudent.LastName = "Jobs";

mystudent.GetFullName();    // e.g. Class function that can return fields
```


You can create multiple objects of a class with different values of properties and fields.


Example: **Create Multiple Objects of a Class**
```cs
Student mystudent1 = new Student();
mystudent1.FirstName = "Steve";
mystudent1.LastName = "Jobs";

Student mystudent2 = new Student();
mystudent2.FirstName = "Bill";
mystudent2.LastName = "Gates";
```


Example: **Instantiate a class (two scripts used)**
```cs
// We create an object of a class (another script) within this script
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            // Instantiate a class
            User myUser = new User();  

            // Working with fields
            Console.WriteLine(myUser.myString); // Print a default value of myString field
            myUser.myString = "Madonna Mia";    // Assign a new value to myString field
            Console.WriteLine(myUser.myString); // Print a default value of myString field

            // Working with methods
            myUser.DoSomething();       // Invoke a method on a class
            myUser.DoSomethingElse(5);  // Pass a parameter `5` in.
            Console.WriteLine(myUser.ReturnSomething(5));   // Pass in a parameter and get a return
        }
    }
}
```
```cs
// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class User
    {
        public string myString = "Bruce Willis";

        // This line is hit when we instantiate this class from another script
        // e.g. User myUser = new User();
        // This Constructor is created by C# automatically
        public User()   // default Constructor: class member
        {

        }

        // This line is hit when we call `myUser.doSomething();`
        // `void` means there's no return
        public void DoSomething()   // 'public' shows this method to other scripts.
        {
            Console.WriteLine("doing something " + "in doSomething method");
        }

        // `private` methods are only used within the script itself
        public void DoSomethingElse(int times)  // ìnt times`: Take an argument in to a parameter variable
        {
            for (int i = 0; i < times; i++)
            {
                Console.WriteLine("Method DoSomethingElse: " + "this is the " + (i+1) + "th time we print it");
            }
        }

        public int ReturnSomething(int x)
        {
            return x*x;
        }
    }
}
```
```
> Bruce Willis
> Madonna Mia

> doing something in doSomething method

> Method DoSomethingElse: this is the 1th time we print it
> Method DoSomethingElse: this is the 2th time we print it
> Method DoSomethingElse: this is the 3th time we print it
> Method DoSomethingElse: this is the 4th time we print it
> Method DoSomethingElse: this is the 5th time we print it

> 25
```



---



## INCAPSULATION

![](images/encapsulation.png)