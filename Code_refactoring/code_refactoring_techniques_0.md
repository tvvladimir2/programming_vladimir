## CODE REFACTORING TECHNIQUES


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


## 2. MOVING FEATURES BETWEEN OBJECTS

Even if you have distributed functionality among different classes in a less-than-perfect way, there is still hope.

These refactoring techniques show how to safely move functionality between classes, create new classes, and hide implementation details from public access.

- 2.1 Move Method
- 2.2 Move Field
- 2.3 Extract Class
- 2.4 Inline Class
- 2.5 Hide Delegate
- 2.6 Remove Middle Man
- 2.7 Introduce Foreign Method
- 2.8 Introduce Local Extension


---


## 3. ORGANIZING DATA

These refactoring techniques help with data handling, replacing primitives with rich class functionality. Another important result is untangling of class associations, which makes classes more portable and reusable.

- 3.1  Change Value to Reference
- 3.2  Change Reference to Value
- 3.3  Duplicate Observed Data
- 3.4  Self Encapsulate Field
- 3.5  Replace Data Value with Object
- 3.6  Replace Array with Object
- 3.7  Change Unidirectional Association to Bidirectional
- 3.8  Change Bidirectional Association to Unidirectional
- 3.9  Encapsulate Field
- 3.10 Encapsulate Collection
- 3.11 Replace Magic Number with Symbolic Constant
- 3.12 Replace Type Code with Class
- 3.13 Replace Type Code with Subclasses
- 3.14 Replace Type Code with State/Strategy
- 3.15 Replace Subclass with Fields


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


## 5. Simplifying Method Calls

These techniques make method calls simpler and easier to understand. This, in turn, simplifies the interfaces for interaction between classes.

- 5.1  Add Parameter
- 5.2  Remove Parameter
- 5.3  Rename Method
- 5.4  Separate Query from Modifier
- 5.5  Parameterize Method
- 5.6  Introduce Parameter Object
- 5.7  Preserve Whole Object
- 5.8  Remove Setting Method
- 5.9  Replace Parameter with Explicit Methods
- 5.10 Replace Parameter with Method Call
- 5.11 Hide Method
- 5.12 Replace Constructor with Factory Method
- 5.13 Replace Error Code with Exception
- 5.14 Replace Exception with Test


---


## Dealing with Generalization

Abstraction has its own group of refactoring techniques, primarily associated with moving functionality along the class inheritance hierarchy, creating new classes and interfaces, and replacing inheritance with delegation and vice versa.

- 6.1  Pull Up Field
- 6.2  Pull Up Method
- 6.3  Pull Up Constructor Body
- 6.4  Push Down Field
- 6.5  Push Down Method
- 6.6  Extract Subclass
- 6.7  Extract Superclass
- 6.8  Extract Interface
- 6.9  Collapse Hierarchy
- 6.10 Form Template Method
- 6.11 Replace Inheritance with Delegation
- 6.12 Replace Delegation with Inheritance

