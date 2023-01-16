# C# DICTIONARY: CONSTRUCTORS


---


## LINKS

[Constructors](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2?view=net-7.0)



---



## CONSTRUCTORS

| # | Constructor                                                                              | Description                                                                                                                                                                                        |
|---|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Dictionary<TKey,TValue>()                                                                | Initializes a new instance of the Dictionary<TKey,TValue> class that is empty, has the default initial capacity, and uses the default equality comparer for the key type.                          |
| 2 | Dictionary<TKey,TValue>(IDictionary<TKey,TValue>)                                        | Initializes a new instance of the Dictionary<TKey,TValue> class that contains elements copied from the specified IDictionary<TKey,TValue> and uses the default equality comparer for the key type. |
| 3 | Dictionary<TKey,TValue>(IDictionary<TKey,TValue>, IEqualityComparer<TKey>)               | Initializes a new instance of the Dictionary<TKey,TValue> class that contains elements copied from the specified IDictionary<TKey,TValue> and uses the specified IEqualityComparer<T>.             |
| 4 | Dictionary<TKey,TValue>(IEnumerable<KeyValuePair<TKey,TValue>>)                          | Initializes a new instance of the Dictionary<TKey,TValue> class that contains elements copied from the specified IEnumerable<T>.                                                                   |
| 5 | Dictionary<TKey,TValue>(IEnumerable<KeyValuePair<TKey,TValue>>, IEqualityComparer<TKey>) | Initializes a new instance of the Dictionary<TKey,TValue> class that contains elements copied from the specified IEnumerable<T> and uses the specified IEqualityComparer<T>.                       |
| 6 | Dictionary<TKey,TValue>(IEqualityComparer<TKey>)                                         | Initializes a new instance of the Dictionary<TKey,TValue> class that is empty, has the default initial capacity, and uses the specified IEqualityComparer<T>.                                      |
| 7 | Dictionary<TKey,TValue>(Int32)                                                           | Initializes a new instance of the Dictionary<TKey,TValue> class that is empty, has the specified initial capacity, and uses the default equality comparer for the key type.                        |
| 8 | Dictionary<TKey,TValue>(Int32, IEqualityComparer<TKey>)                                  | Initializes a new instance of the Dictionary<TKey,TValue> class that is empty, has the specified initial capacity, and uses the specified IEqualityComparer<T>.                                    |
| 9 | Dictionary<TKey,TValue>(SerializationInfo, StreamingContext)                             | Initializes a new instance of the Dictionary<TKey,TValue> class with serialized data.                                                                                                              |