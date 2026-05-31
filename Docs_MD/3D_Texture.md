# 3D Texture

A **3D Texture** is a texture that is sampled using three texture coordinates: u, v, and w. All 3 coordinates are normalized to the 0-1 range. The easiest way to think of a 3D texture is as a stack of 2D textures. What makes a 3D texture special is that two neighboring layers will be sampled and blended together if the w coordinate is somewhere between two layers. For example if you have a 3D texture with a depth of 2 (i.e 2 layers, cache size of 2), the two layers will be at w coordinate 0.25 and w coordinate 0.75. If you sample the texture with a w coordinate of 0.5 (or 0.0 with Texture Extend Mode set to repeat), you'll get a 50/50 blend between the two layers. If you sample it at a w value of 0.3, you'll get mostly layer 1 and some of layer 2. The 3D texture will only blend between 2 layers at a time. 

Notice that a W coordinate of 0 is not the coordinate of the first slice, but rather 50% of the first slice and 50% of the last slice. To get 100% of the first slice, you need a W coordinate which is (0.5 / NumberOfSlices). 

The true power of the 3D texture is in its ability to blend between multiple layers in a single pass. In a single draw you can have a very large 3D texture (often 2048+ layers), and if you have w values ranging all the way from 0 to 1 on your geometry, you will be able to sample any or all of the layers in a single pass. This would be much more costly to do if this was done by sampling many 2D textures manually. This is because the texture memory of a 3D texture is arranged in a way that makes sampling this way more performant. 

As of the 2025.30000+ series of builds, many TOPs can now apply their operations to a 3D Texture. The operation will be applied to all slices. 

### Extra W or P Offset Information

When the [Texture 3D TOP](<./Texture_3D_TOP.md> "Texture 3D TOP") is capturing a new slice every frame (it's default mode), it also maintains an offset that denotes what the 'newest' slice is. This extra offset information (described as a`POffset`in the [Write a GLSL Material](<./Write_a_GLSL_Material.md> "Write a GLSL Material") documentation), allows for some different behavior in some places where a 3D Texture is consumed. Ideally the first slice in the 3D Texture would be the 'newest' slice (W coordinate near 0). However it is too expensive to shift all of the texture layers around every frame. So instead the offset that is maintained is added to the W coordinate when sampling the 3D Texture. This results in that coordinate always sampling the 'newest' slice, even though where in the 3D Texture the newest slice is is changing every frame. 

Materials (such as [Phong MAT](<./Phong_MAT.md> "Phong MAT")) and the [Time Machine TOP](<./Time_Machine_TOP.md> "Time Machine TOP") make use of this offset information. However any TOP that processes the 3D Texture after the [Texture 3D TOP](<./Texture_3D_TOP.md> "Texture 3D TOP") causes this information to get lost. 

## Related Articles

[2D Texture Array](<./2D_Texture_Array.md> "2D Texture Array")
