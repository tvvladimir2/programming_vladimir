// Our main program
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            DoSomething();
            // Program myProgram = new Program();  // Identifier `myProgram` Instantiate
            // myProgram.DoSomething();    // Invoke methods on the object

            // We do not want to run this, results in stack overflow
            // Program.Main();  // Static methods are available directly on a class
        }

        public static void DoSomething()
        {
            User user = new User();
            user.FirstName = "Vladimir";
            user.LastName = "Zelensky";
            user.DoSomething();     // This is a public method of `user` object. It is NOT static.
            User.PrintUser(user);   // Using a static method. We call it directly on a class. A utility method that has something to do with class instances
        }
    }
}