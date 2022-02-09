# FILE HANDLING

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
