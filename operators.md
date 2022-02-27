# OPERATORS


---


## DESCRIPTION
Operators are used to perform operations on variables and values.


---


## ARITHMETIC OPERATORS

Operator  |  Name           |  Example
----------|-----------------|--------------------------------------------------
+         |  Addition       |  x + y
-         |  Subtraction    |  x - y
*         |  Multiplication |  x * y
/         |  Division       |  x / y
%         |  Modulus        |  x % y 	# 7 % 2 = 1 (a whole reminder/остаток)
**        |  Exponentiation |  x ** y 	# 2**3 = 2 to the power of 3, степень
//        |  Floor division |  x // y  # 7 // 2 = 3 whole number, целое деление


---


## PYTHON ASSIGNMENT OPERATORS, IN-PLACE OPERATORS
№ | Operator | Example  | Same_As    | Comments
--|----------|----------|------------|---------
1 | `=`      | x = 5    | x = 5      |
2 | `+=`     | x += 3   | x = x + 3  | In-place operator for +
3 | `-=`     | x -= 3   | x = x - 3  |
4 | `*=`     | x *= 3   | x = x * 3  |
5 | `/=`     | x /= 3   | x = x / 3  |
6 | `%=`     | x %= 3   | x = x % 3  | x = the whole reminder, остаток # 10%3 = 1, остаток
7 | `//=`    | x //= 3  | x = x // 3 | x = the whole number after devision # 10//3 = 3, целочисленное деление
8 | `**=`    | x **= 3  | x = 5**3   | x = 125
9 | `&=`     | x &= 3   |            | returns 1
10| `\|=`    | x \|= 3  |            |
11| `^=`     | x ^= 3   |            |
12| `>>=`    | x >>= 3  |            |
13| `<<=`    | x <<= 3  |            |
14| `:=`     | x=1, y=2 |            | Walrus operator assigns values to variables within an expression, including variables that do not exist yet.

**14. `:=` operator example**
```python
num = int(input())
print(num)
is the same as:
print(num:=int(input()))
```


---


## COMPARISON OPERATORS - RATIONAL OPERATORS
№| Operator| Name                     | Example| Comment
-|---------|--------------------------|--------|---------
1| '=='    | Equal                    | x == y | evaluates to True if the items being compared are equal, and False if they are not
2| '!='    | Not equal                | x != y | evaluates to True if the items being compared aren't equal, and False if they are
3| '>'     | Greater than             | x > y  |  
4| '<'     | Less than                | x < y  |  
5| '>='    | Greater than or equal to | x >= y | print("Annie" > "Andy") # returns True because n > d lexologically
6| '<='    | Less than or equal to    | x <= y |  


---


## LOGICAL OPERATOR
№| Operator | Description                                             | Example  
-|----------|---------------------------------------------------------|--
1| and      | Returns True if both statements are true                | x < 5 and  x < 10
2| or       | Returns True if one of the statements is true           | x < 5 or x < 4
3| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10)


---


## MEMBERSHIP OPERATORS
№| Operator | Description                                                                      | Example
-|----------|----------------------------------------------------------------------------------|---------
1| in       | Returns True if a sequence with the specified value is present in the object     | x in y
2| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y


---


## BITWISE OPERATORS
№| Operator | Name                 | Description  
-|----------|----------------------|-------------
1| `&`      | AND                  | Sets each bit to 1 if both bits are 1
2| `\|`     | OR                   | Sets each bit to 1 if one of two bits is 1
3| `^`      | XOR                  | Sets each bit to 1 if only one of two bits is 1
4| `~`      | NOT                  | Inverts all the bits
5| `<<`     | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off
6| `>>`     | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


---


## OPERATOR PRECEDENCE
Highest precedence at top, lowest at bottom.
Operators in the same box evaluate left to right.

Operators                                                                    | Meaning
-----------------------------------------------------------------------------|----------
`(expressions...)`, `[expressions...]`,`{key: value...}`, `{expressions...}` | Binding or parenthesized expression, list display, dictionary display, set display
`x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute`               | Subscription, slicing, call, attribute reference
`await x `                                                                   | Await expression
`()`                                                                         | Parentheses
`**`                                                                         | Exponent
`+x`, `-x`, `~x`                                                             | Unary plus, Unary minus, Bitwise NOT
`*`, `/`, `//`, `%`                                                          | Multiplication, Division, Floor division, Modulus
`+`, `-`                                                                     | Addition, Subtraction
`<<`, `>>`                                                                   | Bitwise shift operators
`&`                                                                          | Bitwise AND
`^`                                                                          | Bitwise XOR
`\|`                                                                         | Bitwise OR
`==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in`             | Comparisons, Identity, Membership operators
`not`                                                                        | Logical NOT
`and`                                                                        | Logical AND
`or`                                                                         | Logical OR
`if – else `                                                                 | Conditional expression
`lambda`                                                                     | Lambda expression
`:=`                                                                         | Assignment expression


---


# IF STATEMENTS LOGIC OPERATIONS
value1 | operator | value2 | result
-------|----------|--------|-----------
True   | and      | True   | v2 (True)
True   | and      | False  | v2 (False)
False  | and      | True   | v1 (False)
False  | and      | False  | v1 (False)

value1 | operator | value2 | result
-------|----------|--------|-----------
True   | or       | True   | v1 (True)
True   | or       | False  | v1 (True)
False  | or       | True   | v2 (True)
False  | or       | False  | v2 (False)
