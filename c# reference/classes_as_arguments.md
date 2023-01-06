# TAKING CUSTOM TYPES/CLASSES AS ARGUMENTS


---


## DESCRIPTION

This is a concept of a reference type. Every time we pass an object inside a method, they can be edited.

Example: **Use a an obect as an argument (object from  list)**
```cs
// We create an object of a class (another script) within this script
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class RunProgram
    {
        public static void Main(string[] args)
        {
            List<string> firstNames = new List<string>(){"Caleb", "Janna", "Vladimir"};
            List<string> lastNames = new List<string>(){"Evdokimov", "Rtveliashvili", "Tazev"};   

            List<Student> students = new List<Student>();   // Create a list and add these objects

            for(int i = 0; i < firstNames.Count; i++)    // (initializer; condition; iterator)
            {
                Student student = new Student();
                student.FirstName = firstNames[i];
                student.LastName = lastNames[i];
                students.Add(student);
            }

            // 
            takeStudents2(students[0]);

            // take the first object from `students` list and pass it to the method `takeStudent`
            takeStudents(students[0]);
            // do the same directly
            Console.WriteLine(students[0].FullName);
        }
    
        public static void takeStudents(Student student)
        {
            Console.WriteLine(student.FirstName);
            student.FirstName = "Cassandra";
            Console.WriteLine(student.FullName);
        }

        public static void takeStudents2(Student student)
        {
            student = new Student();    // This object exists only inside this method
            student.FirstName = "Pupi";
            Console.WriteLine(student.FullName);
        }
    }
}
```
```
> Pupi Tazeva
> Caleb
> Cassandra Evdokimov
> Cassandra Evdokimov
```



```cs
// Class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Student
    {
        private string _firstName = "MARGARITTA";    // `Margaritta` is a default value
        private string _lastName = "Tazeva";

        public string FirstName
        {
            get{return _firstName;}
            set{_firstName = value;}
        }

        public string LastName
        {
            get{return _lastName;}
            set{_lastName = value;}
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