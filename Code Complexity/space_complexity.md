# SPACE COMPLEXITY



---



## DESCRIPTION

Space complexity measures memory usage of a specific program.

If a program takes a lot of memory space, the compiler will not let you run it.


**Formula**:

```
Space Complexity = Auxiliary space + Space use by input values
```

For any program, memory may be used for the following…

    1. Variables (This includes the constant values, temporary values)
    2. Program Instruction
    3. Execution

**Space Complexity** is the total amount of memory a program an algorithm takes to execute and produce the result.

In any algorithm, the extra space or the `temporary space` that we use is known as `Auxiliary space`. 

![](images/space_complexity_chart.png)


The algorithm uses memory space for three reasons…

1. **Instruction Space**: While writing an algorithm, the compiled version of instructions takes some amount of memory which is known as Instruction space.

2. **Environmental Stack**: It is required to store the environmental information needed to resume the suspended function. This is used when an algorithm is called inside another algorithm. In those situations, we push the current variables into the system stack, where we wait for further execution. After that, we call it inside the algorithm

Let’s take the example of two functions. Function X() and function Y(). Variables of function X() will be stored on the system stack temporarily, while function Y() is called and executed inside function X().

3. **Data Space**: During the execution of a program whatever space is required to store the constants and variable values are considered as Data Space.

**Note**: While writing an algorithm you only need to consider the Data Space. You don’t need to calculate the Instruction Space and Environmental Stack.



---



## INCREASE FACTORS

- Assigning variables
- Creating new data structures
- Function calling and allocation within the function body



---



## CONSTANT SPACE COMPLEXITY O(1)

`a`, `b`, `c`, and `x` all are integer types. Each of them takes 4 bytes. Now we can calculate the total memory. 

(4(4) + 4) = 20 bytes. Additional 4 bytes are for the return value. Here we need a `fixed amount of memory for all the input`.

```cs
{
   int x = a * b * c;
   return(x);
}
```



---



## LINEAR SPACE COMPLEXITY O(n)

We need `4*n bytes of space` for each element of the array. 4 bytes each for `sum`, `n`, `i`, and the return value.

The total amount of memory will be `(4n+16)` which is increasing linearly with an increase in the input value `n`. This is called Linear Space Complexity. If you have a loop variable `I`, then the required space complexity will be 1 word.

```cs
// n is the length of array a[]
int sum(int arr[], int n)
{
    int sum = 0;  // 4 bytes for sum

    for(int i = 0; i < n; i++) // 4 bytes for i
        {  
            sum  = sum + arr[i];  
        }
        return(sum);
}
```



---

