// Every C# statement ends with a semicolon ;.

using System;   // using System means that we can use classes from the System namespace.

namespace HelloWorld    //namespace is used to organize your code, and it is a container for classes and other namespaces.
{
    class Program   /* class is a container for data and methods, which brings functionality to your program.
                    Every line of code that runs in C# must be inside a class.
                    In our example, we named the class Program. */
    {
        static void Main(string[] args) // Main method. Any code inside its curly brackets {} will be executed.
        {
            Console.WriteLine("Hello World!");  /*  Console is a class of the System namespace,
                                                    which has a WriteLine() method that is used to output/print text.
                                                    In our example it will output "Hello World!". */
        }
    }   // The curly braces {} marks the beginning and the end of a block of code.
}