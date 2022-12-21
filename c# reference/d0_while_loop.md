# C#: DO WHILE LOOP


---


## DESCRIPTION

The `do while` loop is the same as while loop except that it executes the code block at least once.

The do-while loop starts with the `do` keyword followed by a code block and a boolean expression with the `while` keyword. The `do while` loop stops execution exits when a boolean condition evaluates to false. Because the `while(condition)` specified at the end of the block, it certainly executes the code block at least once.


---


## SYNTAX

```cs
do
{
    //code block


} while(condition);
```


---


## EXAMPLE

Specify initialization out of the loop and increment/decrement counter inside `do while` loop.

```cs
int i = 0;  // Initialization

do
{
    Console.WriteLine("i = {0}", i);    // Some statements
    i++;    // Increment/Decrement counter

} while (i < 5);    // Condition
```
```
> i = 0
> i = 1
> i = 2
> i = 3
> i = 4
```


---


## EXIT `DO WHILE` LOOP

Use `break` or `return` to exit from the `do while` loop.

```cs
int i = 0;

do
{
    Console.WriteLine("i = {0}", i);
    i++;
    
    if (i > 5)
        break;

} while (i < 10);
```
```
> i = 0
> i = 1
> i = 2
> i = 3
> i = 4
> i = 5 
```


---


## NESTED `DO WHILE` LOOP

The do-while loop can be used inside another do-while loop.

```cs
int i = 0;

do
{
    Console.WriteLine("Value of i: {0}", i);
    int j = i;

    i++;
                
    do
    {
        Console.WriteLine("Value of j: {0}", j);
        j++;
    } while (j < 2);

} while (i < 2);
```
```
> i = 0
> j = 0
> j = 1
> i = 1
> j = 1 
```