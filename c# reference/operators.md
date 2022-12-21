## C# OPERATORS


---


## DESRIPTION

Operators in C# are some special symbols that perform some action on operands. In mathematics, the plus symbol (+) do the sum of the left and right numbers. In the same way, C# includes various operators for different types of operations.

The following example demonstrates the + operator in C#.


---


## UNARY vs BINARY OPERATORS

There are two types of operators in C#, `Unary` operators and `Binary` operators.
 - Unary operators act on single operand.
 - Binary operators act on two operands (left-hand side and right-hand side operand of an operator).


---


## ARITHMETIC OPERATORS

The arithmetic operators perform arithmetic operations on all the numeric type operands such as sbyte, byte, short, ushort, int, uint, long, ulong, float, double, and decimal.

| # |   Operator  |       Name      |                                 Description                                 |     Example     |
|---|:-----------:|-----------------|-----------------------------------------------------------------------------|-----------------|
| 1 | +           | Addition        | Computes the sum of left and right operands.                                | int x = 5 + 5;  |
| 2 | -           | Subtraction     | Subtract the right operand from the left operand                            | int x = 5 - 1;  |
| 3 | *           | Multiplication  | Multiply left and right operand                                             | int x = 5 * 1;  |
| 4 | /           | Division        | Divides the left operand by the right operand                               | int x = 10 / 2; |
| 5 | %           | Reminder        | Computes the remainder after dividing its left operand by its right operand | int x = 5 % 2;  |
| 6 | ++          | Unary increment | Unary increment ++ operator increases its operand by 1                      | x++             |
| 7 | --          | Unary decrement | Unary decrement -- operator decreases its operand by 1                      | x--             |
| 8 | +           | Unary plus      | Returns the value of operand                                                | +5              |
| 9 | -           | Unary minus     | Computes the numeric negation of its operand.                               | -5              |


---


## ASSIGNMENT OPERATORS

The assignment operator = assigns its right had value to its left-hand variable, property, or indexer. It can also be used with other arithmetic, Boolean logical, and bitwise operators.

| # | Operator |            Name            |                                        Description                                        |  Example |
|---|:--------:|:--------------------------:|:-----------------------------------------------------------------------------------------:|:--------:|
| 1 | =        | Assignment                 | Assigns its right had value to its left-hand variable, property or indexer.               | x = 10;  |
| 2 | x op= y  | Compound assignment        | Short form of x =x op y where op = any arithmetic, Boolean logical, and bitwise operator. | x += 5;  |
| 3 | ??=      | Null-coalescing assignment | C# 8 onwards, ??= assigns value of the right operand only if the left operand is null     | x ??= 5; |


---


## COMPARISON OPERATORS

Comparison operators compre two numeric operands and returns true or false. 

| # | Operator |                                   Description                                   | Example |
|---|:--------:|:-------------------------------------------------------------------------------:|:-------:|
| 1 | <        | Returns true if the right operand is less than the left operand                 | x < y;  |
| 2 | >        | Returns true if the right operand is greater than the left operand              | x > y;  |
| 3 | <=       | Returns true if the right operand is less than or equal to the left operand     | x <= y  |
| 4 | >=       | Returns true if the right operand is greater  than or equal to the left operand | x >= y; |


---


## EQUALITY OPERATORS

The equality operator checks whether the two operands are equal or not. 

| # | Operator |                       Description                       | Example |
|---|:--------:|:-------------------------------------------------------:|:-------:|
| 1 | ==       | Returns true if operands are equal otherwise false.     | x == y; |
| 2 | !=       | Returns true if operands are not equal otherwise false. | x != y; |


---


## BOOLEAN LOGICAL OPERATORS

The Boolean logical operators perform a logical operation on bool operands. 

| # | Operator |                                                     Description                                                    |  Example  |
|---|:--------:|:------------------------------------------------------------------------------------------------------------------:|:---------:|
| 1 | !        | Reverses the bool result of bool expression.  Returns false if result is true and returns true if result is false. | !false    |
| 2 | &&       | Computes the logical AND of its bool operands.  Returns true both operands are true, otherwise returns false.      | x && y;   |
| 3 | \|\|     | TWO SLASHESComputes the logical OR of its bool operands. Returns true when any one operand is true.                | x \|\| y; |


---


## OPERATOR EVALUATION & PRECEDENCE

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


# POINTER RELATED OPERATORS

[Pointer related operators (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/pointer-related-operators)


---


## TYPE-TESTING OPERATORS & CAST EXPRESSION

[Type-testing operators and cast expression (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/type-testing-and-cast)


---


## MEMBER ACCESS OPERATORS & EXPRESSION

[Member access operators and expressions (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/member-access-operators)


---


## BITWISE & SHIFT OPERATORS

[Bitwise and shift operators (C# reference)](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators)


---