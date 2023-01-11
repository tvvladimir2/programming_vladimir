# UNITY GAME ENGINE: CLASSES: MATERIAL CONSTRUCTOR


---


## LINKS

[](https://docs.unity3d.com/ScriptReference/Material-ctor.html)



---



## DECLARATION

```cs
public Material(Shader shader);
```

```cs
public Material(Material source);
```

**Parameters**:

| Parameter | Description                                                        |
|-----------|--------------------------------------------------------------------|
| shader    | Create a material with a given Shader.                             |
| source    | Create a material by copying all properties from another material. |



---



## DESCRIPTION

Create a temporary Material.

If you have a script which implements a custom special effect, you implement all the graphic setup using shaders & materials. Use this function to create a custom shader & material inside your script. After creating the material, use `SetColor`, `SetTexture`, `SetFloat`, `SetVector`, `SetMatrix` to populate the shader property values.

See Also: `Materials`, `Shaders`.




