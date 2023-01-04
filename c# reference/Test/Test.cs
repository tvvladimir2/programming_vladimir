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