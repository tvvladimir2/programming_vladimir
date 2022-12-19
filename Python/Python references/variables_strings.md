# STRINGS


---


## DESCRIPTION

Strings are also lists.


---


## CREATE STRINGS

```python
print("Hello")        # single quotation marks
print('Hello')        # double quotation marks
```



---



## STRUCTURE & SYNTAX

`string_name = list(charachter indexes)`
`string_name = 'list.index[0], list.index[1], list.index[2], list.index[3]'`
`string_name = "[-7], [-6], [-5], [-4], [-3], [-2], [-1]"`
`string_name = "[0], [1], [2], [3], [4], [5], [6]"`



---



## MULTILINE STRING

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# is the same as
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
```


---


## STRINGS AS ARRRAYS - INDEXING STRINGS

- Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
- However, Python does not have a character data type, a single character is simply a string with a length of 1.
- Square brackets can be used to access elements of the string.

```python
mystring = "Hello, World!"
print(mystring[1]) #Get the character at position 1 (remember that the first character has the position 0):
```
```
> e
```



---



## LOOPING THROUGH A STRING USING FOR( ) LOOP

```python
for x in "banana":
  print(x)
```
```
b
a
n
a
n
a
```



---



## LEN ( ), STRING LENGTH

```python
txt = "Hello, World!"
print(len(txt))   # len() function returns the length of a string:
```


---



## `IN` / `NOT IN`

Check if object is in a string

```python
txt = "The best things in life are free!"

print("free" in txt)    # Check if "free" is present in the following text:

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```
```
True
No, 'expensive' is NOT present.
```



---



## STRING SLICING

```python
txt = "Hello, World!"
print(txt[1::]) # Get the characters from position 2 to position 5 (not included):
print(txt[1::2]) # Get the characters from position 2 to position 5 (not included):
print(txt[:5])  # from 0 to 5
print(txt[5:])  # from 5 to the end
print(txt[-5:-2]) # Use negative indexes to start the slice from the end
print(txt[-5:-2:3]) # Use negative indexes to start the slice from the end
```
```
> ello, World!
> el,Wrd
> Hello
> , World!
> orl
> o
```



---



## CONCENRATE STRINGS

Add strings together
```python
a = "Hello"
b = "World"
c = a + " " + b # To add a space between them, add a " ":
print(c)
```
```
> Hello World
```



---



## FORMAT STRING

Use the format() method to insert numbers into strings

**Example 1**:
```python
age = 36
myorder = "I want {} pieces of item {} for {} dollars."             # Use placeholders
print(myorder.format(age, '5', 'price'))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."   # Use index numbers {0} for correct placeholders
print(myorder.format(age, '5', 'price'))
```
```
> I want 36 pieces of item 5 for price dollars.
> I want to pay price dollars for 36 pieces of item 5.
```


**Example 2**:
```python
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
```
```
Numbers: 4 5 6
```


**Example 3**:
```python
print("{0}{1}{0}".format("abra", "cad"))
print(a)
```
```
> abracadabra
```


**Example 4**:
```python
a = "{x}, {y}".format(x=5, y=12)              # Name placeholders
print(a)
```
```
> 5, 12
```



---



## ESCAPE CHARACHTERS

```python
txt = "We are the so-called \"Vikings\" from the north."    #use the escape character \" to escape problems
```

Charachter | Description
-----------|------------
\n         | New Line
\'         | Single Quote
\\         | Backslash
\r 	       | Carriage Return
\t 	       | Tab                
\b 	       | Backspace
\f 	       | Form Feed
\ooo 	     | Octal value
\xhh 	     | Hex value

**Example**: `Print()`
```python
for i in range(5):
    for y in range(5):
        print('Hello', end="\t")
    print(end="\n")
```
```
> Hello   Hello   Hello
> Hello   Hello   Hello
> Hello   Hello   Hello
```

**Example**: Escape ' character
```python
a = 'Бабка \'Папка\' ходит \t на \bногах'
print(a)
```
```
> Бабка 'Папка' ходит      наногах
```



---



## MAX ITEM IN A LIST

string is also a list, we use a list method
outputs the max number in a list
alphabet: "a" is min, "z" is max

```python
msg = "Hello"
print(msg.max()) # returns "o"
```
