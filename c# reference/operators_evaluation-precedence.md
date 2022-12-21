# OPERATOR EVALUATION & PRECEDENCE

Evaluation of the operands in an expression starts from left to right. If multiple operators are used in an expression, then the operators with higher priority are evaluated before the operators with lower priority.

The following table lists operators starting with the higher precedence operators to lower precedence operators. 

| #  |                                                            Operators                                                         |              Category             |
|----|:----------------------------------------------------------------------------------------------------------------------------:|:---------------------------------:|
| 1  | x.y, x?.y, x?[y], f(x), a[i], x++, x--, new, typeof, checked, unchecked, default, nameof, delegate, sizeof, stackalloc, x->y | Primary                           |
| 2  | +x, -x, !x, ~x, ++x, --x, ^x, (T)x, await, &x, *x, true and false                                                            | Unary                             |
| 3  | x..y                                                                                                                         | Range                             |
| 4  | x * y, x / y, x % y                                                                                                          | Multiplicative                    |
| 5  | x + y, x � y                                                                                                                | Additive                          |
| 6  | x << y, x >> y                                                                                                               | Shift                             |
| 7  | x < y, x > y, x <= y, x >= y, is, as                                                                                         | Relational and type-testing       |
| 8  | x == y, x != y                                                                                                               | Equality                          |
| 9  | x & y                                                                                                                        | Boolean logical AND               |
| 10 | x ^ y                                                                                                                        | Boolean logical XOR               |
| 11 | x \| y                                                                                                                       | Boolean logical OR                |
| 12 | x && y                                                                                                                       | Conditional AND                   |
| 13 | x \|\| y                                                                                                                     | Conditional OR                    |
| 14 | x ?? y                                                                                                                       | Null-coalescing operator          |
| 15 | c ? t : f                                                                                                                    | Conditional Ternary operator ?:   |
| 16 | x = y, x += y, x -= y, x *= y, x /= y, x %= y, x  &= y, x \|= y, x ^= y, x <<= y, x >>= y, x ??= y, =>                       | Assignment and lambda declaration |


---


## TERNARY OPERATOR

[C# - Ternary Operator ?:](https://www.tutorialsteacher.com/csharp/csharp-ternary-operator)

C# includes a decision-making operator ?: which is called the conditional operator or ternary operator. It is the short form of the if else conditions.

The ternary operator starts with a boolean condition. If this condition evaluates to true then it will execute the first statement after ?, otherwise the second statement after : will be executed.

A ternary operator is short form of if else statement.


**SYNTAX**:
```
condition ? statement 1 : statement 2
```


**EXAMPLE**:
```cs
int x = 20, y = 10;

// a conditional expression x > y returns true, so the first statement after ? will be execute. 
var result = x > y ? "x is greater than y" : "x is less than y";

Console.WriteLine(result);
```
```
x is greater than y
```


---


## NESTED TERNARY OPERATOR

Nested ternary operators are possible by including a conditional expression as a second statement.

**EXAMPLE 1**:
```cs
using System;
					
public class Program
{
	public static void Main()
	{
		int x = 10, y = 100;

		string result = x > y ? "x is greater than y" 
								: x < y ? "x is less than y" 
									: x == y ? "x is equal to y" : "No result";
		
		Console.WriteLine(result);
	}
}
```
```
> x is less than y
```


The ternary operator is right-associative. The expression a ? b : c ? d : e is evaluated as a ? b : (c ? d : e), not as (a ? b : c) ? d : e. 

**EXAMPLE 2**:
```cs
using System;
					
public class Program
{
	public static void Main()
	{
		int x = 5, y = 10, z = 15;

		int result = x * 3 > y ? x : y > z? y : z;
		
		Console.WriteLine(result);
	}
}
```
```
> 5
```