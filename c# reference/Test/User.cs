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

        public void DoSomething()
        {
            Console.WriteLine("doing something" + "in doSomething method");
        }

        // `private` methods are only used within the script itself
        public void DoSomethingElse(int times)  // ìnt times`: Take an argument in to a parameter variable
        {
            for (int i = 0; i < times; i++)
            {
                Console.WriteLine("Method DoSomethingElse: " + "this is the " + (i+1) + "th time we print it");
            }
            // do soemthing else
        }
    }
}