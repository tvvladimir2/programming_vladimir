# C#: ENUMERATIONS TYPE - ENUM


---


## LINKS

[C# Enumerations Type - Enum](https://www.tutorialsteacher.com/csharp/csharp-enum)
[Enum Class at learn.microsoft.com](https://learn.microsoft.com/en-us/dotnet/api/system.enum?view=netframework-4.8)


---


## DESCRIPTION

In C#, an `enum` (or enumeration type) is used to assign constant names to a group of numeric integer values. It makes constant values more readable, for example, `WeekDays.Monday` is more readable then number 0 when referring to the day in a week.

An `enum` is defined using the `enum` keyword, directly inside a namespace, class, or structure. All the constant names can be declared inside the curly brackets and separated by a comma. The following defines an `enum` for the weekdays.

`enum` is an abstract class.


---


## DEFINE ENUM

`WeekDays` enum declares members in each line separated by a comma.

```cs
enum WeekDays
{
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
}
```


---


## ENUM VALUES

If values are not assigned to `enum` members, then the compiler will assign integer values to each member starting with zero by default. The first member of an `enum` will be 0, and the value of each successive enum member is increased by 1. 

**Default Enum Values**:
```cs
enum WeekDays
{
    Monday,     // 0
    Tuesday,    // 1
    Wednesday,  // 2
    Thursday,   // 3
    Friday,     // 4
    Saturday,   // 5
    Sunday      // 6
}
```


You can assign different values to enum member. A change in the default value of an enum member will automatically assign incremental values to the other members sequentially. 

**Assign Enum Values to Enum Members**:
```cs
enum Categories
{
    Electronics,    // 0
    Food,           // 1
    Automotive = 6, // 6 - assign enum value to enum member
    Arts,           // 7 - assign incremental values to the other members sequentially
    BeautyCare,     // 8
    Fashion         // 9
}
```

**Assign Enum Values to each Enum Member**:
```cs
enum Categories
{
    Electronics = 1,  
    Food = 5, 
    Automotive = 6, 
    Arts = 10, 
    BeautyCare = 11, 
    Fashion = 15,
    WomanFashion = 15
}
```


---


## NUMERIC DATA TYPE

The enum can be of any numeric data type such as byte, sbyte, short, ushort, int, uint, long, or ulong. However, an enum cannot be a string type.

Specify the type after enum name as `: type`. The following defines the byte enum.

```cs
using System;

namespace MyApplication
{
  enum Categories: byte     // `: type`
  {
    Electronics = 1,  Food = 5, Automotive = 6, Arts = 10, BeautyCare = 11, Fashion = 15
  }

  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine(Categories.Electronics);
      Console.WriteLine(Categories.Fashion);
    }
  }
}
```
```
> Electronics
> Fashion
```


---


## ACCESS AN ENUM

An `enum` can be accessed using the dot syntax: `enum.member`

```cs
using System;

namespace MyApplication
{

    enum WeekDays
    {
        Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday 
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(WeekDays.Monday); // Monday
            Console.WriteLine(WeekDays.Tuesday); // Tuesday
        }
    }
}
```
```
> Monday
> Tuesday
```


--- 


## CONVERSION

Explicit casting is required to convert from an enum type to its underlying integral type.

```cs
using System;

namespace MyApplication
{
  enum WeekDays
  { 
    Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday 
  }

  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine(WeekDays.Friday); //output: Friday 
      int day = (int) WeekDays.Friday; // enum to int conversion
      Console.WriteLine(day); //output: 4 
      
      var wd = (WeekDays) 5; // int to enum conversion
      Console.WriteLine(wd);//output: Saturday
    }
  }
}
```
```
> Friday
> 4
> Saturday
```


---


## USAGE

**Define Current Game Screen**:
```cs
enum Screen { MainMenu, GameScreen, WinScreen}; // define enum

// declare a variable `currentScreen` of the type `Screen`
Screen currentScreen; 

// or

// declare a variable `currentScreen` of the type `Screen` and initialize it
Screen currentScreen = Screen.MainMenu;
```



