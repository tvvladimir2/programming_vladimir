public class StopWatch
{
    public static int NoOfInstances = 0;
    
    // instance constructor
    public StopWatch()  // runs everytime we create an instance
    {
        StopWatch.NoOfInstances++;  // increments the field
        Console.WriteLine("done");
    }
}