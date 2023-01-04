# CLASSES: CLASS MEMBER: PROPERTIES


---



## DESCRIPTION

A property encapsulates a private field using setter and getter to assign and retrieve underlying field value.
They act like gateways to fields.


Example: **Property**
```cs
class Student
{
    private int id;

    public int StudentId    // Encapsulates a private field
    {
        // Auto implemented property
        get { return id; }
        set { id = value; }
    }

    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```

In the above example, the `id` is a private field that cannot be accessed directly. It will only be accessed using the `StudentId` property. The `get{ }` returns the value of the underlying field and `set{ }` assigns the value to the underlying field `id`.


From C# 3.0 onwards, property declaration has been made easy if you don't want to apply some logic in getter or setter. Using auto-implemented property, you don't need to declare an underlying private field. C# compiler will automatically create it in IL code.

Example: **Auto-implemented Property**
```cs
class Student
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```

In the above example, backing private field for the FirstName and LastName will be created internally by the compiler. This speed up the development time and code readability.


Example: **Additional logic in get and set**
```cs
// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Student
    {
        private int _idCard;
        private string _firstName = "MARGARITTA";    // `Margaritta` is a default value
        private string _lastName = "Tazeva";

        public int StudentId
        {
            get
            {
                return _idCard; // It is the same as not writing anything in this line. Written automatically.
            }

            set
            {
                if (value > 0)
                    _idCard = value;
            }
        }

        public string FirstName
        {
            get
            {
                return _firstName.ToLower();
            }
            // does not have a `set`>> read only
        }

        public string LastName
        {
            get
            {
                return _lastName.ToLower();
            }

            set
            {
                _lastName = value;
            }
        }

        public string FullName
        {
            get
            {
                return FirstName + " " + LastName;
            }
        }
    }
}
```
```cs
// We create an object of a class (another script) within this script
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class RunProgram
    {
        static void Main(string[] args)
        {
            Student myStudent = new Student();  // Instantiate a class

            // myStudent.FirstName = "Madonna";    // Error: `FirstName`is read only because it does not have `set`
            Console.WriteLine(myStudent.FirstName); // Print a default value of myString field

            Console.WriteLine(myStudent.LastName);
            myStudent.LastName = "Evdokimova";
            Console.WriteLine(myStudent.LastName);

            Console.WriteLine(myStudent.FullName);
        }
    }
}
```
```
> margaritta
> tazeva
> evdokimova
> margaritta evdokimova
```



---

stopped at:
https://www.youtube.com/watch?v=S5i7QZfHfe8&list=PL_c9BZzLwBRIXCJGLd4UzqH34uCclOFwC&index=71