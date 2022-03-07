# FUNCTIONAL PROGRAMMING


---


Functional programming is a style of programming that (as the name suggests) is based around functions.
A key part of functional programming is `higher-order functions`. Higher-order functions take other functions as arguments, or return them as results.

**Example:**: The function `apply_twice` takes another function as its argument, and calls it twice inside its body.

```python
def apply_twice(func, arg):         # def apply_twice(func=add_five, arg=10)
    return func(func(arg))          # return apply_twice(apply_twice(10)) >> return apply_twice(15) >> return 20

def add_five(x):                    # 1st call: 15
    return x + 5                    # 2nd call: 20

print(apply_twice(add_five, 10))
```
```
> 20
```


---


## PURE vs UNPURE FUNCTIONS

Functional programming seeks to use `pure functions`.
- Pure functions have no side effects, and return a value that depends only on their arguments.
- This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.

**Example 1**: Pure function:

```python
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

print(pure_function(1, 2))
```
```
> 1.25
```


**Example 2**: Impure function:

```python
some_list = [1,2,3,4]

def impure_function(arg):
  some_list.append(arg)
  return(some_list)

print(impure_function(5))
```
```
> [1, 2, 3, 4, 5]
```

Using pure functions has both advantages and disadvantages.
**Pure functions advantages**:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.

**Pure functions disadvantages**:
The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects.
They can also be more difficult to write in some situations.
