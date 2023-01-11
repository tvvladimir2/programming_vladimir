# Shader.Find


---


## LINKS

[](https://docs.unity3d.com/ScriptReference/Shader.Find.html)



---



## DECLARATION

```cs
public static Shader Find(string name);
```



---



## DESCRIPTION

Finds a shader with the given `name`.

Shader.Find can be used to switch to another shader without having to keep a reference to the shader. `name` is the name you can see in the shader popup of any material, for example "Standard", "Unlit/Texture", "Legacy Shaders/Diffuse" etc.

Note that a shader might be not included into the player build if nothing references it. In that case, Shader.Find will work only in the Editor, and will result in the pink error shader in a build. Because of that, it is advisable to use shader references instead of finding them by name. To make sure a shader is included into the game build, do either of: 1) reference it from some of the materials used in your Scene, 2) add it under "Always Included Shaders" list in ProjectSettings/Graphics or 3) put shader or something that references it (e.g. a Material) into a "Resources" folder.

See Also: `Material` class.


Example: **Unity default example: Create a material from code**
```cs
using UnityEngine;

public class Example : MonoBehaviour
{
    // Create a material from code
    void Start()
    {
        // Create a material with transparent diffuse shader
        Material material = new Material(Shader.Find("Transparent/Diffuse"));
        material.color = Color.green;

        // assign the material to the renderer
        GetComponent<Renderer>().material = material;
    }
}
```