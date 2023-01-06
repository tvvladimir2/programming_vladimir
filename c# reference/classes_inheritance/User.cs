// Base/root/object class
using System;
using System.Collections.Generic;

namespace MySweetProgram
{
    public class User
    {
        // By default all users are not allowed to perform certain actions
        public bool Verified {get ; set; } = false;

        public string FirstName {get ; set; } = string.Empty;
        public string LastName {get ; set; } = string.Empty;
        public string FullName
        {
            get
            {
                return FirstName + " " + LastName;
            }
   
        }
    }
}