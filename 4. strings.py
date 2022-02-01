# STRINGS

# Strings are also lists
# Each letter has an index [0], [1], [2] ...

#Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
# is the same as
print('Hello')

# Multiline string:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# is the same as
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

# STRINGS AS ARRRAYS - INDEXING STRINGS
# - Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# - However, Python does not have a character data type, a single character is simply a string with a length of 1.
# - Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1]) #Get the character at position 1 (remember that the first character has the position 0):

# LOOPING THROUGH A STRING
for x in "banana":
  print(x)

# STRING LENGTH
txt = "Hello, World!"
print(len(txt))   # len() function returns the length of a string:

# CHECK STRING
txt = "The best things in life are free!"
print("free" in txt)    # Check if "free" is present in the following text:
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# SLICE STRINGS
txt = "Hello, World!"
print(txt[2:5]) # Get the characters from position 2 to position 5 (not included):
print(txt[:5])  # from 0 to 5
print(txt[5:])  # from 5 to the end
print(txt[-5:-2]) # Use negative indexes to start the slice from the end

# CONCENRATE / COMBINE STRINGS
a = "Hello"
b = "World"
c = a + b       # Merge variable a with variable b into variable c
c = a + " " + b # To add a space between them, add a " ":
print(c)

# FORMAT STRINGS
age = 36
myorder = "I want {} pieces of item {} for {} dollars." # Use placeholders
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."   # Use index numbers {0} for correct placeholders
print(myorder.format(quantity, itemno, price))  # Use the format() method to insert numbers into strings
#
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg) # returns: Numbers: 4 5 6
#
print("{0}{1}{0}".format("abra", "cad")) # returns: abracadabra
# Name placeholders
a = "{x}, {y}".format(x=5, y=12)
print(a)

# ESCAPE CHARACHTERS
txt = "We are the so-called \"Vikings\" from the north."    #use the escape character \" to escape problems
\n 	    New Line
\' 	    Single Quote
\\ 	    Backslash

\r 	    Carriage Return
\t 	    Tab
\b 	    Backspace
\f 	    Form Feed
\ooo 	Octal value
\xhh 	Hex value

# STRING METHODS
# --------------------------------------------------------

# All string methods
# https://www.w3schools.com/python/python_ref_string.asp
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle() 	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

# UPPER STRING METHOD
txt = "Hello, World!"
print(txt.upper())  # upper() method returns the string in upper case
print("This is a sentence.".upper()) # returns: THIS IS A SENTENCE.

# LOWER STRING METHOD
print(txt.lower())  # lower() method returns the string in lower case:
print("AN ALL CAPS SENTENCE".lower()) # returns: an all caps sentence


# REPLACE METHOD
txt = "Hello, World!"
print(txt.replace("l", "b")) # Replaces all 'l' to 'b' letters
print(x.replace("Hello", "Good morning"))

# SPLIT METHOD
# split string into strings, turns it into a list
# "string1" >> list
txt = "Hello, World!"
print(a.split(",")) # split() method splits the string into substrings if it finds instances of the separator ','
#returns ['Hello', ' World!']

# JOIN METHOD
# joins a list of strings with another string as a separator
# x = string1 + string2 + string3 = "string1, string2, string 3"
x = ", ".join(["spam", "eggs", "ham"])
print(x)
# prints "spam, eggs, ham"

# STRIP METHOD - REMOVE DELETE WHITESPACE
txt = "Hello, World!"
print(txt.strip())    # strip() method removes any whitespace from the beginning or the end:

# MAX ITEM IN A LIST
# string is also a list, we use a list method
# outputs the max number in a list
# alphabet: "a" is min, "z" is max
msg = "Hello"
print(msg.max()) # returns "o"

# COUNT STRING METHOD
# The count() method returns the number of occurrences of a substring in the given string.
message = 'python is popular programming language'
print('Number of occurrence of p:', message.count('p')) # Output: Number of occurrence of p: 4
