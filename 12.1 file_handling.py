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
myfile = open("\\folder\\filename.txt", "w")  # relative path, another directory
myfile = open("F:\\OneDrive - Vutlan s.r.o\\Backups\\GitHub repositories\\pythonLython\\tests\\text.txt (Windows)") # absolute path
#   - 2. File Name: the actual name of the file
#   - 3. Extension: the end of the file path pre-pended with a period (.) used to indicate the file type


# FOLDER STRUCTURE
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


# SYNTAX - STRUCTURE
#------------------------------------------------------------------------------
file = open('path', "mode (read/write/append)")
print(file.read(number_of_bytes))
file.close()


# The argument of the open function is the path to the file. If the file is in the current working directory of the program, you can specify only its name.
# A file must be opened before it is edited.
myfile = open("filename.txt", "w")  # Sending "w" means write mode, for rewriting the contents of a file.
myfile = open("filename.txt", "r")  # Sending "r" means open in read mode, which is the default.
myfile = open("filename.txt", "r+") # Read + write
myfile = open("filename.txt", "a")  # Sending "a" means append mode, for adding new content to the end of the file.
open("filename.txt", "wb")          # Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

cont = myfile.read()
print(myfile.read(16))              # Number of bytes that should be read.
print(myfile.read())                # With no argument, read returns the rest of the file.
print(cont)                         # This will print all of the contents of the file "filename.txt".

myfile.close()                      # Close file after work is done.


# READING BYTE BY BYTE
#------------------------------------------------------------------------------
file = open('F:\\OneDrive - Vutlan s.r.o\\Backups\\GitHub repositories\\pythonLython\\tests\\text.txt', "r")    # text.txt contains "1234567890"
print(file.read(4)) # returns 1234
print(file.read(4)) # returns 5678
print(file.read(4)) # returns 90
print(file.read(4)) # returns 'empty'
file.close()


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
