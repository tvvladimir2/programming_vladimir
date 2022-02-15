# FILE HANDLING
# https://realpython.com/read-write-files-python/


'''
# WHAT IS A FILE?
#------------------------------------------------------------------------------
A file is a contiguous set of bytes used to store data.
Data in the file depends on the format specification used, which is typically represented by an extension (.txt, .py).
In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

MAIN PARTS:
    1. Header: metadata about the contents of the file (file name, size, type, and so on)
    2. Data: contents of the file as written by the creator or editor
    3. End of file (EOF): special character that indicates the end of the file
'''


# FILE PATHS
#------------------------------------------------------------------------------
# The file path is a string that represents the location of a file.
# PARTS:
#   - 1. Folder Path: the file folder location on the file system, folders are separated by a forward slash / (Unix) or backslash \ (Windows)
myfile = open("filename.txt", "w")  # relative path, same directory
myfile = open("\\folder\\filename.txt", "w")  # relative path, another folder/directory
myfile = open("..\\..\\animals.csv", "w")  # relative path, previous-previous directory
myfile = open("F:\\OneDrive - Vutlan s.r.o\\Backups\\GitHub repositories\\pythonLython\\tests\\text.txt") # absolute path for (Windows)
#   - 2. File Name: the actual name of the file
#   - 3. Extension: the end of the file path pre-pended with a period (.) used to indicate the file type


# FOLDER STRUCTURE
#------------------------------------------------------------------------------
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


# LINE ENDINGS
#------------------------------------------------------------------------------
# WINDOWS:
Pug\r\n                     # '\r' means the end of line
Jack Russell Terrier\r\n    # '\n' means the next line
# UNIX:
Pug\r
\n
Jack Russell Terrier\r
\n


# CHARACHTER ENCODINGS
#------------------------------------------------------------------------------
# - Encoding of the byte data
# - An encoding is a translation from byte data to human readable characters.
# - A numerical value is assigned to represent a character.
# - Parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character.
#       - For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding,
#         if there is a character that is outside of those 128 values, then an error will be thrown.
#
# COMMON ENCODINGS:
# - ASCII can only store 128 characters (ASCII is actually a subset of Unicode (UTF-8))
# - Unicode can contain up to 1,114,112 characters.


''' SYNTAX - STRUCTURE '''
#------------------------------------------------------------------------------
file = open('path', "mode (read/write/append)")
print(file.read(number_of_bytes))
file.close()


''' OPENING & CLOSING '''
#------------------------------------------------------------------------------
''' A file must be opened before it is edited. '''
# SYNTAX:
myfile = open(argument, mode)   # invoiking 'open()' function
                                # returns: 'file object'
#
''' Make sure you close the file properly '''
# CLOSING FILE, METHOD 1:
try:
    # Further file processing goes here
finally:
    myfile.close()
#
# CLOSING FILE, METHOD 2:
with open('dog_breeds.txt', 'r') as myfile: # the file will be closed after 'with' block is finished
    # Further file processing goes here
#
# CLOSING FILE, METHOD 3:
myfile.close()  # not as reliable as the two before


''' OPEN MODES '''
#------------------------------------------------------------------------------
''' Character:      Meaning:
    'r':            Open for reading (default)
    'w':            Open for writing, truncating (overwriting) the file first
    'rb' or 'wb':	Open in binary mode (read/write using byte data)'''


''' FILE OBJECT CATEGORIES '''
#------------------------------------------------------------------------------
'''A file object is an object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource.
CATEGORIES OF FILE OBJECTS:
    - Text files
    - Buffered binary files
    - Raw binary files '''
#
# TEXT FILE:
# - This is the default file object returned by open().
file = open('dog_breeds.txt')           # open() will return a default TextIOWrapper file object:
type(file)                              # returns: <class '_io.TextIOWrapper'>
#
# BUFFERED BINARY FILE TYPES:
file = open('dog_breeds.txt', 'rb')     #
type(file)                              # returns: <class '_io.BufferedReader'>
#
file = open('dog_breeds.txt', 'wb')     #
type(file)                              # returns: <class '_io.BufferedWriter'>
#
# RAW FILE TYPES:
# - generally used as a low-level building-block for binary and text streams.
file = open('dog_breeds.txt', 'rb', buffering=0)
type(file)                              # returns: <class '_io.FileIO'>


# READING BYTE BY BYTE
#------------------------------------------------------------------------------
file = open('F:\\OneDrive - Vutlan s.r.o\\Backups\\GitHub repositories\\pythonLython\\tests\\text.txt', "r")    # text.txt contains "1234567890"
print(file.read(4)) # returns 1234
print(file.read(4)) # returns 5678
print(file.read(4)) # returns 90
print(file.read(4)) # returns 'empty'
print(myfile.read())                # With no argument, read returns the rest of the file.


# READLINES() METHOD
#------------------------------------------------------------------------------
# LIST OF LINES
file = open("filename.txt", "r")
print(file.readlines()) # returns a list of lines ['1234567890\n', 'line 2\n', 'line 3\n']
file.close()
#
# ITERATE THROUGH LINES
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()
# returns:
# Line 1 text
#
# Line 2 text
#
# Line 3 text


# LEN() METHOD
# -----------------------------------------------------------------------------
len(open("test.txt").readlines())   # returns a number of lines
