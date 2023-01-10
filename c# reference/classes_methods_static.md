# STATIC METHODS


---


## LINKS

[C# - Static Class, Methods, Constructors, Fields](https://www.tutorialsteacher.com/csharp/csharp-static)



---



## SYNTAX

```
Class User:
    - object1   // instances of User class)
    - object2
    - object3


User object1 = new User();     // Instantiate an object - create an instance
object1.ClassMethod();         // `ClassMethod()` is on `object1` only

User.findInList();             // The method is on the class itself
```



---



## DESCRIPTION

 In C#, static means something which cannot be instantiated. You cannot create an object of a static class and cannot access static members using an object.

C# classes, variables, methods, properties, operators, events, and constructors can be defined as static using the static modifier keyword. 



---



## WHY USE IT?

1. Static fields of a non-static class is shared across all the instances. So, changes done by one instance would reflect in others.



---



## STATIC CLASS

Apply the static modifier before the class name and after the access modifier to make a class static. The following defines a static class with static fields and methods.

Example: **C# Static Class**
```cs
public static class Calculator
{
    private static int _resultStorage = 0;
    
    public static string Type = "Arithmetic";

    public static int Sum(int num1, int num2)
    {
        return num1 + num2;
    }

    public static void Store(int result)
    {
        _resultStorage = result;
    }
}
```

Above, the Calculator class is a static. All the members of it are also static.

You cannot create an object of the static class; therefore the members of the static class can be accessed directly using a class name like ClassName.MemberName, as shown below.

Example: **Accessing Static Members**
```cs
class Program
{
    static void Main(string[] args)
    {
        var result = Calculator.Sum(10, 25); // calling static method
        Calculator.Store(result); 

        var calcType = Calculator.Type; // accessing static variable
        Calculator.Type = "Scientific"; // assign value to static variable
    }
}
```


- Static classes cannot be instantiated.
  
- All the members of a static class must be static; otherwise the compiler will give an error.
  
- A static class can contain static variables, static methods, static properties, static operators, static events, and static constructors
- 
- A static class cannot contain instance members and constructors.
  
- Indexers and destructors cannot be static
  
- `var` cannot be used to define static members. You must specify a type of member explicitly after the `static` keyword.
  
- Static classes are sealed class and therefore, cannot be inherited.
  
- A static class cannot inherit from other classes.
  
- Static class members can be accessed using `ClassName.MemberName`.
  
- A static class remains in memory for the lifetime of the application domain in which your program resides.



---



## STATIC MEMBERS IN NON_STATIC CLASS

The normal class (non-static class) can contain one or more static methods, fields, properties, events and other non-static members.

It is more practical to define a non-static class with some static members, than to declare an entire class as static. 




---



### STATIC FIELDS

Static fields in a non-static class can be defined using the static keyword.

Static fields of a non-static class is shared across all the instances. So, changes done by one instance would reflect in others.

Example: Shared Static Fields
```cs
// The class itself
public class StopWatch
{
    public static int NoOfInstances = 0;
    
    // instance constructor
    public StopWatch()  // runs everytime we create an instance
    {
        StopWatch.NoOfInstances++;  // increments the field
        Console.WriteLine("done");
    }
}
```
```cs
// The program we run
class Program
{
    static void Main(string[] args)
    {
        StopWatch sw1 = new StopWatch();
        StopWatch sw2 = new StopWatch();
        Console.WriteLine(StopWatch.NoOfInstances); //2 
			
        StopWatch sw3 = new StopWatch();
        StopWatch sw4 = new StopWatch();
        Console.WriteLine(StopWatch.NoOfInstances);//4
    }
}
```



---



## STATIC METHODS

You can define one or more static methods in a non-static class. Static methods can be called without creating an object. You cannot call static methods using an object of the non-static class.

The static methods can only call other static methods and access static members. You cannot access non-static members of the class in the static methods.


**RULES**:
- Static methods can be defined using the static keyword before a return type and after an access modifier.
  
- Static methods can be overloaded but cannot be overridden.
  
- Static methods can contain local static variables.
  
- Static methods cannot access or call non-static variables unless they are explicitly passed as parameters.


Example: **Static method**
```cs
class Program
{
    static int counter = 0;
    string name = "Demo Program";

    static void Main(string[] args)
    {
        counter++; // can access static fields
        Display("Hello World!"); // can call static methods

        name = "New Demo Program"; //Error: cannot access non-static members
        SetRootFolder("C:\MyProgram"); //Error: cannot call non-static method
    }

    static void Display(string text)
    {
        Console.WriteLine(text);
    }

    public void SetRootFolder(string path) {  }
}
```


---



### STATIC CONSTRUCTORS

A non-static class can contain a parameterless static constructor. It can be defined with the static keyword and without access modifiers like public, private, and protected.


**RULES**:

- The static constructor is defined using the static keyword and without using access modifiers public, private, or protected.
  
- A non-static class can contain one parameterless static constructor. Parameterized static constructors are not allowed.
  
- Static constructor will be executed only once in the lifetime. So, you cannot determine when it will get called in an application if a class is being used at multiple places.
  
- A static constructor can only access static members. It cannot contain or access instance members.


The following example demonstrates the difference between static constructor and instance constructor.

Example: **Static Constructor vs Instance Constructor**
```cs
public class StopWatch
{
    // static constructor
    static StopWatch()
    {
        Console.WriteLine("Static constructor called");
    }

    // instance constructor
    public StopWatch()
    {
        Console.WriteLine("Instance constructor called");
    }

    // static method
    public static void DisplayInfo()
    {
        Console.WriteLine("DisplayInfo called");
    }

    // instance method
    public void Start() { }

    // instance method
    public void Stop() {  }
}
```

Above, the non-static class StopWatch contains a static constructor and also a non-static constructor.

The static constructor is called only once whenever the static method is used or creating an instance for the first time. The following example shows that the static constructor gets called when the static method called for the first time. Calling the static method second time onwards won't call a static constructor.



---