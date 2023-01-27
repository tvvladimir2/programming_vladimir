# C# Dictionary<TKey,TValue> Class


---


## LINKS

[C# - Dictionary<TKey, TValue>](https://www.tutorialsteacher.com/csharp/csharp-dictionary)

[Dictionary<TKey,TValue> Class](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-7.0)



---



## SYNTAX

```cs
Dictionary<TKey, TValue> dictionaryName = new Dictionary<TKey, TValue>();
```

|        | Description                               |
|--------|-------------------------------------------|
| TKey   | The type of the keys in the dictionary.   |
| TValue | The type of the values in the dictionary. |



---



## DEFINITION

Represents a collection of keys and values. A Dictionary<TKey, TValue> is a generic collection that consists of elements as key/value pairs that are not sorted in an order. For example,

```cs
Dictionary<int, string> country = new Dictionary<int, string>();
```


In example above, `country` is a dictionary that contains `int` type keys and `string` type values.


Charechteristics:

- **Key-value pairs**: The `Dictionary<Tkey, TValue>` is a generic collection that stores data in the form of key-value pairs without any specific order.
  
- **No duplicate keys**: A Dictionary does not allow duplicate keys. If you try to add a key-value pair with a key that already exists in the Dictionary, it will give you compile time error.
  
- **Empty values**: A Dictionary can hold empty values, but the key cannot be empty.
  
- **Data types**: Both the keys and values in a Dictionary must be of a designated data type. The data types for both the keys and values must be specified when creating the Dictionary.
  
- **Thread safety**: By default, a Dictionary is not thread-safe. If you need a thread-safe collection, you can use a ConcurrentDictionary.
  
- **Namespace**: You must import the `System.Collections.Generic` namespace before you can use the Dictionary class in your code.
  
- **Searching elements**: we can easily search or remove elements from the dictionary in C# using a key.



---



## TYPE PARAMETERS

- Namespace: System.Collections.Generic 
- Assembly: System.Collections.dll


|        | Description                               |
|--------|-------------------------------------------|
| TKey   | The type of the keys in the dictionary.   |
| TValue | The type of the values in the dictionary. |


```cs
Inheritance Object >> Dictionary<TKey,TValue>
```


- Derived: System.ServiceModel.MessageQuerySet


Implements:
    - ICollection<KeyValuePair<TKey,TValue>>,
    - IDictionary<TKey,TValue>,
    - IEnumerable<KeyValuePair<TKey,TValue>>,
    - IEnumerable<T>,
    - IReadOnlyCollection<KeyValuePair<TKey,TValue>>,
    - IReadOnlyDictionary<TKey,TValue>,
    - ICollection,
    - IDictionary,
    - IEnumerable,
    - IDeserializationCallback,
    - ISerializable



```cs
public class Dictionary<TKey,TValue> : System.Collections.Generic.ICollection<System.Collections.Generic.KeyValuePair<TKey,TValue>>, System.Collections.Generic.IDictionary<TKey,TValue>, System.Collections.Generic.IEnumerable<System.Collections.Generic.KeyValuePair<TKey,TValue>>, System.Collections.Generic.IReadOnlyCollection<System.Collections.Generic.KeyValuePair<TKey,TValue>>, System.Collections.Generic.IReadOnlyDictionary<TKey,TValue>, System.Collections.IDictionary, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable
```

---



## CREATE DISCTIONARY

To create a dictionary in C#, we need to use the System.Collections.Generic namespace. Here is how we can create a dictionary in C#.

Example: **Create a C# dictionary**
```cs
// dictionaryName: name of the dictionary
// dataType1: datatype of keys
// dataType2: datatype of values
Dictionary<dataType1, dataType2> dictionaryName = new Dictionary<dataType1, dataType2>();
```


Example: **Create a C# dictionary with 3 items and print item with Tkey `3`**
```cs
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<int, string> country = new Dictionary<int, string>();


        // add items to dictionary
        country.Add(5, "Brazil");   // The keys are of `int` type and values are of `string` type.
        country.Add(3, "China");
        country.Add(4, "Usa");

        // print value having key is 3        
        Console.WriteLine("Value having key 3: " + country[3]);
    }
}
```
```
Value having key 3: China
```



---



## ACCESS DICTIONARY ELEMENTS

We can access the elements inside the dictionary using it's keys. For example,

Example: **Access distionary elements using it's keys**
```cs
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> student = new Dictionary<string, string>();

        // add items to dictionary
        student.Add("Name", "Susan");
        student.Add("Faculty", "History");

        // access the value having key "Name"
        Console.WriteLine(student["Name"]);

        // access the value having key "Faculty"
        Console.WriteLine(student["Faculty"]);
    }
}
```
```
> Susan
> History
```

In the above example, we have accessed the values of the dictionary using their keys:

    student["Name"] - accesses the value whose key is "Name"
    student["Faculty"] - accesses the value whose key is "Faculty"



---



## ITERATE THROUGH DICTIONARY

In C#, we can also loop through each element of the dictionary using a `foreach` loop. For example,

Example: **Iterate through a dictionary using `foreach` loop**
```cs
// We loop through car using a foreach loop.
// Here, the Key and Value property returns a collection containing keys and values in the dictionary.
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> car = new Dictionary<string, string>();

        // add items to dictionary
        car.Add("Model", "Hyundai");
        car.Add("Price", "36K");

        // iterate through the car dictionary 
        foreach (KeyValuePair<string, string> items in car)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }
    }
}
```
```
> Model : Hyundai
> Price : 36K
``` 


Example: **Iterate through a list using `for` loop**
```cs
// To get KeyValuePair<TKey,TValue> at a specified index in a sequence, we use the ElementAt() method.
// Thus for every entry in the for loop, at the specified index, we can perform any required operation:
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{	
		var monthsInYear = new Dictionary<int, string>
		{
			{1, "January" },
			{2, "February" },
			{3, "March" },
		};

		for (int index = 0; index < monthsInYear.Count; index++)
			{
				KeyValuePair<int, string> month = monthsInYear.ElementAt(index);
				Console.WriteLine($"{month.Key}: {month.Value}");
			}
	}
}
```
```
1: January
2: February
3: March
```


Example: **Iterate through a list using `ParallelEnumerable.ForAll()` Method**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{	
		var monthsInYear = new Dictionary<int, string>
		{
			{1, "January" },
			{2, "February" },
			{3, "March" },
		};

		monthsInYear.AsParallel()
			.ForAll(month => Console.WriteLine($"{month.Key} : {month.Value}"));
	}
}
```
```
> 3 : March
> 2 : February
> 1 : January 
```



---



## CHANGE DICTIONARY ELEMENTS

We can change the value of elements in dictionary as:

```cs
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> car = new Dictionary<string, string>();

        // add items to dictionary
        car.Add("Model", "Hyundai");
        car.Add("Price", "36K");

        // print the original value
        Console.WriteLine("Value of Model before changing: " + car["Model"]);

        // change the value of "Model" key to "Maruti"
        car["Model"] = "Maruti";

        // print new updated value of "Model"
        Console.WriteLine("Value of Model after changing: " + car["Model"]);
    }
}
```
```
Value of Model before changing: Hyundai
Value of Model after changing: Maruti
```



---



## 