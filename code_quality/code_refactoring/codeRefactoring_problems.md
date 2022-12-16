# CODE REFACTORING PROBLEMS


---


## LINKS

[Code smells](https://refactoring.guru/refactoring/smells)


---


## BLOATERS

Bloaters are code, methods and classes that have increased to such gargantuan proportions that they’re hard to work with. Usually these smells don’t crop up right away, rather they accumulate over time as the program evolves (and especially when nobody makes an effort to eradicate them).


**1. Long Method**

*   A method contains too many lines of code. Generally, any method longer than ten lines should make you start asking questions.


**2. Large Class**

*   A class contains many fields/methods/lines of code.


**3. Primitive Obsession**

*   Use of primitives instead of small objects for simple tasks (such as currency, ranges, special strings for phone numbers, etc.)

*   Use of constants for coding information (such as a constant USER_ADMIN_ROLE = 1 for referring to users with administrator rights.)
    
*   Use of string constants as field names for use in data arrays.


**4. Long Parameter List**

*   More than three or four parameters for a method.


**5. Data Clumps**

*   Sometimes different parts of the code contain identical groups of variables (such as parameters for connecting to a database). These clumps should be turned into their own classes.


---


## OBJECT ORIENTATION ABUSERS

All these smells are incomplete or incorrect application of object-oriented programming principles.

**1. Switch Statements**

*   You have a complex switch operator or sequence of if statements.


**2. Temporary Field**

*   Temporary fields get their values (and thus are needed by objects) only under certain circumstances. Outside of these circumstances, they’re empty.


**3. Refused Bequest**

*   If a subclass uses only some of the methods and properties inherited from its parents, the hierarchy is off-kilter. The unneeded methods may simply go unused or be redefined and give off exceptions.


**4. Alternative Classes with Different Interfaces**

*   Two classes perform identical functions but have different method names.


---


## CHANGE PREVENTERS

These smells mean that if you need to change something in one place in your code, you have to make many changes in other places too. Program development becomes much more complicated and expensive as a result.


**1. Divergent Change**

*   You find yourself having to change many unrelated methods when you make changes to a class. For example, when adding a new product type you have to change the methods for finding, displaying, and ordering products.


**2. Shotgun Surgery**

*   Making any modifications requires that you make many small changes to many different classes.


**3. Parallel Inheritance Hierarchies**

*   Whenever you create a subclass for a class, you find yourself needing to create a subclass for another class.


---


## DISPENSABLES

A dispensable is something pointless and unneeded whose absence would make the code cleaner, more efficient and easier to understand.


**1. Comments**

*   A method is filled with explanatory comments.


**2. Duplicate Code**

*   Two code fragments look almost identical.


**3. Lazy Class**

*   Understanding and maintaining classes always costs time and money. So if a class doesn’t do enough to earn your attention, it should be deleted.


**4. Data Class**

*   A data class refers to a class that contains only fields and crude methods for accessing them (getters and setters). These are simply containers for data used by other classes. These classes don’t contain any additional functionality and can’t independently operate on the data that they own.


**5. Dead Code**

*   A variable, parameter, field, method or class is no longer used (usually because it’s obsolete).


**6. Speculative Generality**

*   There’s an unused class, method, field or parameter.


---


## COUPLERS

All the smells in this group contribute to excessive coupling between classes or show what happens if coupling is replaced by excessive delegation.


**1.Feature Envy**

*   A method accesses the data of another object more than its own data.


**2. Inappropriate Intimacy**

*   One class uses the internal fields and methods of another class.


**3. Message Chains**

*   In code you see a series of calls resembling $a->b()->c()->d()


**4. Middle Man**

*   If a class performs only one action, delegating work to another class, why does it exist at all?


---


## OTHER SMELLS

Below are the smells which don’t fall into any broad category.


**1. Incomplete Library Class**

*   Sooner or later, libraries stop meeting user needs. The only solution to the problem—changing the library—is often impossible since the library is read-only.

