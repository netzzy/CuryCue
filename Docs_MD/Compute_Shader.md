# Compute Shader

## Overview  
  
GPUs can be thought of as processors with 1000s of very light-weight threads that can be run. These threads are usually used to process vertices or pixels. However Compute Shaders allows GLSL developers to utilize these threads in a more general way, separate from the concept of rendering and rasterizing polygons into pixels. 

Typical GLSL vertex/pixel shader programs will transform vertices (vertex shader), rasterize them into pixels and color those pixels using the pixel shader. The number of pixels that are written to is controlled by the number pixels the polygon covers. The results are always written to color and depth buffers. Pixel shaders can only write to the output color buffer once per render pass, they cannot read back neighboring output pixels' results and change their value based on that. They also cannot control where their results are written in the color buffer. The output pixel that is written to is hard-wired based on where the pixel is rendered. 

Compute shaders are different, they don't have a predefined set of inputs and outputs that limit their scope. They are simply run, with a specified configuration for the threads, and what they do is entirely up to the GLSL code. Each thread can read values from textures, perform calculations, and write values out at arbitrary locations. In the same shader they can then read values written by other threads and perform more calculations on those. 

Compute shaders are relatively complex to write properly. There is a lot of caveats on performance, and those caveats are very hardware-dependent. For help on learning how to write compute shaders, please refer to the many tutorials available around the internet. 

Caveat: Compute Shaders need GLSL 4.30 or later. 

See the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") which has one docked compute shader as well as a normal GLSL shader. Change he Mode to Compute Shader.
