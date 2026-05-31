# Rendering

## Overview  
  
Rendering is the creation of a 3D image with the Render TOP. Rendering is also used more generally to include the compositing (with TOPs) to generate an output image. 

Rendering or "rasterization" in TouchDesigner is done through GLSL and includes these features: 
* GLSL pixel shaders, vertex shaders, and geometry shaders
  * deformations in programmable GLSL vertex shaders
  * real-time materials in GLSL pixel shaders
  * advanced material options; bumps, displacements, reflections, transparency, darkness emission
  * real-time rendering of 3D scenes, including multi-pass rendering abilities
  * advanced rendering techniques; anti-aliasing, soft-edge cone lights, rim lights, fog, alpha blends
  * 3D textures and 2D Texture arrays
  * real-time depth shadows
  * multi-layer textures
  * materials and shaders system integrated with TOPs compositing engine
  * integrated particle system with sprite rendering
  * SSAO


Rendering is achieved in TouchDesigner using the [Render TOP](<./Render_TOP.md> "Render TOP") and the [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP"). To render objects you need to do a few things. 
* Create a [Camera COMP](<./Camera_COMP.md> "Camera COMP") and assign it to the Render TOPs **Camera** parameter.
  * Assign [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP")(s) to be rendered
  * Make sure the [Render Flag](<./Render_Flag.md> "Render Flag") is turned on for every SOP and COMP that you want to render.
  * Create and assign [Light COMP](<./Light_COMP.md> "Light COMP")(s)
  * Assign materials ([MATs](<./MAT.md> "MAT")) to the Geometry COMPs. (A default material will be assigned if none is listed).


This may be helpful: [Why is My Render Black](<./Why_is_My_Render_Black.md> "Why is My Render Black")

## What is a Render Pass TOP and why use it?

The Render TOPs uses an off-screen buffer to do its rendering. When it is finished rendering it copies the color output to a texture, which can in turn be used in subsequent renders or as the input into any TOP. 

Today's graphics card have two types of memory on-board. They have fast GPU memory, and slower GPU memory. One of the keys to fast rendering is to make sure the off-screen buffer stays inside this fast memory. Each Render TOP has its own off-screen buffer, so the more Render TOPs you have, the more likely these off-screen buffers will get pushed out of the fast memory. To help avoid this, we created the Render Pass TOP. 

The Render Pass TOP does all of the same things that the Render TOP does, but it re-uses the off-screen buffer that the Render TOP creates. A project that uses a Render TOP and a Render Pass TOP instead of two Render TOPs will usually run significantly faster, even though they are rendering the same amount of geometry. A Render Pass TOP can take either a Render TOP or a Render Pass TOP as an input, so you can have a chain of Render Pass TOPs of any length (the first node just needs to be a Render TOP). 

A common use of the Render Pass TOP is to add things on-top of the previous render. The off-screen buffer that the Render and Render Pass TOPs share also contains the [Depth Buffer](</index.php?title=Depth_Buffer&action=edit&redlink=1> "Depth Buffer \(page does not exist\)"), so an object rendered in a Render Pass TOP will be placed and occluded correctly in the scene, using the depth information that is coming along with the off-screen buffer (assuming the Depth Buffer isn't cleared, which is an option in the Render Pass TOP). 

## Limitations

A consequence of this behavior is that the contents of the off-screen buffer will be polluted by whatever the Render Pass TOP does. Because of this, a 2nd Render Pass TOP that is also trying to use the output of the Render TOP will not have the correct information to start from. 

Due to this issue, Render and Render Pass TOPs must be arranged in a linear fashion. Each Render and Render Pass TOP can only have 1 Render Pass TOP as an output. Trying to connect two Render Pass TOPs to the same Render or Render Pass TOP will result in an error. 

This is also true when using the **Render/Render Pass TOP** parameter in the Render Pass TOP. This parameter is an alternative to wiring the two nodes together. It does not allow for a non-linear chain of Render and Render Pass TOPs, the nodes can just be located in different networks.
