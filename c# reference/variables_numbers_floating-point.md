# FLOATING-POINT TYPES


---


## DESCRIPTION

`Floating-point type` is numbers with one or more decimal points. It can be negative or positive numbers.

| # | type/keyword |        Approximate range       |   Precision   |   Size   |    .NET type   |
|---|:------------:|:------------------------------:|:-------------:|:--------:|:--------------:|
| 1 | float        | ±1.5 x 10−45 to ±3.4 x 1038    | ~6-9 digits   | 4 bytes  | System.Single  |
| 2 | double       | ±5.0 × 10−324 to ±1.7 × 10308  | ~15-17 digits | 8 bytes  | System.Double  |
| 3 | decimal      | ±1.0 x 10-28 to ±7.9228 x 1028 | 28-29 digits  | 16 bytes | System.Decimal |


---


## FLOAT TYPE

The float data type can store fractional numbers from 3.4e−038 to 3.4e+038. It occupies 4 bytes in the memory.
The float keyword is an alias of Single struct in .NET.

Use f or F suffix with literal to make it float type. 

```cs
// INITIAZLIZE
float f1 = 123456.5F;
float f2 = 1.123456f;

// Power of 10
float f = 123.45e-2f;
Console.WriteLine(f);  // 1.2345

// OUTPUT
Console.WriteLine(f1);  //123456.5
Console.WriteLine(f2);  //1.123456
```


---


## DOUBLE TYPE

 The double data type can store fractional numbers from 1.7e−308 to 1.7e+308. It occupies 8 bytes in the memory. The double keyword is an alias of the Double struct in .NET.

Use d or D suffix with literal to make it double type.

```cs
// INITIALIZE
double d1 = 12345678912345.5d;
double d2 = 1.123456789123456d;

// Use e or E to indicate the power of 10 as exponent part of scientific notation
double d = 0.12e2;
Console.WriteLine(d);  // 12;

// OUTPUT
Console.WriteLine(d1);  //12345678912345.5
Console.WriteLine(d2);  //1.123456789123456
```


---


## DECIMAL TYPE

The decimal data type can store fractional numbers from `±1.0 x 10-28 to ±7.9228 x 1028`.
It occupies `16 bytes` in the memory. The decimal is a keyword alias of the Decimal struct in .NET.
Use `m` or `M` suffix with literal to make it decimal type.

**USED FOR**:
The decimal type has more precision and a smaller range than both float and double, and so it is appropriate for financial and monetary calculations.

```cs
// INITIALIZE
decimal d1 = 123456789123456789123456789.5m;
decimal d2 = 1.1234567891345679123456789123m;

// Power of 10
decimal m = 1.2e6m;
Console.WriteLine(m);// 1200000

// OUTPUT
Console.WriteLine(d1);
Console.WriteLine(d2);
```


---