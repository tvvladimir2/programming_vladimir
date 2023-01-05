// We create an object of a class (another script) within this script
using System;
using System.Collections.Generic;
using System.Linq;

namespace MySweetProgram
{
    class RunProgram
    {
        static void Main(string[] args)
        {
            List<string> firstNames = new List<string>(){"Caleb", "Janna", "Vladimir"};
            List<string> lastNames = new List<string>(){"Evdokimov", "Rtveliashvili", "Tazev"};   

            // Create a list and add these objects
            List<Student> students = new List<Student>();

            for(int i = 0; i < firstNames.Count; i++)    // (initializer; condition; iterator)
            {
                Student student = new Student();
                student.FirstName = firstNames[i];
                student.LastName = lastNames[i];
                students.Add(student);
            }

            // Loop through the list of objects
            foreach(Student i in students)
            {
                Console.WriteLine(i.FullName);
            }
        }
    }
}