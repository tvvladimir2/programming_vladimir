# Time.deltaTime


---


## LINKS

[](https://docs.unity3d.com/ScriptReference/Time-deltaTime.html)



---



## DESCRIPTION

The interval in seconds from the last frame to the current one (Read Only).

Example: **Timer for Update function**
```cs
    public float speed = 0.1f;

    private float timer = 0;

    // Update is called once per frame
    void Update()
    {
        if (timer >= speed)         // When `timer` reaches `speed` the code executes
        {
            timer = 0f;
            CountNeighbours();      // Do Something
            PopulationControl();    // DoSomethingElse
        } else
        {
            timer += Time.deltaTime;    // 
        }

    }
```