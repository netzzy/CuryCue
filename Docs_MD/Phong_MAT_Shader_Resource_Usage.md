# Phong MAT Shader Resource Usage

## Overview  
  
Each GPU has a limited set of resources available on the card that it can use when executing a shader. These resource limits affect how many lights, bones, and other features, that can be used at the same time. This limit is on a per-object basis. You can use 100s of lights in your scene, as long as only a limited number of lights affect each individual object (using the Light Mask parameter). 

## Varyings

A varying is a value that is passed from the vertex shader to the pixel shader. This value is calculated on a per-vertex basis, and then gets interpolated across the primitive (using the varyings from the other vertices that make up the primitive to interpolate with). This is how a uv[3] attribute, which is set per-vertex, is able to correctly texture map a primitive. 

Most GPUs today have between 32 and 40 varyings available for use. To find out how many your card has you can look at the $SYS_GFX_GLSL_MAX_VARYINGS variable which is a Built-In [Variable](<./Variables.md> "Variables"). 

Some examples of things that are passed through varyings are, position (light positions), vectors (spotlight directions, normals), texture coordinate, projection mapping and shadow mapping information. 

Depending on how the vector math is done in the shader, some of these values may be given to the pixel shader through Uniforms, instead of calculated in the vertex shader and passed to the pixel shader through varyings. In particular, whether or not normal mapping is used greatly changes the vector math in the shaders, resulting in much different varying usage. 

### Varying Usage when not Normal Mapping

\- For Each Light (of any type), 3 varyings are used for the vector from the light position to the vertex position.  
\- For Each Light (of any type), 1 varying is used if the light is attenuated.  
\- For Each Light (of any type), 4 varyings are used if that light is shadow mapped (and the shadow strength on the MAT isn't 0).  
\- For Each Light (of any type), 3 varyings are used if that light is projection mapped.  
\- If specular is on (specular color isn't (0,0,0)), or varying alpha is used, 3 varyings are used for the vector from the camera position to the vertex position.  
\- If rim lights, diffuse, specular or varying alpha is used, 3 varyings are used for the normal vector.  
\- If environment mapping, 2 varyings are used for the environment texture coordinates.  
\- For each unique texture coordinate set used, 2 or 3 varyings are used for the texture coordinates (3 if a 3d texture is being sampled, 2 otherwise). If you are using many different types of maps (Color Map and Specular Map for example), but they are using the same set of texture coordinates (all are using texture set 0, uv[0-2], for example), then the varying usage is only 2-3. They care both use the same varyings when sampling the textures in the pixel shader.  

### Varying Usage when Normal Mapping

\- For Each Light (of any type), 3 varyings are used for the vector from the light position to the vertex position.  
\- For Each Light (of any type), 1 varying is used if the light is attenuated.  
\- For Each Spot Light, 3 varyings are used for the spot direction.  
\- For Each Light (of any type), 4 varyings are used if that light is shadow mapped (and the shadow strength on the MAT isn't 0).  
\- For Each Light (of any type), 3 varyings are used if that light is projection mapped.  
\- If specular is on (specular color isn't (0,0,0)), or varying alpha is used, 3 varyings are used for the vector from the camera position to the vertex position.  
\- If rim lights are used, 3 varyings are used for the normal vector. For other features that need the normal, they use the one that they get from the normal map.  
\- If environment mapping, 2 varyings are used for the environment texture coordinates.  
\- For each unique texture coordinate set used, 2 or 3 varyings are used for the texture coordinates (3 if a 3d texture is being sampled, 2 otherwise). If you are using many different types of maps (Color Map and Specular Map for example), but they are using the same set of texture coordinates (all are using texture set 0, uv[0-2], for example), then the varying usage is only 2-3. They care both use the same varyings when sampling the textures in the pixel shader.  

### If you need more lights per object

If you need more lights per object than your GPU can do in a single pass, you can use a [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP") to re-render the same geos, using the same camera, with a different set of lights. Then simply use an [Add TOP](<./Add_TOP.md> "Add TOP") to add the results between the first and second render. 

## Uniforms

A uniform is a value that is constant for the entire execution of the shader. Some examples of uniforms are the diffuse, specular, and emission color. Other uniforms are the bone matrices (if doing deforms), and light information like light color.
