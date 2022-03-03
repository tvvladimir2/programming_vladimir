# STRING METHODS


---


### LINKS
[String functions at w3schools.com](https://www.w3schools.com/python/python_ref_string.asp)


---

### TABLE

Python has a set of built-in methods that you can use on strings.

|  | Method         | Description                                                                                   |
|--|----------------|-----------------------------------------------------------------------------------------------|
|1 | capitalize()   | Converts the first character to upper case                                                    |
|2 | casefold()     | Converts string into lower case                                                               |
|3 | center()       | Returns a centered string                                                                     |
|4 | count()        | Returns the number of times a specified value occurs in a string                              |
|5 | encode()       | Returns an encoded version of the string                                                      |
|6 | endswith()     | Returns true if the string ends with the specified value                                      |
|7 | expandtabs()   | Sets the tab size of the string                                                               |
|8 | find()         | Searches the string for a specified value and returns the position of where it was found      |
|9 | format()       | Formats specified values in a string                                                          |
|10| format_map()   | Formats specified values in a string                                                          |
|11| index()        | Searches the string for a specified value and returns the position of where it was found      |
|12| isalnum()      | Returns True if all characters in the string are alphanumeric                                 |
|13| isalpha()      | Returns True if all characters in the string are in the alphabet                              |
|14| isascii()      | Returns True if all characters in the string are ascii characters                             |
|15| isdecimal()    | Returns True if all characters in the string are decimals                                     |
|16| isdigit()      | Returns True if all characters in the string are digits                                       |
|17| isidentifier() | Returns True if the string is an identifier                                                   |
|18| islower()      | Returns True if all characters in the string are lower case                                   |
|19| isnumeric()    | Returns True if all characters in the string are numeric                                      |
|20| isprintable()  | Returns True if all characters in the string are printable                                    |
|21| isspace()      | Returns True if all characters in the string are whitespaces                                  |
|22| istitle()      | Returns True if the string follows the rules of a      title                                  |
|23| isupper()      | Returns True if all characters in the string are upper case                                   |
|24| join()         | Converts the elements of an iterable into a string                                            |
|25| ljust()        | Returns a left justified version of the string                                                |
|26| lower()        | Converts a string into lower case                                                             |
|27| lstrip()       | Returns a left trim version of the string                                                     |
|28| maketrans()    | Returns a translation table to be used in translations                                        |
|29| partition()    | Returns a tuple where the string is parted into three parts                                   |
|30| replace()      | Returns a string where a specified value is replaced with a specified value                   |
|31| rfind()        | Searches the string for a specified value and returns the last position of where it was found |
|32| rindex()       | Searches the string for a specified value and returns the last position of where it was found |
|33| rjust()        | Returns a right justified version of the string                                               |
|34| rpartition()   | Returns a tuple where the string is parted into three parts                                   |
|35| rsplit()       | Splits the string at the specified separator, and returns a list                              |
|36| rstrip()       | Returns a right trim version of the string                                                    |
|37| split()        | Splits the string at the specified separator, and returns a list                              |
|38| splitlines()   | Splits the string at line breaks and returns a list                                           |
|39| startswith()   | Returns true if the string starts with the specified value                                    |
|40| strip()        | Returns a trimmed version of the string                                                       |
|41| swapcase()     | Swaps cases, lower case becomes upper case and vice versa                                     |
|42| title()        | Converts the first character of each word to upper case                                       |
|43| translate()    | Returns a translated string                                                                   |
|44| upper()        | Converts a string into upper case                                                             |
|45| zfill()        | Fills the string with a specified number of 0 values at the beginning                         |


---


## 4. COUNT( ) string method
The count() method returns the number of occurrences of a substring in the given string.

```python
message = 'python is popular programming language'
print('Number of occurrence of p:', message.count('p')) # Output: Number of occurrence of p: 4
```


---


## 6. ENDSWITH( ) string method

The `endswith()` method returns `True` if the string ends with the specified value, otherwise False.

`string_endswith_syntax = string.endswith(value, start, end)`

| Parameter |                              Description                              |
|:---------:|:---------------------------------------------------------------------:|
| value     | Required. The value to check if the string ends with                  |
| start     | Optional. An Integer specifying at which position to start the search |
| end       | Optional. An Integer specifying at which position to end the search   |

**Example**: Check if index position 5 to 11 ends with the phrase "my world.":
```python
txt = "Hello, welcome to my world. Tom"
x = txt.endswith("my world.", 5, 27)
y = txt.endswith("my world.", 5, 29)
print(txt[5:27])
print(txt[5:29])
print(x)
print(y)
```
```
> , welcome to my world.
> , welcome to my world. T
> True
> False
```


---


## 24. JOIN METHOD

The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.

`string_join_syntax = string.join(iterable)`

| Parameter |                               Description                               |
|:---------:|-------------------------------------------------------------------------|
| iterable  | Required. Any iterable object where all the returned values are strings |

**Example 1**: x = string1 + string2 + string3 = "string1, string2, string 3"
```python
x = ", ".join(["spam", "eggs", "ham"])
print(x)
# prints "spam, eggs, ham"
```

**Example 2**: Join all items in a dictionary into a string, using a the word "TEST" as separator.
```python
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)
print(x)
```
```
> nameTESTcountry
```


---


## 26. LOWER( ) string method

The lower() method returns a string where all characters are lower case.
Symbols and Numbers are ignored.

`strint_lower_syntax = string.lower(no parameters)`

```python
txt = 'I\'m Igor Bibor'
print(txt.lower())  # lower() method returns the string in lower case:
print("AN ALL CAPS SENTENCE".lower()) # returns: an all caps sentence
```
```
> i'm igor bibor
> an all caps sentence
```


---


## 30. REPLACE( ) string method

The replace() method replaces a specified phrase with another specified phrase.
Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

`string_replace_syntax = string.replace(oldvalue, newvalue, count)`

| Parameter |                                                        Description                                                       |
|:---------:|--------------------------------------------------------------------------------------------------------------------------|
| oldvalue  | Required. The string to search for                                                                                       |
| newvalue  | Required. The string to replace the old value with                                                                       |
| count     | Optional. A number specifying how many occurrences of the old value you      want to replace. Default is all occurrences |

```python
txt = "Hello, World!"
print(txt.replace("l", "b")) # Replaces all 'l' to 'b' letters
print(txt.replace("Hello", "Good morning"))
```
```
> Hebbo, Worbd!
> Good morning, World!
```


---


## 37. SPLIT( ) string method

Split string into strings, turns it into a list
"string1" >> list

```python
txt = "Hello, World!"
print(a.split(",")) # split() method splits the string into substrings if it finds instances of the separator ','
#returns ['Hello', ' World!']
```


---


### 39. STARTSWITH( ) string method

The `startswith()` method returns `True` if the string starts with the specified value, otherwise False.

`string_syntax = string.startswith(value, start, end)`

| Parameter | Description                                                           |
|:---------:|:---------------------------------------------------------------------:|
| value     | Required. The value to check if the string starts with                |
| start     | Optional. An Integer specifying at which position to start the search |
| end       | Optional. An Integer specifying at which position to end the search   |

**Example**: Check if position 7 to 20 starts with the characters "wel":

```python
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)
```
```
> True
```


---


## 40. STRIP( ) string method
REMOVE DELETE WHITESPACE

```python
txt = "Hello, World!"
print(txt.strip())    # strip() method removes any whitespace from the beginning or the end:
```


---


## 44. UPPER( ) string method

The `upper()` method returns a string where all characters are in upper case.
Symbols and Numbers are ignored.

`string_upper_syntax = string.upper(no parameters)`

```python
txt = "Hello, World!"
print(txt.upper())  # upper() method returns the string in upper case
print("This is a sentence.".upper()) # returns: THIS IS A SENTENCE.
```
```
> HELLO, WORLD!
> THIS IS A SENTENCE.
```
