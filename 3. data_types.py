# DATA TYPES

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:
# Text Type:        str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview

x = 5
print(type(x)) # Get data type

# In Python, the data type is set when you assign a value to a variable:
x = "Hello World" 	                             # str
x = 20 	                                         # int
x = 20.5 	                                     # float
x = ["apple", "banana", "cherry"] 	             # list
x = range(6) 	                                 # range
x = ("apple", "banana", "cherry") 	             # tuple
x = True 	                                     # bool

x = 1j 	                                         # complex
x = {"name" : "John", "age" : 36} 	             # dict
x = {"apple", "banana", "cherry"} 	             # set
x = frozenset({"apple", "banana", "cherry"}) 	 # frozenset
x = b"Hello" 	                                 # bytes
x = bytearray(5) 	                             # bytearray
x = memoryview(bytes(5)) 	                     # memoryview

# Specify the data type:
x = str("Hello World") 	                        # str
x = int(20) 	                                # int
x = float(20.5) 	                            # float
x = list(("apple", "banana", "cherry")) 	    # list
x = range(6) 	                                # range
x = tuple(("apple", "banana", "cherry")) 	    # tuple
x = bool(5) 	                                # bool

x = complex(1j) 	                            # complex
x = dict(name="John", age=36) 	                # dict
x = set(("apple", "banana", "cherry")) 	        # set
x = frozenset(("apple", "banana", "cherry"))    # frozenset
x = bytes(5) 	                                # bytes
x = bytearray(5) 	                            # bytearray
x = memoryview(bytes(5)) 	                    #memoryview
