# Texture Coordinates and Texture Sampling

Texturing is the act of applying an image (a [TOP](<./TOP.md> "TOP")) to geometry (a [SOP](<./SOP.md> "SOP")). This is by applying a [MAT](<./MAT.md> "MAT") the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") where the SOP resides, and assigning the TOP to one of the parameters in the MAT that accept a TOP.   
  
## Applying Texture Coordinates to a SOP

To figure out how to apply the TOP onto a SOP's surface, the SOP's texture coordinates are used. The SOP's texture coordinates are the attribute called **uv**. UVs are assigned on a per point or per vertex basis by the Texture SOP and primitive SOPs like Tube, Grid, Torus, Sphere. 

## Sampling the Texture

When the geometry is rendered these uv values get interpolated over the surface of the primitive so that every pixel has a different uv value to sample the TOP with. Based on the uv, the sampling functionality returns a single color from the TOP. 

[![](./images/e/e3/Visualuv.jpg)](</File:Visualuv.jpg>)

A visual representation of uv coordinates being interpolated. Red is the U coordinate and green is the V coordinate.

When a TOP is sampled with a given uv, the [GPU](<./GPU.md> "GPU") must decide which pixel from the TOP to return (these are known as texels). In TOPs, a U == 0.0 means refers to the leftmost edge of the leftmost texel in the TOP, and a U = 1.0 refers to the rightmost edge of the rightmost texel in the TOP. Similarly V == 0.0 is the bottom of the bottommost texel in the TOP. 

## Texel Interpolation

If you imagine a TOP with a resolution of 2x1 pixels, a U = 0.5 refers to the edge between the two texels, while a U = 0.33 refers t the center of the leftmost texel. A V = 0.5 is the center of the texels (since it's only 1 texel high). So what happens in this case if the TOP is sampled using a uv = (0.40, 0.5). This uv is somewhere in right portion of the left pixel, so what color does it return? The decision that the GPU makes depends on what [Texture Filtering](<./Texture_Filtering.md> "Texture Filtering") mode is selected. If Nearest texture filtering is selected the it will return the left texel, since that is the nearest pixel to the uv. If Linear is selected it will return a blend between the left and the right pixel. The blend will be 70% of the left pixel and 30% of the right pixel because 0.4 is 30% of the way from the center of the left pixel. In practice the blend is actually between the 4 closest texels to the sample point (8 in the case of a [3D Texture](<./3D_Texture.md> "3D Texture")), where both the U and V are used to decide which 4 texels to blend between.
