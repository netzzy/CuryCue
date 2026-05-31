# Mipmapping

## Overview

[![](./images/a/ab/Mipmap.jpg)](</File:Mipmap.jpg>)

An example of all of the mipmap levels of a texture

Mipmapping is a texturing technique used to reduce artifacts caused by mapping a large texture onto a small area in screen space. These artifacts occur because only a small subset of the pixels in the texture are used to color the geometry due to the small amount of pixels that are being drawn. The artifact usually looks like the texture is sparkling or is noisy as it moves around the screen. 

For example: say we have a 512x512 image, and its mapped onto a polygon that is only taking up 50x50 pixels of screen space. When texturing this quad the GPU will sample the texture are various points. But since it only has 50x50 pixels to draw, it will only end up sampling 10-20% of the pixels on the image. If the objects moves around the screen, the 10-20% of the pixels that are sampled in one frame can be very different than the 10-20% that are sampled on the next frame, causing the image to look like it's sparkling or is noisy. 

To see this artifact, open up the file [ noisemipmap.toe](</images/d/df/Noisemipmap.toe> "Noisemipmap.toe"). Ensure your node viewers are on and simply zoom in and out of the network. The left [Noise TOP](<./Noise_TOP.md> "Noise TOP") is not mipmapped, while the right one is. Notice how the left one sparkles as you zoom out in the network, while the right one shows a nice visual continuity. You will also notice how the sparkling only occurs when the amount of pixels the node viewers are taking up is less than the size of the texture. In this case the textures are 256x256 pixels wide, so so when viewing them larger than this, they will look the same. 

## The Technique

Mipmapping is accomplished by creating pre-downsized versions of the texture. A mipmap level is a single downsized version of the original texture, at some resolution. Multiple mipmap levels will be created, each one half the size of the previous one. For example a 256x256 texture will have mipmap levels of 128x128, 64x,64, 32x32, 16x16, 8x8, 4x4, 2x2, and 1x1. Each mipmap level is created by downsizing the previous level. So the 128x128 level is created by downsizing the original 256x256 texture, and similarly the 8x8 level is created by downsizing the 16x16 level. The downsize uses a 2x2 box-filter to average the pixel color of the source texture when creating the new mipmap level. 

When rendering, the GPU will automatically choose the 2 most appropriate mipmap levels to sample from based on the amount of pixels the renderer geometry is taking up. For example if the rendered geometry takes up 90x90 pixels, then the mipmap levels 128x128 and 64x64 will be used. The GPU will blend between these two levels when texturing, which is why as we zoom out in the network there is no visual discontinuity. 

## Using mipmaps in Materials (MATs)

Mipmapping will be used automatically for any [MAT](<./MAT.md> "MAT") sampling a texture. You can turn off mipmapping in the MAT by clicking the + next to each map, and selecting something other than Mipmap Linear filtering. 

## Using Mipmaps in Textures (TOPs)

All [TOPs](<./TOP.md> "TOP") can sample their inputs as mipmaps. This can help reduce sparkling artifacts when animating the position or scale of images, especially when using images with lots of small detail. 

**Mipmap Pixels** option can be found in the **Input Smoothness** and **Viewer Smoothness** menus on the common page of all TOPs. See also [TOP Generator Common Page](<./TOP_Generator_Common_Page.md> "TOP Generator Common Page") and [TOP Filter Common Page](<./TOP_Filter_Common_Page.md> "TOP Filter Common Page"). 

## GPU Memory Cost

Mipmaps for a TOP will cause that TOP to use up 33% more GPU memory. You can see if mipmaps have been created for a particular TOP by middle clicking on it and looking for **Mipmaps: Yes**.
