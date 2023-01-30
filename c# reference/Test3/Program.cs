using System;
using System.Collections.Generic;

class ListStorage
{
    private List<string> ourList = new List<string>() { "0058", "0059", "0100", "0101", "0102", "0103", "0104", "0105", "0106", "0107", "0108", "0109", "0110", "0111", "0112" };

    static void Main()
    {
        ListStorage program = new ListStorage();
        foreach (string item in program.ourList)
            Console.WriteLine(item);
    }

    static string SortString(string input)
    {
        char[] myTemporaryArray = input.ToArray();
        Array.Sort(myTemporaryArray);
        string myTemporaryString = string.Join("", myTemporaryArray);
        return myTemporaryString;
    }
}

