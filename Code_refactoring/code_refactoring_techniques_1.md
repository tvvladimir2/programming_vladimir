## CODE REFACTORING TECHNIQUE: COMPOSITING METHODS


---


## LINKS

[Refactoring Techniques](https://refactoring.guru/refactoring/techniques)


---


## 1. COMPOSITING METHODS

Much of refactoring is devoted to correctly composing methods. In most cases, excessively long methods are the root of all evil. The vagaries of code inside these methods conceal the execution logic and make the method extremely hard to understand—and even harder to change.

The refactoring techniques in this group streamline methods, remove code duplication, and pave the way for future improvements.

- 1.1 Extract Method
- 1.2 Inline Method
- 1.3 Extract Variable
- 1.4 Inline Temp
- 1.5 Replace Temp with Query
- 1.6 Split Temporary Variable
- 1.7 Remove Assignments to Parameters
- 1.8 Replace Method with Method Object
- 1.9 Substitute Algorithm


---


## 1.1 Extract Method

**Problem**

You have a code fragment that can be grouped together.

```cs
void PrintOwing() 
{
  this.PrintBanner();

  // Print details.
  Console.WriteLine("name: " + this.name);
  Console.WriteLine("amount: " + this.GetOutstanding());
}
```


**Solution**

Move this code to a separate new method (or function) and replace the old code with a call to the method.

```cs
void PrintOwing()
{
  this.PrintBanner();
  this.PrintDetails();
}

void PrintDetails()
{
  Console.WriteLine("name: " + this.name);
  Console.WriteLine("amount: " + this.GetOutstanding());
}
```


---


## 1.2 Inline Method

**Problem**

When a method body is more obvious than the method itself, use this technique.

```cs
class PizzaDelivery 
{
  // ...
  int GetRating() 
  {
    return MoreThanFiveLateDeliveries() ? 2 : 1;
  }
  bool MoreThanFiveLateDeliveries() 
  {
    return numberOfLateDeliveries > 5;
  }
}
```


**Solution**

Replace calls to the method with the method’s content and delete the method itself.

```cs
class PizzaDelivery 
{
  // ...
  int GetRating() 
  {
    return numberOfLateDeliveries > 5 ? 2 : 1;
  }
}
```


---


## 1.3 Extract Variable

**Problem**

You have an expression that’s hard to understand.

```cs
void RenderBanner() 
{
  if ((platform.ToUpper().IndexOf("MAC") > -1) &&
       (browser.ToUpper().IndexOf("IE") > -1) &&
        wasInitialized() && resize > 0 )
  {
    // do something
  }
}
```


**Solution**

Place the result of the expression or its parts in separate variables that are self-explanatory.


```cs
void RenderBanner() 
{
  readonly bool isMacOs = platform.ToUpper().IndexOf("MAC") > -1;
  readonly bool isIE = browser.ToUpper().IndexOf("IE") > -1;
  readonly bool wasResized = resize > 0;

  if (isMacOs && isIE && wasInitialized() && wasResized) 
  {
    // do something
  }
}
```


---


## 1.4 Inline Temp

**Problem**

You have a temporary variable that’s assigned the result of a simple expression and nothing more.

```cs
bool HasDiscount(Order order)
{
  double basePrice = order.BasePrice();
  return basePrice > 1000;
}
```

**Solution**

Replace the references to the variable with the expression itself.

```cs
bool HasDiscount(Order order)
{
  return order.BasePrice() > 1000;
}
```


---


## 1.5 Replace Temp with Query

**Problem**

You place the result of an expression in a local variable for later use in your code.

```cs
double CalculateTotal() 
{
  double basePrice = quantity * itemPrice;
  
  if (basePrice > 1000) 
  {
    return basePrice * 0.95;
  }
  else 
  {
    return basePrice * 0.98;
  }
}
```


**Solution**

Move the entire expression to a separate method and return the result from it. Query the method instead of using a variable. Incorporate the new method in other methods, if necessary.

```cs
double CalculateTotal() 
{
  if (BasePrice() > 1000) 
  {
    return BasePrice() * 0.95;
  }
  else 
  {
    return BasePrice() * 0.98;
  }
}
double BasePrice() 
{
  return quantity * itemPrice;
}
```


---


## 1.6 Split Temporary Variable

**Problem**

You have a local variable that’s used to store various intermediate values inside a method (except for cycle variables).

```cs
double temp = 2 * (height + width);
Console.WriteLine(temp);
temp = height * width;
Console.WriteLine(temp);
```


**Solution**

Use different variables for different values. Each variable should be responsible for only one particular thing.

```cs
readonly double perimeter = 2 * (height + width);
Console.WriteLine(perimeter);
readonly double area = height * width;
Console.WriteLine(area);
```


---


## 1.7 Remove Assignments to Parameters

**Problem**

Some value is assigned to a parameter inside method’s body.

```cs
int Discount(int inputVal, int quantity) 
{
  if (quantity > 50) 
  {
    inputVal -= 2;
  }
  // ...
}
```


**Solution**

Use a local variable instead of a parameter.

```cs
int Discount(int inputVal, int quantity) 
{
  int result = inputVal;
  
  if (quantity > 50) 
  {
    result -= 2;
  }
  // ...
}
```


---


## 1.8 Replace Method with Method Object

**Problem**

You have a long method in which the local variables are so intertwined that you can’t apply Extract Method.

```cs
public class Order 
{
  // ...
  public double Price() 
  {
    double primaryBasePrice;
    double secondaryBasePrice;
    double tertiaryBasePrice;
    // Perform long computation.
  }
}
```


**Solution**

Transform the method into a separate class so that the local variables become fields of the class. Then you can split the method into several methods within the same class.

```cs
public class Order 
{
  // ...
  public double Price() 
  {
    return new PriceCalculator(this).Compute();
  }
}

public class PriceCalculator 
{
  private double primaryBasePrice;
  private double secondaryBasePrice;
  private double tertiaryBasePrice;
  
  public PriceCalculator(Order order) 
  {
    // Copy relevant information from the
    // order object.
  }
  
  public double Compute() 
  {
    // Perform long computation.
  }
}
```


---


## 1.9 Substitute Algorithm

**Problem**

So you want to replace an existing algorithm with a new one?

```cs
string FoundPerson(string[] people)
{
  for (int i = 0; i < people.Length; i++) 
  {
    if (people[i].Equals("Don"))
    {
      return "Don";
    }
    if (people[i].Equals("John"))
    {
      return "John";
    }
    if (people[i].Equals("Kent"))
    {
      return "Kent";
    }
  }
  return String.Empty;
}
```


**Solution**

Replace the body of the method that implements the algorithm with a new algorithm.

```cs
string FoundPerson(string[] people)
{
  List<string> candidates = new List<string>() {"Don", "John", "Kent"};
  
  for (int i = 0; i < people.Length; i++) 
  {
    if (candidates.Contains(people[i])) 
    {
      return people[i];
    }
  }
  
  return String.Empty;
}
```

