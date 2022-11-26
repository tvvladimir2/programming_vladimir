## CODE REFACTORING TECHNIQUES


---


## LINKS

[Refactoring Techniques](https://refactoring.guru/refactoring/techniques)


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


---


## 6.1 Pull Up Field

**Problem**

Two classes have the same field.

![](images/Pull_Up_Field_Before.png)


**Solution**

Remove the field from subclasses and move it to the superclass.

![](images/Pull_Up_Field_After.png)


---


## 6.2 Pull Up Method

**Problem**

Your subclasses have methods that perform similar work.

![](images/Pull_Up_Method_Before.png)


**Solution**

Make the methods identical and then move them to the relevant superclass.

![](images/Pull_Up_Method_After.png)


---


## 6.3 Pull Up Constructor Body

**Problem**

Your subclasses have constructors with code that’s mostly identical.

```cs
public class Manager: Employee 
{
  public Manager(string name, string id, int grade) 
  {
    this.name = name;
    this.id = id;
    this.grade = grade;
  }
  // ...
}
```


**Solution**

Create a superclass constructor and move the code that’s the same in the subclasses to it. Call the superclass constructor in the subclass constructors.

```cs
public class Manager: Employee 
{
  public Manager(string name, string id, int grade): base(name, id)
  {
    this.grade = grade;
  }
  // ...
}
```


---


## 6.4 Push Down Field

**Problem**

Is a field used only in a few subclasses?

![](images/Push_Down_Field__Before.png)


**Solution**

Move the field to these subclasses.

![](images/Push_Down_Field_After.png)


---


## 6.5 Push Down Method

**Problem**

Is behavior implemented in a superclass used by only one (or a few) subclasses?

![](images/Push_Down_Method_Before.png)


**Solution**

Move this behavior to the subclasses.

![](images/Push_Down_Method_After.png)


---


## 6.6 Extract Subclass

**Problem**

A class has features that are used only in certain cases.

![](images/Extract_Subclass_Before.png)


**Solution**

Create a subclass and use it in these cases.

![](images/Extract_Subclass_After.png)


---


## 6.7 Extract Superclass

**Problem**

You have two classes with common fields and methods.

![](images/Extract_Superclass_Before.png)


**Solution**

Create a shared superclass for them and move all the identical fields and methods to it.

![](images/Extract_Superclass_After.png)


---


## 6.8 Extract Interface

**Problem**

Multiple clients are using the same part of a class interface. Another case: part of the interface in two classes is the same.

![](images/Extract_Interface_Before.png)


**Solution**

Move this identical portion to its own interface.

![](images/Extract_Interface_After.png)


---


## 6.9 Collapse Hierarchy

**Problem**

You have a class hierarchy in which a subclass is practically the same as its superclass.

![](images/Collapse_Hierarchy_Before.png)


**Solution**

Merge the subclass and superclass.

![](images/Collapse_Hierarchy_After.png)


---


## 6.10 Form Template Method

**Problem**

Your subclasses implement algorithms that contain similar steps in the same order.

![](images/Form_Template_Method_Before.png)


**Solution**

Move the algorithm structure and identical steps to a superclass, and leave implementation of the different steps in the subclasses.

![](images/Form_Template_Method_After.png)


---


## 6.11 Replace Inheritance with Delegation

**Problem**

You have a subclass that uses only a portion of the methods of its superclass (or it’s not possible to inherit superclass data).

![](images/Replace_Inheritance_with_Delegation_Before.png)


**Solution**

Create a field and put a superclass object in it, delegate methods to the superclass object, and get rid of inheritance.

![](images/Replace_Inheritance_with_Delegation_After.png)


---


## 6.12 Replace Delegation with Inheritance

**Problem**

A class contains many simple methods that delegate to all methods of another class.

![](images/Replace_Delegation_with_Inheritance_Before.png)


**Solution**

Make the class a delegate inheritor, which makes the delegating methods unnecessary.

![](images/Replace_Delegation_with_Inheritance_After.png)


