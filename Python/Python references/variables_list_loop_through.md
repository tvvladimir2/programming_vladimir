# LISTS LOOPS


---


## LOOP THROUGH THE LIST OF ITEMS

You can loop through the list items by using a `for loop`.

```python
thislist = ["apple", "banana", "cherry"]
for x in thislist:  # loops 3 times
  print(x)  # returns the value of each item
```
```
> apple
> banana
> cherry
```


---



# LOOP THROUGH THE INDEX NUMBERS USING FOR LOOP

- You can also loop through the list items by referring to their index number.
- Use the range() and len() functions to create a suitable iterable.
- Print all items by referring to their index number:

```python
thislist = ["apple", "banana", "cherry"]
for i in range(len  (thislist)):
    print(i)
    print(thislist[i]) # returns:
```
```
> 0
> apple
> 1
> banana
> 2
> cherry
```



---



## LOOP THROUGH THE INDEX NUMBERS MATHEMATICALLY

```python
colors = ["red", "yellow", "blue", "green"]
for x in range(1500):
    y = colors[x%4] # Loops through the list, 0,1,2,3,0,1,2,3,0
    print(y, x, x%4)
```
```
> red 0 0
> yellow 1 1
> blue 2 2
> green 3 3
> red 4 0
```



---



## USING WHILE LOOP

```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(i)
    print(thislist[i])
    i = i + 1
```
```
> 0
> apple
> 1
> banana
> 2
> cherry
```
