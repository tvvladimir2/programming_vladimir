# C# LIST <T> CLASS: EMTHODS


## LINKS

[List<T> Class: METHODS](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1?view=net-7.0)



---


## TABLE

| #  | Method                                      | Description                                                                                                                                                                                                                                                                      |
|----|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Add(T)                                      | Adds an object to the end of the List<T>.                                                                                                                                                                                                                                        |
| 2  | AddRange(IEnumerable<T>)                    | Adds the elements of the specified collection to the end of the List<T>.                                                                                                                                                                                                         |
| 3  | AsReadOnly()                                | Returns a read-only ReadOnlyCollection<T> wrapper for the current collection.                                                                                                                                                                                                    |
| 4  | BinarySearch(Int32, Int32, T, IComparer<T>) | Searches a range of elements in the sorted List<T> for an element using the specified comparer and returns the zero-based index of the element.                                                                                                                                  |
| 5  | BinarySearch(T)                             | Searches the entire sorted List<T> for an element using the default comparer and returns the zero-based index of the element.                                                                                                                                                    |
| 6  | BinarySearch(T, IComparer<T>)               | Searches the entire sorted List<T> for an element using the specified comparer and returns the zero-based index of the element.                                                                                                                                                  |
| 7  | Clear()                                     | Removes all elements from the List<T>.                                                                                                                                                                                                                                           |
| 8  | Contains(T)                                 | Determines whether an element is in the List<T>.                                                                                                                                                                                                                                 |
| 9  | ConvertAll<TOutput>(Converter<T,TOutput>)   | Converts the elements in the current List<T> to another type, and returns a list containing the converted elements.                                                                                                                                                              |
| 10 | CopyTo(Int32, T[], Int32, Int32)            | Copies a range of elements from the List<T> to a compatible one-dimensional array, starting at the specified index of the target array.                                                                                                                                          |
| 11 | CopyTo(T[])                                 | Copies the entire List<T> to a compatible one-dimensional array, starting at the beginning of the target array.                                                                                                                                                                  |
| 12 | CopyTo(T[], Int32)                          | Copies the entire List<T> to a compatible one-dimensional array, starting at the specified index of the target array.                                                                                                                                                            |
| 13 | EnsureCapacity(Int32)                       | Ensures that the capacity of this list is at least the specified capacity. If the current capacity is less than capacity, it is successively increased to twice the current capacity until it is at least the specified capacity.                                                |
| 14 | Equals(Object)                              | Determines whether the specified object is equal to the current object. (Inherited from   Object)                                                                                                                                                                                |
| 15 | Exists(Predicate<T>)                        | Determines whether the List<T> contains elements that match the conditions defined by the specified predicate.                                                                                                                                                                   |
| 16 | Find(Predicate<T>)                          | Searches for an element that matches the conditions defined by the  specified predicate, and returns the first occurrence within the entire List<T>.                                                                                                                             |
| 17 | FindAll(Predicate<T>)                       | Retrieves all the elements that match the conditions defined by the specified predicate.                                                                                                                                                                                         |
| 18 | FindIndex(Int32, Int32, Predicate<T>)       | Searches for an element that matches the conditions defined by the  specified predicate, and returns the zero-based index of the first  occurrence within the range of elements in the List<T> that starts at the specified index and contains the specified number of elements. |
| 19 | FindIndex(Int32, Predicate<T>)              | Searches for an element that matches the conditions defined by the  specified predicate, and returns the zero-based index of the first  occurrence within the range of elements in the List<T> that extends from the specified index to the last element.                        |
| 20 | FindIndex(Predicate<T>)                     | Searches for an element that matches the conditions defined by the  specified predicate, and returns the zero-based index of the first occurrence within the entire List<T>.                                                                                                     |
| 21 | FindLast(Predicate<T>)                      | Searches for an element that matches the conditions defined by the  specified predicate, and returns the last occurrence within the entire List<T>.                                                                                                                              |
| 22 | FindLastIndex(Int32, Int32, Predicate<T>)   | Searches for an element that matches the conditions defined by the  specified predicate, and returns the zero-based index of the last  occurrence within the range of elements in the List<T> that contains the specified number of elements and ends at the specified index.    |
| 23 | FindLastIndex(Int32, Predicate<T>)          | Searches for an element that matches the conditions defined by the  specified predicate, and returns the zero-based index of the last  occurrence within the range of elements in the List<T> that extends from the first element to the specified index.                        |
| 24 | FindLastIndex(Predicate<T>)                 | Searches for an element that matches the conditions defined by the  specified predicate, and returns the zero-based index of the last  occurrence within the entire List<T>.                                                                                                     |
| 25 | ForEach(Action<T>)                          | Performs the specified action on each element of the List<T>.                                                                                                                                                                                                                    |
| 26 | GetEnumerator()                             | Returns an enumerator that iterates through the List<T>.                                                                                                                                                                                                                         |
| 27 | GetHashCode()                               | Serves as the default hash function.(Inherited from   Object)                                                                                                                                                                                                                    |
| 28 | GetRange(Int32, Int32)                      | Creates a shallow copy of a range of elements in the source List<T>.                                                                                                                                                                                                             |
| 29 | GetType()                                   | Gets the Type of the current instance. (Inherited from   Object)                                                                                                                                                                                                                 |
| 30 | IndexOf(T)                                  | Searches for the specified object and returns the zero-based index of the first occurrence within the entire List<T>.                                                                                                                                                            |
| 31 | IndexOf(T, Int32)                           | Searches for the specified object and returns the zero-based index of the first occurrence within the range of elements in the List<T> that extends from the specified index to the last element.                                                                                |
| 32 | IndexOf(T, Int32, Int32)                    | Searches for the specified object and returns the zero-based index of the first occurrence within the range of elements in the List<T> that starts at the specified index and contains the specified number of elements.                                                         |
| 33 | Insert(Int32, T)                            | Inserts an element into the List<T> at the specified index.                                                                                                                                                                                                                      |
| 34 | InsertRange(Int32, IEnumerable<T>)          | Inserts the elements of a collection into the List<T> at the specified index.                                                                                                                                                                                                    |
| 35 | LastIndexOf(T)                              | Searches for the specified object and returns the zero-based index of the last occurrence within the entire List<T>.                                                                                                                                                             |
| 36 | LastIndexOf(T, Int32)                       | Searches for the specified object and returns the zero-based index of the last occurrence within the range of elements in the List<T> that extends from the first element to the specified index.                                                                                |
| 37 | LastIndexOf(T, Int32, Int32)                | Searches for the specified object and returns the zero-based index of the last occurrence within the range of elements in the List<T> that contains the specified number of elements and ends at the specified index.                                                            |
| 38 | MemberwiseClone()                           | Creates a shallow copy of the current Object. (Inherited from   Object)                                                                                                                                                                                                          |
| 39 | Remove(T)                                   | Removes the first occurrence of a specific object from the List<T>.                                                                                                                                                                                                              |
| 40 | RemoveAll(Predicate<T>)                     | Removes all the elements that match the conditions defined by the specified predicate.                                                                                                                                                                                           |
| 41 | RemoveAt(Int32)                             | Removes the element at the specified index of the List<T>.                                                                                                                                                                                                                       |
| 42 | RemoveRange(Int32, Int32)                   | Removes a range of elements from the List<T>.                                                                                                                                                                                                                                    |
| 43 | Reverse()                                   | Reverses the order of the elements in the entire List<T>.                                                                                                                                                                                                                        |
| 44 | Reverse(Int32, Int32)                       | Reverses the order of the elements in the specified range.                                                                                                                                                                                                                       |
| 45 | Sort()                                      | Sorts the elements in the entire List<T> using the default comparer.                                                                                                                                                                                                             |
| 46 | Sort(Comparison<T>)                         | Sorts the elements in the entire List<T> using the specified Comparison<T>.                                                                                                                                                                                                      |
| 47 | Sort(IComparer<T>)                          | Sorts the elements in the entire List<T> using the specified comparer.                                                                                                                                                                                                           |
| 48 | Sort(Int32, Int32, IComparer<T>)            | Sorts the elements in a range of elements in List<T> using the specified comparer.                                                                                                                                                                                               |
| 49 | ToArray()                                   | Copies the elements of the List<T> to a new array.                                                                                                                                                                                                                               |
| 50 | ToString()                                  | Returns a string that represents the current object. (Inherited from   Object)                                                                                                                                                                                                   |
| 51 | TrimExcess()                                | Sets the capacity to the actual number of elements in the List<T>, if that number is less than a threshold value.                                                                                                                                                                |
| 52 | TrueForAll(Predicate<T>)                    | Determines whether every element in the List<T> matches the conditions defined by the specified predicate.                                                                                                                                                                       |



