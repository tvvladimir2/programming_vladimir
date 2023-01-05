# CLASSES: LIST OF A CUSTOM CLASS


---


## DESCRIPTION

Working with the classes as if they were Types, because they are.


Example: **Manually input student data in a list** 
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
            // Instantiate first object
            Student myStudent1 = new Student();
            myStudent1.FirstName = "Katerina";
            myStudent1.LastName = "Ushakova";

            // Instantiate second object
            Student myStudent2 = new Student();
            myStudent2.FirstName = "Antonio";
            myStudent2.LastName = "Banderas";

            // Create a list and add these objects
            List<Student> students = new List<Student>();
            // var students = new List<Student>();    // Same as above line
            students.Add(myStudent1);
            students.Add(myStudent2);

            // Loop through the list of objects
            foreach(Student i in students)
            {
                Console.WriteLine(i.FullName);
            }
        }
    }
}
```
```
> Katerina Ushakova
> Antonio Banderas
```



Example: **Input student data in a list using For loop** 
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
            List<string> firstNames = new List<string>(){"Caleb", "Janna", "Vladimir"};
            List<string> lastNames = new List<string>(){"Evdokimov", "Rtveliashvili", "Tazev"};   

            // Create a list and add these objects
            List<Student> students = new List<Student>();

            for(int i = 0; i < firstNames.Count; i++)    // (initializer; condition; iterator)
            {
                Student student = new Student();
                student.FirstName = firstNames[i];
                student.LastName = lastNames[i];
                students.Add(student);
            }

            // Loop through the list of objects
            foreach(Student i in students)
            {
                Console.WriteLine(i.FullName);
            }
        }
    }
}
```
```
> Caleb Evdokimov
> Janna Rtveliashvili
> Vladimir Tazev
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