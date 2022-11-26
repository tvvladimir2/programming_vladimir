## C# SWITCH STATEMENT


---


## LINKS

[C# - Switch Statement](https://www.tutorialsteacher.com/csharp/csharp-switch)


---


# DESCRIPTION

The `switch` statement can be used instead of `if else` statement when you want to test a variable against three or more conditions. Here, you will learn about the switch statement and how to use it efficiently in the C# program.

The following is the general syntax of the switch statement.

The switch statement starts with the switch keyword that contains a match expression or a variable in the bracket switch(match expression). The result of this match expression or a variable will be tested against conditions specified as cases, inside the curly braces { }. A case must be specified with the unique constant value and ends with the colon :. Each case includes one or more statements to be executed. The case will be executed if a constant value and the value of a match expression/variable are equal. The switch statement can also contain an optional default label. The default label will be executed if no cases executed. The break, return, or goto keyword is used to exit the program control from a switch case. 

C# 7.0 onward, switch cases can include non-unique values. In this case, the first matching case will be executed.

---


## SYNTAX

```cs
switch(match expression/variable)
{
    case constant-value:
        statement(s) to be executed;
        break;  // break, return, goto keywords to exit the program
    default:    // a default label to be executed in case if none of the value match
        statement(s) to be executed;
        break;
}
```


---


## EXAMPLES

The `switch(x)` statement includes a variable `x` whose value will be matched with the value of each case value. The `switch` statement contains three cases with constant values 5, 10, and 15. It also contains the default label, which will be executed if none of the case value match with the switch variable/expression. Each case starts after `:` and includes one statement to be executed. The value of `x` matches with the second case `case 10:`, so the output would be `Value of x is 10`. 

```cs
using System;
					
public class Program
{
	public static void Main()
	{
        // variable `x` is tested
		int x = 10;

		switch (x)
		{ 
			case 5:
				Console.WriteLine("Value of x is 5");
				break;
			case 10:
				Console.WriteLine("Value of x is 10");
				break;
			case 15:
				Console.WriteLine("Value of x is 15");
				break;
			default:
				Console.WriteLine("Unknown value");
				break;
		}
	}
}
```
```
> Value of x is 10 
```


The switch statement can also include an expression whose result will be tested against each case at runtime.

```cs
int x = 125;

// expression `x % 2` is tested
switch (x % 2)
{ 
    case 0:
        Console.WriteLine($"{x} is an even value");
        break;
    case 1:
        Console.WriteLine($"{x} is an odd Value");
        break;
}
```
```
> 125 is an odd value
```


## SWITCH CASE

The switch cases must be unique constant values. It can be bool, char, string, integer, enum, or corresponding nullable type.

Note:
 - C# 7.0 onward, switch cases can include non-unique values. In this case, the first matching case will be executed.

Consider the following example of a simple switch statement.

```cs
string statementType = "switch";

switch (statementType)
{
    case "if.else": // test against a `string`
        Console.WriteLine("if...else statement");
        break;
    case "ternary":
        Console.WriteLine("Ternary operator");
        break;
    case "switch":
        Console.WriteLine("switch statement");
        break;
}
```
```
> switch statement
```


Multiple cases can be combined to execute the same statements.

```cs
int x = 5;

switch (x)
{ 
    case 1:
        Console.WriteLine("x = 1");
        break;
    case 2:
        Console.WriteLine("x = 2");
        break;
    case 4:
    case 5:
        Console.WriteLine("x = 4 or x = 5");
        break;
    default:
        Console.WriteLine("x > 5");
        break;
}
```
```
> x = 4 or x = 5
```


## BREAK, RETURN, GOTO EXIT STATEMENTS

Each case must exit the case explicitly by using `break`, `return`, `goto` statement, or some other way, making sure the program control exits a case and cannot fall through to the default case.

**USING RETURN FOR A FUCNTION**:
```cs
using System;
					
public class Program
{
	public static void Main()
	{
		var x = 125;
		
        // Test `ìsOdd(x)` function using Ternary ?: operator
		Console.Write(isOdd(x)?"Even value":"Odd value");
	}
	
	static bool isOdd(int x)    // run a function
	{
		switch (x % 2)
		{ 
			case 0:
				return true;
			case 1:
				return false;
		}
		
		return false;
	}
}
```
```
> Odd value
```

**MISSING THE BREAK, RETURN, GOTO STATEMENT GIVES ERROR**:
```cs
using System;
					
public class Program
{
	public static void Main()
	{
		int x = 10;

		switch (x)
		{ 
			case 1:
				Console.WriteLine("Value of x is 5");
				break;
			case 10:
				Console.WriteLine("Value of x is 15");
                // Break statement is missing leads to a compile-time error.
			default:
				Console.WriteLine("Unknown value");
				break;
		}
	}
}


---


## NESTED SWITCH STATEMENTS

A `switch` statement can be used inside another `switch` statement.

```cs
using System;
					
public class Program
{
	public static void Main()
	{
		int j = 5;

		switch (j)
		{
			case 5:
				Console.WriteLine(5);
				switch (j - 1)
				{
					case 4:
						Console.WriteLine(4);
						switch (j - 2)
						{
							case 3:
								Console.WriteLine(3);
								break;
						}
						break;
				}
				break;
			case 10:
				Console.WriteLine(10);
				break;
			case 15:
				Console.WriteLine(15);
				break;
			default:
				Console.WriteLine(100);
				break;
		}
	}
}
```
```
> 5
> 4
> 3
```


---