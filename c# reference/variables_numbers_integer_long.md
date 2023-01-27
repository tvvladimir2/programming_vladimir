# C# LONG


---


## LINKS

[]()



---



## 7. DESCRIPTION

The `long` type is `64-bit signed integers`. It can store numbers from `-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807`.
Use l or L suffix with number to assign it to long type variable. The long keyword is an alias of Int64 struct in .NET.

The `ulong` type stores positive numbers from `0 to 18,446,744,073,709,551,615`.
If a number is suffixed by UL, Ul, uL, ul, LU, Lu, lU, or lu, its type is ulong.
The ulong keyword is an alias of UInt64 struct in .NET.



---



## INITIALIZATION

```cs
long l1 = -9223372036854775808;
long l2 = 9223372036854775807;

ulong ul1 = 18223372036854775808ul;
ulong ul2 = 18223372036854775808UL;

Console.WriteLine(Int64.MaxValue);//9223372036854775807
Console.WriteLine(Int64.MinValue);//-9223372036854775808
Console.WriteLine(UInt64.MaxValue);//18446744073709551615
Console.WriteLine(UInt64.MinValue);//0
```