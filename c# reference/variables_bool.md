# BOOLEANS


---


## LINKS

[Convert methods: TODO: NOT READ](https://code-maze.com/csharp-convert-string-to-bool/)


---



## DESCRIPTION

The bool (boolean) data type is one of the simplest found in the .NET framework, because it only has two possible values: false or true.



---



## DECLARATION & INITIALIZATION

```cs
internal class Program
{
    private static void Main(string[] args)
    {
        bool isAdult;   // unassigned local variable
        isAdult = true; // assigned
        Console.WriteLine(isAdult.GetType());
        Console.WriteLine(isAdult);
    }
}
```
```
> System.Boolean
> True
```



---



## USE IN `IF`CONDITIONAL STATEMENT

**The same as 2 next examples**:
```cs
internal class Program
{
    private static void Main(string[] args)
    {
        bool isAdult = true;  
        if (isAdult == true)  
            Console.WriteLine("An adult");  
        else  
            Console.WriteLine("A child");
    }
}
```
```
> An adult
```

**The same as the previous or next example**:
```cs
internal class Program
{
    private static void Main(string[] args)
    {
        bool isAdult = true;  
        if (isAdult)  
            Console.WriteLine("An adult");  
        else  
            Console.WriteLine("A child");
    }
}
```
```
> An adult
```


**Same as two previous examples**:
```cs
internal class Program
{
    private static void Main(string[] args)
    {
        bool isAdult = true;  
        if (!isAdult)  
            Console.WriteLine("NOT an adult");  
        else  
            Console.WriteLine("An adult");
    }
}
```
```
> An adult
```



---



## TYPE CONVERSION

Booleans are sometimes represented as either `0` (false) or `1` (true).

Best to use a `Convert Class` for most conversion tasks:
[](https://msdn.microsoft.com/en-us/library/system.convert(v=vs.110).aspx)

```cs
internal class Program
{
    private static void Main(string[] args)
    {
        int val = 1;
        bool isAdult = Convert.ToBoolean(val);
        Console.WriteLine("Bool: " + isAdult.ToString());
        Console.WriteLine("Int: " + Convert.ToInt32(isAdult).ToString());
    }
}
```
```
> Bool: True
> Int: 1
```



---



## TOGGLE VALUE / CHANGE TO OPPOSITE VALUE

Example: **Change field member to opposite value**
```cs
internal class Program
{
    private static void Main(string[] args)
    {
        bool isAdult = true;
        isAdult = !isAdult; // True = not True; or False = not False
        Console.WriteLine(isAdult);
    }
}
```
```
> False
```


Example: **Call a function with opposite value**
```cs
bool isAdult = true;
DoSomethingMethod(!isAdult); // True = not True; or False = not False
```

