# C# WHILE LOOPS


---


## DESCRIPTIOPN

C# provides the `while` loop to repeatedly execute a block of code as long as the specified condition returns `true`.

The `while` loop starts with the `while` keyword, and it must include a boolean conditional expression inside brackets that returns either true or false. It executes the code block until the specified conditional expression returns false.

The `for` loop contains the initialization and increment/decrement parts. When using the `while` loop, initialization should be done before the loop starts, and increment or decrement steps should be inside the loop.

***C# WHILE LOOP**:
```cs
int i = 0; // initialization

while (i < 10) // condition
{
    Console.WriteLine("i = {0}", i);

    i++; // increment
}
```
```
> i = 0
> i = 1
> i = 2
> i = 3
> i = 4
> i = 5
> i = 6
> i = 7
> i = 8
> i = 9
```

Above, a `while` loop includes an expression `i < 10`. Inside a while loop, the value of i increased to 1 using `i++`. The above `while` loop will be executed when the value of i equals to 10 and a condition `i < 10` returns false.


---


## SYNTAX

```cs
While(condition)
{
    //code block
}
```


---


## EXIT ON CONDITION

```cs
int i = 0;

while (true)
{
    Console.WriteLine("i = {0}", i);

    i++;

    if (i > 10)
        break;
}
```


---


## INFINITE `WHILE` LOOP

Ensure that the conditional expression evaluates to false or exit from the while loop on some condition to avoid an infinite loop. The following loop is missing an appropriate condition or break the loop, which makes it an infinite while loop.

```cs
int i = 1;

while (i > 0)
{
    Console.WriteLine("i = {0}", i);
    i++;
}
```
```
> i = 1
> i = 2
> i = 3
> i = 4
> ...
```


---


## NESTED `WHILE` LOOP

C# allows `while` loops inside another `while` loop, as shown below. However, it is not recommended to use nested `while` loop because it makes it hard to debug and maintain.

```cs
int i = 0, j = 1;

while (i < 2)
{
    Console.WriteLine("i = {0}", i);
    i++;

    while (j < 2)
    {
        Console.WriteLine("j = {0}", j);
        j++;
    }
}
```
```
> i = 0
> j = 1
> i = 1
```