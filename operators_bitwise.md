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
2| `\|`     | a \| b  | Bitwise OR                 | Sets each bit to 1 if one of two bits is 1
3| `^`      | a ^ b   | Bitwise XOR (exclusive OR) | Sets each bit to 1 if only one of two bits is 1
4| `~`      | ~a      | Tilde. Bitwise NOT         | Unary operand. Inverts all the bits
5| `<<`     | a << n  | Bitwise left shift         | Zero fill left shift. Shift left by pushing zeros in from the right and let the leftmost bits fall off
6| `>>`     | a >> n  | Bitwise right shift        | Signed right shift. Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


---


## 1. `&` Bitwise AND

The bitwise AND operator (&) performs `logical conjunction` on the corresponding bits of its operands. For each pair of bits occupying the same position in the two numbers, it returns a one only when both bits are switched on:

![AND (&)](images/and.gif)

The resulting bit pattern is an `intersection` of the operator’s arguments. It has two bits turned on in the positions where both operands are ones. In all other places, at least one of the inputs has a zero bit.

Arithmetically, this is equivalent to a `product` of two bit values. You can calculate the bitwise AND of numbers a and b by multiplying their bits at every index _i_:

(a & b)<sub>i</sub> = a<sub>i</sub> * b<sub>i</sub>

A one multiplied by one gives one, but anything multiplied by zero will always result in zero. Alternatively, you can take the `minimum` of the two bits in each pair. Notice that when operands have unequal bit-lengths, the shorter one is automatically padded with zeros to the left.


|        	|   	|   	|   	|   	|     |
|---------|---	|---	|---	|---	|---  |
| Input1 	| 0 	| 0 	| 1 	| 1 	| &   |
| Input2 	| 0 	| 1 	| 0 	| 1 	|     |
| Output 	| 0 	| 0 	| 0 	| 1 	|     |


**Example**:
```python
a = 50      # 110010 &
b = 25      # 011001
c = a & b   # 010000
print(c)
print(bin(c))
```
```
> 16
> 0b10000
```


**Example**:
```python
a = 5       #   101 &
b = 25      # 11001
c = a & b   # 00001
print(c)
print(bin(c))
```
```
> 1
> 0b1
```



---



## 2. `\|` BITWISE OPERATOR `OR`

The bitwise OR operator (|) performs `logical disjunction`. For each corresponding pair of bits, it returns a one if at least one of them is switched on:

![OR (|)](images/or.gif)

The resulting bit pattern is a `union` of the operator’s arguments. It has five bits turned on where either of the operands has a one. Only a combination of two zeros gives a zero in the final output.

The arithmetic behind it is a combination of a `sum` and a `product` of the bit values. To calculate the bitwise OR of numbers a and b, you need to apply the following formula to their bits at every index _i_:

(a | b)<sub>i</sub> = a<sub>i</sub> + b<sub>i</sub> - (a<sub>i</sub> * b<sub>i</sub>)
