# UNITY GAME ENGINE: TAGS


---



## PROS & CONS

| Pros                            | Cons                       |
|---------------------------------|----------------------------|
| Just one per game object        | Is based on a string       |
| Very simple to use in inspector | Have to rename in 2 places |
| Makes for clear code            | Nothing "keeps you honet"  |

**Cons explained**:
- Genral rule of programming: Only use a `string` if it will be immidatly put out on a screen. We are breaking this rule when using a string.
- We have to change it in the Unity object inspector and in the code.
- Better use Components to tag objects. But it is more heavy weight.