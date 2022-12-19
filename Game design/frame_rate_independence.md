# FRAME-RATE INDEPENDENCE


---


## DESCRIPTION

- The time each frame takes can vary wildly from moment to moment, and machine to machine. E.g. from 1/1000 of a second to 1/10 of a second.
- `Time.deltaTime` tells you the last frame time.
- This is a good predictor of the current frame time.
- We can use it to adjust our movement.
- Longer frames lead to more movement.
- If the frame took longer to render e.g. 1/1000 s >> the object needs to move/rotate a lot more.
- If it rendered in a 1/1000 of a second >> the object has to catch up in it's movement
- e.g. `rotation = rcsThrust * Time.deltaTime`;
- `rcsThrust` is constant. If `Time.deltaTime` is smaller >> `rotation` will be smaller. And otherwise.