---



## 1. Add(T)





---



## 2. AddRange(IEnumerable<T>)

Use the `AddRange()` method to add all the elements from an array or another collection to List.

`AddRange()` signature: `void AddRange(IEnumerable<T> collection)` 

Example: **Adding an Array to a list**
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{
		string[] cities = new string[3]{ "Mumbai", "London", "New York" };	// Array1

		var popularCities = new List<string>();	// List1
        Console.WriteLine(popularCities.Count); // Show count of elements in a list before

		// Adding an Array1 to List1
		popularCities.AddRange(cities);

		Console.WriteLine(popularCities.Count);	// Show count of elements in a list after	
	}
}
```
```
> 0
> 3
```


Example: **Adding a List to a List
```cs
using System;
using System.Collections.Generic;

public class Program
{
	public static void Main()
	{
        var countriesList = new List<string>()	// List1
                            {
                                "Slovakia",
                                "France",
                                "Germany",
                                "Ukraine"                    
                            };

		var newList = new List<string>();	// new empty List2
		Console.WriteLine(newList.Count);	// Count before

		// Adding a List1 to List2 
		newList.AddRange(countriesList);
		Console.WriteLine(newList.Count);	// Count after
	}
}
```
```
> 0
> 4
```



---



## 7. Clear()

```cs
using System;
using System.Collections.Generic;

