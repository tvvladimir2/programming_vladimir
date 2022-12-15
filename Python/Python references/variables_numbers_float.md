# PYTHON: FLOATING POINT NUMBERS


---


## DESCRIPTION

A `floating-point number`, or `float` for short, is a number with a decimal place. 1.0 is a floating-point number, as is `-2.75`. The name of the floating-point data type is `float`.
Floats do have a maximum size. The maximum floating-point number depends on your system, but something like 2e400 ought to be well beyond most machines’ capabilities. 2e400 is 2×10⁴⁰⁰, which is far more than the total number of atoms in the universe!


---


## CREATE AND ASSIGN

```python
var1 = 1000000.0
var2 = 1_000_000.0              # use underscores (_) to group digits in integer literals
var3 = 1e6                      # exponential notation (E notation) to create a float literal
var4 = 1e-4
var5 = 200000000000000000.0     # Python uses E notation to display large floating-point numbers:
var6 = 2e400                    # the number is larger than maximum, return `inf` or `-inf`. The type of `inf` is still float
var7 = -2e400

print(var1)
print(var2)   
print(var3)
print(var5)
print(var6)
print(var7)
```
```
> 1000000.0
> 1000000.0
> 1000000.0
> 0.0001
> 2e+17                     
> inf
> -inf
```


---


## DETERMINE THE TYPE

```python
print(type(1.0))
```
```
> <class 'float'>
```