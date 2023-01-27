using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        // adding elements using add() method
        List<int> primeNumbersList = new List<int>();
        primeNumbersList.Add(1); // adding elements using add() method
        primeNumbersList.Add(3);
        primeNumbersList.Add(5);
        primeNumbersList.Add(7);
        Console.WriteLine("primeNumbersList" + " has " + primeNumbersList.Count + " elements.");
        
        var citiesList = new List<string>();
        citiesList.Add("New York");
        citiesList.Add("London");
        citiesList.Add("Mumbai");
        citiesList.Add("Chicago");
        citiesList.Add(null);// nulls are allowed for reference type list
        Console.WriteLine("");
        Console.WriteLine("citiesList" + " has " + citiesList.Count + " elements.");

        //adding elements using collection-initializer syntax
        var countriesList = new List<string>()
                            {
                                "Slovakia",
                                "France",
                                "Germany",
                                "Ukraine"                    
                            };
        Console.WriteLine("");
        Console.WriteLine("countriesList" + " has " + countriesList.Count + " elements.");

        // Add Custom Class Objects in List
        var studentsList = new List<Student>() { 
                new Student(){ Id = 1, Name="Bill"},
                new Student(){ Id = 2, Name="Steve"},
                new Student(){ Id = 3, Name="Ram"},
                new Student(){ Id = 4, Name="Abdul"}
            };
        Console.WriteLine("");
        Console.WriteLine("studentsList" + " has " + studentsList.Count + " elements.");
    }
}

class Student{
	public int Id { get; set; }
	public string Name { get; set; }
}
