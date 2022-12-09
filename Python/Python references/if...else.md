# FLOW CONTROL IN PYTHON


---


## DESCRIPTION

You can use if statements to run code if a certain condition holds.
If an expression evaluates to True, some statements are carried out. Otherwise, they aren't carried out.


---


## STRUCTURE

An if statement looks like this:

```python
if condition:   # first condition, expression leading to True or False
    statement   # always indented, mandatory indentation or a white space
    statement   # executed if first condition is True
elif condition:            # short for else/if statement for chaining if and else statements
    statement   # executed if `elif` condition is True
    statement
else:           # Else statement can be used to run some statements when the condition of the if statement is False.
    statement   # False branch
    statement   # executed if no conditions are True
```


---


## NESTED IF STATEMENTS

If statements can be nested, one inside the other:

```python
num = 12
if num > 5:
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")
else:   # Every if condition block can have only one else statement.
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")
```


---


## MULTIPLE CONDITIONS

```python
a = 200
b = 33
c = 500
if a > b and c > a: # The AND keyword is a logical operator used to combine conditional statements:
  print("Both conditions are True")
```


---
