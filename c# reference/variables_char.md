# C# VARIABLES > VALUE TYPES > SIMPLE TYPES >  CHAR


---


## LINKS

[The Char type](https://csharp.net-tutorials.com/data-types/the-char-type/)



---



## DESCRIPTION

The `System.Char` data type is used to hold a single, unicode character. C# has an alias for it, called `char`, which you can use when declaring your `char` variables:

- .NET actually uses a list of char's to represent a string
- a `char` is a numerical value, where each character has a specific number in the `Unicode` "alphabet"
- There are more than 130.000 different Unicode characters, ranging from the Latin/western alphabet to historical scripts.


---



## INITIALIZE

```cs
using System;

class Program
{
    static void Main()
    {
        char charVariable;    // Initialize a `char`
    }
}
```



---



## INITIALIZE AND DECLARE

```cs
using System;

class Program
{
    static void Main()
    {
        char charVariable = 'H';    // Initialize and Declare Declare a `char`
        // char charVariable = "H"; // shall not work because of double quotations
    }
}
```



---



## A LIST OF `CHAR`s REPRESENTS A `STRING`

.NET actually uses a list of char's to represent a string. That also means that you can pull out a single char from a string, or iterate over a string and get each character as a char data type:

```cs
using System;

class Program
{
    static void Main()
    {
        string helloWorld = "Hello!";
        foreach(char c in helloWorld)
        {
            Console.WriteLine(c);
        }
    }
}
```
```
> H
> e
> l
> l
> o
> !
```



---



## CONVERT `CHAR` TO `UNICODE` NUMBER

You can very easily go from a `char` data type to its numeric representation as `int`

```cs
string helloWorld = "Hello!";
foreach(char c in helloWorld)
{
    Console.WriteLine(c + ": " + (int)c);
}

char charVariable = '0';
Console.WriteLine("zero is " + (int)charVariable);
```
```
> H: 72
> e: 101
> l: 108
> l: 108
> o: 111
> !: 33

> zero is 48
```



---



## CONVERT `INT` TO `CHAR`

```cs
using System;

class Program
{
	public static void Main()
	{	
		int myInteger = 65;
        char myChar = Convert.ToChar(myInteger);
        Console.WriteLine(myChar);
	}
}
```
```
> A
```