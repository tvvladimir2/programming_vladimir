using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class User
    {
        public string myString = "Bruce Willis";

        // This line is hit when we instantiate this class from another script
        // e.g.
        // Program myProgram = new Program();
        // This Constructor is created by C# automatically
        public User()   // default Constructor: class member
        {

        }

        public void doSomething()
        {
            Console.WriteLine("doing something" + "in doSomething method");
        }
    }
}