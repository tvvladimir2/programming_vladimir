# SETS


---


## DESCRIPTION

Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is:
- unordered, so you cannot be sure in which order the items will appear. Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
- unchangeable, but you can remove items and add new items.
- unindexed
- unique, do not allow duplicate values
- heterogeneous, can contain data of any type

When to use sets:
- Use a set if you need uniqueness for the elements.


---


## CREATE

Sets are written with curly brackets.

```python
# 1. Simple
my_set = {"apple", "banana", "cherry"}
print('1. ', my_set)

# 2. int, string, float, complex, list, bool,
my_set_types = {20, 'Vladimir', 12.34, (2 + 3j), True}
print('2. ', my_set_types)

# 3. Use `set()` constructor from a Tuple
my_set_tuple = set(("apple", "banana", "cherry")) # note the double round-brackets
print('3. ', my_set_tuple)

# 4. Use `set()` constructor from a List
my_set_list = set(["apple", "banana", "cherry"]) # note the double round-brackets
print('4. ', my_set_list)
```
```
> 1. {'cherry', 'apple', 'banana'}
> 2. {True, 20, 'Vladimir', (2+3j), 12.34}
> 3. {'cherry', 'apple', 'banana'}
> 4. {'cherry', 'apple', 'banana'}
```



---



## DUPLICATE ITEMS IGNORED

Word `apple` is written twice and thus it is ignored the second time.

```python
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
```
```
{'apple', 'cherry', 'banana'}
```



---



## `IN` KEYWORD

**Example 1**: Check if the item is in a set

```python
num_set = {1, 2, 3, 4, 5}
print(3 in num_set)
```
```
> True
```


**Example 2**: `IF` & `IN` combination
```python
letters = {"a", "b", "c", "d"}

if "e" not in letters:
  print(1)
else:
  print(2)
```
```
> 1
```



---



## SETS vs LISTS

Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.



---



## ACCESS ELEMENTS IN A LIST

**Acces first letter of the first item**:
```python
strs = ["flower","flow","flight"]
prefix = ""
print(strs[0][0])
```
```
> f
```