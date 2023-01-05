// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Student
    {
        private string _firstName = "MARGARITTA";    // `Margaritta` is a default value
        private string _lastName = "Tazeva";

        public string FirstName
        {
            get{return _firstName;}
            set{_firstName = value;}
        }

        public string LastName
        {
            get{return _lastName;}
            set{_lastName = value;}
        }

        public string FullName
        {
            get
            {
                return FirstName + " " + LastName;
            }
        }
    }
}