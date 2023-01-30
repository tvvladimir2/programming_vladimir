using System;
using System.Collections.Generic;

public class Test
{
	void Main()
	{
		int myInteger = 65;

        int h0 = Math.Floor(myInteger - (myInteger % 10));

        Console.Writeline(h0);
	}
}
