# Camera.ScreenToWorldPoint


## LINKS

[](https://docs.unity3d.com/ScriptReference/Camera.ScreenToWorldPoint.html)



---



## DECLARATION

```cs
public Vector3 ScreenToWorldPoint(Vector3 position);
```

```cs
public Vector3 ScreenToWorldPoint(Vector3 position, Camera.MonoOrStereoscopicEye eye); 
```



---



## DESCRIPTION

Transforms a point from screen space into world space, where world space is defined as the coordinate system at the very top of your game's hierarchy.

World space coordinates can still be calculated even when provided as an off-screen coordinate, for example for instantiating an off-screen object near a specific corner of the screen.

Screenspace is defined in pixels. The bottom-left of the screen is (0,0); the right-top is (`pixelWidth`,`pixelHeight`). The z position is in world units from the camera.
