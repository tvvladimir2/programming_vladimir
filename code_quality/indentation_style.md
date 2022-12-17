# INDANTATION STYLE


---


## LINKS

[](https://en.wikipedia.org/wiki/Indentation_style)


---


## DESCRIPTION

The main difference between indentation styles lies in the placing of the braces of the compound statement `({...})` that often follows a control statement (`if`, `while`, `for`...). The table below shows this placement for the style of statements discussed in this article; function declaration style is another case. The style for brace placement in statements may differ from the style for brace placement of a function definition. For consistency, the indentation depth has been kept constant at 4 spaces, regardless of the preferred indentation depth of each style.


---


### 1. ALLMAN

```cs
while (x == y)
{
    something();
    somethingelse();
}
```


---


### 2. K&R

```cs
while (x == y) {
    something();
    somethingelse();
}
```


---


### 3. GNU

```cs
while (x == y)
  {
    something ();
    somethingelse ();
  }
```


---


### 4. WHITESMITHS

```cs
while (x == y)
    {
    something();
    somethingelse();
    }
```


---


### 5. HOSTMANN

```cs
while (x == y)
{   something();
    somethingelse();
}
```


---


### 6. HASKELL

```cs
while (x == y)
  { something()
  ; somethingelse()
  ;
  }
```


---


### 7. PICO

```cs
while (x == y)
{   something();
    somethingelse(); }
```


---


### 8. RATLIFF

```cs
while (x == y) {
    something();
    somethingelse();
    }
```


---


### 9. LISP

```cs
while (x == y)
  { something();
    somethingelse(); }
```


---


### 10. APL

```cs
#define W(c,b) {while(c){b}}
W(x==y,s();se();)
```



