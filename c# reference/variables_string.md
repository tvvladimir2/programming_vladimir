# C# STRING


---


## LINKS

[](https://www.tutorialsteacher.com/articles/difference-between-string-and-string-in-csharp)



---



## DESCRIPTION

In C#, a string is a series of characters that is used to represent text.
It can be a character, a word or a long passage surrounded with the double quotes ".
The following are string literals.

The maximum size of a String object in memory is 2GB or about 1 billion characters. However, practically it will be less depending upon CPU and memory of the computer.



---



## DECLARE A STRING VARIABLE

There two ways to declare a string variable in C#. Using `System.String` class and using `string` keyword. Both are the same and make no difference. Learn string vs String for more info.

Essentially, there is no difference between `string` and `String` (capital S) in C#.

String (capital S) is a class in the .NET framework in the System namespace. The fully qualified name is System.String. Whereas, the lower case string is an alias of System.String.

It is recommended to use string (lower case) over String. However, it's a matter of choice. You can use any of them. Many developers use string to declare variables in C# and use System.String class to use any built-in string methods e.g., String.IsNullOrEmpty().

you must import System namespace at the top of your .cs file to use String class, whereas string keyword can be used directly without any namespace.

```cs
string ch = "S";                    // Charachter
string word = "String";             // Word
string text = "This is a string.";  // Long passage

string str1= "Hello";               // string is an alias of System.String
String str2 = "World!";             // a class in the .NET framework in the System namespace

// The output is the sameBoth are the same
Console.WriteLine(str1.GetType().FullName); // System.String
Console.WriteLine(str2.GetType().FullName); // System.String
```



---



## STRING IS A COLLECTION OR AN ARRAY OF CHARACHTERS

In C#, a string is a collection or an array of characters. So, string can be created using a char array or accessed like a char array.


```cs
char[] chars = {'H','e','l','l','o'};

string str1 = new string(chars);  // Hello
String str2 = new String(chars);  // Hello

foreach (char c in str1)
{
    Console.WriteLine(c);
}
```
```
> Hello
> Hello
> H
> e
> l
> l
> o
```


```cs
string word = "String";

Console.WriteLine(word);

foreach (char c in word)
{
    Console.WriteLine(c);
}
```
```
> String
> S
> t
> r
> i
> n
> g
```



---



## SPECIAL CHARACHTERS

Because a string is surrounded with double quotes, it cannot include " in a string.


Example: **Give a compile-time error**:
```cs
string text = "This is a "string" in C#.";
```
```
> The build failed. Fix the build errors and run again.
```


Use backslash \ before double quotes and some special characters such as \,\n,\r,\t, etc. to include it in a string. 

Example: **Using special charachters**
```cs
string text = "This is a \"string\" in C#.";
string str = "xyzdef\\rabc";
string path = "\\\\mypc\\ shared\\project";

Console.WriteLine(text);
Console.WriteLine(str);
Console.WriteLine(path);
```
```
> This is a "string" in C#.
> xyzdef\rabc
> \\mypc\ shared\project
```



---



## VERBATIM STRINGS

It is tedious to prefix \ to include every special characters. Verbatim string in C# allows a special characters and line brakes. Verbatim string can be created by prefixing @ symbol before double quotes. 


Example: **ESCAPE SEQUENCE**:
```cs
string str = @"xyzdef\rabc";
string path = @"\\mypc\shared\project";
string email = @"test@test.com";

Console.WriteLine(str);
Console.WriteLine(path);
Console.WriteLine(email);
```
```
> xyzdef\rabc
> \\mypc\shared\project
> test@test.com
```


Example: **DOUBLE QUOTES IN VERBATIM STRING**:
```cs
using System;

string text1 = "This is a \"string\" in C#.";   // valid
string text = @"This is a "string." in C#.";    // error
string text = @"This is a \"string\" in C#.";   // error
string text4 = @"This is a ""string"" in C#.";  // valid

Console.WriteLine(text1);
Console.WriteLine(text4);
```
```
> This is a "string" in C#.
> This is a "string" in C#.
```



---



## MULTI-LINE STRING

Example: **Multi-line strings**
```cs
string str1 = "this is a \n" + 
        "multi line \n" + 
        "string";
		
// The @ symbol can also be used to declare a multi-line string. 
string str2 = @"this is a 
        multi line 
string";

Console.WriteLine(str1);
Console.WriteLine(str2);
```
```
> this is a 
> multi line
> string
> this is a 
>         multi line
> string
```



---



## STRING CONCATENATION - ADDITION METHOD 1

Multiple strings can be concatenated with `+` operator.


Example: **Adding strings**
```cs
string name = "Mr." + "James " + "Bond" + ", Code: 007";

string firstName = "James";
string lastName = "Bond";
string code = "007";
string agent = "Mr." + firstName + " " + lastName + ", Code: " + code;

Console.WriteLine(name);
Console.WriteLine(firstName);
Console.WriteLine(lastName);
Console.WriteLine(code);
Console.WriteLine(agent);
```
```
> Mr.James Bond, Code: 007
> James
> Bond
> 007
> Mr.James Bond, Code: 007
```


A String is immutable in C#. It means it is read-only and cannot be changed once created in the memory. Each time you concatenate strings, .NET CLR will create a new memory location for the concatenated string. So, it is recommended to use StringBuilder instead of string if you concatenate more than five strings.

[C# - StringBuilder](https://www.tutorialsteacher.com/csharp/csharp-stringbuilder)



---



## STRING INTERPOLATION - ADDITION METHOD 2

String interpolation is a better way of concatenating strings. We use + sign to concatenate string variables with static strings.

C# 6 includes a special character `$` to identify an interpolated string. An interpolated string is a mixture of static string and string variable where string variables should be in {} brackets.

```cs
string firstName = "James";
string lastName = "Bond";
string code = "007";

// $ indicates the interpolated string, and {} includes string variable to be incorporated with a string.
string fullName = $"Mr. {firstName} {lastName}, Code: {code}";

Console.WriteLine(fullName);
```
```
> Mr. James Bond, Code: 007
```



---



## ITERATE OVER STRING CHARACHTERS

Example: **Iterate using `foreach` loop**
```cs
using System;

class Program
{
    static void Main()
    {
        const string value = "abc";
        // Version 1: use foreach-loop.
        foreach (char c in value)
        {
            Console.WriteLine(c);
            Console.WriteLine(c.GetType());
        }
    }
}
```
```
> a
> System.Char
> b
> System.Char
> c
> System.Char
```


Example: **Iterate over String charachters using `For` loop**
```cs
using System;

class Program
{
    static void Main()
    {
        const string value = "abc";

        // Loop over string in reverse.
        for (int i = 0; i < value.Length; i++)
        {
            Console.WriteLine(value[i]);
            Console.WriteLine(value[i].GetType());
        }

        Console.WriteLine("");

        // Loop over string in reverse.
        for (int i = value.Length - 1; i >= 0; i--)
        {
            Console.WriteLine("REVERSE: {0}", value[i]);
        }
    }
}
```
```
> a
> System.Char
> b
> System.Char
> c
> System.Char
> 
> REVERSE: c
> REVERSE: b
> REVERSE: a
```



---



## `INT` TO `STRING`

```cs
using System;

class Program
{
    static void Main()
    {
        string[] myArray = { "Miami", "Berlin", "Hamburg"};

        string myString = string.Join(" ", myArray);
        
        Console.WriteLine("myString");
    }
}
```
```
> 123
> -123
```



---



## CONVERT `ARRAY` TO `STRING`




---



## ACCESS STRING `CHAR`s

Example: **First string `char`**
```cs
using System;

class Program
{
    static void Main()
    {
        string myString = "Hello";
        Console.WriteLine(myString[0]);
    }
}
```
```
> H
```


Example: **Access last string char**
```cs
using System;

class Program
{
    static void Main()
    {
        string myString = "-1294";
        Console.WriteLine(myString[myString.Length - 1]);
    }
}
```
```
> 4
```



---



## ITERATE USING `WHILE` LOOP

Example: **Deletes all zeros at the end**
```cs
using System;

class Program
{
    static void Main()
    {
        string stringVariable = "-1294000";

        Console.WriteLine("only first" + stringVariable);

        while (true)
        {
            char myZero = '0';

            if (stringVariable[stringVariable.Length - 1] == myZero)
            {
                stringVariable = stringVariable.Remove(stringVariable.Length - 1);
                Console.WriteLine(stringVariable);
            }
            else
            {
                break;
            }
        }
    }
}
```