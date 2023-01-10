# `MAIN` METHOD


---


## LINKS

[Main() and command-line arguments](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/main-command-line)



---


## DESCRIPTION

- The `Main` method is the entry point of an executable program; it is where the program control starts and ends.
  
- `Main` is declared inside a class or struct. `Main` must be `static` and it need not be `public`. (In the earlier example, it receives the default access of `private`.) The enclosing class or struct is not required to be static.
  
- `Main` can either have a `void`, `int`, `Task`, or `Task<int>` return type.
  
- If and only if `Main` returns a `Task` or `Task<int>`, the declaration of `Main` may include the `async` modifier. This specifically excludes an `async void Main` method.
  
- The `Main` method can be declared with or without a `string[]` parameter that contains command-line arguments. When using Visual Studio to create Windows applications, you can add the parameter manually or else use the `GetCommandLineArgs()` method to obtain the command-line arguments. Parameters are read as zero-indexed command-line arguments. Unlike C and C++, the name of the program is not treated as the first command-line argument in the args array, but it is the first element of the `GetCommandLineArgs()` method.



---


## CREATE MAIN METHOD

```cs
class TestClass
{
    static void Main(string[] args)
    {
        // Display the number of command line arguments.
        Console.WriteLine(args.Length);
    }
}
```


Starting in C# 9, you can omit the Main method, and write C# statements as if they were in the Main method, as in the following example:

```cs
using System.Text;

StringBuilder builder = new();
builder.AppendLine("Hello");
builder.AppendLine("World!");

Console.WriteLine(builder.ToString());
```



---


## Main() return values
## Async Main return values
## Command-Line Arguments