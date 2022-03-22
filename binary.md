# BINARY SYSTEM

People naturally favor the base-ten numeral system, also known as the decimal system, because it plays nicely with counting on fingers. A `denary number` is a number in the base 10, or decimal, system.

Computers, on the other hand, treat data as a bunch of numbers expressed in the base-two numeral system, more commonly known as the binary system. Such numbers are composed of only two digits, zero and one.

Electronic devices use different voltage levels. By employing only two states, you make the system more reliable and resistant to noise.


---


## BINARY CONVERSION

| Power of base      | 2**7  | 2**6 | 2**5 | 2**4 | 2**3 | 2**2 | 2**1 | 2**0 |       |
|--------------------|-------|------|------|------|------|------|------|------|-------|
| Denary number      | 128   | 64   | 32   | 16   | 8    | 4    | 2    | 1    | = 255 |

The "0b" is a prefix to denote that the number is in binary.

|         | prefix | Interpretation | Base | Example |
|---------|--------|----------------|------|---------|
| Base 2  | 0b, 0B | Binary         | 2    | 0b1010  |  
| Base 8  | 0o, 0O | Octal          | 8    | 0o100   |
| Base 16 | 0x, 0X | Hexidecimal    | 16   | 0xff112 |


Max. number = 0b11111111 = 255 = (11111111)<sub>2</sub>

Min. number = 0b00000000 = 0

**Example**: Binary signed 2's complement
256 = 00000001 00000000

**Example**:

1011012 = (1 × 2<sup>5</sup>) + (0 × 2<sup>4</sup>) + (1 × 2<sup>3</sup>) + (1 × 2<sup>2</sup>) + (0 × 2<sup>1</sup>) + (1 × 2<sup>0</sup>) = 32 + 0 + 8 + 4 + 0 + 1 = 45<sub>10</sub>
