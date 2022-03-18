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
