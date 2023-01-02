// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class User
    {
        public string myString = "Bruce Willis";

        // This line is hit when we instantiate this class from another script
        // e.g. User myUser = new User();
        // This Constructor is created by C# automatically
        public User()   // default Constructor: class member
        {

        }

        // This line is hit when we call `myUser.doSomething();`
        // `void` means there's no return
        public void DoSomething()   // 'public' shows this method to other scripts.
        {
            Console.WriteLine("doing something " + "in doSomething method");
        }

        // `private` methods are only used within the script itself
        public void DoSomethingElse(int times)  // ìnt times`: Take an argument in to a parameter variable
        {
            for (int i = 0; i < times; i++)
            {
                Console.WriteLine("Method DoSomethingElse: " + "this is the " + (i+1) + "th time we print it");
            }
        }

        public int ReturnSomething(int x)
        {
            return x*x;
        }
    }
}