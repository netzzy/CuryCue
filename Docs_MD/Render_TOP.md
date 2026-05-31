# Render TOP

##   
  
Summary

The Render TOP is used to render all 3D scenes in TouchDesigner. You need to give it a [Camera](<./Camera_COMP.md> "Camera COMP") object and a [Geometry](<./Geometry_COMP.md> "Geometry COMP") object as a minimum. 

The Geometry object needs to have a [Material](<./MAT.md> "MAT") assigned to it. Materials can be pre-packaged ones like the [Phong](<./Phong_MAT.md> "Phong MAT") material, or they can be OpenGL GLSL shaders. All textures and bump maps in TouchDesigner materials are TOPs, i.e. files must be read in via [Movie File In TOPs](<./Movie_File_In_TOP.md> "Movie File In TOP"). 

Rendering in TouchDesigner ties in nicely with compositing via the Render TOP and all other TOPs. 

The Render TOP renders in many RGBA and single-channel formats, in 8-bit fixed-point up to to 32-bit floating point per pixel component. 

It can render transparent surfaces correctly using Multi-Pass Depth Peeling. See below: Order Independent Transparency. 

Multiple Cameras: The Render TOP is able to render multiple cameras (more quickly than separately) in a single node. You specify multiple cameras in one Camera parameter, and use Render Select TOP to pull out those camera results. This feature is even faster on GPUs that support [Multi-Camera Rendering](<./Multi-Camera_Rendering.md> "Multi-Camera Rendering"). 

Multiple Images out: The Render TOP, working with the GLSL MATs, can output multiple image at arbitrary formats, through the Images page. 

