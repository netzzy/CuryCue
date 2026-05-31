# Optimize Geometry for Rendering

## Overview

This article covers the aspects of rendering geometry in [Render TOPs](<./Render_TOP.md> "Render TOP"). Its information does not take into account the cook times of individual [SOPs](<./SOP.md> "SOP"), which is a whole other subject. 

This article describes the current state of geometry rendering in TouchDesigner. Improvements are constantly being made so things that are currently slow may speed up in future. 

There are a few things to take into account when rendering geometry. 
* Primitive type and primitive count
  * Vertex count
  * SOP count

## The Quick Answer

The quick answer to fast geometry rendering is: 
* If your geometry is static, have it all in 3 vertex polygons (triangles) or triangle strips.
  * If your geometry is changing every frame due to a SOP cooking, then have your geometry in triangle strips. Make sure it's converted into triangle strips beforehand, as the CPU cost to convert geometry into triangle strips is very expensive.

## Geometry Batches

There are 5 main costs involved with rendering geometry.   
1\. The CPU may or may not need to convert the geometry to a format Vulkan can render.   
2\. The CPU needs to prepare the GPU memory for the pending copy.  
3\. The CPU needs to copy the geometry data to the GPU.   
4\. The CPU needs to tell the GPU how to render the geometry.   
5\. The GPU needs to render the geometry. 

Cost #1 only happens with some special geometry types like metaballs, bezier/NURBs surfaces and convex polygons. You can see this cost in the cook time of the SOP.   
Cost #2 can also be seen in the SOP cook time. This cost generally increases with the number of primitives in the geometry (not the vertex count). Cost #3 will generally be hidden because it's done in another thread on a different CPU (if available). If you see "Waiting For VBO Update" in the performance monitor then it means the other thread wasn't able to copy the geometry before it was time to render it, and the rendering had to wait for the thread to finish.   
**Costs #1, #2 and #3 only occur if the SOP is cooking. If your geometry is static you don't need to worry about these costs.   
  
**

Cost #4 occurs when the Render TOP cooks. You'll see "Rendering a batches of VBOs" in the Performance Monitor, this is cost #4. This can very often be the biggest slowdown in a synth if the geometry is in a format that the CPU can't tell the GPU to render in as few commands as possible. The 'cost' of one of these draw commands is the same regardless of the complexity of the geometry. For example telling the GPU to render a single triangle has the same CPU cost as telling the GPU to render 10,000 triangles. Some primitive types can be batched together in single draw command (like triangles), some can't. Knowing which can and which can't is important for good performance on today's GPU hardware. TouchDesigner does it's best to automatically do this for you, but there are some types of primitives that just can't be done automatically. 

A single draw command can be thought of as 'batch'. Reducing the number of batches can greatly increase the speed of your synth. Geometry can be batched if it's in a format that can be rendered with a single draw command. Refer to the section below about geometry that can be rendered with a single draw command. Along with this, at the minimum each SOP will result in 1 batch. If two SOPs share the same material and both contain primitive that can be batched (like triangles), using a Merge SOP to join them will result in a single batch for the entire set of geometry. 

Cost #5 is a separate issue from this article, as it pertains to shaders, pixel fill rates and lighting complexity. In general cost #5 will be the same regardless of how the geometry is specified. 

## How Geometry is Prepared for Rendering

Once a SOP is done cooking, it checks to see if it's render flag is on, or if someone is looking at it's geometry through a viewer. If either of those is true then the SOP will update something called a VBO. A VBO is special data structure the GPU uses to render geometry from. The contents of the SOP need to be copied and converted to the VBO so the geometry can be rendered. 

While TouchDesigner supports a large number of primitive types (tubes, nurbs, meshs etc.), Vulkan does not. Different primitive types need to be converted to one of the primitive types that Vulkan supports. This conversion and copy operation can be seen in the Performance Monitor under the heading "Updating SOP's VBO" and "Waiting for VBO Update" 

### Primitive Type and Primitive Count

Depending on the primitive type, the geometry may or may not be able to be batched. If the geometry can be batched, then the primitive count won't have an effect on speed. If the geometry can't be batched the the primitive count will have a large impact on speed. In fact each non -batched primitive adds a constant cost to the render (i.e 2 primitives is 2x slower than rendering 1 primitive, 100 primitives is 100x slower than rendering 1 primitive). 
* Triangle Strip - Triangle strips can be rendered by Vulkan very quickly. Any number of triangle strips can be rendered as one batch. This is done using a technique called Triangle Strip Stitching. 
    * Cost #1 : None
    * Cost #2 : Low
    * Cost #3 : Low
    * Cost #4 : Low
