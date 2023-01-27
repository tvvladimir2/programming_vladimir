# C# DATA TYPES: INTEGRAL: INTEGER TYPES: BYTE & SBYTE TYPES


---


## LINKS

[]()



---



## DESCRIPTION

The `byte` data type stores numbers from `0 to 255`. It occupies `8-bit in the memory`.
The byte keyword is an alias of the Byte struct in .NET.

The `sbyte` is the same as byte, but it can store negative numbers from `-128 to 127`.
The sbyte keyword is an alias for SByte struct in .NET.



---



## INITIALIZE

```cs
// Initialize
byte b1 = 255;
byte b2 = -128; // compile-time error: Constant value '-128' cannot be converted to a 'byte'
sbyte sb1 = -128;
sbyte sb2 = 127;

// Check range
Console.WriteLine(Byte.MaxValue);   //255
Console.WriteLine(Byte.MinValue);   //0
Console.WriteLine(SByte.MaxValue);  //127
Console.WriteLine(SByte.MinValue);  //-128
```