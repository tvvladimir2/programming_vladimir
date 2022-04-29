# SCOPE RULE - Resolving Names in the Code


---


## LINKS

[Realpython.org Scope rule](https://realpython.com/python-scope-legb-rule/)


---


## DESCRIPTION

The concept of scope rules how variables and names are looked up in your code. It determines the visibility of a variable within the code. The scope of a name or variable depends on the place in your code where you create that variable. The Python scope concept is generally presented using a rule known as the LEGB rule.

- 4. Built-in (Python)
  Names preassigned in the built-in names module: open, range, SyntaxError...

  - 3. Global (module)
    Names assigned at the top level of a module file, or declared global in a definition within the file.

    - 2. Enclosing function locals (can be one in another)
      Names in the local at any and all enclosing functions (def or lambda), from inner to outer.

      - 1. Local (function)
        Names assigned in any way within a fucntion (def or lambda), and not declared global in that function.

**Example**: LEGB
```python
# 3. Global
name = 'This is a global name!'

# 2 Enclosing function locals
def greet():
  name = 'Lisa'

  # 1. Local fucntion
  def hello():
    print('Hello' + name)

  hello()

print(greet())
print(name)
```
```
> HelloLisa
> None
> This is a global name!
```

**Example**: Global not used
```python
y = 50

def func2():
  y = 100

print('Before function call y is =: ', y)
func2()
print('After function call y is =: ', y)
```
```
> Before function call y is =:  50
> After function call y is =:  50
```

**Example**: Global used
```python
y = 50

def func2():
  global y
  y = 100

print('Before function call y is =: ', y)
func2()
print('After function call y is =: ', y)
```
```
> Before function call y is =:  50
> After function call y is =:  100
```
