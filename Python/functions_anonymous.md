# ANONYMOUS FUNCTIONS (LAMBDA EXPRESSIONS)


---


## Description

Anonymous functions = Lambda expressions = A function with no name = Lambda function

Can not use `Lambda` expressions for multiline functions. Used for simple expressions.
Best used once a single times.
Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.


---


# SYNTAX STRUCTURE

`lambda arguments : expression`

` lambda_keyword x(1), x(2), x(3), ..., x(n): single expression (return value)    # `:` = calling `

```python
y = lambda x: x
print(y(1))
```
```
> 1
```


---


## LAMBDA vs FUNCTIONS

```python
x = lambda a, b : a * b
print(x(5, 6))
```
```
> 30
```

is the same as:

```python
def f_multiply(a, b):
  return (a * b)

print( f_multiply(5, 6) )
```
```
> 30
```


---


## DEFINE & CALL IMMEDIATELY

```python
print( (lambda x, y: x + y)(2, 3) )
```
```
> 5
```


---


## LAMBDA INSIDE A FUNCTION

```python
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)         # mytripler = lambda a: a * 3

print(mytripler(11))          # lambda 11: 11 * 3  >> 33
```
```
> 33
```


---


## FORMAT STRINGS

```python
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

print( full_name('Vladimir', 'Tazev') )
```
```
> Full name: Vladimir Tazev
```


---


## HIGHER ORDER FUNCTION

```python
high_ord_func = lambda x, func: x + func(x)     # : 2 + (x*x) = 2 + (2*2) = 6
high_ord_func(2, lambda x: x * x)
```
```
> 6
```


---


## SEVERAL LINES

```python
y = (lambda x:
(x + 4))(3)     # 1 and
print(y)
```
```
> 7
```


---


## SUPPORTED ARGUMENTS

Supported arguments                                       | Example  |
----------------------------------------------------------|----------|
Positional arguments                                      |          |
Named arguments (sometimes called keyword arguments)      |          |
Variable list of arguments (often referred to as varargs) |          |
Variable list of keyword arguments                        |          |
Keyword-only arguments                                    |          |


---


## LAMBDA with MAP( ) function

**Example**: Multiply each item in a list by 2

```python
nums = [33,45,65,32,44]

a = list(map(lambda x: x*2, nums))
print(a)
```
```
> [66, 90, 130, 64, 88]
```


---


## COMPARISON FILTER USING IF

```python
y = lambda x: x < 5
print(y(1))
print(y(6))
```
```
> True
> False
```


---


## COMPARISON LAMBDA with FILTER( ) FUNCTION

**Example**: Fill in the blanks to extract all items that are less than 5 from the list.

```python
nums = [1, 2, 5, 8, 3, 0, 7]

y = list( filter(lambda x: x < 5, nums))

print(y)
```
```
> [1, 2, 3, 0]
```


---
