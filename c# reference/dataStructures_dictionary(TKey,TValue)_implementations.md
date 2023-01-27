# C# DICTIONARY: Explicit Interface Implementations


---


## LINKS

[Explicit Interface Implementations](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-7.0)



---



## EXPLICIT INTERFACE IMPLEMENTATION

| #  | Explicit Interface Implementation                                                 |                                                                                                                                 |
|----|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 1  | ICollection.CopyTo(Array, Int32)                                                  | Copies the elements of the ICollection<T> to an array, starting at the specified array index.                                   |
| 2  | ICollection.IsSynchronized                                                        | Gets a value that indicates whether access to the ICollection is synchronized (thread safe).                                    |
| 3  | ICollection.SyncRoot                                                              | Gets an object that can be used to synchronize access to the ICollection.                                                       |
| 4  | ICollection<KeyValuePair<TKey,TValue>>.Add(KeyValuePair<TKey,TValue>)             | Adds the specified value to the ICollection<T> with the specified key.                                                          |
| 5  | ICollection<KeyValuePair<TKey,TValue>>.Contains(KeyValuePair<TKey,TValue>)        | Determines whether the ICollection<T> contains a specific key and value.                                                        |
| 6  | ICollection<KeyValuePair<TKey,TValue>>.CopyTo(KeyValuePair<TKey,TValue>[], Int32) | Copies the elements of the ICollection<T> to an array of type KeyValuePair<TKey,TValue>, starting at the specified array index. |
| 7  | ICollection<KeyValuePair<TKey,TValue>>.IsReadOnly                                 | Gets a value that indicates whether the dictionary is read-only.                                                                |
| 8  | ICollection<KeyValuePair<TKey,TValue>>.Remove(KeyValuePair<TKey,TValue>)          | Removes a key and value from the dictionary.                                                                                    |
| 9  | IDictionary.Add(Object, Object)                                                   | Adds the specified key and value to the dictionary.                                                                             |
| 10 | IDictionary.Contains(Object)                                                      | Determines whether the IDictionary contains an element with the specified key.                                                  |
| 11 | IDictionary.GetEnumerator()                                                       | Returns an IDictionaryEnumerator for the IDictionary.                                                                           |
| 12 | IDictionary.IsFixedSize                                                           | Gets a value that indicates whether the IDictionary has a fixed size.                                                           |
| 13 | IDictionary.IsReadOnly                                                            | Gets a value that indicates whether the IDictionary is read-only.                                                               |
| 14 | IDictionary.Item[Object]                                                          | Gets or sets the value with the specified key.                                                                                  |
| 15 | IDictionary.Keys                                                                  | Gets an ICollection containing the keys of the IDictionary.                                                                     |
| 16 | IDictionary.Remove(Object)                                                        | Removes the element with the specified key from the IDictionary.                                                                |
| 17 | IDictionary.Values                                                                | Gets an ICollection containing the values in the IDictionary.                                                                   |
| 18 | IDictionary<TKey,TValue>.Keys                                                     | Gets an ICollection<T> containing the keys of the IDictionary<TKey,TValue>.                                                     |
| 19 | IDictionary<TKey,TValue>.Values                                                   | Gets an ICollection<T> containing the values in the IDictionary<TKey,TValue>.                                                   |
| 20 | IEnumerable.GetEnumerator()                                                       | Returns an enumerator that iterates through the collection.                                                                     |
| 21 | IEnumerable<KeyValuePair<TKey,TValue>>.GetEnumerator()                            | Returns an enumerator that iterates through the collection.                                                                     |
| 22 | IReadOnlyDictionary<TKey,TValue>.Keys                                             | Gets a collection containing the keys of the IReadOnlyDictionary<TKey,TValue>.                                                  |
| 23 | IReadOnlyDictionary<TKey,TValue>.Values                                           | Gets a collection containing the values of the IReadOnlyDictionary<TKey,TValue>.                                                |