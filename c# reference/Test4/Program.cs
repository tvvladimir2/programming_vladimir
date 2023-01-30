using System;

class Program
{
    static void Main()
    {
        string[] myArray = { "0", "1", "0", "0"};

        string myString = string.Join("", myArray);
        
        Console.WriteLine(myString);
    }
}