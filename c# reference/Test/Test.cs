using System;
using System.Collections;

class Test
{
    public static void Main()
    {
        // create a dictionary 
        Dictionary<string, string> mySongs = new Dictionary<string, string>();

        // add items to dictionary
        mySongs.Add("Queen", "Break Free");
        mySongs.Add("Free", "All right now");
        mySongs.Add("Pink Floyd", "The Wall");

        Console.WriteLine(mySongs);
    }
}