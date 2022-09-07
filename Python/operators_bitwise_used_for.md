# WHAT `BITWISE OPERATORS` ARE USED FOR


---


## LINKS

[Bitwise Operators in Python - Tutorial & Application Fields](https://www.youtube.com/watch?v=i1wQOiljBvY)


---


## 1. FLAGS - permissions


---


### `&` BITWISE OPERATOR `AND`

**Example**: Permissions for file reading

```python
# Permissions:
# Read, Write, Execute, Change policy

# People permissions
person1 = 0b1000      # True, False, False, False
person2 = 0b1110
person3 = 0b1111
person4 = 0b1010
person5 = 0b1101

# What is the least powerful permission that they all have in common?
# What anyone of them can do? Common permission across all of them.
together1 = person1 & person2 & person3 & person4 & person5
print(bin(together1))
```
```
> 0b1000
```


**Example**: Permissions for file reading

```python
# Permissions:
# Read, Write, Execute, Change policy

# People permissions
person1 = 0b1000
person2 = 0b1110
person3 = 0b1111
person4 = 0b1010
person5 = 0b0101  # Different from Example 1

# What is the least powerful permission that they all have in common?
# What anyone of them can do? Common permission across all of them.
together1 = person1 & person2 & person3 & person4 & person5
print(bin(together1))
```
```
> 0b0     # None
```


**Example**: Check if the numbers are even or odd

```python
some_number = 345345

print(bin(some_number))         # 0b1010100010100000001
print(bin(some_number & 1))     # 0b1

if some_number & 1 == 0:
  print('Even')
else:
  print('Odd')
```
```
> Odd
```


---


### `|` BITWISE OPERATOR `OR`

**Example**: Permissions for file reading

```python
# Permissions:
# Read, Write, Execute, Change policy

# People permissions
person1 = 0b1000      # True, False, False, False
person2 = 0b0000
person3 = 0b1000
person4 = 0b1010
person5 = 0b1111

# If at least one of the people has a permission, all will have a permission.
together1 = person1 | person2 | person3 | person4 | person5
print(bin(together1))
```
```
> 0b1111
```



**Example**: Check if the user is allowed to do something.

```python
NEURAL_READ = 0b1000
NEURAL_WRITE = 0b0100
NEURAL_EXEC = 0b0010
NEURAL_CHANGE = 0b0001

def myfunction(permission):
  print(bin(permission))

# Combine permissions into one full permission
myfunction(NEURAL_WRITE | NEURAL_READ)
```
```
> 0b1100
```


---


## `^` Bitwise XOR Operator (exclusive OR)

**Example**: Swap the values of two variables without needing a placeholder.

```python
a = 10
b = 20

a,b = b,a
print('a =', a)
print('b =', b)
```
```python
a = 10            # 01010
b = 20            # 10100

# Indicate where `a` & `b` were different at the beginning.
a ^= b            # 11110
b ^= a            # 01010
a ^= b            # 10100

print('a =', a)
print('b =', b)
```


---


## `>>` Bitwise RIGHT SHIFT operator

**Example**: Division by 2

```python
x = 56              # 56 = 0b111000
y = x

# Simple method
x = x/2
print(x)

x = y

# Bitwise method
x = x >> 1          # 0b11100 = 28
print(x)
```
```
> 28.0
> 28
```


---
