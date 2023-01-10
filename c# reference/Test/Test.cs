public class Test
{
    // static constructor
    static Test()
    {
        Console.WriteLine("Static constructor called");
    }

    // instance constructor
    public Test()
    {
        Console.WriteLine("Instance constructor called");
    }

    // static method
    public static void DisplayInfo()
    {
        Console.WriteLine("DisplayInfo called");
    }

    // instance method
    public void Start() { }

    // instance method
    public void Stop() {  }
}