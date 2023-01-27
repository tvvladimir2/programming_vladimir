using System;

class Program
{
    static void Main()
    {
        string myString = "-1294";
        char myZero = '4';

        Console.WriteLine(myString[myString.Length - 1]);

        if (myString[myString.Length - 1] == myZero)
        {
            Console.WriteLine("huh");
        }
    }
}