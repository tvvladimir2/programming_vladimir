# Random.Range


---


## LINKS

[Random.Range](https://docs.unity3d.com/ScriptReference/Random.Range.html)



---



## DECLARATION

public static float Range(float minInclusive, float maxInclusive);
public static int   Range(int minInclusive, int maxExclusive); 


Example: **Select a percentage of random outcome**
```cs
// used in Game.cs in "youtube: How to make Conway's Game of Life in Unity - Part 2 - Cells"
bool RandomAliveCell()
{
    // System.Collections and UnityEngine both have Random class >> leads to ambigous space error
    int rand = UnityEngine.Random.Range(0, 100);
    if (rand > 75)
    {
        return true;
    }else
    {
        return false;
    }
}
```



---


