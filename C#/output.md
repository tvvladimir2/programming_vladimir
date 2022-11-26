# C# OUTPUT


---


## LINKS
[C# Output](https://www.w3schools.com/cs/cs_output.php)
See `namespaces.md`
See `methods.md`


---


## EMPTY CODE EXAMPLE

```cs
using System;   // we can use classes from the System namespace.

namespace HelloWorld    
{
  class Program   
    {
      static void Main(string[] args)
      {
        // `Console` is a class of the `System` namespace, which has a `WriteLine()` method that is used to output and print text.

        // Output a `string`.
        Console.WriteLine("Hello World!");

        //Output a mathematical calculation
        Console.WriteLine(3 + 3);

        // `Write` does not insert a new line at the end
        Console.Write("Hello World! ");
        Console.Write(3 + 3);
        System.Console.Write("Hello World! ");  // we can write so if you omit the using `System` line
      }
  }
}
```
```
> Hello World!
> 6
> Hello World! 6Hello World!
```