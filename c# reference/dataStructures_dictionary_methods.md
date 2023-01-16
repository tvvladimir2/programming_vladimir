# C# DICTIONARY METHODS


---


## LINKS

[Methods ](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-7.0)



---



## METHODS TABLE

| #  | Methods                                            | Description                                                                                                                          |
|----|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Add(TKey, TValue)                                  | Adds the specified key and value to the dictionary.                                                                                  |
| 2  | Clear()                                            | Removes all keys and values from the Dictionary<TKey,TValue>.                                                                        |
| 3  | ContainsKey(TKey)                                  | Determines whether the Dictionary<TKey,TValue> contains the specified key.                                                           |
| 4  | ContainsValue(TValue)                              | Determines whether the Dictionary<TKey,TValue> contains a specific value.                                                            |
| 5  | EnsureCapacity(Int32)                              | Ensures that the dictionary can hold up to a specified number of entries without any further expansion of its backing storage.       |
| 6  | Equals(Object)                                     | Determines whether the specified object is equal to the current object. (Inherited from   Object)                                    |
| 7  | GetEnumerator()                                    | Returns an enumerator that iterates through the Dictionary<TKey,TValue>.                                                             |
| 8  | GetHashCode()                                      | Serves as the default hash function. (Inherited from   Object)                                                                       |
| 9  | GetObjectData(SerializationInfo, StreamingContext) | Implements the ISerializable interface and returns the data needed to serialize the Dictionary<TKey,TValue> instance.                |
| 10 | GetType()                                          | Gets the Type of the current instance. (Inherited from   Object)                                                                     |
| 11 | MemberwiseClone()                                  | Creates a shallow copy of the current Object. (Inherited from   Object)                                                              |
| 12 | OnDeserialization(Object)                          | Implements the ISerializable interface and raises the deserialization event when the deserialization is complete.                    |
| 13 | Remove(TKey)                                       | Removes the value with the specified key from the Dictionary.                                                                        |
| 14 | Remove(TKey, TValue)                               | Removes the value with the specified key from the Dictionary<TKey,TValue>, and copies the element to the value parameter.            |
| 15 | ToString()                                         | Returns a string that represents the current object. (Inherited from   Object)                                                       |
| 16 | TrimExcess()                                       | Sets the capacity of this dictionary to what it would be if it had been originally initialized with all its entries.                 |
| 17 | TrimExcess(Int32)                                  | Sets the capacity of this dictionary to hold up a specified number  of entries without any further expansion of its backing storage. |
| 18 | TryAdd(TKey, TValue)                               | Attempts to add the specified key and value to the dictionary.                                                                       |
| 19 | TryGetValue(TKey, TValue)                          | Gets the value associated with the specified key.                                                                                    |



---



### 1. Add(TKey, TValue)

C# provides the Add() method using which we can add elements in the dictionary. For example,

```cs
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> mySongs = new Dictionary<string, string>();

        // add items to dictionary
        mySongs.Add("Queen", "Break Free");
        mySongs.Add("Free", "All right now");
        mySongs.Add("Pink Floyd", "The Wall");

        // iterate through the car dictionary 
        foreach (KeyValuePair<string, string> items in mySongs)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }
    }
}
```
```
> Queen : Break Free  
> Free : All right now
> Pink Floyd : The Wall
```

In the above example, we have created a Dictionary<TKey, TValue> named mySongs.

Here we have added key/value pairs using the Add() method where,

- keys: "Queen", "Free" and "Pink Floyd"
- values: "Break Free", "All right now" and "The Wall"



---



### 13. Remove(TKey)

Removes the key/value pair from the dictionary.

```cs
using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> employee = new Dictionary<string, string>();

        // add items to dictionary
        employee.Add("Name", "Marry");
        employee.Add("Role", "Manager");
        employee.Add("Address", "California");

        Console.WriteLine("Original Dictionary :");

        // iterate through the modified dictionary 
        foreach (KeyValuePair<string, string> items in employee)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }

        // remove value with key "Role"
        employee.Remove("Role");

        Console.WriteLine("\nModified Dictionary :");

        // iterate through the modified dictionary 
        foreach (KeyValuePair<string, string> items in employee)
        {
            Console.WriteLine("{0} : {1}", items.Key, items.Value);
        }
    }
}
```
```
> Original Dictionary :
> Name : Marry
> Role : Manager
> Address : California
>
> Modified Dictionary :
> Name : Marry
> Address : California
```

In the above example, we have removed the element whose key is `Role`.

Here, `employee.Remove("Role")` removes the key/value pair `"Role" : "Manager"` from the `employee` dictionary.

So when we iterate through `employee` we get a modified dictionary.

Note: If you want to remove all the elements of the dictionary, use the `Clear()` method.