public class Program
{
   public static void Main()
   {
      List<string> myList = new List<string>(){"one","two","three"};

      Console.WriteLine("Elements in the list = " + myList.Count);
      
      myList.Clear();	// this makes a list empty
      Console.WriteLine("Elements in the list after using Clear() = " + myList.Count);
   }
}
```
```
> Elements in the list = 3
> Elements in the list after using Clear() = 0
```



---



## 8. Contains(T)

Use the `Contains()` method to determine whether an element is in the `List<T>` or not.

Example: **Check if list contains elements**
```cs
using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
		var numbers = new List<int>(){ 10, 20, 30, 40 };

		Console.WriteLine(numbers.Contains(10));	// returns True
		Console.WriteLine(numbers.Contains(11));	// returns False
	}
}
```
```
> True
> False
```



---



## 33. Insert(Int32, T)

 Use the `Insert()` method inserts an element into the `List<T>` collection at the specified index.

`Insert()` signature: `void Insert(int index, T item); `

Example: **Insert elements into List**
```cs
using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
		var numbers = new List<int>(){ 10, 20 };

		numbers.Insert(1, 11);// inserts 11 at 1st index: after 10.
		
		foreach (var num in numbers)
			Console.WriteLine(num);
	}
}
```
```
> 10
> 11
> 20
```



---



## 39. Remove(T)

Use the `Remove()` method to remove the `first occurrence of the specified element` in the `List<T>` collection. If no element at the specified index, then the `ArgumentOutOfRangeException` will be thrown.

Remove() signature: `bool Remove(T item)`

```cs
using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
		var numbers = new List<int>(){ 10, 20, 10};

		numbers.Remove(10); // removes 10 elements from a list

		foreach (var num in numbers)
			Console.WriteLine(num);
	}
}
```
```
> 20
> 10
```



---



## 41. RemoveAt(Int32)

Use the `RemoveAt()` method to remove an element from the specified index. If no element at the specified index, then the `ArgumentOutOfRangeException` will be thrown.

RemoveAt() signature: `void RemoveAt(int index)`

```cs
using System;
using System.Collections.Generic;
					
public class Program
{
	public static void Main()
	{
		var numbers = new List<int>(){ 10, 20, 30};
		
		numbers.RemoveAt(2); //removes the 3rd element, removes 30
		
		// numbers.RemoveAt(10); // Throws an exception, no such element

		foreach (var num in numbers)
			Console.WriteLine(num);
	}
}
```
```
> 10
> 20
``` 