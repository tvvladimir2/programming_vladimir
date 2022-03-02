# GENERATORS


---


## GENRATORS vs LIST COMPREHENSION

Trying to create a list in a very extensive `range` will result in a MemoryError when using `list comprehension`.
This code shows an example where the list comprehension runs out of memory.

```python
even = [2*i for i in range(10**100)]
```
```
> MemoryError
```


---
