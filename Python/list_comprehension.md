# LISTS COMPREHENSION


---


## STRUCTURE - SYNTAX

`list_variable` = `[mapping-expression for element in source-list if filter-expression]`

```python
list = [print(x) for x in thislist]
list = [x for x in fruits if "a" in x]
list = [i**3 for i in range(5)]
list = [i**2 for i in range(10) if i**2 % 2 == 0]
```


---


## CREATE LIST FROM A LIST

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```
```
> ['apple', 'banana', 'mango']
```


---


# PRINT( ) USING LIST COMPREHENSION
```python
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]    #A short hand 'for' loop that will print all items in a list:
print([x[0] for x in thislist])
```
```
> apple
> banana
> cherry
> ['a', 'b', 'c']
```


---


## CREATE A LIST WITH RANGE( ) METHOD

```python
mylist = [i**3 for i in range(5)]
print(mylist)
```
```
> [0, 1, 8, 27, 64]
```


---
