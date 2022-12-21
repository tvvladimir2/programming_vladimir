# C# - IF, ELSE IF, ELSE STATEMENTS


---


## LINKS

[C# - if, else if, else Statements](https://www.tutorialsteacher.com/csharp/csharp-if-else)


---


## DESCRIPTION

C# provides many decision-making statements that help the flow of the C# program based on certain logical conditions. Here, you will learn about if, else if, else, and nested if else statements to control the flow based on the conditions.

C# includes the following flavors of if statements:

1. if statement
2. else-if statement
3. else statement

Multiple else if statements can be used after an if statement. It will only be executed when the if condition evaluates to false. So, either if or one of the else if statements can be executed, but not both.

The else statement can come only after if or else if statement and can be used only once in the if-else statements. The else statement cannot contain any condition and will be executed when all the previous if and else if conditions evaluate to false.

C# supports if else statements inside another if else statements. This are called nested if else statements. The nested if statements make the code more readable. 


---


## SYNTAX

**SIMPLE STATEMENT**:
```cs
if(condition1)  // a boolean condition
{
    // code block to be executed when if condition1 evaluates to true
}
else if(condition2)
{
    // code block to be executed when 
    //      condition1 evaluates to flase
    //      condition2 evaluates to true
}
else if(condition3)
{
    // code block to be executed when 
    //      condition1 evaluates to flase
    //      condition2 evaluates to false
    //      condition3 evaluates to true
}
```

**NESTED STATEMENTS**:
```cs
if(condition1)
{
   if(condition2)
    {
        // code block to be executed when 
        //      condition1 and condition2 evaluates to true
    }
    else if(condition3)
    {
        if(condition4)
        {
            // code block to be executed when 
            //      only condition1, condition3, and condition4 evaluates to true
        }
        else if(condition5)
        {
            // code block to be executed when 
            //      only condition1, condition3, and condition5 evaluates to true
        }
        else
        {
            // code block to be executed when 
            //      condition1, and condition3 evaluates to true 
            //      condition4 and condition5 evaluates to false
        }
    }
}
```


---


## EXAMPLES


**SINGLE LINE IF ELSE STATEMENTS**:
```cs
int i = 20, j = 20;

if (i > j)
{
    Console.WriteLine("i is greater than j");
}
else if (i < j)
{
    Console.WriteLine("i is less than j");
}
else
{
    Console.WriteLine("i is equal to j");
}
```
```
> i is equal to j
```


**NESTED IF ELSE STATEMENTS**:
```cs
int i = 10, j = 20;

if (i != j)
{
    if (i < j)
    {
        Console.WriteLine("i is less than j");
    }
    else if (i > j)
    {
       Console.WriteLine("i is greater than j");
    }
}
else
    Console.WriteLine("i is equal to j");
```
```
> i is less than j
```


---


## ALTERNATIVE TERNARY OPERATOR

[C# - Ternary Operator ?: ](https://www.tutorialsteacher.com/csharp/csharp-ternary-operator)


---



