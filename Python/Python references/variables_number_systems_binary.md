# BINARY SYSTEM

People naturally favor the base-ten numeral system, also known as the decimal system, because it plays nicely with counting on fingers. A `denary number` is a number in the base 10, or decimal, system.

Computers, on the other hand, treat data as a bunch of numbers expressed in the base-two numeral system, more commonly known as the binary system. Such numbers are composed of only two digits, zero and one.

Electronic devices use different voltage levels. By employing only two states, you make the system more reliable and resistant to noise.


---


## BINARY CONVERSION

| Power of base      | 2**7  | 2**6 | 2**5 | 2**4 | 2**3 | 2**2 | 2**1 | 2**0 |       |
|--------------------|-------|------|------|------|------|------|------|------|-------|
| Denary number      | 128   | 64   | 32   | 16   | 8    | 4    | 2    | 1    | = 255 |


**Example**:

```python
print(bin(75))            # Integer to a binary
print(int(0b1001011))     # The "0b" is a prefix to denote that the number is in binary.
print(int(1001011))       # Python sees this as an integer
```
```
> 0b1001011
> 75
> 1001011
```


---

## CREATE BINARY

```python
# 1. Interpret binary string to integer.
x = int('10101010', 2)      # > 170

# 2.
x = 0b10101010              # > 170, Python automatically makes it it an integer.
```



---


## BINARY to DECIMAL

**Example**: Convert binary number 10111 to its decimal form.

10111 = (10111)<sub>2</sub> =

= (1 × 2<sup>4</sup>) + (0 × 2<sup>3</sup>) + (1 × 2<sup>2</sup>) + (1 × 2<sup>1</sup>) + (1 × 2<sup>0</sup>)

= (1 × 16) + (0 × 8) + (1 × 4) + (1 × 2) + (1 × 1)

= 16 + 0 + 4 + 2 + 1

= 23 = 23<sub>10</sub>


---


## DECIMAL to BINARY


---

**Example**: Convert decimal number 165 to binary.

| Power of base          | 2**7  | 2**6 | 2**5 | 2**4 | 2**3 | 2**2 | 2**1 | 2**0 | Remainder |
|------------------------|-------|------|------|------|------|------|------|------|           |
| Denary number          | 128   | 64   | 32   | 16   | 8    | 4    | 2    | 1    |           |
| Magnituge of each term | 128   |      |      |      |      |      |      |      | = 37      |
| Magnituge of each term |       |      | 32   |      |      |      |      |      | = 5       |
| Magnituge of each term |       |      |      |      |      | 4    |      |      | = 1       |
| Magnituge of each term |       |      |      |      |      |      |      | 1    | = 1       |
| Binary number          | 1     | 0    | 1    | 0    | 0    | 0    | 0    | 1    |           |

165 = 165<sub>10</sub> = 10100001 = 10100001<sub>2</sub>


---


## DECIMAL POINT

| Binary number          | 1  | 1  | 1  | . | 1   | 0   | 1    | 1     | Decimal number |
|------------------------|----|----|----|---|-----|-----|------|-------|----------------|
| Power of base          | 22 | 21 | 20 |   | 2-1 | 2-2 | 2-3  | 2-4   |                |
| Decimal equivalent     | 4  | 2  | 1  |   | .5  | .25 | .125 | .0625 |                |
| Magnitude of each term | 4  | 2  | 1  |   | .5  | 0   | .125 | .0625 | 7.6875         |

**Example**:
```python
print(int(0b111.1011))
```
```
> TypeError: 'float' object cannot be interpreted as an integer
```


---


## BINARY COMPLEMENTS

8 bit system only supports decimal numbers up to 255.
If we use 8 bit system, then we can record number higher numbers as:

256<sub>10</sub> = 00000001 00000000

**Example**: Binary signed 2's complement

```python
print(bin(256))
```
```
> 0b100000000
```


---


## NEGATIVE BINARY NUMBERS

```python
print(bin(-256))
```
```
> -0b100000000
```


---
