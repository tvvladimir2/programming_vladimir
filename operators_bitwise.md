# BITWISE OPERATORS


---


## LINKS

[Bitwise Operators in Python (realpython.com)](https://realpython.com/python-bitwise-operators/)


---


## DESCRIPTION

Computers store all kinds of information as a stream of binary digits called bits. Python’s bitwise operators let you manipulate those individual bits of data at the most granular level.

You can use bitwise operators to implement algorithms such as compression, encryption, and error detection as well as to control physical devices in your Raspberry Pi project or elsewhere. Often, Python isolates you from the underlying bits with high-level abstractions. You’re more likely to find the overloaded flavors of bitwise operators in practice. But when you work with them in their original form, you’ll be surprised by their quirks!

You can think of them as functions that take advantage of a more compact prefix and infix syntax.


---


## TABLE

Bitwise operators look virtually the same across different programming languages:

№| Operator | Example | Name                       | Description  
-|----------|---------|----------------------------|-------------
1| `&`      | a & b   | Bitwise AND                | Sets each bit to 1 if both bits are 1
2| `\|`       | a | b   | Bitwise OR                 | Sets each bit to 1 if one of two bits is 1
3| `^`      | a ^ b   | Bitwise XOR (exclusive OR) | Sets each bit to 1 if only one of two bits is 1
4| `~`      | ~a      | Tilde. Bitwise NOT         | Inverts all the bits
5| `<<`     | a << n  | Bitwise left shift         | Zero fill left shift. Shift left by pushing zeros in from the right and let the leftmost bits fall off
6| `>>`     | a >> n  | Bitwise right shift        | Signed right shift. Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


---


## 1. `&` Bitwise AND

Input1 | Operator | Input2   | Output |  
:-----:|:--------:|:--------:|:------:|
0      | &        | 0        | 0      |
0      | &        | 1        | 0      |
1      | &        | 0        | 0      |
1      | &        | 1        | 1      |

```python
a = 50      # 110010
b = 25      # 011001
c = a & b   # 010000
print(c)
```
```
> 16
```
