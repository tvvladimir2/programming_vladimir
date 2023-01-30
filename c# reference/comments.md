# C# COMMENTS


---


## LINKS
[C# Comments](https://www.w3schools.com/cs/cs_comments.php)


---


## ABOUT COMMENTS

Comments can be used to explain C# code, and to make it more readable. It can also be used to prevent execution when testing alternative code.


---


## SINGLE-LINE COMMENTS

```cs
using System;   // we can use classes from the System namespace.

namespace HelloWorld    
{
  class Program   
    {
      static void Main(string[] args)
      {
        // THIS IS A COMMENT: Single-line comments start with two forward slashes (//).
        Console.WriteLine("Hello World!");
      // Any text between // and the end of the line is ignored by C# (will not be executed).
        Console.WriteLine("Hello World!");  // Single-line comments at the end of a line of code
      }
  }
}
```
```
> Hello World!
> Hello World!
```



---



## MULTI-LINE COMMENTS

```cs
using System;   // we can use classes from the System namespace.

namespace HelloWorld    
{
  class Program   
    {
      static void Main(string[] args)
      {
        /* This is a multi-line comments.
        All text is ignored in between.
        You can write as much as you want. */
        Console.WriteLine("Hello World!");
      }
  }
}
```
```
> Hello World!
```



---



## XML DOCUMENTATION COMMENTS: CLASS

[Documentation comments](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/)

```cs
/// <summary>
///  This is a summary about a class. XML is generated for IDEs.
/// </summary>

using System;

namespace HelloWorld
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Hello World!");
		}
	}
}
```

The XML documentation (.xml file) generated will contain:

```xml
<?xml version="1.0"?>
<doc>
	<assembly>
		<name>HelloWorld</name>
	</assembly>
	<members>
	</members>
</doc>
```



## XML DOCUMENTATION COMMENTS: `METHOD`

```cs
using System;

namespace HelloWorld
{
	class Program
	{
		public static void Main(string[] args)
		{
			CalledMethod(5, 6)
		}

    private int CalledMethod(int x, int y)
    {
      /// <summary>
      /// This is a summary about the method
      /// </summary>
      /// <param name="a">A summary about parameter a</param>
      /// <param name="b">A summary about parameter b</param>
      /// <returns>A summary about return</returns>
      Console.WriteLine("Hello World!");
      return x + y;
    }
	}
}
```
