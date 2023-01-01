# C# METHODS / FUNCTIONS


---


## DESCRIPTION

A `method` is a block of code which only runs when it is called.

You can pass data, known as parameters, into a method.

Methods are used to perform certain actions, and they are also known as `functions`.

Why use methods? To reuse code: define the code once, and use it many times.


---


## SYNTAX

```cs
void Start() {
  FunctionName(argument1, argument2); // function called
}

// function defined
void functionName(parameter1, parameter2)
{
  // body of the method
  statement1;
  statement2;
}
```


---


## CREATE A METHOD

A method is defined with the name of the method, followed by parentheses `()`. C# provides some pre-defined methods, which you already are familiar with, such as `Main()`, but you can also create your own methods to perform certain actions:

```cs
class Program
{
    // static means that the method belongs to the Program class and not an object of the Program class.
    // void means that this method does not have a return value.
    // In C#, it is good practice to start with an uppercase letter when naming methods.
    static void MyMethod()    // MyMethod() is the name of the method
    {
        // code to be executed
    }
}
```


---


## CALL A METHOD

To call (execute) a method, write the method's name followed by two parentheses `()` and a semicolon;

In the following example, `MyMethod()` is used to print a text (the action), when it is called:

```cs
static void MyMethod()  // Create a method
{
    Console.WriteLine("I just got executed!");
}


static void Main(string[] args)
{
    // Inside Main(), call the myMethod() method:
    MyMethod();
    MyMethod();
    MyMethod();
}
```
```
> I just got executed!
> I just got executed!
> I just got executed!
```


---


## PARAMETERS & ARGUMENTS

Information can be passed to methods as parameter. Parameters act as variables inside the method.

They are specified after the method name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

The following example has 

**Example**:
```cs
// A method `MyMethod` takes a string called `fname` as parameter.
// `void` means the functions shall not return a value
using System;

namespace MyApplication
{
  class Program
  {
    static void MyMethod(string fname)  // fname is a parameter
    {
      Console.WriteLine(fname + " Refsnes");
    }

    static void Main(string[] args) // void means the functions shall not return a value
    {
        // When the method is called, we pass along a first name,
        // which is used inside the method to print the full name:
        MyMethod("Liam");   // "Liam" is an argument 
        MyMethod("Jenny");  // "Jenny" is an argument
        MyMethod("Anja");   // "Anja" is an argument
    }  
  }
}
```
```
> Liam Refsnes
> Jenny Refsnes
> Anja Refsnes
```


---


## MULTIPLE PARAMETERS

You can have as many parameters as you like, just separate them with commas:

```cs
// `void` means the functions shall not return a value

using System;

namespace MyApplication
{
  class Program
  {
    static void MyMethod(string fname, int age) // fname is the first parameter; age is the second parameter
    {
      Console.WriteLine(fname + " is " + age);
    }

    static void Main(string[] args) 
    {
      MyMethod("Liam", 5);  // "Liam" is the first argument; 5 is the second argument
      MyMethod("Jenny", 8);
      MyMethod("Anja", 31);
    }
  }
}
```
```
> Liam is 5
> Jenny is 8
> Anja is 31
```


---


## DEFAULT PARAMETER VALUE

You can also use a default parameter value, by using the equals sign (=).

```cs
// `void` means the functions shall not return a value
using System;

namespace MyApplication
{
  class Program
  {
    static void MyMethod(string country = "Norway") // "Norway" is a default parameter value 
    {
      Console.WriteLine(country);
    }

    static void Main(string[] args)
    {
      MyMethod("Sweden");
      MyMethod("India");
      MyMethod();   // if we call the method without an argument, it uses the default value ("Norway")
      MyMethod("USA");
    }
  }
}
```
```
> Sweden
> India
> Norway
> USA
```


---


## RETURN VALUE

If you want the method to return a value, you can use a primitive data type (such as `int` or `double`) instead of `void`, and use the `return` keyword inside the method:

**Return 1 parameter**:
```cs
using System;

namespace MyApplication
{
  class Program
  {
    static int MyMethod(int x)
    {
      return 5 + x;
    }

    static void Main(string[] args)
    {
      Console.WriteLine(MyMethod(3));
    }
  }
}
```
```
> 8
```


**Return a sum of two parameters**:
```cs
using System;

namespace MyApplication
{
  class Program
  {
    static int MyMethod(int x, int y)
    {
      return x + y;
    }

    static void Main(string[] args)
    {
      Console.WriteLine(MyMethod(5, 3));
    }
  }
}
```
```
> 8
```

**Store result in a variable**:
You can also store the result in a variable (recommended, as it is easier to read and maintain):

```cs
using System;

namespace MyApplication
{
  class Program
  {
    static int MyMethod(int x, int y)
    {
      return x + y;
    }

    static void Main(string[] args)
    {
      int z = MyMethod(5, 3);
      Console.WriteLine(z);
    }
  }
}
```
```
> 8
```


---


## NAMED ARGUMENTS

It is also possible to send arguments with the key: value syntax.

That way, the order of the arguments does not matter:

```cs
using System;

namespace MyApplication
{
  class Program
  {
    static void MyMethod(string child1, string child2, string child3)
    {
      Console.WriteLine("The youngest child is: " + child3);
    }

    static void Main(string[] args)
    {
      MyMethod(child3: "John", child1: "Liam", child2: "Liam"); // send arguments with the key: value syntax
    }
  }
}
```
```
> The youngest child is: John
```


---


## METHOD OVERLOADING

With method overloading, multiple methods can have the same name with different parameters:

**For example**:
```cs
int MyMethod(int x)
float MyMethod(float x)
double MyMethod(double x, double y)
```

```cs
using System;

namespace MyApplication
{
  class Program
  {
    static int PlusMethod(int x, int y) // same method with integer
    {
      return x + y;
    }

    static double PlusMethod(double x, double y) // same method with double
    {
      return x + y;
    }

    static void Main(string[] args)
    {
      int myNum1 = PlusMethod(8, 5);
      double myNum2 = PlusMethod(4.3, 6.26);
      Console.WriteLine("Int: " + myNum1);
      Console.WriteLine("Double: " + myNum2);
    }  
  }
}
```
```
> Int: 13
> Double: 10.559999999999999
```



---



## ESCAPE A METHOD / CONDITION A METHOD


```cs
void OurMethod(int a, int b)
{
    if (x == true){ return; }    // ignore this method if `x == true`

    y = a + b;
    return y;
}
```



---