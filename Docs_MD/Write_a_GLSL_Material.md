# Write a GLSL Material

## Overview

This document explains the finer points of writing a GLSL Material in TouchDesigner. It is assumed the reader already has an understanding of the GLSL language. The official GLSL documentation can be found at [this address.](<https://www.khronos.org/opengl/wiki/Core_Language_\(GLSL\)>)

### GLSL Version

TouchDesigner uses GLSL 3.30 and newer versions as it's language. Many online examples, as well as WebGL shaders, are written against GLSL 1.20. There are some significant language differences between GLSL 1.20 and GLSL 3.30+. For information about some of these differences, please refer to [Changes from GLSL 1.20](<#Changes_from_GLSL_1.20>)

### The concept of GLSL Shaders

A GLSL [Shader](<./Shader.md> "Shader") is a program that is applied to geometry as it is being rendered. A GLSL shader is split into two main components, vertex shader and pixel shader. 

**Vertex Shader** \- A vertex shader is a program that is applied to every vertex of the geometry the Material is applied to. 

**Pixel Shader** \- A pixel shader is a program that is applied to every pixel that is drawn. This is often also referred to as a Fragment Shader. 

There is also the **Geometry Shader**, which is a stage between the vertex and pixel stages, but it isn't used very often. For more information on Geometry Shaders have a look [here](<https://open.gl/geometry>). 

### TouchDesigner GLSL conventions

All functions and uniforms provided by TouchDesigner as augmentations of the GLSL language will follow these conventions. 
* Function names will always start with the letters`TD`. e.g.`TDLighting()`.
* Uniforms will start with the letters`uTD`.
* Samplers will start with the letters`sTD`.
* Images will start with the letters`mTD`.
* Vertex input attributes will be named the same as they are in the TouchDesigner SOP interface (P, N, uv).


Most uniforms provided by TouchDesigner will be contained in Uniform Blocks. This means instead of accessing a single matrix by`uTDMatrixName`, the matrices will be stored a single block with many matrices such as`uTDMats`, which has members such as`uTDMats[0].worldCam`and`uTDMats[0].projInverse`. 

## Shader Stages

### Vertex Shader

Inside a vertex shader you only have access to one vertex, you don't know the positions of other vertices are or what the output of the vertex shader for other vertices will be. 

The input to a vertex shader is all the data about the particular vertex that the program is running on. Data like the vertex position in SOP space, texture coordinate, color, normal are available. These values are called attributes. Attributes are declared in the vertex shader using the`in`keyword. 

The vertex shader can output many things. The primary things it will output are the vertex position (after being transformed by the world, camera and projection matrix), color, and texture coordinates. It can output any other values as well using output variables declared using`out`. Outputs from a vertex shader are linearly interpolated across the surface of the primitive the vertex is a part of. For example, if you output a value of 0.2 at 1st vertex and a value of 0.4 at the 2nd vertex on a line, a pixel drawn half-way between these two points will receive a value of 0.3. 

### Pixel Shader

The inputs to a pixel shader are all of the outputs from the vertex shader, and any uniforms that are defined. The outputs from the vertex shader will have been linearly interpolated across the polygon that the vertices created. A pixel shader can output two things: Color and Depth. Color is output through the variable declared as`layout(location = 0) out vec4 whateverName`. Depth is output through a variable declared as`out float depthName`. You can name these variables whatever you want. You are required to write out a color value, but you do not need to write out depth (in fact it's best if you don't unless absolutely needed). GLSL will automatically output the correct depth value for you if you don't write out a depth value. If you are outputting to multiple color buffer, you declare more color outputs with the`location`value set to 1, 2, 3, etc., instead of 0. 

### Geometry Shader

A geometry shader takes a single point primitive points, line or triangle, and outputs set of points, line strips, or triangle strips. Currently in TouchDesigner the input primitive types you must use to match with what we are rendering is one of: 
[code] 
     layout(points) in;
     layout(lines_adjacency) in;
     layout(triangles) in;
    
[/code]

Other input types such as`lines`or`triangles_adjacency`is not currently supported. 

**Note** \- In the 2018.20000 series of builds`lines`were supported and`lines_adjacency`were not, so the change to the 2019.10000 that switched the support to`lines_adjacency`unfortunetely breaks existing geometry shaders. 

## A Basic Shader

### Vertex Shader

This vertex shader will simply transform each vertex correctly and leave it entirely up to the pixel shader to color the pixels: 
[code] 
    void main()
    {
    	// P is the position of the current vertex
    	// TDDeform() will return the deformed P position, in world space.
    	// Transform it from world space to projection space so it can be rasterized
    	gl_Position = TDWorldToProj(TDDeform(TDPos()));
    }
    
[/code]

### Pixel Shader

This pixel shader simply sets every pixel to red: 
[code] 
    // We need to declare the name of the output fragment color (this is different from GLSL 1.2 where it was automatically declared as gl_FragColor)
    out vec4 fragColor;
    void main()
    {
    	fragColor = vec4(1, 0, 0, 1);
    }
    
[/code]

## Working with Geometry Attributes

The follow vertex shader attributes (inputs) will always be declared for you to use in your vertex shader. You do not need to declare them yourself. 
[code] 
    vec3 TDPos(); // Vertex position
    vec3 TDNormal(); // normal
    vec3 TDTexCoord(uint coordLayer); // texture coordinate layers
    
[/code]

**Other Attributes**

All other attributes you want to use need to be declared in your shader code. are passed as custom attributes. For forward compatibility with POPs in the future, these attributes should be declared using the 'Attributes' page on the GLSL MAT. The declared attributes can be accessed via a function call to`TDAttrib_AttribName()`. For example if you declare a custom attribute called 'life'. You would access it in the shader using`TDAttrib_life()`. 

For convenience`TDTexAttrib_AttribName(uint textureLayer)`returns`TDAttrib_AttribName()`for POPs and`uv[textureLayer]`for SOPs so shader code can be more easily shared between POPs and SOPs 

For POPs the attribute value for any vertex can be accessed by specifying a vertex index argument. 
[code] 
    attribType TDAttrib_AttribName(uint arrayIndex, uint vertIndex) //access to input geo attribute (has to be declared on Attributes page)
    TDAttrib_AttribName(uint arrayIndex) = TDAttrib_AttribName(arrayIndex, gl_VertexID); //vertIndex is optional, defaults to gl_VertexID
    TDAttrib_AttribName() = TDAttrib_AttribName(0, gl_VertexID);
    //for points and primitive attributes lookups are performed based on the vertex;
    
    const uint cTDAttribArraySize_AttribName //constant with size of array for array attributes
    
[/code]

**Other POP Attributes**

To access any POP attribute by element index, you can use the Buffers page: 
[code] 
    attribType TDBuffer_AttribName(uint elementIndex, uint arrayIndex); //access to POP attribute buffer declared on Buffer Page
    TDBuffer_AttribName(uint elementIndex) = TDBuffer_AttribName(elementIndex, 0); //arrayIndex is optional, defaults to 0
    
    const uint TDBufferLength_AttribName(); //length of buffer
    const uint cTDBufferArraySize_AttribName; //constant with size of array for array attributes
    
[/code]

## TouchDesigner specific defines

Shaders in TouchDesigner are dynamically recompiled based on a few things such as the number and types of lights in the scene or the number of cameras used in this pass (in the case of [Multi-Camera Rendering](<#Multi-Camera_Rendering>)). This is done for optimization purposes since loops with known amounts of iterations are far faster in GLSL. Some defines are provided which allow code written by end-users to be recompiled with different numbers of lights/cameras correct. 
[code] 
    // This define will be defined at compile time, and your shader will be recompiled for each combination
    // of lights in use (if it's is used in multiple light configurations). You can use it for things like a loop
    // counter to loop over all lights in the scene, as you will see if you output example code from the Phong MAT.
    // Environment COMPs are counted separately from regular Light COMPs.
    #define TD_NUM_LIGHTS <defined at compile time>
    #define TD_NUM_ENV_LIGHTS <defined at compile time>
    
[/code]
[code] 
    // On newer hardware multiple cameras can be rendered at the same time. This define will be set to the
    // number of cameras done on this render pass. This may be 1 or more, depending on many factors.
    // Code should be written in a way that should work regardless of what this value is.
    #define TD_NUM_CAMERAS <defined at compiler time>
    
[/code]
[code] 
    // One of these defines will be set depending on which shader stage is being compiled.
    // This allows shaders to use #ifdef <stageName> and #ifndef <stageName> to either include or
    // omit code based on the current shader stage being included. This also allows for single
    // large DATs to contain all the code for all stages, with each portion #ifdef-ed in for
    // each stage.
    #define TD_VERTEX_SHADER
    #define TD_GEOMETRY_SHADER
    #define TD_PIXEL_SHADER
    #define TD_COMPUTE_SHADER
    
[/code]

## TouchDesigner specific Uniforms

These are uniform that TouchDesigner will automatically set for you. You do not need to declare any of these, you can just use them in your shaders. 
[code] 
    // General rendering state info
    struct TDGeneral {
      vec4 ambientColor;  // Ambient light color (sum of all Ambient Light COMPs used)
      vec4 viewport;      // viewport info, contains (x, y, 1.0 / w, 1.0 / h). x/y/w/h are in pixel units.   
    };
    uniform TDGeneral uTDGeneral;
    // So for example you'd get the ambient color by doing 
    // vec4 ambientColor = uTDGeneral.ambientColor;
    
[/code]
[code] 
    // Matrices
    struct TDMatrix
    {
    	mat4 world;			// world transform matrix, combination of hierarchy of Object COMPs containing the SOP.
    						// transforms from SOP space into World Space
    	mat4 worldInverse;	// inverse of the world matrix
    	mat4 worldCam;		// multiplication of the world and the camera matrix. (Cam * World)
    	mat4 worldCamInverse;
    	mat4 cam;			// camera transform matrix, obtained from the Camera COMP used to render
    	mat4 camInverse;
    	mat4 camProj;		// camera transform and the projection matrix from the camera COMP, (Proj * Cam)
    	mat4 camProjInverse;
    	mat4 proj;			// projection matrix from the Camera COMP. The Z range will be [0,1], Vulkan style.
    	mat4 projInverse;
    	mat4 worldCamProj;	// multiplication of the world, camera and projection matrices. (Proj * Cam * World)
    						// takes a vertex in SOP space and puts it into projection space
    	mat4 worldCamProjInverse;
    	mat3 worldForNormals;	// Inverse transpose of the world matrix, use this to transform normals
    							// from SOP space into world space
    	mat3 camForNormals;		// Inverse transpose of the camera matrix, use this to transform normals
    							// from world space into camera space
    	mat3 worldCamForNormals;	// Inverse transpose of the worldCam matrix, use this to transform normals
    								// from SOP space into camera space inverse(transpose(Cam * World))
    	   
    };
    uniform TDMatrix uTDMats[TD_NUM_CAMERAS];
    // For example you'd transform the vertex in SOP space into camera space with this line of code
    // vec4 camSpaceVert = uTDMats[TDCameraIndex()].worldCam * vec4(TDPos(), 1.0);
    
[/code]
[code] 
    struct TDCameraInfo
    {
    	vec4 nearFar;			// near/far plane info, contains (near, far, far - near, 1.0 / (far - near))
    	vec4 fog;				// fog info, as defined in the Camera COMP
    							// contains (fogStart, fogEnd, 1.0 / (fogEnd - fogStart), fogDensity)
    	vec4 fogColor;			// Fog Color as defined in the Camera COMP
    	int renderTOPCameraIndex;	// Says which camera from the Render TOP's 'Cameras' parameter this particular camera is.
    };
    uniform TDCameraInfo uTDCamInfos[TD_NUM_CAMERAS];
    
[/code]

In general you don't need to do anything with any of these light uniforms/samplers, as it's all done for you in the`TDLighting(), TDLightingPBR() and, TDEnvLightingPBR()`functions. Only if you are doing custom lighting will you need to worry about these. 
[code] 
    struct TDLight
    {
    	vec4 position;		// the light's position in world space
    	vec3 direction;		// the light's direction in world space
    	vec3 diffuse;		// the light's diffuse color
    	vec4 nearFar;		// the near and far settings from the light's View page
    						// contains (near, far, far - near, 1.0 / (far - near)
    	vec4 lightSize;		// values from the light's Light Size parameter
    						// containers (light width, light height, light width / light projection width, light height / light projection height)
    	vec4 misc;			// misc parameters values, right now it contains
    						// (Max shadow softness, 0, 0, 0)
    	vec4 coneLookupScaleBias;	// applied to a cone light's contribution to create the spot lit area
    								// contains (coneLookupScale, coneLookupBias, 1.0, 0.0).
                                    // If the light is not a cone light, this will contain (0.0, 0.0, 0.0, 0.0).
    	vec4 attenScaleBiasRoll;	// applied to the light's distance from the point to get an attenuation value
    								// contains (attenuation scale, attenuation bias, attenuation rolloff, 0)
    	mat4 shadowMapMatrix;		// transforms a point in world space into the projection space of the shadow mapped light
    								// also rescales projection space from [-1, 1] to [0, 1], so the value can be used
    								// to lookup into a shadow map
    	mat4 shadowMapCamMatrix;	// transforms a point in world space into the camera space of the shadow mapped light
    	vec4 shadowMapRes;			// the resolution of the shadow map associated with this light
    								// contains (1.0 / width, 1.0 / height, width, height)
    								// filled with 0s if the light isn't shadow mapped
    	mat4 projMapMatrix;			// transforms a point in world space into the projection map space of the light
    								// used when using textureProj() function for projection mapping
    } 
    uniform TDLight uTDLights[TD_NUM_LIGHTS];
    
[/code]
[code] 
    struct TDEnvLight
    {
    	vec3 color;					// Color of the env light (not counting it's environment map)
    	mat3 rotate;				// Rotation to be applied to the env light.
    };
    uniform TDEnvLight uTDEnvLights[TD_NUM_ENV_LIGHTS];
    
[/code]
[code] 
    // This one is held differently since it's backed by a storage buffer object and not a uniform buffer object.
    buffer TDEnvLightBuffer
    {
    	vec3 shCoeffs[9]; // Spherical harmonic coefficients calculated from the environment map. Used for diffuse PBR lighting.
    } uTDEnvLightBuffers[TD_ENV_LIGHTS_ARRAY_SIZE];
    
[/code]

When using sampler3D created using a [Texture 3D TOP](<./Texture_3D_TOP.md> "Texture 3D TOP"), it can sometimes be useful to know which slice is the 'newest' slice in the array, when using the [Texture 3D TOP](<./Texture_3D_TOP.md> "Texture 3D TOP") as a circular cache. The P-coordinate location of where the newest slice will provided by a uniform named the same as your sampler, with the suffix 'POffset'. For example if you have a uniform named sColorMap, you can declare a matching`sColorMapPOffset`uniform and it will automatically be filled in for you. 
[code] 
    uniform float sColorMapPOffset; // P offset to newest slice in sampler3D named sColorMap
    
[/code]

## TouchDesigner specific Functions

Further details about each of these functions are given in the sections following this. 

### Vertex Shader Only Functions
[code] 
    // Transforms a point from world space to projection space. 
    // These functions should always be used to output to gl_Position, allowing TouchDesigner to do custom manipulations
    // of the values as needed for special operations and projections.
    // The extra manipulations that are currently done are:
    // 1. Conversions to other projections such as FishEye
    // 2. Conversions to Quad Reprojection using TDQuadReproject()
    // 3. Adjustments needed for picking using TDPickAdjust().
    // When using this function you should not call the above functions, since it will do those for you.
    // Both the vec4 and vec3 version of TDWorldToProj() treat the xyz as a point, not a vector.
    vec4 TDWorldToProj(vec4 v);
    vec4 TDWorldToProj(vec3 v);
    
    
    // These ones take an extra 'uv' coordinate, which is used when UV Unwrapping is done in the Render TOP.
    // If the version without the uv is used, then TDInstanceTexCoord(TDUVUnwrapCoord()) will be used to get the texture coord.
    vec4 TDWorldToProj(vec4 v, vec3 uv);
    vec4 TDWorldToProj(vec3 v, vec3 uv);
    
[/code]
[code] 
    // Returns the color for this vertex/point, including handling alpha-premultiplication correctly.
    // This replaces accessing it directly via 'Cd', as was done in the past.
    vec4 TDPointColor();
    
[/code]
[code] 
    // Returns the instance ID for the current instance. This should always be used, not gl_InstanceID directly.
    // For more information look at the Instancing section of this document.
    int TDInstanceID();
    
[/code]
[code] 
    // Returns the index of the camera for this particular vertex, within this batch. Needed to support Multi-Camera Rendering.
    // This is always 0-based, and it does not reflect which camera is being currently being used from the Render TOP.
    // Due to multiple batches being needed for split up larger amounts of cameras, this number resets to be 0 each batch.
    // To get the actual camera index as it's listed in the Render TOP, use the uTDCamInfos[TDCameraIndex()].renderTOPCameraIndex
    // or, in builds 2022.32790 and later TDTrueCameraIndex().
    int TDCameraIndex();
    
[/code]
[code] 
    // Available in builds 2022.32790 and later.
    // Returns the index of the camera as it's listed in the Render TOP.
    int TDTrueCameraIndex();
    
[/code]
[code] 
    // Deforms a point or vector using instancing and skinned deforms. The returned result is in World Space.
    // Be sure to use the *Vec version in the case of vectors to get correct results.
    // Also use the *Norm version when deforming a normal, to make sure it still matches the surface correctly.
    /// These functions will internally call TDSkinnedDeform() and TDInstanceDeform().
    vec4 TDDeform(vec4 pos);
    vec4 TDDeform(vec3 pos);
    vec3 TDDeformVec(vec3 v);
    vec3 TDDeformNorm(vec3 n);
    
[/code]
[code] 
    // These versions allow you to control the instanceID used for the deform.
    vec4 TDDeform(int instanceID, vec3 pos);
    vec3 TDDeformVec(int instanceID, vec3 v);
    vec3 TDDeformNorm(int instanceID, vec3 n);
    
[/code]
[code] 
    // ** In general you don't need to call any of the below functions, just calling TDDeform or TDDeformVec will
    // do all the work for you
    // Just the skinning or instancing portion of the deforms
    // Returned position/vector is in SOP space for the *Skinned* version, and world space for the *Instance* version.
    vec4 TDSkinnedDeform(vec4 pos);
    vec3 TDSkinnedDeformVec(vec3 vec);
    vec4 TDInstanceDeform(vec4 pos);
    vec3 TDInstanceDeformVec(vec3 vec);
    
[/code]
[code] 
    // You also don't need to call these usually, but are available for special cases
    // For instancing functions, if you don't provide an index, it will use TDInstanceID().
    mat4 TDBoneMat(int boneIndex);
    mat4 TDInstanceMat(int instanceID);
    mat4 TDInstanceMat();
    // Returns a 3x3 matrix only. Useful if you are only working with vectors, not positions.
    // If you are using both, it is faster to just call TDInstanceMat(), and cast the result to a mat3
    // when required.
    mat3 TDInstanceMat3(int instanceID);
    mat3 TDInstanceMat3();
    
[/code]
[code] 
    // To calculate the texture coordinates for your instance (if used in the Geometry COMP's parameters), use these functions
    // For texture coordinates the passed in variable 't' is the current texture coordinate to be modified/replaced
    vec3 TDInstanceTexCoord(int instanceID, vec3 t);
    vec3 TDInstanceTexCoord(vec3 t);
    
[/code]
[code] 
    // TDWorldToProj() will already apply the Quad Reproject feature if used by the [[Camera COMP]].
    // However in same cases you may be doing custom operations that require it to be applied manually.
    // This function just returns the point unchanged if Quad Reproject isn't being used.
    vec4 TDQuadReproject(vec4 v, int camIndex);
    
[/code]
[code] 
    // Available in builds 2019.32020 or later.
    // TDWorldToProj() will already apply the Picking adjustment if required (when picking is occuring).
    // However in same cases you may be doing custom operations that require it to be applied manually.
    // This function should be given the position after it's been transformed into projection space.
    // This function just returns the point unchanged if picking isn't active for this render.
    vec4 TDPickAdjust(vec4 v, int camIndex);
    
[/code]
[code] 
    // Returns the uv coordinate that was selected for UV unwrapping in the Render TOP
    vec3 TDUVUnwrapCoord();
    
[/code]

### Geometry Shader Only Functions
[code] 
    // Similar to th ones in the vertex shader, but require a camera index since it
    // needs to be passed through to the geometry shader via a input variable.
    vec4 TDWorldToProj(vec4 v, vec3 uv, int cameraIndex);\n";
    vec4 TDWorldToProj(vec3 v, vec3 uv, int cameraIndex);\n";
    vec4 TDWorldToProj(vec4 v, int cameraIndex);\n";
    vec4 TDWorldToProj(vec3 v, int cameraIndex);\n";
    vec4 TDQuadReproject(vec4 v, int camIndex);
    
[/code]

### Pixel Shader Only Functions
[code] 
    // This function is provided as a wrapper for gl_FrontFacing.
    // It is required since some GPUs (Intel on macOS mainly) have broken
    // functionality for gl_FrontFacing.
    // On most GPUs this just returns gl_FrontFacing. On GPUs where the behavior
    // is broken, an alternative method using position and normal is used to 
    // determine if the pixel is front or back facing.
    // Position and normal should be in the same space, and normal must be normalized.
    bool TDFrontFacing(vec3 position, vec3 normal);
    
[/code]
[code] 
    // Call this function to give TouchDesigner a chance to discard some pixels if appropriate.
    // This is used in things such as order-indepdendent transparency and dual-paraboloid rendering.
    // For best performance call it at the start of the pixel shader.
    // It will do nothing if no features that require it are active, so it's safe to always call it.
    void TDCheckDiscard();
    
[/code]
[code] 
    // Obtain the texture coordinate for point sprite primitives.
    // This must be used instead of gl_PointCoord, otherwise the coordinates may be flipped vertically
    // in some cases.
    vec2 TDPointCoord();
    
[/code]
[code] 
    // Obtain the modified color for this pixel. Pass in the interpolated point color from the vertex shader.
    // This function usually just returns back the passed argument, but when doing Geo Text COMP rendering,
    // it is needed to create the text glyphs.
    vec4 TDPixelColor(vec4 c);
    
[/code]
[code] 
    // Call this function to apply the alpha test to the current pixel. This function will do nothing
    // if the alpha test is disabled, so it can be safely always called
    void TDAlphaTest(float alphaValue);
    
[/code]
[code] 
    // Call this to apply the Camera COMPs fog to the passed color. Requires the world space vertex position also
    // This function will do nothing if fog is disabled, so it's safe to always call it at the end of your shader
    // there would be no performance impact from calling it if fog is disabled
    // the cameraIndex should be passed through from the vertex shader using a varying, sourced from TDCameraIndex()
    vec4 TDFog(vec4 curColor, vec3 worldSpacePos, int cameraIndex);
    
[/code]
[code] 
    // Call this at the end of your shadow to apply a dither to your final color. This function does nothing
    // if dithering is disabled in the Render TOPs parameters
    vec4 TDDither(vec4 curColor);
    
[/code]
[code] 
    // Pass any color value through this function before writing it out to a color buffer.
    // This is needed to ensure that color channels are output to the correct channels
    // in the color buffer, based on hardware limitation that may store alpha-only
    // textures as red-only internally, for example
    vec4 TDOutputSwizzle(vec4 curColor);
    
[/code]

The TDLighting() functions are called per light to determine that light's diffuse and specular contributions. Shadowing, projection mapping are all automatically handled for you inside this functions. 
* The`TDPBRResult or TDPhongResult`return structure will be filled with the results.
  *`lightIndex`is the light index to calculate
  *`worldSpacePos`is the world space vertex position
  *`shadowStrength`is a scalar on the shadow to increase or decrease its effect for example a value of 0.5 would give a maximum 50% shadow.
  *`shadowColor`is a vec3 for the color to shift to when something is shadowed. Usually this is vec3(0).
  *`worldSpaceNorm`is the normalized world space normal
  *`vertToCamVec`is the normalized vector from the vertex position to the camera position.
  *`shininess`is the specular shininess exponent.

#### Physically Based (PBR) Lighting
[code] 
    // Will be filled with the results of the lighting calculations
    struct TDPBRResult
    {
    	vec3 diffuse;
    	vec3 specular;
        // Contains how much the pixel is inside a shadow for this light. 0 means no shadow, 1 means fully shadowed.
    	float shadowStrength;
    };
    
[/code]
[code] 
    // For all regular lights. Should be called in a loop from 0 to TD_NUM_LIGHTS
    TDPBRResult TDLightingPBR(
    	int lightIndex,
    	vec3 diffuseColor,
    	vec3 specularColor,
    	vec3 worldSpacePos,
    	vec3 worldSpaceNormal,
    	float shadowStrength,
    	vec3 shadowColor,
    	vec3 vertToCamVec,
    	float roughness);
    
[/code]
[code] 
    // For environment lights. Should be called in a loop from 0 to TD_NUM_ENV_LIGHTS
    TDPBRResult TDEnvLightingPBR(
    	inout vec3 diffuseContrib,
    	inout vec3 specularContrib,
    	int lightIndex,
    	vec3 diffuseColor,
    	vec3 specularColor,
    	vec3 worldSpaceNormal,
    	vec3 vertToCamVec,
    	float roughness,
    	float ambientOcclusion);
    
[/code]

#### Phong Lighting
[code] 
    // Will be filled with the results of the lighting calculations
    struct TDPhongResult
    {
    	vec3 diffuse;
    	vec3 specular;
    	vec3 specular2;
    	// Contains how much the pixel is inside a shadow for this light. 0 means no shadow, 1 means fully shadowed.
        // This is already accounted for in the returned diffuse/specular colors, but is returned here as extra
        // meta-information which can be used for other 
    	float shadowStrength;
    };
    
[/code]
[code] 
    TDPhongResult TDLighting(
    	int lightIndex,
    	vec3 worldSpacePos,
    	vec3 worldSpaceNorm,
    	float shadowStrength,
    	vec3 shadowColor,
    	vec3 vertToCamVec,
    	float shininess,
    	float shininess2
    );
    
[/code]

#### Common Lighting Functions
[code] 
    // In general you don't need to use these functions, they are called for you in the TDLighting() functions.
    // These functions return the shadow strength at the current pixel for light at the given index.
    // Also requires the world space vertex position to do its calculations
    // returns undefined results if the shadow isn't mapped using the chosen shadow type
    // The returned value is 0 for no shadow, 1 for 100% shadowed
    // Due to percentage closer filtering, hard shadows can still have values between 0 and 1 at the edges of the shadow
    float TDHardShadow(int lightIndex, vec3 worldSpacePos);
    // This one will apply soft shadows with both 25 search steps done, and 25 filter samples.
    float TDSoftShadow(int lightIndex, vec3 worldSpacePos);
    // Allows for control of search steps and filter samples.
    float TDSoftShadow(int lightIndex, vec3 worldSpacePos, int samples, int searchSteps);
    
[/code]
[code] 
    // Gets the projection map color for the given world space vertex position.
    // No other lighting calculations are applied to the returned color
    // If the given light index is not using a projection map, then 'defaultColor' is returned.
    vec4 TDProjMap(int lightIndex, vec3 worldSpacePosition, vec4 defaultColor);
    
[/code]
[code] 
    // Directly access environment maps for the env lights. Will be black for lights that don't have a map
    // of that particular dimensionality.
    // For the 2D map based env lights.
    vec4 TDEnvLightTextureLod(int lightIndex, vec2 coord, float mipLevel);
    // For the Cube map based env lights.
    vec4 TDEnvLightTextureLod(int lightIndex, vec3 coord, float mipLevel);
    
[/code]
[code] 
    // For directly accessing the shadow maps. All of these access the same maps (per index), but are setup in compare or sampling mode.
    // A returned value of 1 means it's fully in the shadow, 0 means it's not in the shadow.
    // For lights indices that aren't generating shadows, these functions will return 0.
    // These two first one is used in the function texture(sampler2DShadow, vec3) or textureProj(sampler2DShadow, vec4)
    // for automatic depth comparison and hardware percentage closer filtering.
    float TDCompareShadowTexture(int lightIndex, vec2 coord, float depth);
    float TDCompareShadowTextureProj(int lightIndex, vec4 coord);
    
    // These ones is used for directly getting the depth from the shadow map using
    // texture(sampler2D, vec2) or textureProj(sampler2D, vec3).
    // If using hard shadows the values are in [0, 1] post-projection depth units.
    // If using soft shadows the values are in camera space of the light (not the camera being rendered from).
    float TDShadowTexture(int lightIndex, vec2 coord);
    float TDShadowTextureProj(int lightIndex, vec3 coord);
    
[/code]
[code] 
    // The projection maps defined in the Projection Map parameter of the Light COMP.
    // The map will return black if the light doesn't have a projection map defined.
    vec4 TDProjTexture(int lightIndex, vec2 coord, float mipMapBias);
    // Samples the texture using the same rules as textureProj().
    vec4 TDProjTextureProj(int lightIndex, vec3 coord);
    
[/code]
[code] 
    // The falloff ramp from when the cone light starts to fade out until it reaches black.
    // Used in combination with uTDLights[].coneLookupScaleBias.
    // Will return 1.0 when the light is not a cone light.
    float TDConeLookup(int lightIndex, float coord);
    
[/code]

### Common Functions

Available in all shader stages. 

#### General functions
[code] 
    // A function that gives a half-sine ramp from 0 to 1.
    // Sampling it with a coordinate outside the (0, 1) range will return 0 for anything below 0 and 1 for anything above 1.
    // It's possibly faster than using the GLSL sin() function, depending on the hardware.
    float TDSineLookup(float coord);
    
[/code]

#### Matrix functions
[code] 
    // Creates a translation matrix for the given 3 translation values.
    mat4 TDTranslate(float x, float y, float z);
    
    // Creates a rotation matrix that rotates around the +X, +Y and +Z axis repectively.
    mat3 TDRotateX(float radians);
    mat3 TDRotateY(float radians);
    mat3 TDRotateZ(float radians);
    
    // Creates a rotation matrix that rotates around the 'axis', the given number of 'radians'
    // The 'axis' vector must already be normalized before being passed to this function.
    mat3 TDRotateOnAxis(float radians, vec3 axis);
    
    // Creates a scale matrix for the given 3 scale values.
    mat3 TDScale(float x, float y, float z);
    
    // Creates a rotation matrix that rotates starting from looking down +Z, to the 'forward' vector direction.
    // The 'forward' and 'up' vectors passed to this function do not need to be normalized.
    mat3 TDRotateToVector(vec3 forward, vec3 up);
    
    // Creates a rotation matrix to rotate from vector 'from' to vector 'to'. The solution isn't particularly stable, but useful in some cases.
    // The 'from' and 'to' vectors must already be normalized before being passed to this function.
    mat3 TDCreateRotMatrix(vec3 from, vec3 to);
    
[/code]
[code] 
    // Takes a surface normal, the tangent to the surface, and a handedness value (either -1 or 1)
    // Returns a matrix that will convert vectors from tangent space, to the space the normal and tangent are in
    // Both the normal and the tangent must be normalized before this function is called.
    // The w coordinate of the T attribute created by the [[Attribute Create SOP]] contains the handedness
    // that should be passed in as-is.
    mat3 TDCreateTBNMatrix(vec3 normal, vec3 tangent, float handedness);
    
[/code]

#### Perlin and Simplex noise functions
[code] 
    // Noise functions
    // These will return the same result for the same input
    // Results are between -1 and 1
    // Can be slow so just be aware when using them. 
    // Different dimensionality selected by passing vec2, vec3 or vec4. 
    float TDPerlinNoise(vec2 v);
    float TDPerlinNoise(vec3 v);
    float TDPerlinNoise(vec4 v);
    float TDSimplexNoise(vec2 v);
    float TDSimplexNoise(vec3 v);
    float TDSimplexNoise(vec4 v);
    
[/code]

#### HSV Conversion
[code] 
    // Converts between RGB and HSV color space
    vec3 TDHSVToRGB(vec3 c);
    vec3 TDRGBToHSV(vec3 c);
    
[/code]

#### Projection Conversions
[code] 
    // Converts a 0-1 equirectangular texture coordinate into cubemap coordinates.
    // A 0 for the U coordinate corresponds to the middle of the +X face. So along the vec3(1, Y, 0) plane.
    // As U rises, equirectangular coordinates rotate from +X, to +Z, then -X and -Z.
    vec3 TDEquirectangularToCubeMap(vec2 equiCoord);
    
[/code]
[code] 
    // Converts from cubemap coordinates to equirectangular
    // cubemapCoord MUST be normalized before calling this function.
    vec2 TDCubeMapToEquirectangular(vec3 cubemapCoord);
    
    // Available in builds 2019.18140
    // This version will also output a mipmap bias float. This float should be passed in the 'bias'
    // parameter of texture(), to help select the mipmap level. This helps avoids seams at the edge
    // of equirectangular map.
    vec2 TDCubeMapToEquirectangular(vec3 cubemapCoord, out float mipMapBias);
    
[/code]

## Working with Lights

To help shaders be as fast as possible, a lot of the logic to calculate lights is hard-coded into the shader depending on what features are enabled and what the light type is. Shaders written for the GLSL MAT will be recompiled with different implementation of TDLightingPBR(), TDLighting() etc depending on the number and types of lights in the scene. This allows the same GLSL MAT to be used in multiple different scenes without needing to be changed based on the number of lights in the scene. These compilations are cached, so each permutation of lighting settings will only cause one compilation to occur, each time TD is run. 

**TIP:** Geometry viewers have built-in lighting separate from your scene's lighting objects. For information on how to duplicate that lighting, see the [Geometry Viewer](<./Geometry_Viewer.md> "Geometry Viewer") article. 

### Custom work with lights

If you decide to do custom lighting work, this section describes how a lot of the light values are used in our shader. 

#### Knowing which variables correspond to which Light COMPs

The variables will be indexed to differentiate the lights, starting at 0. Light 0 will be the first light listed in the [Render TOP](<./Render_TOP.md> "Render TOP"), Light 1 will be the 2nd light listed and so on. In the event that lights are selected using a wildcard such as light*, the lights gathered from this wildcard will be sorted alpha-numerically. 

For example, say the [Render TOP](<./Render_TOP.md> "Render TOP") has "/light3 /container1/light* /alight1" listed in its Light parameter, and /container1/ has two light COMPs, named light1 and light2. In this case the lights would correspond to the following indices:   
/light3 would be index 0   
/container1/light1 would be index 1   
/container1/light2 would be index 2   
/alight1 would be index 3 

#### Light Parameters

All of the parameters for the lights are defined in the uTDLights structure, defined [ here](<./Write_a_GLSL_Material.htm#TouchDesigner_specific_Uniforms> "Write a GLSL Material"). 

#### Cone Lighting Technique

TouchDesigner's built-in shaders use a custom cone-lighting technique that you can mimic in your shader. The intensity of the cone light is pre-computed into a 1D texture (a lookup table) to reduce the workload in the shader. The start of the 1D texture (texture coordinate 0.0) is the intensity of the light at the edge of the cone angle (the first pixel is always 0). The end of the 1D texture (texture coordinate 1.0) is the intensity of the light at the center of the cone. This lookup table is accessed via: 
[code] 
    float TDConeLookup(int lightIndex, float coord);
    
[/code]

A second helper uniform is also given to the shader to make looking up in the 1D texture easier: 
[code] 
    uTDLights[i].coneLookupScaleBias;
    
[/code]

To correctly look into this lookup table the following algorithm should be used: 
[code] 
    // 'spot' is the spot vector
    // 'lightV' is the vector coming from the light position, pointing towards
    // the point on the geometry we are shading.
    // It doesn't matter which space these vectors are in (camera space, object space), 
    // as long as they are both in the same space.
    // Determine the cosine of the angle between the two vectors, will be between [-1, 1]
    float spotEffect = dot(spot, lightV);
    // Now rescale the value using the special helper uniform so that value is between [0,1]
    // A value of 0 will mean the angle between the two vectors is the same as the total 
    // cone angle + cone delta of the light
    spotEffect = (spotEffect * uTDLights[i].coneLookupScaleBias.x) + uTDLights[i].coneLookupScaleBias.y;
    // Finally lookup into the lookup table
    float dimmer = TDConeLookup(i, spotEffect);
    // You can now multiply the strength of the light by 'dimmer' to create the correct
    // light intensity based on this pixels position in or outside the cone light's area of
    // influence
    
[/code]

#### Attenuation

Attenuation is handled for you in the TDLighting() function, but if you want to add it yourself this section describes how. 

To determine the attenuation from the light to a point in space, use this function.`lightDist`is the distance from the vertex to the light. 
[code] 
    // Will return 1 if there is no attenuation, 0 if the light is fully attenuated, and something in between if it's in the fade-off region.
    float TDAttenuateLight(int lightIndex, float lightDist);
    
[/code]

The math behind TDAttenutateLight is as follows: 

TouchDesigner's built-in shaders use a custom attenuation technique. Like the cone lighting, a pre-calculated scale and bias is provided for you that will allow you to get the correct attenuated intensity of the light. The uniform is:   

[code] 
    uTDLights[i].attenScaleBiasRoll // Contains (1 / -(attenEnd - attenStart), attenEnd / (attenEnd - attenStart), attenRolloff)
    
[/code]

TDAttenutateLight is defined as: 
[code] 
    float TDAttenuateLight(int lightIndex, float lightDist)
    {
        float lightAtten = lightDist * uTDLights[lightIndex].attenScaleBiasRoll.x;
        lightAtten += uTDLights[lightIndex].attenScaleBiasRoll.y;
        lightAtten = clamp(lightAtten, 0.0, 1.0) * 1.57073963
        lightAtten = sin(lightAtten);
        lightAtten = pow(lightAtten, uTDLights[lightIndex].attenScaleBiasRoll.z);
        return lightAtten;
    }
    
[/code]

#### Projection and Shadow Mapping

Projection mapping and shadowing mapping are handled for you in the TDLighting() functions, but you can do it yourself if you want using the below information. 

Projection and Shadow mapping are very similar operations. The only difference is a projection map will be used to color the surface, while a shadow map will be used to decide if that surface receives lighting from a certain light. 

##### Projection Mapping

Use the`TDProjMap()`function, which will give you back the projection map color, including handling different projection types. 

##### Shadow Mapping

Use`TDHardShadow()`or`TDSoftShadow()`to manually get the shadow value. 

## Multiple Render Targets

Using the '# Of Color Buffers' parameter in the [Render TOP](<./Render_TOP.md> "Render TOP") along with the [Render Select TOP](<./Render_Select_TOP.md> "Render Select TOP"), you can write GLSL shaders that output multiple color values per pixel. This is done by declaring and writing to pixel shader outputs declare like this: 
[code] 
    layout(location = 0) vec4 fragColor[TD_NUM_COLOR_BUFFERS];
    
[/code]

The constant TD_NUM_COLOR_BUFFERS with automatically be set for you based on the render settings. Ensure you are not writing beyond the number of buffers provided, or corruption/GPU crashes may occur. 

## Multi-Camera Rendering

Multi-Camera Rendering is rendering multiple cameras in a single rendering pass, all looking at the same scene. This means the scene-graph is only traversed once, which avoids many calls to the graphics driver. Lights, textures, material and draw calls only need to be done once for the entire set of cameras being rendered. This feature is supported by Nvidia Pascal (Geforce 1000, Quadro P-Series) or AMD Polaris (Radeon R9, Radeon Pro WX) and newer GPUs. This feature is important for VR rendering, as well as things such as rendering a Cube Map in a single pass (instead of one pass per side). 

Multi-Camera Rendering will not function if the Cameras have different light masks. The cameras will be rendered one pass at a time in that case. 

This feature is used by the [Render TOP](<./Render_TOP.md> "Render TOP") when multiple cameras are listed in the 'Cameras' parameter. The 'Multi-Camera Hint' parameter can help control how this feature is used for that particular Render TOP. The results of each camera's render can be obtained using [Render Select TOP](<./Render_Select_TOP.md> "Render Select TOP"). 

Nvidia calls this feature 'Simultaneous Multi-Projection'. 

The multi-camera functionality on these GPUs is not general and requires some tricks to function properly. Because of this it's important all of your shaders make use of the TD* functions such as TDWorldToProj(), TDInstanceID() instead of doing those things manually and using built-in GLSL functionality. Functions such as TDFog() also require a camera index to be passed to it to apply fog for the correct camera. 

## Image Outputs

In the [Render TOP](<./Render_TOP.htm#Parameters_-_Images_Page> "Render TOP") you can allocate extra image outputs that can be accessed during rendering. These outputs are arbitrarily sized images that can be written and read from at any location (similar to the Compute shader workflow for the GLSL TOP), using`TDImageStore_Name()`and`TDImageLoad_Name()`. Where 'Name' will be replaced with what you named the image output as. The images will automatically be declared for you inside of the shader, you should not declare them yourself (as you do for other uniforms). This is because there is a lot of extra decoration required for the image uniforms. Currently when compiling in the GLSL MAT itself your code will result in an error, since the images are not available there. You can avoid those compile errors by using this around your code that uses the`TDImage*`functions 
[code] 
    #ifdef TD_RENDER_TOP
    // Render TOP only code
    #endif
    
[/code]

When you apply your MAT to a geometry and render it via the Render TOP, a new version of your shader will be compiled that has the images declared. 

Images should be written and read to using these functions. The 'Name' portion should be replaced with the name of the image output as defined in the Render TOP. These functions are used instead of the workflow before 2025.30000 which used`imageStore()/imageLoad()`directly. This has changed because writing and reading from sRGB encoded textures requires special handling with`imageStore()/imageLoad()`, so this is handled automatically for you via these functions. You also do **not** need to apply`TDOutputSwizzle()`to the color before using these functions, it will apply it automatically for you internally. The ivec3 vs. uvec3 version do the same thing, and are just duplicated for convinience. If the image dimension is requires less than 3 coordinates, the extra ones are ignored. 

If the image is declared with an Array Size of 0 (not an array), then arrayIndex should be set to 0. 
[code] 
    void TDImageStore_Name(uint arrayIndex, ivec3 coord, vec4 color);
    void TDImageStore_Name(uint arrayIndex, uvec3 coord, vec4 color);
    vec4 TDImageLoad_Name(uint arrayIndex, ivec3 coord);
    vec4 TDImageLoad_Name(uint arrayIndex, uvec3 coord);
    
[/code]

For example if the Image Output was named 'test', then the functions would be called`TDImageStore_test()`## Outputting gl_Position

Although in general you can transform your points/vectors using the built-in model/view and projection matrices at will, when outputting to gl_Position you should use the built-in functions. These functions allow TouchDesigner to do some manipulation of the values for final output, depending on the rendering setup. For example for doing optimized [Multi-Camera Rendering](<#Multi-Camera_Rendering>), the position will need to be multiplied by the correct camera for this execution of the vertex shader. To give TouchDesigner a chance to do this manipulation, you should call the built-in functions to transform your vertex position: 
[code] 
    vec4 TDWorldToProj(vec4 v);
    vec4 TDWorldToProj(vec3 v);
    
[/code]

So for example at the end of your shader you would do: 
[code] 
    gl_Position = TDWorldToProj(worldSpacePosition);
    
[/code]

## Specilization Constants

Specialization Constants are a new feature in Vulkan that allow code to be re-optimized based on integer constant values, without doing a full recompilation of the shader code. These are useful to set the value for rarely changing values such as 'modes' in shader, or selection of particular code paths that are doing via a switch() or if() statement. In the past this may have been done with a`#define`statement, or a`uniform`. A specialized version of a shader will be cached and re-used, but takes up GPU resources. So they should not be used for constantly changing values, but instead for values that are only changed sometimes, within a limited range of values. 

To define a specialization constant, declare a constant with an extra layout() qualifier. 
[code] 
     layout(constant_id = 0) const int SomeMode = 0;
    
[/code]

Then you can use`SomeMode`just as you would any other variable. If you don't want it to be = 0, you can assign a different value on the 'Constants' page of the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP"), [GLSL MAT](<./GLSL_MAT.md> "GLSL MAT") etc. You can declare multiple specialization constants, you just need to give each one it's own unique`constant_id`value (0, 1, 2, etc.). 

## Working with Deforms

Currently there are two different types deformations that can be applied to geometry: [ skinned deforms](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)") and instanced transforms. 

TouchDesigner automatically encapsulates all of the work for both of these deforms in the GLSL functions. Use the *Vec version when deforming vectors.  
**These functions always return the point/vector in World space, not model/ SOP.**
[code] 
    vec4 TDDeform(vec4 p);
    vec3 TDDeform(vec3 p);
    vec3 TDDeformVec(vec3 v);
    vec3 TDDeformNorm(vec3 v);
    
[/code]

  
As the shader writer, it's your job to manipulate the vertex attributes such as the position and normal (since there's no place for TouchDesigner to do it if you're the one writing the shader), so it's up to you to call the TDDeform() function. In general you will simply call it simply like this: 
[code] 
    vec4 worldSpaceVert = TDDeform(vec4(TDPos(), 1.0)); 
    vec3 worldSpaceNorm = TDDeformNorm(TDNormal()));
    
[/code]

However you can use the below declared functions directly. 

### Skinning Deforms (Bone Deforms)

When you enable the Deform feature in the GLSL MAT, TouchDesigner will automatically declare some attributes, varyings, uniforms and functions for you to use to deform your geometry in the same way that other MATs deform geometry. It's important you don't re-use any of these reserved words when using deforms to avoid name conflicts when compiling the shader. Even when not using deforms though, the below listed functions will be declared anyway so shader code will run correctly both when deforms are turned on and off. The functions do nothing when deforms are off (and have no cost to the shader speed). The bone matrices for deforms are built by using the pCaptPath and pCaptData detail attributes along with the the bone's current position based on the skeleton at that frame. In SOPs the 'pCapt' attribute holds pairs of indices/weights for each bone affecting the vertex. In POPs these are instead loaded into two attributes called 'BoneIndices' and 'BoneWeights'. More information on how Skinning Deforms work can be found here: [Deforming Geometry (Skinning)](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)")

#### Functions

You generally will not need to call these directly, they are called by the`TDDeform()`function. 

In the vertex shader: 
[code] 
    vec4 TDSkinnedDeform(vec4 pos);
    vec3 TDSkinnedDeformVec(vec3 vec);
    
[/code]

You can get the bone matrix for the given matrix index with this function: 
[code] 
    mat4 TDBoneMat(int boneIndex);
    
[/code]

### Instancing

When you enable instancing on the Instance page of the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") the TDDeform() functions will automatically call the correct lower level function that will transform the instance, based on the channels given in the XForm CHOP parameter. If you don't specify a CHOP, then all of the instances will be drawn at the same spot, unless you transform them yourself. 

#### Instance Index/ID

To calculate the instance ID, use the provided TDInstanceID() function. Do not use gl_InstanceID directly because the number of instances being rendered may be larger than requested due to [Multi-Camera Rendering](<#Multi-Camera_Rendering>). 
[code] 
    int TDInstanceID();
    
[/code]

Since this function is only available in the vertex shader, you will need to pass it onwards to the pixel shader through an out/in, if you require it in the pixel shader. 
[code] 
    // In the vertex shader, declare something like this, and assign vInstanceID = TDInstanceID() in the main()
    flat out int vInstanceID;
    void main()
    {
    	vInstanceID = TDInstanceID();
    	// other main vertex function stuff
    	// ....
    }
    
[/code]

And in the pixel shader you can read this value if it's declared like this: 
[code] 
    // Pixel shader
    flat in int vInstanceID;
    
[/code]

This is declared as`flat`since`int`variable types can not be interpolated across a primitive. 

#### Deform Functions

You generally will not need to call any of these directly, they are called by the TDDeform() function. These functions are only available in the vertex shader. 

In the vertex shader: 
[code] 
    vec4 TDInstanceDeform(vec4 pos);
    vec3 TDInstanceDeformVec(vec3 vec);
    
[/code]

For the transform, access these matrices using the functions: 
[code] 
    mat4 TDInstanceMat(int instanceIndex);
    mat4 TDInstanceMat();
    
[/code]

These matrices will contain the entire transform, including TX, TY, TZ, SX, SY, SZ as well as Rotate To. 

#### Attribute Functions

When modifying the texture coordinates, these functions do the texture coordinate modifications per instance. t is the texture coordinate to modify. The version without instanceIndex will use the current value for gl_InstanceID automatically. 
[code] 
    vec3 TDInstanceTexCoord(int instanceIndex, vec3 t);
    vec3 TDInstanceTexCoord(vec3 t);
    
[/code]

To modify diffuse color, these functions will replace/add/subtract from the original diffuse color. In general you'll want to pass in the result of TDPointColor() into these functions to have them modify it. If instance color is not in use, this function will just return the passed in color, unmodified. 
[code] 
    vec4 TDInstanceColor(vec4 curColor);
    vec4 TDInstanceColor(int instanceIndex, vec4 curColor);
    
[/code]

Custom instance attributes can be retrieved using these functions: 
[code] 
    vec4 TDInstanceCustomAttrib0();
    vec4 TDInstanceCustomAttrib0(int instanceIndex);
    vec4 TDInstanceCustomAttrib1();
    vec4 TDInstanceCustomAttrib1(int instanceIndex);
    vec4 TDInstanceCustomAttrib2();
    vec4 TDInstanceCustomAttrib2(int instanceIndex);
    vec4 TDInstanceCustomAttrib3();
    vec4 TDInstanceCustomAttrib3(int instanceIndex);
    
[/code]

#### Instance Texturing

Instance texturing allows mapping larger number of individual textures onto instances. The number of textures available to be used in a single render varies by GPU. The resolution/pixel format of each texture can be different. It avoids needing to use a 2D Texture Array to map multiple images onto instances. Only one type of texture dimension is supported at a time (2D, Cube etc). Access the textures is a two step process. First you need to get the texture index for the current instance you are outputting. This is achieved through`TDInstanceTextureIndex()`. Then you can use that texture index in a call to`TDInstanceTexture()`to obtain the sampled texture color at the passed coordinates. There are a few variations of these functions. In the vertex shader there are versions that can implicitly know the current instance index and output using that. In both vertex/pixel shaders there is also versions that allow you to manually specify the instance index via a parameter. You will typically be sampling the texture in the pixel shader, in which case you want to obtain the texture index in the vertex shader, then pass it through to the pixel shader via a`flat uint`in/out variable. 
[code] 
    // AVAILABLE IN THE VERTEX SHADER ONLY
    // Implicitly uses the current instance. Returns the texture index for this instance.
    uint TDInstanceTextureIndex();
    // Returns the texture color at the given 'uv', implicitly using the current instance index to determine which texture to sample.
    // You will not usually be using these versions of TDInstanceTexture(), since they are only available in the vertex shader.
    vec4 TDInstanceTexture(vec2 uv);
    vec4 TDInstanceTexture(vec3 uv);
    
[/code]

If you require more custom control of which instance texture you which to use, you can use these functions instead: 
[code] 
    // AVAILABLE IN ALL SHADER STAAGES
    // Gives to you the textureIndex for the given instanceIndex.
    uint TDInstanceTextureIndex(int instanceIndex);
    // Samples the texture 'texIndex' at the given 'uv'.
    vec4 TDInstanceTexture(uint texIndex, vec3 uv);
    vec4 TDInstanceTexture(uint texIndex, vec2 uv);
    
[/code]

The best way to see this code being used in a live example is to output a shader from the Phong MAT that is doing instance texturing. 

## Point Sprites

Point Sprites must now use`vec2 TDPointCoord()`instead of`gl_PointCoord`to obtain the texture coordinates for the sprite. Using gl_PointCoord will result in the texture coordinates being flipped vertically in some cases. 

When rendering point sprites primitives you are required to write to the vertex shader output`gl_PointSize`. This output variable determines how large the point sprite is (in pixels) when it is rendered. If you don't write to the output then your point sizes are undefined. 

Each point sprite will be rendered as a square of pixels`gl_PointSize`pixels wide. The square of pixels will receive textures coordinates from 0-1 over the entire square in the pixel shader, obtained via`TDPointCoord()`. 

## Order Independent Transparency

You can make your shader support Order Independent Transparency by simply adding this line at the start of your pixel shader's main() function. If Order Independent Transparency isn't enabled in the Render TOP, then this function will do nothing. 
[code] 
    TDCheckOrderIndTrans();
    
[/code]

## Dithering

If dithering is enabled in the [Render TOP](<./Render_TOP.md> "Render TOP"), you can have this dithering applied to your color by simply calling: 
[code] 
    finalColor = TDDither(finalColor);
    
[/code]

You generally want to do this right at the end of the shader, just before you write the value to your output color. If dithering is disabled in the Render TOP this function will still be available (to avoid compiler errors), but it will leave the color unchanged. 

## Picking

The Render Pick DAT and CHOP do their work with a render operation, so they need to interact with the shader to do their work. If you export a Phong MAT shader you will see the following lines in it 
[code] 
    #ifndef TD_PICKING_ACTIVE
    	// All the typical shader code
    #else
    	TDWritePickingValues();
    #endif
    
[/code]

The key thing that is occurring here is that when picking is occuring, the define TD_PICKING_ACTIVE is set and only the code inside the #else block is executed. The function: 
[code] 
    void TDWritePickingValues();
    
[/code]

Will write default values for picking, which the Render Pick DAT/CHOP will read. If you have a custom shader that changes vertex positions in a non standard way, or if you want to output different kinds of information (like a color other than TDPointColor()), you can replace the values that have been written by this function afterwards. The values available to you are: 
[code] 
    TDPickVertex {
    	vec3 sopSpacePosition;
    	vec3 worldSpacePosition;
    	vec3 camSpacePosition;
    	vec3 sopSpaceNormal;
    	vec3 worldSpaceNormal;
    	vec3 camSpaceNormal;
    	vec3 uv[1];
    	flat int instanceId;
    	vec4 color;
    } vTDPickVert;
    
[/code]

So for example if you modifying the vertex position in a way different from the standard TDDeform() way, you could write these newly calculated values to like this: **Be sure to do this AFTER the call to TDWritePickingValues(), otherwise that call will overwrite your values**. 
[code] 
    TDWritePickingValues();
    vTDPickVert.sopSpacePosition = newPosition;
    vTDPickVert.worldSpacePosition = uTDMats[TDCameraIndex()].world * vec4(newPosition, 1.0);
    vTDPickVert.camSpacePosition = uTDMats[TDCameraIndex()].worldCam * vec4(newPosition, 1.0);
    
[/code]

You do not have to write to all the entries in this structure, but you can for completeness. Only the values that are being read by the Render Pick CHOP/DAT (selected in their parameters) must be filled in. 

For custom attributes that you set for picking in the [Render Pick CHOP](<./Render_Pick_CHOP.md> "Render Pick CHOP") or [Render Pick DAT](<./Render_Pick_DAT.md> "Render Pick DAT"), the attributes are available in`vTDCustomPickVert`with the name and size as defined in the Render Pick node. 

## Shadertoy

### VR Shaders

Shaders that come from [Shadertoy](<http://www.shadertoy.com>) that support VR rendering will have a`mainVR`function defined. Re-creating the`fragRayOri`and`fragRayDir`variables that function uses inside of TD is simple. In the vertex shader: 
[code] 
    vec4 worldSpaceVert = TDDeform(TDPos());
    vec4 worldSpaceCamPos = uTDMat.camInverse[3]; // The last column of the camera transform is it's position
    
    vec3 fragRayOri = worldSpaceCamPos.xyz;
    vec3 fragRayDir = worldSpaceVert.xyz - worldSpaceCamPos.xyz;
    // Pass these variables to the pixel shader using 'out' variables named of your choosing
    
[/code]

And in the pixel shader you just need to normalize whatever variable the`fragRayDir`was went through. The variable that came from`fragRayOri`and be used as-is. 

To support these shaders, which are usually raymarching shaders, you'll want to render geometry that covers the entire viewport, such as putting a sphere around your camera. 

## Other Notes

### #version statement

The #version statement will be added to the code automatically for you. Your code should not have a #version statement, otherwise compile errors may occur. 

### #include statements

You can use an #include statement in one DAT to include code from another DAT. The path can be absolute or relative. 
[code] 
     #include </project1/text1>
     #include <../../geo1/text2>
     #include "text2"
    
[/code]

### Diagnosing crashes due to GLSL

If you are experiencing a full application crash when writing GLSL code, you may want to refer to [this article](<./Debugging_crashes_triggered_by_GLSL_errors.md> "Debugging crashes triggered by GLSL errors") for tips on diagnosing these issues. 

### Changes from GLSL 1.20

Shaders written for 1.20 will not compile as 3.30 shaders. The language received a large overhaul, changing the name of many key functions and replacing a lot of functionality. All of the changes can be seen in the official GLSL documentation linked to earlier. Some of the more important changes are: 
* Removed`texture1D(sampler1D, float), texture2D(sampler2D, vec2), etc.`All texture sampling is done with identical function names, regardless of the dimensionality of the texture. e.g.`texture(sampler1D, float), or texture(sampler2D, vec2)`.
* Removed the keyword`varying`. Instead use`in`and`out`(depending on if the value is getting outputted from the shader or inputted from a previous shader stage). Examples later on in the article.
* Removed the keyword`attribute`. Instead just use`in`in your vertex shader.
* Removed built-in varyings`gl_TexCoord[]`. You'll need to always declare your own variables that get output/input between shader stages.
* Removed`gl_FragColor`and`gl_FragData[]`. Instead you name your own color outputs using the syntax`layout(location = 0) vec4 oFragColor[TD_NUM_COLOR_BUFFERS]`.
* Removed all built-in attributes such as`gl_Vertex, gl_MultiTexCoord0, gl_Normal`. In TouchDesigner these attributes will be accessible through automatically declared attributes such as`in vec3 TDPos(); in vec3 TDTexCoord(uint coordLayer); in vec3 TDNormal(); vec4 TDPointColor()`. More details on this [later](<#Working_with_Geometry_Attributes>).
* Removed almost all built-in uniforms such as matrices (`gl_ModelViewMatrix, gl_ProjectionMatrix`), light information (`gl_LightSource[]`), fog information (`gl_Fog`). All of this data will be available through new means provided by TouchDesigner, detailed [later](<#TouchDesigner_specific_Uniforms>).
* Arrays of samplers are now supported, and are used extensively in TouchDesigner when appropriate. There are limitations on how these samplers are indexed though, detailed in the GLSL spec for the particular version you are using (3.30 has different rules from 4.10, for example).

### Major changes since TouchDesigner088

A lot of changes have been done to TouchDesigner's GLSL API in 099. Most of these changes were done to better facilitate [Multi-Camera Rendering](<#Multi-Camera_Rendering>). A summary of most of these changes is: 
* Lighting and other work is now done in World space instead of Camera space. This makes code cleaner since the shaders would need to do their work in multiple different camera spaces for multiple cameras. Legacy GLSL shaders are supported with the [GLSL TOPs](<./GLSL_TOP.md> "GLSL TOP") 'Lighting Space' parameter which will be set to Camera Space for older shaders.
  *`TDInstanceID()`should be used instead of`gl_InstanceID/uTDInstanceIDOffset`.
  *`uTDMat`has been removed when lighting in World Space, use the array`uTDMats[]`instead.
  * Some values from the`uTDGeneral`structure have been moved to`uTDCamInfos[]`, since that info is camera specific.
  * A notion of camera index (obtained in the vertex shader using`TDCameraIndex()`), is needed for some functions such as`TDFog()`.
  *`TDAlphaTest(float)`must be called to apply the alpha test. It can be safely called when the alpha test is disabled on the MAT, it'll do nothing in that case.
  * Before writing any color to a output color buffer, it should be passed through`vec4 TDOutputSwizzle(vec4)`. This ensures the channels are in the correct place depending on how the channels are stored in the output texture. For example Alpha-only textures may be stored in a 'Red-only' texture internally, so the alpha value will need to be swizzled over to the red channel before output.

## Related Articles
