# C# VAR


---


## EXPLICITLY TYPED VARIABLE

In C#, variables must be declared with the data type. These are called explicitly typed variables.

```cs
int i = 100;// explicitly typed variable
```


---


## IMPLICITLY TYPED LOCAL VARIABLE

C# 3.0 introduced `var` keyword to declare method level variables without specifying a data type explicitly. 

```cs
using System;
using System.IO;
			
public class Program
{
	public static void Main()
	{
		var i = 10; // System.Int32
    	Console.WriteLine("Type of i is {0}", i.GetType());

		var str = "Hello World!!";  // System.String
		Console.WriteLine("Type of str is {0}", str.GetType()); 

		var dbl = 100.50d;  // System.Double
		Console.WriteLine("Type of dbl is {0}", dbl.GetType());

		var isValid = true; // System.Boolean
		Console.WriteLine("Type of isValid is {0}", isValid.GetType());

		var ano = new { name = "Steve" };   // <>f__AnonymousType0`1[System.String]
		Console.WriteLine("Type of ano is {0}", ano.GetType());

		var arr = new[] { 1, 10, 20, 30 };  // System.Int32[]
		Console.WriteLine("Type of arr is {0}", arr.GetType());

		var file = new FileInfo("MyFile");  // System.IO.FileInfo
		Console.WriteLine("Type of file is {0}", file.GetType());
	}
}
```
```
> Type of i is System.Int32
> Type of str is System.String
> Type of dbl is System.Double
> Type of isValid is System.Boolean
> Type of ano is <>f__AnonymousType0`1[System.String]
> Type of arr is System.Int32[]
> Type of file is System.IO.FileInfo
```

The compiler will infer the type of a variable from the expression on the right side of the `=` operator. Above, `var` will be compiled as `int`.


---


## INITIALIZATION & DECLARATION

Implicitly-typed variables must be initialized at the time of declaration; otherwise C# compiler would give an error: Implicitly-typed variables must be initialized.

```cs
var i; // Compile-time error: Implicitly-typed variables must be initialized
i = 100;
```


Multiple declarations of `var` variables in a single statement are not allowed.

```cs
var i = 100, j = 200, k = 300; // Error: cannot declare var variables in a single statement

//The followings are also valid
var i = 100; 
var j = 200; 
var k = 300;
```


---


## `VAR` FROM EXPRESSION

```cs
int i = 10;
var j = i + 1; // compiles as int
```


--- 


## FUNCTION PARAMETERS

var cannot be used for function parameters.

```cs
void Display(var param) //Compile-time error
{
    Console.Write(param);
}
```


--- 


## `FOR` & `FOREACH` LOOPS

`var` can be used in for, and foreach loops.

```cs
for(var i = 0; i < 10; i++)
{
    Console.Write(i);
}
```
```
> 0123456789
```


---


## LINQ QUERIES

`var` can also be used with LINQ queries.

```cs
using System;
using System.Linq;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{
		// string collection
		IList<string> stringList = new List<string>() { 
			"C# Tutorials",
			"VB.NET Tutorials",
			"Learn C++",
			"MVC Tutorials" ,
			"Java" 
		};
		
		// LINQ Query Syntax
		var result = from s in stringList
					where s.Contains("Tutorials") 
					select s;
		
		foreach (var str in result)
		{
			Console.WriteLine(str);
		}
	}
}
```
```
C# Tutorials
VB.NET Tutorials
MVC Tutorials
```


---

