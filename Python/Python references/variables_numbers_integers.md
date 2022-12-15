# PYTHON: INTEGERS


---


## DESCRIPTION

An integer is a whole number with no decimal places.
There’s no limit to how large an integer can be, which might be surprising considering that computers have a finite amount of memory.


---


## CREATE AND ASSIGN

The value 25 is called an `integer literal` because the integer is literally typed into the code.

```python
varNumber1 = 10000
varNumber2 = 10_000 # use underscores (_) to group digits in integer literals

print(varNumber1)
print(varNumber2)
```
```
> 10000
> 10000
```

---


## DETERMINE THE TYPE

The name for the integer data type is `int`, which you can see with `type()` built-in function:

```python
type(1)
```
```
> <class 'int'>
```


---


## CONVERT OTHER TYPES TO INTEGER

```python
print("var1 = ", int("25"))  # string to integer
```
```
> var1 =  25
```


---

