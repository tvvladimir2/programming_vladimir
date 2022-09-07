# ERRORS


---


# TABLE

|   | Error name     | Example                                                     | Description                                    |
|---|----------------|-------------------------------------------------------------|------------------------------------------------|
| 1 | AttributeError | AttributeError: 'Rectangle' object has no attribute 'color' | Caused by trying to access unknown attributes? |
| 2 |                |                                                             |                                                |
| 3 |                |                                                             |                                                |


---


## 1. AttributeError

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
print(rect.color)
```
```
> AttributeError: 'Rectangle' object has no attribute 'color'
```


---


##
