using System;
using System.Collections;
class Program
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> student = new Dictionary<string, string>();

        // add items to dictionary
        student.Add("Name", "Susan");
        student.Add("Faculty", "History");

        // access the value having key "Name"
        Console.WriteLine(student["Name"]);

        // access the value having key "Faculty"
        Console.WriteLine(student["Faculty"]);
    }
}