﻿using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Test
    {
        static void Main(string[] args)
        {
            User myUser = new User();  // Instantiate a class
            myUser.DoSomething();    // Invoke a method on a class
            myUser.DoSomethingElse(5);    // Invoke a method on a class
            Console.WriteLine(myUser.myString);
        }
    }
}