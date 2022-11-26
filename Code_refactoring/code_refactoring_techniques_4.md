## CODE REFACTORING TECHNIQUES


---


## LINKS

[Refactoring Techniques](https://refactoring.guru/refactoring/techniques)


---


## 4. Simplifying Conditional Expressions

Conditionals tend to get more and more complicated in their logic over time, and there are yet more techniques to combat this as well.

- 4.1 Consolidate Conditional Expression
- 4.2 Consolidate Duplicate Conditional Fragments
- 4.3 Decompose Conditional
- 4.4 Replace Conditional with Polymorphism
- 4.5 Remove Control Flag
- 4.6 Replace Nested Conditional with Guard Clauses
- 4.7 Introduce Null Object
- 4.8 Introduce Assertion


---


## 4.1 Consolidate Conditional Expression

**Problem**

You have multiple conditionals that lead to the same result or action.

```cs
double DisabilityAmount() 
{
  if (seniority < 2) 
  {
    return 0;
  }
  if (monthsDisabled > 12) 
  {
    return 0;
  }
  if (isPartTime) 
  {
    return 0;
  }
  // Compute the disability amount.
  // ...
}
```


**Solution**

Consolidate all these conditionals in a single expression.
JavaC#PHPPythonTypeScript

```cs
double DisabilityAmount()
{
  if (IsNotEligibleForDisability())
  {
    return 0;
  }
  // Compute the disability amount.
  // ...
}
```


---


## 4.2 Consolidate Duplicate Conditional Fragments

**Problem**

Identical code can be found in all branches of a conditional.

```cs
if (IsSpecialDeal()) 
{
  total = price * 0.95;
  Send();
}
else 
{
  total = price * 0.98;
  Send();
}
```


**Solution**

Move the code outside of the conditional.

```cs
if (IsSpecialDeal())
{
  total = price * 0.95;
}
else
{
  total = price * 0.98;
}
Send();
```


---


## 4.3 Decompose Conditional

**Problem**

You have a complex conditional (if-then/else or switch).

```cs
if (date < SUMMER_START || date > SUMMER_END) 
{
  charge = quantity * winterRate + winterServiceCharge;
}
else 
{
  charge = quantity * summerRate;
}
```


**Solution**

Decompose the complicated parts of the conditional into separate methods: the condition, then and else.

```cs
if (isSummer(date))
{
  charge = SummerCharge(quantity);
}
else 
{
  charge = WinterCharge(quantity);
}
```


---


## 4.4 Remove Control Flag

**Problem**

You have a boolean variable that acts as a control flag for multiple boolean expressions.


**Solution**

Instead of the variable, use break, continue and return.


---


## 4.5 Replace Nested Conditional with Guard Clauses

**Problem**

You have a group of nested conditionals and it’s hard to determine the normal flow of code execution.

```cs
public double GetPayAmount()
{
  double result;
  
  if (isDead)
  {
    result = DeadAmount();
  }
  else 
  {
    if (isSeparated)
    {
      result = SeparatedAmount();
    }
    else 
    {
      if (isRetired)
      {
        result = RetiredAmount();
      }
      else
      {
        result = NormalPayAmount();
      }
    }
  }
  
  return result;
}
```


**Solution**

Isolate all special checks and edge cases into separate clauses and place them before the main checks. Ideally, you should have a “flat” list of conditionals, one after the other.

```cs
public double GetPayAmount() 
{
  if (isDead)
  {
    return DeadAmount();
  }
  if (isSeparated)
  {
    return SeparatedAmount();
  }
  if (isRetired)
  {
    return RetiredAmount();
  }
  return NormalPayAmount();
}
```


---


## 4.6 Replace Conditional with Polymorphism

**Problem**

You have a conditional that performs various actions depending on object type or properties.

```cs
public class Bird 
{
  // ...
  public double GetSpeed() 
  {
    switch (type) 
    {
      case EUROPEAN:
        return GetBaseSpeed();
      case AFRICAN:
        return GetBaseSpeed() - GetLoadFactor() * numberOfCoconuts;
      case NORWEGIAN_BLUE:
        return isNailed ? 0 : GetBaseSpeed(voltage);
      default:
        throw new Exception("Should be unreachable");
    }
  }
}
```


**Solution**

Create subclasses matching the branches of the conditional. In them, create a shared method and move code from the corresponding branch of the conditional to it. Then replace the conditional with the relevant method call. The result is that the proper implementation will be attained via polymorphism depending on the object class.

```cs
public abstract class Bird 
{
  // ...
  public abstract double GetSpeed();
}

class European: Bird 
{
  public override double GetSpeed() 
  {
    return GetBaseSpeed();
  }
}
class African: Bird 
{
  public override double GetSpeed() 
  {
    return GetBaseSpeed() - GetLoadFactor() * numberOfCoconuts;
  }
}
class NorwegianBlue: Bird
{
  public override double GetSpeed() 
  {
    return isNailed ? 0 : GetBaseSpeed(voltage);
  }
}

// Somewhere in client code
speed = bird.GetSpeed();
```


---


## 4.7 Introduce Null Object

**Problem**

Since some methods return null instead of real objects, you have many checks for null in your code.

```cs
if (customer == null) 
{
  plan = BillingPlan.Basic();
}
else 
{
  plan = customer.GetPlan();
}
```


**Solution**

Instead of null, return a null object that exhibits the default behavior.

```cs
public sealed class NullCustomer: Customer 
{
  public override bool IsNull 
  {
    get { return true; }
  }
  
  public override Plan GetPlan() 
  {
    return new NullPlan();
  }
  // Some other NULL functionality.
}

// Replace null values with Null-object.
customer = order.customer ?? new NullCustomer();

// Use Null-object as if it's normal subclass.
plan = customer.GetPlan();
```


---


## 4.8 Introduce Assertion

**Problem**

For a portion of code to work correctly, certain conditions or values must be true.

```cs
double GetExpenseLimit() 
{
  // Should have either expense limit or
  // a primary project.
  return (expenseLimit != NULL_EXPENSE) ?
    expenseLimit :
    primaryProject.GetMemberExpenseLimit();
}
```


**Solution**

Replace these assumptions with specific assertion checks.

```cs
double GetExpenseLimit() 
{
  Assert.IsTrue(expenseLimit != NULL_EXPENSE || primaryProject != null);

  return (expenseLimit != NULL_EXPENSE) ?
    expenseLimit:
    primaryProject.GetMemberExpenseLimit();
}
```

