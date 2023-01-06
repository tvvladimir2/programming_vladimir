// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            Program myProgram = new Program();
            myProgram.DoSomething();
        }

        public void DoSomething()
        {
            Console.WriteLine("Hello");
            Student me = new Student(); // Student has inherited from User
            me.FirstName = "Jingle";    // User functions are available for Student from USer
            me.Verified = true;         // Also inherited by Student from User
            Console.WriteLine(me.FirstName + " access level is " + me.Verified);
        }
    }
}