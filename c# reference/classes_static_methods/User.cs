// The class itself
using System;

namespace MySweetProgram
{
    public class User
    {
        public string FirstName {get ; set; } = string.Empty;
        public string LastName {get ; set; } = string.Empty;
        public string FullName
        {
            get
            {
                return FirstName + " " + LastName;
            }
        }
        
        public void DoSomething()
        {
            Console.WriteLine("Using static method to call this public field");
        }

        // Static methods are not inherited by the instances
        public static void PrintUser(User user) // We pass in a user to a static method
        {
            Console.WriteLine("This is from public static method");  // We invoke the `DoSomething`method on the user
            user.DoSomething();
        }
    }
}