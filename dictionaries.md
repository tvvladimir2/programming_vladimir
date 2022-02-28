# Python Dictionary


---


## LINKS

**Programiz video link:** [https://youtu.be/_4wOvc-vt4k](https://youtu.be/_4wOvc-vt4k)
**Dictionaries at RealPython.com** [https://realpython.com/python-dicts/](https://realpython.com/python-dicts/)


---


## DESCRIPTION
- A dictionary is a collection of key/value pairs, data structures used to map arbitrary keys to values.
- It is similar to associative arrays in other programming languages.


---


## STRUCTURE SYNTAX
mydictionary  = {key1:value1, key2:value2, key3:value3}


---


## CREATE DISCTIONARIES
To create a dictionary, we put the key/value pairs separated by a colon `:` inside the curly braces `{}`.

**Example 1**: simple
```python
peopleList = {}                               # Create an empty list
peopleList = {"name": "Linus",
              "age": 21}     # Create a list with two values
print(peopleList)
```
```
>> {"name": "Linus", "age": 21}
```

|Key    |Value   |
|-------|--------|
|"name" |"Linus" |
|"age"  |21      |

**Notes:**
- Keys of a dictionary can be any immutable objects like numbers, strings and tuples. However, they cannot be objects that can be modified like lists.
- Keys must be unique for identification.

**Example 2**:
```python
pairs = {1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
```
```
> [2, 3, 4]
> None
> not in dictionary
```

**Example 3**:
```python
fib = {1: 1, 2: 1, 3: 2, 4: 3}

print(fib.get(4, 0) + fib.get(7, 5))
```
```
> 8
```


## Allowed `Key` types in dictionaries

|Key         | allowed? | comment
|------------|----------|---------
| integer    | yes      |
| float      | yes      |
| string     | yes      |
| boolean    | yes      |
| list       | no       | Are mutable
| dictionary | no       | Are mutable


---


## ACCESS DICTIONARY ELEMENTS - INDEXATION

**Call elements:**
Dictionaries are optimized to get values when the key is known.
Similar to numbered indexes like `0`, `1`, `2` to get elements from sequences like lists and tuples, keys are used as indices for dictionaries.

```python
person1 = {"name": "Linus", "age": 21}
print(person1["name"])
print(person1["age"])
```
```
>> Linus
>> 21
```

**Call a key in an empty dictionary:**
Can not index elements in an empty dictionary.

```python
mydictionary = {}
print(mydictionary[0])  # Such index does not exists
```
```
>> KeyError
```

**A key not in list:**
If we try to access a key that is not in the dictionary, we will get `KeyError`.

```python
person1 = {"name": "Linus", "age": 21}
print(person1["hobbies"])
```
```
>> Traceback (most recent call last):
>>  File "<string>", line 2, in <module>
>> KeyError: 'hobbies'
```

**Check a key in list with get( ) method:**
Sometimes instead of getting this `KeyError` error, we may just want to know if the key exists or not and decide what to do based on it.
If the key is not found in the dictionary `get()` returns another specified value instead ('None', by default).

```python
person1 = {"name": "Linus", "age": 21}
print(person1.get("namr"))
print(person1.get("hobbies"))
```
```
>> Linus
>> None
```

Instead of an error, we get `None` which denotes empty or no value. This value can be used with `if` statement to make different decision as per the need.


**Check secondary a key in list with get( ) method:**
We can also pass a second default argument to the `get()` method that will be returned instead of `None` if the key is not found.

```python
person1 = {"name": "Linus", "age": 21}
print(person1.get("hobbies", ["dancing", "fishing"]))
print(person1.get("hobbies", "key not found"))
```
```
>> ["dancing", "fishing"]
```


---


## ADD AND CHANGE DICTIONARY ELEMENTS

```python
person1 = {"name": "Linus", "age": 21}
# changing existing keys
person1["name"] = "Dennis"
print(person1)
# adding new keys
person1["hobbies"] = ["dancing", "fishing"]
print(person1)
```
```
>> {'name': 'Dennis', 'age': 21}
>> {'name': 'Dennis', 'age': 21, 'hobbies': ['dancing', 'fishing']}
```


---


## REMOVE ELEMENTS FROM DICTIONARY
To remove an item from the dictionary, we can use the dictionary's `pop()` method. The `pop()` method also returns the value of the removed key. For example,

```python
person1 = {"name": "Linus", "age": 21}
print(person1.pop("name"))
print(person1)
```
```
>> Linus
>> {"age": 21}
```


---


## ITERATING THROUGH A DICTIONARY

Similar to sequences, we can easily iterate through items of a dictionary by using a `for` loop. We get one key in every iteration:

```python
person1 = {"name": "Linus", "age": 21}
for key in person1:
   print(key)
   print(person1[key])
```
```
>> name
>> Linus
>> age
>> 21
```

>**Note:** Starting from Python 3.7, the order of items in a dictionary is preserved. So when we iterate through a dictionary, we get the keys in the order in which they are inserted in the dictionary.


---


## CHECK IF KEY IS IN DICTIONARY
To determine whether a `key` is in a `dictionary`, you can use `in` and `not in`, just as you can for a list.
```python
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
```
```
> True
> False
> True
```


---


## PROGRAMMING TASK
**Can you guess the output of this program?**

```python
synonyms = {"mountain": "peak", "forest": "jungle"}
print("1.", synonyms["mountain"])
synonyms["terrain"] = "land"
print("2.", synonyms)
synonyms.pop("forest")
print("3.", synonyms)
```
```
>> 1. peak
>> 2. {'mountain': 'peak', 'forest': 'jungle', 'terrain': 'land'}
>> 3. {'mountain': 'peak', 'terrain': 'land'}
```
