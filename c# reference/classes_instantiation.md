# CLASSES: INSTANTIATE: OBJECTS OF A CLASS

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