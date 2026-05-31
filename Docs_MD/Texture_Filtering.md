# Texture Filtering

## Overview

Texturing filtering occurs when the GPU is rendering geometry with a texture mapped to it. It also occurs when simply looking at a texture, like in a TOP viewer. Texture filtering is used to help textures look better when they are rendered at resolutions different than their native resolution. To understand how texture filtering works, first make sure you understand how [Texture Coordinates and Texture Sampling](<./Texture_Coordinates_and_Texture_Sampling.md> "Texture Coordinates and Texture Sampling") works. There are 3 main types of texture filtering: 

**Nearest** \- Nearest filtering will just take the pixel color of the single pixel that is closest to the texture coordinates it is currently trying to sample at. Nearest filtering will make the image look more pixelated, but can be useful when trying to get pixel perfection. 

**Linear** \- Linear filtering, also known as interpolation, will blend of the 4 pixels closest to the coordinate where the GPU is currently sampling. The blend is a linear blend that will give more weight to the pixels that the coordinate is closest to. 

**Mipmap Linear** \- Mipmap linear, also known as Trilinear, is Linear Filtering, with the addition of sampling and blending between two different mipmap levels. Refer to the article on **[Mipmapping](<./Mipmapping.md> "Mipmapping")** for more information. 

## Controlling Texturing Filtering in TouchDesigner

Depending on where you texture is being used, there are many places to control texture filtering in TouchDesigner. 

### In TOPs

On the Common page of every TOP there are two parameters that pertain to texture filtering. 

**Input Smoothness** \- This parameter controls how the input TOPs into this node are filtered when doing the node's operation. If the resolution of the input TOPs are the same as the resolution of the current TOP, this parameter will have no affect (since the pixels will match up perfectly). 

**Viewer Smoothness** \- This parameter will affect how the texture is filtered when drawing it in the TOP viewer and the network background. It does not affect the actual texture data of the node, just how the image looks when viewing it in a TOP viewer. This parameter does not affect how the texture is sampled when rendering using MATs. MATs have their own parameters to control how TOPs are sampled. 

Both of these parameters have two options: 

**Nearest Pixel** \- This is Nearest Filtering.  
**Interpolate Pixels** \- This is Linear Filtering.  
**Mipmap Pixels** \- This uses Mipmaps to display the texture at different sizes. See [Mipmapping](<./Mipmapping.md> "Mipmapping"). 

Why Mipmap? When you shrink an image, one or more pixels are combined to get each new pixel. When shrinking, Nearest Pixel, and Interpolate Pixel don't take into account all pixels. TOPs sample their input as Mipmaps gives better averaging of pixels when images are made smaller, either by reducing the image resolution, or by shrinking via TOPs like Corner Pin Transform. 

### In MATs

In MATs, next to each parameter that takes a TOP as an input, there is a + button. Pressing this button will bring up a dialog with different settings on how that texture will be used in this MAT. 

The Filter Type parameter is what controls the filtering for this particular texture. The three options are: Nearest, Linear and Mipmap Linear. Mipmap linear is the default value. If the TOP doesn't have mipmaps generated, the MAT will automatically use Linear Filtering for this TOP. In general you will just want to leave this setting to Mipmap Linear. 

## Additional texture sampling methods

Along with these methods, [Anisotropic Filtering](<./Anisotropic_Filtering.md> "Anisotropic Filtering") can be used to increase the visual quality of textured geometry. Anisotropic Filtering is a filtering method that takes into account the angle the polygons are facing the camera at, changing how the texture is filtered based on this information. For more information refer to the [Anisotropic Filtering](<./Anisotropic_Filtering.md> "Anisotropic Filtering") article.
