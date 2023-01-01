# Debug.isDebugBuild


---


## LINKS

[](https://docs.unity3d.com/ScriptReference/Debug-isDebugBuild.html)



---



## USED FOR

For examoke, we use special key commands that help in the development process.
We can disable these keys in the final game.



---



## ENABLE / DISABLE

Unity Game Engine >> File >> Build Settings >> Development build: true or false

If ticked, the debug keys will work in the final build.



---



## EXAMPLE

```cs
if (Debug.isDebugBuild)
{
RespondToDebugKeys();
}
```