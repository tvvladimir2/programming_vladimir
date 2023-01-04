// The class itself
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class Student
    {
        private int _idCard;
        private string _firstName = "MARGARITTA";    // `Margaritta` is a default value
        private string _lastName = "Tazeva";

        public int StudentId
        {
            get
            {
                return _idCard; // It is the same as not writing anything in this line. Written automatically.
            }

            set
            {
                if (value > 0)
                    _idCard = value;
            }
        }

        public string FirstName
        {
            get
            {
                return _firstName.ToLower();
            }
            // does not have a `set`>> read only
        }

        public string LastName
        {
            get
            {
                return _lastName.ToLower();
            }

            set
            {
                _lastName = value;
            }
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