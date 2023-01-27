# C# DATA TYPES: INTEGRAL NUMERIC TYPES: INT TYPE


---



## LINKS

[Integral numeric types (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types)



---



## DESCRIPTION

The `int` data type is `32-bit signed integer`. It can store numbers from `-2,147,483,648 to 2,147,483,647`.
The int keyword is an alias of Int32 struct in .NET.

The `uint` is `32-bit unsigned integer`. The uint keyword is an alias of UInt32 struct in .NET.
It can store positive numbers from `0 to 4,294,967,295`. Optionally use U or u suffix after a number to assign it to uint variable.



---



## INITIALIZATION

Example: **Initialize `int` numbers**
```cs
using System;

class Program
{
    static void Main()
    {
        int a = -2147483648;
        int b = 2147483647;

        // Used against `Use of unassigned local variable` error
        int defaultInteger = default;	// The value is 0

        // The number is too big for `int`. It should be `uint`
        // int c = 4294967295; //Compile-time error: Cannot implicitly convert type 'uint' to 'int'.

        Console.WriteLine(a);
        Console.WriteLine(b);
        Console.WriteLine(defaultInteger);
    }
}
```
```
-2147483648
2147483647
0
```

Example: **Initialize `int` numbers**
```cs
using System;

class Program
{
    static void Main()
    {
        uint a = 4294967295;

        // uint can not be negative
        // uint b =-1;   //Compile-time error: Constant value '-1' cannot be converted to a 'uint'

        // Used against `Use of unassigned local variable` error
        uint defaultUInt = default;	// The value is 0

        Console.WriteLine(a);
        Console.WriteLine(defaultUInt);
    }
}
```
```
> 4294967295
> 0
```



---



## MAX & MIN VALUES OF INT & UINT

```cs
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Int ranges from " + Int32.MinValue);  //-2147483648
        Console.WriteLine("to " + Int32.MaxValue);  //2147483647
        Console.WriteLine("");
        Console.WriteLine("Uint ranges from " + UInt32.MinValue); //0
        Console.WriteLine("to " + UInt32.MaxValue); //4294967295
    }
}
```
```
> Int ranges from -2147483648
> to 2147483647
> 
> Uint ranges from 0
> to 4294967295
```


---



## USAGE: FOR HEXADECIMAL & BINARY NUMBERS

The int data type is also used for hexadecimal and binary numbers. A hexadecimal number starts with 0x or 0X prefix. C# 7.2 onwards, a binary number starts with 0b or 0B.

```cs
// HEXADECIMAL, BINARY
int hex = 0x2F;
int binary = 0b_0010_1111;

Console.WriteLine(hex);
Console.WriteLine(binary);
```



---



## CONVERT FROM FLOAT & CHECK

Example: **Convert `Float` to `Int`**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{	
		float floatVariable = 33.9f;
		int resultVariable;

		resultVariable = (int)floatVariable;    // Simply deletes all decimal values
		Console.WriteLine(resultVariable);
	}
}
```
```
> 33
```


Example: **Check if `Float` is `Int`**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{	
		float floatVariable = 4.0f; // Our Float
        // float floatVariable = 4.01f; // Our Float
		int resultVariable;         // Our result Int

		if (CheckFloatIsAnInteger(floatVariable))
		{
			resultVariable = (int)floatVariable;	// Casting
			Console.WriteLine("Initial value is: " + floatVariable.ToString("0.00"));
			Console.WriteLine("Our variable is an integer, it is: " + resultVariable);
		}
		else
		{
			Console.WriteLine("Our variable is a float, it is: " + floatVariable.ToString("0.0"));
		}
		

		bool CheckFloatIsAnInteger(double x)	// Bool Method
		{
			try
			{
				int y = Int16.Parse(x.ToString());
				Console.WriteLine("Return value will be true");
				return true;
			}
			catch 
			{
				Console.WriteLine("Return value will be false");
				return false;
				
			}
		}
	}
}
```
**if (floatVariable == 4.0f)**
```
> Return value will be true
> Initial value is: 4.00
> Our variable is an integer, it is: 4
```
**if (floatVariable == 4.01f)**
```
> false
> Our variable is a float, it is: 4.01
```



---



## CONVERT FROM CHAR TO INT

```cs
using System;

class Program
{
    static void Main()
    {
        int myInteger = default;
        const string value = "123";

        // Version 1: use foreach-loop.
        foreach (char i in value)
        {
            Console.WriteLine("myInteger = " + int.Parse(i.ToString()));
        }
        Console.WriteLine("myInteger is of type: " + myInteger.GetType());
    }
}
```
```
> myInteger = 1
> myInteger = 2
> myInteger = 3
> myInteger is of type: System.Int32
```



---



## CONVERT FROM STRING TO INT

