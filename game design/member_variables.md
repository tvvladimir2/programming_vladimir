# UNITY GAME ENGINE: VARIABLES



---



# MEMBER VARIABLES

Any variable defined outside of any function defines a member variable. The variables are accessible through the inspector inside Unity. Any value stored in a member variable is also automatically saved with the project. 

**Public member variables**:
```cs
var enemy : Transform;                  // member variable
[SerializeField] AudioClip mainEngine;  // member variable

function Update() {
    if ( Vector3.Distance( enemy.position, transform.position ) < 10 )
        print("I sense the enemy is near!");
}
```


You can also create private member variables. Private member variables are useful for storing state that should not be visible outside the script. Private member variables are not saved to disk and are not editable in the inspector. They are visible in the inspector when it is set to debug mode. This allows you to use private variables like a real time updating debugger. 

**Global member variables**:
```cs
private var lastCollider : Collider;

function OnCollisionEnter(collisionInfo : Collision ) {
    lastCollider = collisionInfo.collider;
}
```



---



## `public` vs `[SerializeField]` MEMBER VARIABLES

Can make the variable `public`or `[SerializeField]`

| Modifier         | Change in Inspector? | Change From Other Scripts? |
|------------------|----------------------|----------------------------|
| [SerializeField] | Yes                  | No                         |
| public           | Yes                  | Yes                        |



---



## GLOBAL MEMBER VARIABLES

You can also create global variables using the `static` keyword.

```cs
// The static variable in a script named 'TheScriptName.js'
static var someGlobal = 5;

// You can access it from inside the script like normal variables:
print(someGlobal);
someGlobal = 1;
```

To access it from another script you need to use the name of the script followed by a dot and the global variable name.print(TheScriptName.someGlobal);
TheScriptName.someGlobal = 10;



---



## CHANGING LEVEL/SCENE

Any member variables are reset when changing a scene.
E.g. You can not store an integer that counts a number of passed levels, because this variable is reset each level.

