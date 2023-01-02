// We create an object of a class (another script) within this script
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            // Instantiate a class
            User myUser = new User();  

            // Working with fields
            Console.WriteLine(myUser.myString); // Print a default value of myString field
            myUser.myString = "Madonna Mia";    // Assign a new value to myString field
            Console.WriteLine(myUser.myString); // Print a default value of myString field

            // Working with methods
            myUser.DoSomething();       // Invoke a method on a class
            myUser.DoSomethingElse(5);  // Pass a parameter `5` in.
            Console.WriteLine(myUser.ReturnSomething(5));   // Pass in a parameter and get a return
        }
    }
}