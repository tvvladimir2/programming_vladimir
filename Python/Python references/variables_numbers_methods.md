# PYTHON: DATA TYPES: NUMBERS: METHODS


---


## LINKS

[](https://realpython.com/python-numbers/)


---


## NUMBER METHODS

Python has a few built-in functions that you can use to work with numbers.

| # | Method  | Description                                           |
|---|---------|-------------------------------------------------------|
| 1 | round() | for rounding numbers to some number of decimal places |
| 2 | abs()   | for getting the absolute value of a number            |
| 3 | pow()   | for raising a number to some power                    |


---


## 1. round()

For rounding numbers to some number of decimal places.

Python 3 rounds numbers according to a strategy called rounding ties to even. A tie is any number whose last digit is five. 2.5 and 3.1415 are ties.
When you round ties to even, you first look at the digit one decimal place to the left of the last digit in the tie. If that digit is even, then you round down. If the digit is odd, then you round up.

```python
print(round(2.3))
print(round(2.7))

print(round(3.5))   # digit to the left of 5 is odd >> up
print(round(4.5))   # digit to the left of 5 is even >> round down

print(round(3.14159, 3))    # round to 3 decimal places
print(round(2.71828, 2))    # round to 2 decimal places
```
```
> 2
> 3

> 4
> 4

> 3.142
> 2.72
```

---


