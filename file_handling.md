# FILE HANDLING
---

## Useful links
[RealPython article course](https://realpython.com/read-write-files-python/)

[Programiz Python course markdown files](https://github.com/programiz/python-course/)



---


## WHAT IS A FILE?
  - A file is a contiguous set of bytes used to store data.
  - Data in the file depends on the format specification used, which is typically represented by an extension (.txt, .py).
  - In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.


---


##### Main parts of a file:
Element               |  Element
--                    |  --
1. HEADER:            |  Metadata about the contents of the file (file name, size, type, and so on)
2. DATA:              |  codeontents of the file as written by the creator or editor.
3. END OF LIFE (EOF): |  Special character that indicates the end of the file.


---


## FILE PATHS
The file path is a string that represents the location of a file.
PARTS:

  1. **FOLDER PATH**: the file folder location on the file system, folders are separated by a forward slash / (Unix) or backslash \ (Windows).

  ```python
  import os

  # returns:
  # C:\Users\VladimirWorkPC\AppData\Local\atom\app-1.59.0
  print(os.getcwd())

  # returns:
  # F:\OneDrive - Vutlan s.r.o\Backups\GitHub repositories\pythonLython\tests\test.py
  # Это не тот путь что нам нужен!!!
  print(os.path.realpath(__file__))

  # returns:
  # F:\OneDrive - Vutlan s.r.o\Backups\GitHub repositories\pythonLython\tests
  print(os.path.dirname(__file__))

  myfile = open("filename.txt", "w")            # relative path, same directory
  file = open(dir_path + '//test.txt', 'r')     # relative path, same directory

  myfile = open("\\folder\\filename.txt", "w")  # relative path, another folder/directory
  file = open(dir_path + '//test//test.txt', 'r') # relative path, another folder/directory

  myfile = open("..\\..\\animals.csv", "w")     # relative path, previous-previous directory
  myfile = open("F:\\folder\\text.txt")         # absolute path for (Windows):
  ```

  2. **FILE NAME**: the actual name of the file
  3. **EXTESNION**: the end of the file path pre-pended with a period (.) used to indicate the file type


---


## FOLDER STRUCTURE
```
/
│
├── path/
|   │
│   ├── to/
│   │   └── cats.gif
│   │
│   └── dog_breeds.txt
|
└── animals.csv
```


## LINE ENDINGS
##### WINDOWS:
```
Jack the Crack\r\n          # '\r' means the end of line
Jack Russell Terrier\r\n    # '\n' means the next line
```
##### UNIX:
```
Jack the Crack\r
\n
Jack Russell Terrier\r
\n
```


---


## CHARACHTER ENCODINGS
- Encoding of the byte data
- An encoding is a translation from byte data to human readable characters.
- A numerical value is assigned to represent a character.
- Parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character.

> For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding, if there is a character that is outside of those 128 values, then an error will be thrown.
>


---


## COMMON ENCODINGS:
  - **ASCII** can only store 128 characters (ASCII is actually a subset of Unicode (UTF-8))
  - **Unicode** can contain up to 1,114,112 characters.


---


## OPENING & CLOSING
  - A file must be opened before it is edited.


---


##### OPEN:
```python
myfile = open('path argument', 'mode argument')   # invoking 'open()' function
myfile = open('dog_breeds.txt', 'w')              # returns: 'file object'
```


---


##### CLOSING FILE, Method 1 (best method):
Always close files!
This ensures that the file is always closed, even if an error occurs.

```python
try:
  myfile = open("filename.txt")
  print(myfile.read())
  
finally:
    myfile.close()
```


---


##### CLOSING FILE, Method 2 (Semi best method):
The file is automatically closed at the end of the with statement, even if exceptions occur within it.

```python
With open('dog_breeds.txt', 'r') as myfile:
```


---


##### CLOSING FILE, Method 3 (worst method):
If error happens, the file will not close.

```python
myfile.close()  # not as reliable as the two before
```


---


## OPEN MODES
Charachter      |  Meaning
--              |  --
'r':            |  Open for reading (default)
'w':            |  Open for writing, truncating (overwriting) the file first
'rb' or 'wb':   |  Open in binary mode (read/write using byte data)


---


## FILE OBJECT CATEGORIES
A file object is an object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource.

N | CATEGORIES OF FILE OBJECTS:
--                          | --
1                           | Text files
2                           | Buffered binary files
3                           | Raw binary files


---


##### 1. TEXT FILE:
This is the default file object returned by open().
```python
file = open('dog_breeds.txt')           # open() will return a default TextIOWrapper file object:
type(file)                              # returns: <class '_io.TextIOWrapper'>
```


---


##### 2. BUFFERED BINARY FILE TYPES:
```python
file = open('dog_breeds.txt', 'rb')     #
type(file)                              # returns: <class '_io.BufferedReader'>
```

```python
file = open('dog_breeds.txt', 'wb')     #
type(file)                              # returns: <class '_io.BufferedWriter'>
```


---


##### 3. RAW FILE TYPES:
Generally used as a low-level building-block for binary and text streams.
```python
file = open('dog_breeds.txt', 'rb', buffering=0)
type(file)                              # returns: <class '_io.FileIO'>
```


---


## READING FILES
Method              |  What it does
--------------------|--------------
.read(size=-1)      |  This reads from the file based on the number of size bytes.If no argument is passed or None or -1 is passed, then the entire file is read.  |  
.readline(size=-1)  |  This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
.readlines()        |  This reads the remaining lines from the file object and returns them as a list.


---


##### 1. READ( ) Method
```python
file = open('F:\\Folder\\text.txt', "r")    # text.txt contains "1234567890"
print(file.read(4))                         # returns 1234
print(file.read(4))                         # returns 5678
print(file.read(4))                         # returns 90
print(file.read(4))                         # returns 'empty'
print(myfile.read())                        # With no argument, read returns the rest of the file.
```


---


##### 2. READLINE( ) Method

###### Simple example:
```python
with open('F:\\Folder\\text.txt', 'r') as reader:
  # Read & print the first 5 characters of the line 5 times
  print(reader.readline(5))
  # Notice that line is greater than the 5 chars and continues
  # down the line, reading 5 chars each time until the end of the
  # line and then "wraps" around
  print(reader.readline(5))
  print(reader.readline(5))
  print(reader.readline(5))
  print(reader.readline(5))
```


---


##### 3. READLINES( ) Method

###### Example:
```python
file = open("filename.txt", "r")
print(file.readlines()) # returns a list of lines ['1234567890\n', 'line 2\n', 'line 3\n']
file.close()
```


---


## ITERATE THROUGH A FILE
Worse method at the beginning, best at the end.

##### 1. Iterate througha  list using readlines():
```python
with open('dog_breeds.txt', 'r') as reader:
  for line in reader.readlines():
    print(line, end='')
```


---


###### 2. Iterate through lines using line():
```python
with open('dog_breeds.txt', 'r') as reader:
  # Read and print the entire file line by line
  line = reader.readline()
  while line != '':  # The End-of-File (EOF) char is an empty string
      print(line, end='')
      line = reader.readline()
```


---


###### 3. Iterate through the file itself:
```python
# Iterating over the file object itself
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()
```
returns:
```
Line 1 text

Line 2 text

Line 3 text
```


---


## WRITING FILES

- The write method returns the number of bytes written to a file, if successful.
- When a file is opened in write mode, the file's existing content is deleted.

Method              |  What it does
--                  |--
`.write(string)`    |  This writes the string to the file.
`.writelines(seq)`  |  This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).

###### 1. WRITE( )
Write string to a file.
```python
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()
```

###### 2. WRITE( )
Returns the number of bytes written to a file

```python
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
```























###### Create a list out of a file object:
```python
f = open('dog_breeds.txt')
list(f)
```


---


## OTHER METHODS:
##### 1. LEN( ) METHOD
```python
len(open("test.txt").readlines())   # returns a number of lines
```

---


# ATTRIBUTES

## filename.`__file__`
- `__file__` is a variable that contains the path to the module that is currently being imported.
- Python creates a __file__ variable for itself when it is about to import a module.
- The updating and maintaining of this variable is the responsibility of the import system.
- The import system can choose to leave the variable empty when there is no semantic meaning, that is when the module/file is imported from the database.
- This attribute is a String.
```python
file = open('dog_breeds.txt', 'r')     #
print(file.__file__)                             # returns: <class '_io.BufferedReader'>
```
