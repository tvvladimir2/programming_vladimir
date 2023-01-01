# COMPARING FLOATS


---


## DESRIPTION

- Two `float`s can vary by a tiny amount
- Therefor, it is unpredictable to use `==` with `float`s.
- That is why, always specify an acceptable difference
- The smallest float in Unity Game Engine is `Mathf.Epsilon`
- Always compare to this rather than `zero`.


**WRONG Example**:
```cs
if (period == 0)
{
    print(x);
}
```


**CORRECT Example**:
```cs
if (period <= Mathf.Epsilon)
{
    print(x);
}
```
