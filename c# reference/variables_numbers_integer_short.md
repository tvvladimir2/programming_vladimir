#


---


## LINKS

[]()



---



## DESCRIPTION

The `short` data type is a `signed integer` that can store numbers from `-32,768 to 32,767`. It occupies `16-bit memory`.
The short keyword is an alias for Int16 struct in .NET.

The `ushort` data type is an `unsigned integer`. It can store only positive numbers from `0 to 65,535`.
The ushort keyword is an alias for UInt16 struct in .NET. 



---



## INITIALIZE

```cs
short s1 = -32768;
short s2 = 32767;
short s3 = 35000;   //Compile-time error: Constant value '35000' cannot be converted to a 'short'

ushort us1 = 65535;
ushort us2 = -32000;    //Compile-time error: Constant value '-32000' cannot be converted to a 'ushort'

Console.WriteLine(Int16.MaxValue);  //32767
Console.WriteLine(Int16.MinValue);  //-32768
Console.WriteLine(UInt16.MaxValue); //65535
Console.WriteLine(UInt16.MinValue); //0
```