* Polygons with 3 vertices - These are triangles which Vulkan supports and can render very quickly. Any number of triangles can be rendered in a single batch. 
    * Cost #1 : None
    * Cost #2 : High
    * Cost #3 : High
    * Cost #4 : Low
* Polygons with 4 vertices - These will rendered as 2 triangles, which Vulkan supports and can render very quickly. Any number of quads can be rendered in a single batch. 
    * Cost #1 : None
    * Cost #2 : High
    * Cost #3 : High
    * Cost #4 : Low
* Polygons with 5 or more points - These will be converted into triangles, since Vulkan does not support polyons with N numbers of points. This can be expensive. TouchDesigner will automatically convert your [Concave Polygons](<./Convex_and_Concave_Polygons.md> "Convex and Concave Polygons") into triangle strips when copying the data from the SOP to the VBO. This will result in a single batch for all of the concave polygons. The conversion does result in some extra CPU cost though when updating the VBO. [Convex Polygons](<./Convex_and_Concave_Polygons.md> "Convex and Concave Polygons") need to be broken up into smaller polygons, and are not currently optimized for fast rendering.


For Concave Polygons 
* * Cost #1 : Low
    * Cost #2 : High
    * Cost #3 : High
    * Cost #4 : Low


For Convex Polgyons, or a mix of convex and concave. 
* * Cost #1 : Medium
    * Cost #2 : High
    * Cost #3 : High
    * Cost #4 : High
* Mesh - Meshes are rendered as triangle strips. Also by using triangle strip stitching any number of meshes can be rendered as a single batch. 
    * Cost #1 : None
    * Cost #2 : Low
    * Cost #3 : Medium
    * Cost #4 : Low
* Circle, Tube and Sphere primitives - Vulkan does not support these primitives so for each one a set of triangle strips needs to be created. Each primitive will be rendered individually as one batch. Although they are rendered using triangle strips, they can not currently benefit from triangle strip stitching. Therefore rendering a large number of primitive circle, tubes or spheres will have a large CPU cost. 
    * Cost #1 : High
    * Cost #2 : Medium
    * Cost #3 : Medium
    * Cost #4 : High
* Particles - Particles are either converted to points/lines, or Point Sprites. Any number particles can rendered with a single batch. 
    * Cost #1 : None
    * Cost #2 : Medium
    * Cost #3 : Medium
    * Cost #4 : Low
* NURB/Bezier Surfaces and Curves - These surfaces first need to be converted polygons, triangles, and triangle strips. This conversion has a large CPU cost, as well as the CPU cost involved with all of the batches needed. 
    * Cost #1 : High
    * Cost #2 : Medium
    * Cost #3 : Medium
    * Cost #4 : High
* Metaballs - Metaballs are converted into polygons. The conversion to polygons has a large CPU cost. It should only require one batch to render a metaball though. 
    * Cost #1 : High
    * Cost #2 : Medium
    * Cost #3 : High
    * Cost #4 : Low


A SOP with a mix of primitive types throws this information off though. For example a triangle followed by a metaball followed by a triangle will result in 3 batches. While a triangle followed by a triangle followed by a metaball would only result in 2 batches. Essentially having a mix of primitive types can cause Cost #4 to be high no matter what. If you find you have large 'Rendering a Batch of VBO' entries in your performance monitor, you should consider simplifying your geometry into a single type of primitive that has a low cost for cost #4. 

### Vertex Count

Depending on what kind of shader is in use, the vertex count may or not be an important factor. If you are using the default Phong MAT, or any shader with a cheap vertex shader, the vertex count is unlikely to affect your rendering speed. In fact it's more likely a high vertex count will cause memory shortages before it causes rendering slowdowns. 

Exceptions to this are when you have a heavy vertex shader. A material that is doing deforms with a *very* large number of bones per vertex, or a shader that is doing vertex shader texture lookups may suffer if the vertex count of your geometry is high, but this is still unlikely. 

### SOP Count

As mentioned earlier, each SOP requires at least 1 batch to render. Whenever possible, reducing the number of SOPs using Merge SOPs will result in both CPU and GPU speed improvements. If your SOPs are cooking every frame though, Merge SOPs can be more expensive than the CPU cost of rendering extra batches, so Merge SOPs should be avoided if they will cook every frame.
