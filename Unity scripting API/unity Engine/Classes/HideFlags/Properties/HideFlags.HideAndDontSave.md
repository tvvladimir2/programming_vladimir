# HideFlags.HideAndDontSave


---


## LINKS

[](https://docs.unity3d.com/ScriptReference/HideFlags.html)



---



## DESCRIPTION

The GameObject is not shown in the Hierarchy, not saved to Scenes, and not unloaded by `Resources.UnloadUnusedAssets`.

This is most commonly used for GameObjects which are created by a script and are purely under the script's control.

Example: **Unity default example**
```cs
using UnityEngine;
using System.Collections;

public class ExampleClass : MonoBehaviour
{
    // Creates a Material that is explicitly created & destroyed by the component.
    // Resources.UnloadUnusedAssets will not unload it, and it will not be editable by the Inspector.
    private Material ownedMaterial;
    void OnEnable()
    {
        ownedMaterial = new Material(Shader.Find("Diffuse"));
        ownedMaterial.hideFlags = HideFlags.HideAndDontSave;
        GetComponent<Renderer>().sharedMaterial = ownedMaterial;
    }

    // Objects created as hide and don't save must be explicitly destroyed by the owner of the object.
    void OnDisable()
    {
        DestroyImmediate(ownedMaterial);
    }
}
```


Example: **GridOverlay.cs in Conway's game of life game**
```cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GridOverlay : MonoBehaviour
{
    private Material lineMaterial;
    
    void CreateLineMaterial()
    {
        if (!lineMaterial)
        {
            // `shader` variable is used to give the color of the lines
            var shader = Shader.Find("Hidden/Internal-Colored");    // Finds a shader with the given `name`.
            lineMaterial = new Material(shader);

            lineMaterial.hideFlags = HideFlags.HideAndDontSave;
        }
    }
}
```