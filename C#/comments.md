# C# COMMENTS


---


## LINKS
[C# Comments](https://www.w3schools.com/cs/cs_comments.php)


---


## ABOUT COMMENTS

Comments can be used to explain C# code, and to make it more readable. It can also be used to prevent execution when testing alternative code.


---


## EXAMPLES

```cs
using System;   // we can use classes from the System namespace.

namespace HelloWorld    
{
  class Program   
    {
      static void Main(string[] args)
      {
        // Single-line comments start with two forward slashes (//).
        // Any text between // and the end of the line is ignored by C# (will not be executed).
        // THIS IS A COMMENT:
        Console.WriteLine("Hello World!");

        Console.WriteLine("Hello World!");  // Single-line comments at the end of a line of code

        // Multi-line comments start with /* and ends with */.
        // Any text between /* and */ will be ignored by C#.
        /* The code below will print the words Hello World
        to the screen, and it is amazing */
        Console.WriteLine("Hello World!");
      }
  }
}
```
```
> Hello World!
> Hello World!
> Hello World!
```