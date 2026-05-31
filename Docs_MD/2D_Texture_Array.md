# 2D Texture Array

A 2D Texture Arrays is much like a [3D Texture](<./3D_Texture.md> "3D Texture"). It is created in the same way ([Texture 3D TOP](<./Texture_3D_TOP.md> "Texture 3D TOP"), [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP")). The only difference between a 2D Texture Array and a 3D Texture is how they are used for texturing. A 3D Texture is sampled using a normalized (0-1) w texture coordinate, supports extend modes such as repeat and clamp in the w direction, and will blend between slices when the w coordinate falls between different slices. 3D Textures don't support mipmapping. 

A 2D Texture Array on the other hand is sampled using non-normalized w coordinate. 0 for the first slice, 1 for the second slice, 2 for the 3rd slice and so on. No blending is done between slices (1.4 will give you the same result as 1). You can blend two slices yourself in a GLSL shader. In a 2D Texture Array each slice can be mipmapped. Extend modes for the w direction aren't supported, if you sample at an index beyond the end of the array, it will return the last slice of the array. 

## GLSL

To use a 2D Texture Array you need to enable the OpenGL extension, by including this line at the start of your shader: 
[code] 
     #extension GL_EXT_texture_array : enable
    
[/code]

The samplers are declared as 
[code] 
     uniform sampler2DArray name;
    
[/code]

and sampled using the function 
[code] 
     texture2DArray(samplerName, vec3)
    
[/code]

## Related Articles

[3D Texture](<./3D_Texture.md> "3D Texture")
