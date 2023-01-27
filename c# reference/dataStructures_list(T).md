# C# LIST <T> CLASS


---


## LINKS

[List<T> Class](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-7.0)

[C# - List<T>](https://www.tutorialsteacher.com/csharp/csharp-list)



---



## SYNTAX

```cs
List<Tkey> primeNumbers = new List<Tkey>();
```

- **Tkey**: Type parameter of data stored
---



## DESCRIPTION

The `List<T>` is a collection of strongly typed objects that can be accessed by index and having methods for sorting, searching, and modifying list. It is the `generic` version of the `ArrayList` that comes under `System.Collections.Generic` namespace.


Characteristics:

- `List<T>` equivalent of the `ArrayList`, which implements `IList<T>`.
- It comes under `System.Collections.Generic` namespace.
- `List<T>` can contain elements of the specified type. It provides compile-time type checking and doesn't perform boxing-unboxing because it is generic.
- Elements can be added using the `Add()`, `AddRange()` methods or collection-initializer syntax.
- Elements can be accessed by passing an index e.g. `myList[0]`. Indexes start from zero.
- `List<T>` performs faster and less error-prone than the `ArrayList`.
- `nulls` values are allowed for reference type list



---



## LIST CLASS HIERARCHY

The following diagram illustrates the List<T> hierarchy.

![](images/csharp_list(t)_class_hierarchy.png)



---



## CREATE A LIST

The `List<T>` is a generic collection, so you need to specify a type parameter for the type of data it can store. The following example shows how to create list and add elements.

```cs
using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        // 1. adding elements using add() method
        List<int> primeNumbersList = new List<int>();
        primeNumbersList.Add(1); // adding elements using add() method
        primeNumbersList.Add(3);
        primeNumbersList.Add(5);
        primeNumbersList.Add(7);
        Console.WriteLine("1. primeNumbersList" + " has " + primeNumbersList.Count + " elements.");
        
        // 2.
        var citiesList = new List<string>();
        citiesList.Add("New York");
        citiesList.Add("London");
        citiesList.Add("Mumbai");
        citiesList.Add("Chicago");
        citiesList.Add(null);// nulls are allowed for reference type list
        Console.WriteLine("");
        Console.WriteLine("2. citiesList" + " has " + citiesList.Count + " elements.");

        //3. adding elements using collection-initializer syntax
        var countriesList = new List<string>()
                            {
                                "Slovakia",
                                "France",
                                "Germany",
                                "Ukraine"                    
                            };
        Console.WriteLine("");
        Console.WriteLine("3. countriesList" + " has " + countriesList.Count + " elements.");

        // 4. Add Custom Class Objects in List
        var studentsList = new List<Student>() { 
                new Student(){ Id = 1, Name="Bill"},
                new Student(){ Id = 2, Name="Steve"},
                new Student(){ Id = 3, Name="Ram"},
                new Student(){ Id = 4, Name="Abdul"}
            };
        Console.WriteLine("");
        Console.WriteLine("4. studentsList" + " has " + studentsList.Count + " elements.");
    }
}

class Student{
	public int Id { get; set; }
	public string Name { get; set; }
}
```
```
> 1. primeNumbersList has 4 elements.
> 
> 2. citiesList has 5 elements.
> 
> 3. countriesList has 4 elements.
> 
> 4. studentsList has 4 elements.
```


---



## ACCESSING LIST ELEMENTS

A list can be accessed using:
- an index,
- a for/foreach loop,
- using LINQ queries.

Indexes of a list start from zero. Pass an index in the square brackets to access individual list items, same as array. Use a `foreach` or `for` loop to iterate a `List<T>` collection.


Example: **Access a list using an `index`**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{		
		List<int> intList = new List<int>() { 10, 20, 30, 40, 50 };	// Our list

		Console.WriteLine(intList[0]); // Access using an index
	}
}
```
```
> 10
```


Example: **Access a list using a `Foreach` loop**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{		
		List<int> intList = new List<int>() { 10, 20, 30};	// Our list

		// Method 1
		intList.ForEach(el => Console.WriteLine(el));

		Console.WriteLine("");

		// Method 2
		foreach (var el in intList)
        	Console.WriteLine(el);
	}
}
```
```
> 10
> 20
> 30
> 
> 10
> 20
> 30
```


Example: **Access a list using a `For` loop**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{		
		List<int> intList = new List<int>() { 10, 20, 30 };	// Our list

		for(int i =0; i < intList.Count; i++)
			Console.WriteLine(intList[i]);
	}
}
```
```
> 10
> 20
> 30
```


Example: **Access a list using LINQ method**
```cs
// The List<T> implements the IEnumerable interface. So, we can query a list using LINQ query syntax or method syntax, as shown below.
using System;
using System.Linq;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{
		var students = new List<Student>() { 
                new Student(){ Id = 1, Name="Bill" },
                new Student(){ Id = 2, Name="Steve" },
                new Student(){ Id = 3, Name="Ram" },
                new Student(){ Id = 4, Name="Abdul" },
				new Student(){ Id = 5, Name="Bill" }
		};
		
		//get all students whose name is Bill
		var studNames = from s in students
			where s.Name == "Bill"
			select s;
		
		foreach(var student in studNames)
			Console.WriteLine("ID: " + student.Id + ", Name: " +student.Name);
	}
}

public class Student
{ 
	public int Id { get; set; }
	public string Name { get; set; }
}
```
```
> ID: 1, Name: Bill
> ID: 5, Name: Bill
```