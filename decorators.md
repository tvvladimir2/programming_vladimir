# Python Decorators


---


## LINKS


---


## DESCRIPTION

A Python decorator is a function that takes in a function, adds some functionality to it and returns the original function.
Python decorators is a technique for changing the behavior of an existing function without changing actual code inside the function.

Even though we are changing the behavior of the function, there should not have any change in the function definition and function call. It means:

- The code inside the original function should not be changed.
- There should not have any change in the function call.

When do we use them?:

- You are asked to make the changes in a certain complex function.
- You don’t need to make changes in the already tested function.
- You don’t need to make any changes to the function call. This will be very useful if there are multiple function calls in your project source code.
- You can also pass the arguments to the decorators. You can modify these arguments inside the decorators before passing them to the original function.

---


## SYNTAX STRUCTURE

```python
# Decorator function
def myWrapper(func):                  #
    def myInnerFunc():                   #
        print("============")                       
        func()                    #
        print("============")                       
    return myInnerFunc                   #     

# Function to be decorated
def myFunc():                 #
    print("Hello world!")                       

decorated = myWrapper(myFunc)                       
decorated()                       #
```

the same as:

```python
# Decorator function
def myWrapper(func):              # 3   # func = myFunc()
    def myInnerFunc():            # 4
        print("============")
        func()                    # 5
        print("============")
    return myInnerFunc            # 4

@myWrapper                        # 2   # pre-pending the function definition with a decorator name and the @ ("address sign", "at") symbol.
def myFunc():                     # 6
    print("Hello world!")

myFunc()                          # 1
```
```
> ============
> Hello world!
> ============
```

steps of execution:

- 1. The original function is called.
- 2. There is a function wrapper name specified above the function definition (2). This indicates, there is a function decorator assigned to the function.
- 3. The decorator function gets called. The program controller passes the function object as a parameter to the decorator function (3).
- 4. The function inside the decorator function gets executed (4).
- 5. The inner function calls the actual function (5).
- 6. The original function starts execution (6).


---


## PASSING ARGUMENTS

**Example**: Add text at the end of Upper case function
```python
text = 'This is my text'

def uppercase_decorator(func):      # func = func_upper_case(text)
    def wrapper(text):
        #your code goes here
        result = func(text)
        result += '. the end'
        return(result)

    return wrapper

@uppercase_decorator
def func_upper_case(text):
    text = text.upper()
    return(text)

print(func_upper_case(text))
```
```
> THIS IS MY TEXT. the end
```


---


## Chaining Decorators in Python

In Python, a function can be decorated multiple times with different or the same decorator.

Here, are two decorator functions called `star` and `percent`. These functions print a series of star and percentage symbols before and after executing the function

```python
def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner
def percent(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer("Decorators are wonderful")
```
```
> ******************************
> %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
> Decorators are wonderful
> %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
> ******************************
```

As you can see, these decorators are chained and they wrap the original function.

Here, we have first called the `star` function, and then the `percent` function. So the `star` function wraps the `percent` function which in turn wraps the `printer` function.
