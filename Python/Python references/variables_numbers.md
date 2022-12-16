# PYTHON: NUMBERS


---


# NUMERIC DATA TYPES

| Numeric Data Types | Example  | Description                                                                                           |
|--------------------|----------|-------------------------------------------------------------------------------------------------------|
| int                | x = 20   | Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.      |
| float              | x = 20.5 | Float, or "floating point number" is a number, positive or negative, containing one or more decimals. |
| complex            | x = 1j   | Complex numbers are written with a "j" as the imaginary part:                                         |


---


## BASIC ARITHMETICS

**Substraction and addition**:
```python
print(1 + 2)
print(1.0 + 2)
print(5-1)
print(2--1)
print(2 - (-1))
```
```
> 3
> 3.0
> 4
> 3
> 3
```


**Multiplication and devision**:
```python
print(3 * 3)
print(27 / 3)
print(27.0 / 3)
print(int(27.3 / 3))    # int() discards any fractional part of the number
```
```
> 9
> 9.0
> 9.0
> 9
```


**Division by 0**:
```python
print(1 / 0)
```
```
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ZeroDivisionError: division by zero
```


**Raise a number to the power**:
```python
print(3 ** 2)
print(3 ** 2.0)
print(81 ** 0.5)
print(2 ** -1)
print(2 ** -2)
```
```
> 9
> 9.0
> 9.0
> 0.5
> 0.25
```


**Integer division**:

The // operator first divides the number on the left by the number on the right and then rounds down to an integer.

```python
print(9 // 3)
print(5.0 // 2) # returns a floating-point number when one of the operands is a float.
print(5 // 2)
print(-3 // 2)  # First, -3 is divided by 2 to get -1.5. Then -1.5 is rounded down to -2.
```
```
> 3
> 2.0
> 2
> -2
```

**Modulus operator**:

The % operator, or the modulus, returns the remainder of dividing the left operand by the right operand:

```python
print(5 % 3)
print(20 % 7)
print(16 % 8)

# equation used: r = x - (y * (x // y))
print(5 % -3)   # Since 5 / -3 is about -1.67, that means 5 // -3 is -2. Now Python multiplies that by -3 to get 6. Finally, Python subtracts 6 from 5 to get -1.
print(-5 % 3)
print(-5 % -3)
```
```
> 2
> 6
> 0
> -1
> 1
> -2
```

```python
print(1 % 0)    # 1 % 0 gives the remainder of dividing 1 by 0. But you can’t divide 1 by 0
```
```
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ZeroDivisionError: integer division or modulo by zero
```


---


## ARITHMETIC EXPRESSIONS

You can combine operators to form complex expressions. An `expression` is a combination of numbers, operators, and parentheses that Python can compute, or evaluate, to return a value.

Order of operations is the same as in arithmetics.
See `operator precedence` to know more.

```python
print(2*3 - 1)
print(4/2 + 2**3)
print(-1 + (-3*2 + 4))
```
```
> 5
> 10.0
> -3
```


---


## FLOATING-POINT REPRESENTATION ERROR

Floating-point representation has nothing to do with Python. It’s related to the way floating-point numbers are stored in a computer’s memory.

```python
# Python adds together the binary approximations for 0.1 and 0.2, which gives a number that is not the binary approximation for 0.3.
print(0.1 + 0.2)
```
```
> 0.30000000000000004   
```

The number `0.1` can be represented as the fraction `1/10`. Both the number 0.1 and its fraction 1/10 are `decimal representations`, or `base-10 representations`. Computers, however, store floating-point numbers in `base-2 representation`, more commonly called `binary representation`.

When represented in binary, something familiar yet possibly unexpected happens to the decimal number 0.1. `The fraction 1/3 has no finite decimal representation`. That is, `1/3 = 0.3333...` with infinitely many 3s after the decimal point. The same thing happens to the fraction 1/10 in binary.

The binary representation of 1/10 is the following infinitely repeating fraction:

```
0.00011001100110011001100110011...
```

Computers have finite memory, so the number 0.1 must be stored as an approximation and not as its true value. The approximation that gets stored is slightly higher than the actual value and looks like this:

```
0.1000000000000000055511151231257827021181583404541015625
```

You may have noticed, however, that when asked to print 0.1, Python prints 0.1 and not the approximated value above:

```python
print(0.1)
```
```
> 0.1
```

Python doesn’t just chop off the digits in the binary representation for 0.1. What actually happens is a little more subtle.

Because the approximation of 0.1 in binary is just that—an approximation—it’s entirely possible that more than one decimal number has the same binary approximation.

For example, both 0.1 and 0.10000000000000001 have the same binary approximation. Python prints out the shortest decimal number that shares the approximation.

This explains why, in the first example of this section, 0.1 + 0.2 doesn’t equal 0.3. Python adds together the binary approximations for 0.1 and 0.2, which gives a number that is not the binary approximation for 0.3.

If all this is starting to make your head spin, don’t worry! Unless you’re writing programs for finance or scientific computing, you don’t need to worry about the imprecision of floating-point arithmetic.


---