See also [Rendering](<./Rendering.md> "Rendering"), all the articles in the [Rendering Category](<http://www.derivative.ca/wiki/index.php?title=Category:Rendering>), the [Render Pass TOP](<./Render_Pass_TOP.md> "Render Pass TOP"), and the troubleshooting page [Why is My Render Black](<./Why_is_My_Render_Black.md> "Why is My Render Black"). 

NOTE: If you are doing non-realtime GPU-intensive renders (ones that take multiple seconds to render a single SOP), see the note in Windows GPU Driver Timeouts in the [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[renderTOP_Class](<./RenderTOP_Class.md> "RenderTOP Class")

## 

Parameters - Render Page

Camera(s)`camera`\- Specifies which [Cameras](<./Camera_COMP.md> "Camera COMP") to look through when rendering the scene. You can specify multiple cameras and retrieve each camera image using the Render Select TOP. 

Multi-Camera Hint`multicamerahint`\- ⊞ \- Helps the Render TOP optimize rendering when multiple cameras are used. Controls the [Multi-Camera Rendering](<./Multi-Camera_Rendering.md> "Multi-Camera Rendering") behavior for this node. 
* Automatic`automatic`\- The node will decide based on the GPU and setup if [Multi-Camera Rendering](<./Multi-Camera_Rendering.md> "Multi-Camera Rendering") can be used and enable it if possible. Currently Multi-Camera rendering works for 2D and Cube Map renders on supported GPUs. For 2D renders multiple cameras can not be rendered in a single pass if their 'Camera Light Mask' parameters don't result in the same lights being used in the scene. Use of Depth Peeling or Order Independent Transparency will also disable Multi-Camera rendering.
* Off (One Pass Per Camera)`off`\- Forces Multi-Camera Render to be disabled, so each camera is rendered one pass at a time.
* X-Offset Stereo Cameras`stereocameras`\- Should be set only if the pair of cameras have transform/projection matrices that result in a difference only in the X-axis after being applied, as is the case for most VR headsets. Other differences between the cameras such as FOV, near/far plane etc will be ignored, and the values form the first camera will be used. This hint allows the TOP to run faster for this particular case, when appropriate hardware is available.


Geometry`geometry`\- Specifies which [Geometry](<./Geometry_COMP.md> "Geometry COMP") will be included in the rendered scene. You can use [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") to specify objects using patterns. Example:`geo* ^geo7`will render all Geometry components whose names start with`geo`except`geo7`. 

Lights`lights`\- Specifies which [Lights](<./Light_COMP.md> "Light COMP") will be used to render the scene. You can use [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching") here as well. 

Anti-Alias`antialias`\- ⊞ \- Sets the level of anti-aliasing in the scene. Setting this to higher values uses more graphics memory. 
* 1x (Off)`aa1`-
* 2x`aa2`-
* 4x`aa4`-
* 8x (Medium)`aa8mid`-
* 8x (High)`aa8high`-
* 16x (Low)`aa16low`-
* 16x (Medium)`aa16mid`-
* 16x (High)`aa16high`-
* 32x`aa32`-


Background Color`bgcolor`\- ⊞ \- This is combined with the [Camera COMP](<./Camera_COMP.md> "Camera COMP")'s Background Color to determine the final Background Color of the render. 
* Background Color`bgcolorr`-
* Background Color`bgcolorg`-
* Background Color`bgcolorb`-
* Background Color`bgcolora`-


Pre-Multiply RGB by Alpha`premultrgbbyalpha`\- 

Render Mode`rendermode`\- ⊞ \- You can render different projections: normal 2D, Cube Map, Fish Eye (180), or Dual Paraboloid. The Cube Map renders 6 views as needed for environment maps in the [Phong MAT](<./Phong_MAT.md> "Phong MAT") and [Environment Light COMP](<./Environment_Light_COMP.md> "Environment Light COMP"). 

See also the [Cube Map TOP](<./Cube_Map_TOP.md> "Cube Map TOP") and the [Projection TOP](<./Projection_TOP.md> "Projection TOP"). 
* 2D`render2d`\- The standard 2D render mode.
* Cube Map`cubemap`\- Does 6 renders, each with 90 degree FOV. The camera is automatically turned to face down each of the 6 axis, with the -Z axis being where the camera is facing to start.
* Fish-Eye (180)`fisheye180`\- A single 2D render that warps the projection so it renders 180 degree FOV in all directions from where the camera is pointing (90 to each side). Since this render doesn't preserve straight lines, geometry that has large polygons that cover a lot of the viewport will suffer from artifacts. Well tesselated geometry is best for this mode.
* Dual Paraboloid`dualparaboloid`\- Similar to Fisheye, but renders twice at 180 degrees, once forward and once backwards. The projection isn't the same as fisheye either. This is a legacy mode that isn't currently consumed by anything in TouchDesigner, but there are articles online that discuss how to sample from it.
* UV Unwrap`uvunwrap`\- A 2D render that uses the UV coordinates of the geometry to unwrap it across the output image.
* Cube Map (Omnidirectional Stereo)`cubemapods`\- This mode renders a stereo pair (two eyes) of cubemaps that can be used to record out stereo 360 videos. You can obtain the second eye's output by using a [Render Select TOP](<./Render_Select_TOP.md> "Render Select TOP") and selecting Camera Index=1. The [Camera COMP](<./Camera_COMP.md> "Camera COMP")'s IPD Shift parameter is used here to offset each eye viewport.


Positive Sides`posside`\- ⊞ \- When Render Mode is Cube Map, specify which sides if the cube map are rendered, +X, +Y, or +Z. 
* Positive Sides`possidex`-
* Positive Sides`possidey`-
* Positive Sides`possidez`-


Negative Sides`negside`\- ⊞ \- When Render Mode is Cube Map, specify which sides if the cube map are rendered, -X, -Y, or -Z. 
* Negative Sides`negsidex`-
* Negative Sides`negsidey`-
* Negative Sides`negsidez`-


UV Unwrap SOP Coord`uvunwrapcoord`\- ⊞ \- When Render Mode is UV Unwrap Coord, for SOPs this selects which Texture Layer coordinates the rendering is done to. 
* Texture Layer 0 (uv[0-2])`uv0`-
* Texture Layer 1 (uv[3-5])`uv1`-
* Texture Layer 2 (uv[6-8])`uv2`-
* Texture Layer 3 (uv[9-11])`uv3`-
* Texture Layer 4 (uv[12-14])`uv4`-
* Texture Layer 5 (uv[15-17])`uv5`-
* Texture Layer 6 (uv[18-20])`uv6`-
* Texture Layer 7 (uv[21-23])`uv7`-


UV Unwrap POP Coord Attribute`uvunwrapcoordattrib`\- When Render Mode is UV Unwrap Coord, for POPs this should be the name of the texture coordinate attribute rendering is done to. 

Transparency`transparency`\- ⊞ \- Helps to render transparent geometry in proper depth order. More in-depth discussion available in the [Transparency article](<./Transparency.md> "Transparency"). 
* Sorted Draw with Blending`sortedblending`\- [https://docs.derivative.ca/Transparency#Sorting_Geometry_Objects](<./Transparency.htm#Sorting_Geometry_Objects>)
* Order Independent Transparency`orderind`\- [https://docs.derivative.ca/Transparency#Order-Independent_Transparency](<./Transparency.htm#Order-Independent_Transparency>)
* Alpha-to-Coverage`alphatocoverage`\- [https://docs.derivative.ca/Transparency#Alpha-to-Coverage](<./Transparency.htm#Alpha-to-Coverage>)


Depth Peel`depthpeel`\- Depth peeling is a technique used as part of Order-Independent Transparency, but this parameter allows you to use it in a different way. This parameter enables rendering depth-peels, but without combining all the layers using blending to create order independent transparency. Instead is keeps all the layers separate and they can be retrieved using a [Render Select TOP](<./Render_Select_TOP.md> "Render Select TOP"). Depth peeling is done by first rendering rendering geometry normally and saving that image and depth. Then another render is done but the closest pixels that were occluded by the previous pass are written to the color buffer instead. This can be done multiple times, each time peeling back farther into the scene. If you are rendering a sphere the first render will be the outside of the sphere, and the second peel layer will be the back-inside of the sphere. 

Transparency/Peel Layers`transpeellayers`\- Number of passes the renderer will use when Order Independant Transparency is turned on. 

## 

Parameters - Advanced Page

Render`render`\- Enables rendering; 1 = on, 0 = off. 

Render Pulse`renderpulse`\- The the 'Render' toggle above is Off, click this to render a sinlge frame. 

Dither`dither`\- Dithers the rendering to help deal with banding and other artifacts created by precision limitations of 8-bit displays. 

Color Output Needed`coloroutputneeded`\- This is an optimization if you don't actually need the color result from this pass. Turning this off avoids a copy from the offscreen render buffer to the TOP's texture. When anti-aliasing is enabled, turning this off will also avoid 'resolving' the anti-aliasing. 

Draw Depth Only`drawdepthonly`\- This will cause the render to only draw depth values to the depth buffer. No color values will be created. To make use of the depth buffer, use the [Depth TOP](<./Depth_TOP.md> "Depth TOP"). 

# of Color Buffers`numcolorbufs`\- Any shader you write can output to more than one RGBA buffer at a time. For GLSL 3.3+ you would use the layout(location = 1) specifier on an out variable in the pixel shader to write to the 2nd buffer. In GLSL 1.2 instead of writing to`gl_FragColor`in your shader, you write to`gl_FragData[i]`where i is the color buffer index you want to write the value to. 

Allow Blending for Extra Buffers`allowbufblending`\- Controls if blending (as enabled by the MAT common page setting) will be enabled for extra buffers beyond the first one. Often the extra buffers are used to write other types of information such as normals or positions, where blending wouldn't be desirable. 

Depth Buffer Format`depthformat`\- ⊞ \- Use either a 24-bit Fixed-Point or 32-bit Floating-Point depth buffer (single channel image). 
* 24-Bit Fixed-Point`fixed24`-
* 32-Bit Floating-Point`float32`-


Cull Face`cullface`\- ⊞ \- Front Faces, Back Faces, Both Faces, Neither. Will cause the render to avoid rendering certain polygon faces depending on their orientation to the camera. Refer to [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling") for more information. 
* Neither`neither`-
* Back Faces`backfaces`-
* Front Faces`frontfaces`-
* Both Faces`bothfaces`-


Override Material`overridemat`\- This allows you to specify a material that will be applied to every Geometry that is rendered in the Render TOP. It is useful for pre-processing passes where we are outputting information about the geometry rather then lighting them and outputting RGB. 

Polygon Depth Offset`polygonoffset`\- This feature pushes the polygons back into space a tiny fraction. This is useful when you are rendering two polygons directly ontop of each other and are experiencing [Z-Fighting](<./Z-Fighting.md> "Z-Fighting"). Refer to [Polygon Depth Offset](<./Polygon_Depth_Offset.md> "Polygon Depth Offset") for more information. This is also an important feature when doing shadows. 

Offset Factor`polygonoffsetfactor`\- Adds an offset to the Z value that depends on how sloped the surface is to the viewer. 

Offset Units`polygonoffsetunits`\- Adds a constant offset to the Z value. 

Display Overdraw`overdraw`\- This feature visually shows the overdraw in the scene. Refer to the [Early Depth-Test](<./Early_Depth-Test.md> "Early Depth-Test") article for more information. In particular the Analyzing Overdraw section. 

Overdraw Limit`overdrawlimit`\- This value quantizes the outputted color value to some # of overdraws. Refer to the [Early Depth-Test](<./Early_Depth-Test.md> "Early Depth-Test") for more information. 

## 

Parameters - Crop Page

Cropping here occurs using the projection matrix. It reduces the amount of the output render that is visible, without changing the resolution. It's particuarly useful to create sub-portion of an overall render in different buffers, such as for rendering across multiple instances of TouchDesigner. Be careful to set the aspect ratio of the Render TOP to match the 'real' aspect of the overall output image, not the aspect of this subsection. Otherwise the projection will be stretched incorrectly. 

Crop Left`cropleft`\- Positions the left edge of the rendered image. 

Crop Left Unit`cropleftunit`\- ⊞ \- Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio). 
* P`pixels`-
* F`fraction`-
* A`fractionaspect`-


Crop Right`cropright`\- Positions the right edge of the rendered image. 

Crop Right Unit`croprightunit`\- ⊞ \- Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio). 
* P`pixels`-
* F`fraction`-
* A`fractionaspect`-


Crop Bottom`cropbottom`\- Positions the bottom edge of the rendered image. 

Crop Bottom Unit`cropbottomunit`\- ⊞ \- Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio). 
* P`pixels`-
* F`fraction`-
* A`fractionaspect`-


Crop Top`croptop`\- Positions the top edge of the rendered image. 

Crop Top Unit`croptopunit`\- ⊞ \- Select the units for this parameter from Pixels, Fraction (0-1), Fraction Aspect (0-1 considering aspect ratio). 
* P`pixels`-
* F`fraction`-
* A`fractionaspect`-

## 

Parameters - Vectors Page

These vectors will be passed to all GLSL MATs used in the render. They allow for global parameters to more easily be passed to many GLSL MATs from a single spot. 

Vector`vec`\- Sequence of uniform name and value pairs. 

Uniform Name`vec0name`\- The uniform name, as declared in the shader. 

Value`vec0value`\- ⊞ \- The value to assign the vector uniform. 
* Value`vec0valuex`-
* Value`vec0valuey`-
* Value`vec0valuez`-
* Value`vec0valuew`-

## 

Parameters - Samplers Page

These samplers will be passed to all GLSL MATs used in the render. They allow for global parameters to more easily be passed to many GLSL MATs from a single spot. 

Uniform Name`uni0name`\- The uniform name, as declared in the shader. 

Sampler`sampler`\- Sequence of sampler parmaeters, including uniform name, TOP reference, and sampling parameters. 

Sampler Name`sampler0name`\- This is the sampler name that the GLSL program will use to sample from this TOP. The samplers need to be declared as the same dimensions as the TOP (sampler2D for a 2D TOP, sampler3D for 3D TOP). 

TOP`sampler0top`\- ⊞ \- This is the TOP that will be referenced by the above sampler name above it. 

Extend U`sampler0extendu`\- ⊞ \- 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Extend V`sampler0extendv`\- ⊞ \- 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Extend W`sampler0extendw`\- ⊞ \- 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Filter`sampler0filter`\- ⊞ \- 
* Nearest`nearest`-
* Linear`linear`-
* Mipmap Linear`mipmaplinear`-


Anisotropic Filter`sampler0anisotropy`\- ⊞ \- 
* Off`off`-
* 2x`2x`-
* 4x`4x`-
* 8x`8x`-
* 16x`16x`-

## 

Parameters - Images Page

Images are texture data that can be both read and written to at arbitrary pixels during a render operation, using a [GLSL MAT](<./GLSL_MAT.md> "GLSL MAT"), via the`TDImageStore_Name()`and`TDImageLoad_Name()`. Refer to [Write_a_GLSL_Material#Image_Outputs](<./Write_a_GLSL_Material.htm#Image_Outputs> "Write a GLSL Material") for more information. You can obtain the results of the Image after the render is completed using a [Render Select TOP](<./Render_Select_TOP.md> "Render Select TOP"). The images will automatically be declared for you inside of the shader, you should not declare them yourself (as you do for other uniforms). This is because there is a lot of extra decoration required for the image uniforms. Currently when compiling in the [GLSL MAT](<./GLSL_MAT.md> "GLSL MAT") itself your code will result in an error, since the images are not available there. However when you apply your MAT to a geometry and render it via the Render TOP, a new version of your shader will be included that has that image declared. 

Image`image`\- A sequence of parameters to control image outputs available for the GLSL MATs. 

Name`image0name`\- The uniform name for the image. 

Array Length`image0arraylength`\- If this value is 1 or greater, then the uniform is declared as an array and should be accessed using []. If this is 0 then it is not an array. 

Resolution`image0res`\- ⊞ \- The resolution the image should be. 
* Resolution`image0resw`-
* Resolution`image0resh`-


Format`image0format`\- ⊞ \- The pixel format the image should be allocated as. 
* Use Output`useoutput`\- Use the same pilxe format that the Render TOPs main texture is set to be.
* 8-bit fixed (RGBA)`rgba8fixed`-
* sRGB 8-bit fixed (RGBA)`srgba8fixed`-
* 16-bit float (RGBA)`rgba16float`-
* 32-bit float (RGBA)`rgba32float`-
* _separator_`_separator_`-
* 10-bit RGB, 2-bit Alpha, fixed (RGBA)`rgb10a2fixed`-
* 16-bit fixed (RGBA)`rgba16fixed`-
* 11-bit float (RGB), Positive Values Only`rgba11float`-
* 8-bit fixed (Mono)`mono8fixed`-
* 16-bit fixed (Mono)`mono16fixed`-
* 16-bit float (Mono)`mono16float`-
* 32-bit float (Mono)`mono32float`-
* 8-bit fixed (RG)`rg8fixed`-
* 16-bit fixed (RG)`rg16fixed`-
* 16-bit float (RG)`rg16float`-
* 32-bit float (RG)`rg32float`-
* 8-bit fixed (A)`a8fixed`-
* 16-bit fixed (A)`a16fixed`-
* 16-bit float (A)`a16float`-
* 32-bit float (A)`a32float`-
* 8-bit fixed (Mono+Alpha)`monoalpha8fixed`-
* 16-bit fixed (Mono+Alpha)`monoalpha16fixed`-
* 16-bit float (Mono+Alpha)`monoalpha16float`-
* 32-bit float (Mono+Alpha)`monoalpha32float`-


Type`image0type`\- ⊞ \- Specify what type of texture to create with the image output. 
* 2D Texture`texture2d`-
* 2D Texture Array`texture2darray`-
* 3D Texture`texture3d`-
* Cube Texture`texturecube`-


Depth`image0depth`\- Set the depth when output Type is 2D Texture Array or 3D Texture. 

Access`image0access`\- ⊞ \- Controls how the output textures will be accessed. If the textures will be read from (such as using values generated by other shader executions within the same frame), then the access should be changed to Read-Write instead of Write Only. 
* Write Only`writeonly`-
* Read-Write`readwrite`-

## 

Parameters - Common Page

Output Resolution`outputresolution`\- ⊞ \- quickly change the resolution of the TOP's data. 
* Use Input`useinput`\- Uses the input's resolution
* Eighth`eighth`\- Multiply the input's resolution by that amount.
* Quarter`quarter`\- Multiply the input's resolution by that amount.
* Half`half`\- Multiply the input's resolution by that amount.
* 2X`2x`\- Multiply the input's resolution by that amount.
* 4X`4x`\- Multiply the input's resolution by that amount.
* 8X`8x`\- Multiply the input's resolution by that amount.
* Fit Resolution`fit`\- Grow or shrink the input resolution to fit this resolution, while keeping the aspect ratio the same.
* Limit Resolution`limit`\- Limit the input resolution to be not larger than this resolution, while keeping the aspect ratio the same.
* Custom Resolution`custom`\- Directly control the width and height.


Resolution`resolution`\- ⊞ \- Enabled only when the Resolution parameter is set to Custom Resolution. Some Generators like Constant and Ramp do not use inputs and only use this field to determine their size. The drop down menu on the right provides some commonly used resolutions. 
* W`resolutionw`-
* H`resolutionh`-


Resolution Menu`resmenu`\- A drop-down menu with some commonly used resolutions. 

Use Global Res Multiplier`resmult`\- Uses the Global Resolution Multiplier found in **Edit >Preferences>TOPs**. This multiplies all the TOPs resolutions by the set amount. This is handy when working on computers with different hardware specifications. If a project is designed on a desktop workstation with lots of graphics memory, a user on a laptop with only 64MB VRAM can set the Global Resolution Multiplier to a value of half or quarter so it runs at an acceptable speed. By checking this checkbox on, this TOP is affected by the global multiplier. 

Output Aspect`outputaspect`\- ⊞ \- Sets the image aspect ratio allowing any textures to be viewed in any size. Watch for unexpected results when compositing TOPs with different aspect ratios. (You can define images with non-square pixels using xres, yres, aspectx, aspecty where xres/yres != aspectx/aspecty.) 
* Use Input`useinput`\- Uses the input's aspect ratio.
* Resolution`resolution`\- Uses the aspect of the image's defined resolution (ie 512x256 would be 2:1), whereby each pixel is square.
* Custom Aspect`custom`\- Lets you explicitly define a custom aspect ratio in the Aspect parameter below.


Aspect`aspect`\- ⊞ \- Use when Output Aspect parameter is set to Custom Aspect. 
* Aspect1`aspect1`-
* Aspect2`aspect2`-


Aspect Menu`armenu`\- A drop-down menu with some commonly used aspect ratios. 

Input Smoothness`inputfiltertype`\- ⊞ \- This controls pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. This is how you get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail.


Fill Viewer`fillmode`\- ⊞ \- Determine how the TOP image is displayed in the viewer. 

**NOTE:** To get an understanding of how TOPs work with images, you will want to set this to **Native Resolution** as you lay down TOPs when starting out. This will let you see what is actually happening without any automatic viewer resizing. 
* Use Input`useinput`\- Uses the same Fill Viewer settings as it's input.
* Fill`fill`\- Stretches the image to fit the edges of the viewer.
* Fit Horizontal`width`\- Stretches image to fit viewer horizontally.
* Fit Vertical`height`\- Stretches image to fit viewer vertically.
* Fit Best`best`\- Stretches or squashes image so no part of image is cropped.
* Fit Outside`outside`\- Stretches or squashes image so image fills viewer while constraining it's proportions. This often leads to part of image getting cropped by viewer.
* Native Resolution`nativeres`\- Displays the native resolution of the image in the viewer.


Viewer Smoothness`filtertype`\- ⊞ \- This controls pixel filtering in the viewers. 
* Nearest Pixel`nearest`\- Uses nearest pixel or accurate image representation. Images will look jaggy when viewing at any zoom level other than Native Resolution.
* Interpolate Pixels`linear`\- Uses linear filtering between pixels. Use this to get TOP images in viewers to look good at various zoom levels, especially useful when using any Fill Viewer setting other than Native Resolution.
* Mipmap Pixels`mipmap`\- Uses [ mipmap](<./Mipmapping.md> "Mipmapping") filtering when scaling images. This can be used to reduce artifacts and sparkling in moving/scaling images that have lots of detail. When the input is 32-bit float format, only nearest filtering will be used (regardless of what is selected).


Passes`npasses`\- Duplicates the operation of the TOP the specified number of times. For every pass after the first it takes the result of the previous pass and replaces the node's first input with the result of the previous pass. One exception to this is the [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") when using compute shaders, where the input will continue to be the connected TOP's image. 

Channel Mask`chanmask`\- Allows you to choose which channels (R, G, B, or A) the TOP will operate on. All channels are selected by default. 

Pixel Format`format`\- ⊞ \- Format used to store data for each channel in the image (ie. R, G, B, and A). Refer to [Pixel Formats](<./Pixel_Formats.md> "Pixel Formats") for more information. 
* Use Input`useinput`\- Uses the input's pixel format.
* 8-bit fixed (RGBA)`rgba8fixed`\- Uses 8-bit integer values for each channel.
* sRGB 8-bit fixed (RGBA)`srgba8fixed`\- Uses 8-bit integer values for each channel and stores color in sRGB colorspace. Note that this does **not** apply an sRGB curve to the pixel values, it only stores them using an sRGB curve. This means more data is used for the darker values and less for the brighter values. When the values are read downstream they will be converted back to linear. For more information refer to [sRGB](<./SRGB.md> "SRGB").
* 16-bit float (RGBA)`rgba16float`\- Uses 16-bits per color channel, 64-bits per pixel.
* 32-bit float (RGBA)`rgba32float`\- Uses 32-bits per color channel, 128-bits per pixels.
* 10-bit RGB, 2-bit Alpha, fixed (RGBA)`rgb10a2fixed`\- Uses 10-bits per color channel and 2-bits for alpha, 32-bits total per pixel.
* 16-bit fixed (RGBA)`rgba16fixed`\- Uses 16-bits per color channel, 64-bits total per pixel.
* 11-bit float (RGB), Positive Values Only`rgba11float`\- A RGB floating point format that has 11 bits for the Red and Green channels, and 10-bits for the Blue Channel, 32-bits total per pixel (therefore the same memory usage as 8-bit RGBA). The Alpha channel in this format will always be 1. Values can go above one, but can't be negative. ie. the range is [0, infinite).
* 16-bit float (RGB)`rgb16float`-
* 32-bit float (RGB)`rgb32float`-
* 8-bit fixed (Mono)`mono8fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 8-bits per pixel.
* 16-bit fixed (Mono)`mono16fixed`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 16-bit float (Mono)`mono16float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 16-bits per pixel.
* 32-bit float (Mono)`mono32float`\- Single channel, where RGB will all have the same value, and Alpha will be 1.0. 32-bits per pixel.
* 8-bit fixed (RG)`rg8fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 8-bits per channel, 16-bits total per pixel.
* 16-bit fixed (RG)`rg16fixed`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 16-bit float (RG)`rg16float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 16-bits per channel, 32-bits total per pixel.
* 32-bit float (RG)`rg32float`\- A 2 channel format, R and G have values, while B is 0 always and Alpha is 1.0. 32-bits per channel, 64-bits total per pixel.
* 8-bit fixed (A)`a8fixed`\- An Alpha only format that has 8-bits per channel, 8-bits per pixel.
* 16-bit fixed (A)`a16fixed`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 16-bit float (A)`a16float`\- An Alpha only format that has 16-bits per channel, 16-bits per pixel.
* 32-bit float (A)`a32float`\- An Alpha only format that has 32-bits per channel, 32-bits per pixel.
* 8-bit fixed (Mono+Alpha)`monoalpha8fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 8-bits per channel, 16-bits per pixel.
* 16-bit fixed (Mono+Alpha)`monoalpha16fixed`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 16-bit float (Mono+Alpha)`monoalpha16float`\- A 2 channel format, one value for RGB and one value for Alpha. 16-bits per channel, 32-bits per pixel.
* 32-bit float (Mono+Alpha)`monoalpha32float`\- A 2 channel format, one value for RGB and one value for Alpha. 32-bits per channel, 64-bits per pixel.


Parameter Color Space`parmcolorspace`\- ⊞ \- Controls how all color parameters on this node are interpreted. The color values as treated as being in the selected color space, and are converted to the Working [Color Space](<./Color_Space.md> "Color Space") before they are used as part of the node's operation. Note that this does not change the color space of the node itself, as that is always in the Working Color Space. 
* sRGB`srgb`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with sRGB transfer function. Considered an SDR color space with respect to Reference White.
* sRGB - Linear`srgblinear`\- [sRGB](<https://en.wikipedia.org/wiki/SRGB>) color space, with linear transfer function. Considered an SDR color space with respect to Reference White.
* Rec.601 (NTSC)`rec601ntsc`\- [Rec.601](<https://en.wikipedia.org/wiki/Rec._601>) with NTSC primaries color space, with Rec.601 transfer function. Considered an SDR color space with respect to Reference White.
* Rec.709`rec709`\- [Rec.709](<https://en.wikipedia.org/wiki/Rec._709>) color space, with Rec.709 (same as Rec.2020) transfer function. Considered an SDR color space with respect to Reference White.
* Rec.2020`rec2020`\- [Rec.2020](<https://en.wikipedia.org/wiki/Rec._2020>) color space, with Rec.2020 (same as Rec.709) transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3`dcip3`\- [DCI-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* DCI-P3 (D60)`dcip3d60`\- [DCI-P3 "D60 sim"](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D60 white point, and 2.6 gamma transfer function. Considered an HDR color space with respect to Reference White.
* Display-P3 (D65)`displayp3d65`\- [Display-P3](<https://en.wikipedia.org/wiki/DCI-P3>) color space, with D65 white point, and sRGB gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACES2065-1`aces2065-1`\- [ACES 2065-1](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP0) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* ACEScg`acescg`\- [ACEScg](<https://en.wikipedia.org/wiki/Academy_Color_Encoding_System>) (also known as ACES AP1) color space, with a linear gamma transfer function. Considered an HDR color space with respect to Reference White.
* Passthrough`passthrough`\- When selected, the color values will be used as-is in the operation, without any modification or attempt to convert them into the Working Color Space.


Parameter Reference White`parmreferencewhite`\- ⊞ \- When converting a parameter color value to the Working Color Space, this controls how it should be treated with respect to [Reference White](<./Color_Space.htm#Reference_White> "Color Space"). If the Working Color Space is the same Reference White, then no adjustment is done. If they are different, then the Reference White level (brightness) of this color will be adjusted to the range expected by the Working Color Space. For example if the project is set to have a SDR Reference White of 120 nits, and the HDR Reference White is 80 nits, then a color of (1, 1, 1), which is 120 nits in the SDR color space, will be converted to be (1.5, 1.5, 1.5), which is 120 nits still in the HDR Working Color Space. 
* Default For Color Space`default`\- Will use either the SDR or the HDR Reference White, based on the color space selected.
* Use Parent Panel`useparent`\- Will use the Reference White that the parent panel has selected. If the top-level panel also has 'Use Parent' selected, then 'UI Reference White' will be used.
* Standard (SDR)`sdr`\- Will treat the Parameter Color Space as SDR for it's reference white value.
* High (HDR)`hdr`\- Will treat the Parameter Color Space as HDR for it's reference white value.
* UI`ui`\- Will treat the Parameter Color Space as UI for it's reference white value. This uses the 'UI Reference White Nits' value for it's brightness.

## 

Info CHOP Channels

Extra Information for the Render TOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common TOP Info Channels
* resx \- Horizontal resolution of the TOP in pixels.
* resy \- Vertical resolution of the TOP in pixels.
* aspectx \- Horizontal aspect of the TOP.
* aspecty \- Vertical aspect of the TOP.
* depth \- Depth of 2D or 3D array if this TOP contains a 2D or 3D texture array.
* gpu_memory_used \- Total amount of texture memory used by this TOP.

### 

Common Operator Info Channels
* total_cooks \- Number of times the operator has cooked since the process started.
* cook_time \- Duration of the last cook in milliseconds.
* cook_frame \- Frame number when this operator was last cooked relative to the component timeline.
* cook_abs_frame \- Frame number when this operator was last cooked relative to the absolute time.
* cook_start_time \- Time in milliseconds at which the operator started cooking in the frame it was cooked.
* cook_end_time \- Time in milliseconds at which the operator finished cooking in the frame it was cooked.
* cooked_this_frame \- 1 if operator was cooked this frame.
* warnings \- Number of warnings in this operator if any.
* errors \- Number of errors in this operator if any.


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.300002023.112802021.100002020.200002019.146502018.28070before 2018.28070

TOPs   
---  
[Add ](<./Add_TOP.md> "Add TOP")• [Analyze ](<./Analyze_TOP.md> "Analyze TOP")• [Anti Alias ](<./Anti_Alias_TOP.md> "Anti Alias TOP")• [Blob Track ](<./Blob_Track_TOP.md> "Blob Track TOP")• [Bloom ](<./Bloom_TOP.md> "Bloom TOP")• [Blur ](<./Blur_TOP.md> "Blur TOP")• [Cache Select ](<./Cache_Select_TOP.md> "Cache Select TOP")• [Cache ](<./Cache_TOP.md> "Cache TOP")• [Channel Mix ](<./Channel_Mix_TOP.md> "Channel Mix TOP")• [CHOP to ](<./CHOP_to_TOP.md> "CHOP to TOP")• [Chroma Key ](<./Chroma_Key_TOP.md> "Chroma Key TOP")• [Circle ](<./Circle_TOP.md> "Circle TOP")• [Composite ](<./Composite_TOP.md> "Composite TOP")• [Constant ](<./Constant_TOP.md> "Constant TOP")• [Convolve ](<./Convolve_TOP.md> "Convolve TOP")• [Corner Pin ](<./Corner_Pin_TOP.md> "Corner Pin TOP")• [CPlusPlus ](<./CPlusPlus_TOP.md> "CPlusPlus TOP")• [Crop ](<./Crop_TOP.md> "Crop TOP")• [Cross ](<./Cross_TOP.md> "Cross TOP")• [Cube Map ](<./Cube_Map_TOP.md> "Cube Map TOP")• [Depth ](<./Depth_TOP.md> "Depth TOP")• [Difference ](<./Difference_TOP.md> "Difference TOP")• [Direct Display Out ](<./Direct_Display_Out_TOP.md> "Direct Display Out TOP")• [DirectX In ](<./DirectX_In_TOP.md> "DirectX In TOP")• [DirectX Out ](<./DirectX_Out_TOP.md> "DirectX Out TOP")• [Displace ](<./Displace_TOP.md> "Displace TOP")• [Edge ](<./Edge_TOP.md> "Edge TOP")• [Emboss ](<./Emboss_TOP.md> "Emboss TOP")• [Feedback ](<./Feedback_TOP.md> "Feedback TOP")• [Fit ](<./Fit_TOP.md> "Fit TOP")• [Flip ](<./Flip_TOP.md> "Flip TOP")• [Function ](<./Function_TOP.md> "Function TOP")• [GLSL Multi ](<./GLSL_Multi_TOP.md> "GLSL Multi TOP")• [GLSL ](<./GLSL_TOP.md> "GLSL TOP")• [HSV Adjust ](<./HSV_Adjust_TOP.md> "HSV Adjust TOP")• [HSV to RGB ](<./HSV_to_RGB_TOP.md> "HSV to RGB TOP")• [Import Select ](<./Import_Select_TOP.md> "Import Select TOP")• [In ](<./In_TOP.md> "In TOP")• [Inside ](<./Inside_TOP.md> "Inside TOP")• [Introduction To s Vid ](<./Introduction_To_TOPs_Vid.md> "Introduction To TOPs Vid")• [Kinect Azure Select ](<./Kinect_Azure_Select_TOP.md> "Kinect Azure Select TOP")• [Kinect Azure ](<./Kinect_Azure_TOP.md> "Kinect Azure TOP")• [Kinect ](<./Kinect_TOP.md> "Kinect TOP")• [Layer Mix ](<./Layer_Mix_TOP.md> "Layer Mix TOP")• [Layer ](<./Layer_TOP.md> "Layer TOP")• [Layout ](<./Layout_TOP.md> "Layout TOP")• [Leap Motion ](<./Leap_Motion_TOP.md> "Leap Motion TOP")• [Lens Distort ](<./Lens_Distort_TOP.md> "Lens Distort TOP")• [Level ](<./Level_TOP.md> "Level TOP")• [Limit ](<./Limit_TOP.md> "Limit TOP")• [Lookup ](<./Lookup_TOP.md> "Lookup TOP")• [Luma Blur ](<./Luma_Blur_TOP.md> "Luma Blur TOP")• [Luma Level ](<./Luma_Level_TOP.md> "Luma Level TOP")• [Math ](<./Math_TOP.md> "Math TOP")• [Matte ](<./Matte_TOP.md> "Matte TOP")• [Mirror ](<./Mirror_TOP.md> "Mirror TOP")• [Monochrome ](<./Monochrome_TOP.md> "Monochrome TOP")• [MoSys ](<./MoSys_TOP.md> "MoSys TOP")• [Movie File In ](<./Movie_File_In_TOP.md> "Movie File In TOP")• [Movie File Out ](<./Movie_File_Out_TOP.md> "Movie File Out TOP")• [MPCDI ](<./MPCDI_TOP.md> "MPCDI TOP")• [Multiply ](<./Multiply_TOP.md> "Multiply TOP")• [Ncam ](<./Ncam_TOP.md> "Ncam TOP")• [NDI In ](<./NDI_In_TOP.md> "NDI In TOP")• [NDI Out ](<./NDI_Out_TOP.md> "NDI Out TOP")• [Noise ](<./Noise_TOP.md> "Noise TOP")• [Normal Map ](<./Normal_Map_TOP.md> "Normal Map TOP")• [Notch ](<./Notch_TOP.md> "Notch TOP")• [Null ](<./Null_TOP.md> "Null TOP")• [NVIDIA Background ](<./NVIDIA_Background_TOP.md> "NVIDIA Background TOP")• [NVIDIA Denoise ](<./NVIDIA_Denoise_TOP.md> "NVIDIA Denoise TOP")• [NVIDIA Flex ](<./NVIDIA_Flex_TOP.md> "NVIDIA Flex TOP")• [NVIDIA Flow ](<./NVIDIA_Flow_TOP.md> "NVIDIA Flow TOP")• [NVIDIA Upscaler ](<./NVIDIA_Upscaler_TOP.md> "NVIDIA Upscaler TOP")• [OAK Select ](<./OAK_Select_TOP.md> "OAK Select TOP")• [Oculus Rift ](<./Oculus_Rift_TOP.md> "Oculus Rift TOP")• [OP Viewer ](<./OP_Viewer_TOP.md> "OP Viewer TOP")• [OpenColorIO ](<./OpenColorIO_TOP.md> "OpenColorIO TOP")• [OpenVR ](<./OpenVR_TOP.md> "OpenVR TOP")• [Optical Flow ](<./Optical_Flow_TOP.md> "Optical Flow TOP")• [Orbbec Select ](<./Orbbec_Select_TOP.md> "Orbbec Select TOP")• [Orbbec ](<./Orbbec_TOP.md> "Orbbec TOP")• [Ouster Select ](<./Ouster_Select_TOP.md> "Ouster Select TOP")• [Ouster ](<./Ouster_TOP.md> "Ouster TOP")• [Out ](<./Out_TOP.md> "Out TOP")• [Outside ](<./Outside_TOP.md> "Outside TOP")• [Over ](<./Over_TOP.md> "Over TOP")• [Pack ](<./Pack_TOP.md> "Pack TOP")• [Photoshop In ](<./Photoshop_In_TOP.md> "Photoshop In TOP")• [Point File In ](<./Point_File_In_TOP.md> "Point File In TOP")• [Point File Select ](<./Point_File_Select_TOP.md> "Point File Select TOP")• [Point Transform ](<./Point_Transform_TOP.md> "Point Transform TOP")• [POP to ](<./POP_to_TOP.md> "POP to TOP")• [PreFilter Map ](<./PreFilter_Map_TOP.md> "PreFilter Map TOP")• [Projection ](<./Projection_TOP.md> "Projection TOP")• [Ramp ](<./Ramp_TOP.md> "Ramp TOP")• [RealSense ](<./RealSense_TOP.md> "RealSense TOP")• [Rectangle ](<./Rectangle_TOP.md> "Rectangle TOP")• [Remap ](<./Remap_TOP.md> "Remap TOP")• [Render Pass ](<./Render_Pass_TOP.md> "Render Pass TOP")• [Render Select ](<./Render_Select_TOP.md> "Render Select TOP")• [Render Simple ](<./Render_Simple_TOP.md> "Render Simple TOP")• Render • [RenderStream In ](<./RenderStream_In_TOP.md> "RenderStream In TOP")• [RenderStream Out ](<./RenderStream_Out_TOP.md> "RenderStream Out TOP")• [Reorder ](<./Reorder_TOP.md> "Reorder TOP")• [Resolution ](<./Resolution_TOP.md> "Resolution TOP")• [RGB Key ](<./RGB_Key_TOP.md> "RGB Key TOP")• [RGB to HSV ](<./RGB_to_HSV_TOP.md> "RGB to HSV TOP")• [Scalable Display ](<./Scalable_Display_TOP.md> "Scalable Display TOP")• [Screen Grab ](<./Screen_Grab_TOP.md> "Screen Grab TOP")• [Screen ](<./Screen_TOP.md> "Screen TOP")• [Script ](<./Script_TOP.md> "Script TOP")• [Select ](<./Select_TOP.md> "Select TOP")• [Shared Mem In ](<./Shared_Mem_In_TOP.md> "Shared Mem In TOP")• [Shared Mem Out ](<./Shared_Mem_Out_TOP.md> "Shared Mem Out TOP")• [SICK ](<./SICK_TOP.md> "SICK TOP")• [Slope ](<./Slope_TOP.md> "Slope TOP")• [Spectrum ](<./Spectrum_TOP.md> "Spectrum TOP")• [SSAO ](<./SSAO_TOP.md> "SSAO TOP")• [ST2110 In ](<./ST2110_In_TOP.md> "ST2110 In TOP")• [ST2110 Out ](<./ST2110_Out_TOP.md> "ST2110 Out TOP")• [Stype ](<./Stype_TOP.md> "Stype TOP")• [Substance Select ](<./Substance_Select_TOP.md> "Substance Select TOP")• [Substance ](<./Substance_TOP.md> "Substance TOP")• [Subtract ](<./Subtract_TOP.md> "Subtract TOP")• [SVG ](<./SVG_TOP.md> "SVG TOP")• [Switch ](<./Switch_TOP.md> "Switch TOP")• [Syphon Spout In ](<./Syphon_Spout_In_TOP.md> "Syphon Spout In TOP")• [Syphon Spout Out ](<./Syphon_Spout_Out_TOP.md> "Syphon Spout Out TOP")• [Text ](<./Text_TOP.md> "Text TOP")• [Texture 3D ](<./Texture_3D_TOP.md> "Texture 3D TOP")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Threshold ](<./Threshold_TOP.md> "Threshold TOP")• [Tile ](<./Tile_TOP.md> "Tile TOP")• [Time Machine ](<./Time_Machine_TOP.md> "Time Machine TOP")• [Tone Map ](<./Tone_Map_TOP.md> "Tone Map TOP")• [TOP ](<./TOP.md> "TOP")• [TOP Viewer ](<./TOP_Viewer.md> "TOP Viewer")• [Touch In ](<./Touch_In_TOP.md> "Touch In TOP")• [Touch Out ](<./Touch_Out_TOP.md> "Touch Out TOP")• [Transform ](<./Transform_TOP.md> "Transform TOP")• [Under ](<./Under_TOP.md> "Under TOP")• [Video Device In ](<./Video_Device_In_TOP.md> "Video Device In TOP")• [Video Device Out ](<./Video_Device_Out_TOP.md> "Video Device Out TOP")• [Video Stream In ](<./Video_Stream_In_TOP.md> "Video Stream In TOP")• [Video Stream Out ](<./Video_Stream_Out_TOP.md> "Video Stream Out TOP")• [Vioso ](<./Vioso_TOP.md> "Vioso TOP")• [Web Render ](<./Web_Render_TOP.md> "Web Render TOP")• [ZED Select ](<./ZED_Select_TOP.md> "ZED Select TOP")• [ZED ](<./ZED_TOP.md> "ZED TOP")
