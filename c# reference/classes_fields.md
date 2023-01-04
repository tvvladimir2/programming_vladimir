### CLASSES: CLASS MEMBER: FIELDS


---


## DESCTIPTION

A class can have one or more fields. It is a `class-level variable` that holds a value.

Example: **Field initiation and instantiation**
```cs
// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Student
    {
        private int _studentAge = 18;     // Can only be accessed withing this class

        // Not recommended to use. Best to use a property.
        public int StudentClass = 11;  // Can be accessed outside this class.
        public string FirstName = "Madonna";
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
            // Instantiate a class
            Student myStudent = new Student(); 

            // Working with fields
            Console.WriteLine(myStudent.FirstName); // Print a default value of myString field
            myStudent.FirstName = "Margaritta";    // Assign a new value to myString field
            Console.WriteLine(myStudent.FirstName); // Print a default value of myString field
        }
    }
}
```


---