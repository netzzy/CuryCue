# GLSL Advanced POP

## 

Summary

**Refer to the[Write GLSL POPs](</Write_GLSL_POPs> "Write GLSL POPs") article for more info on using this POP.**

In single shader dispatch mode, runs a single compute shader that can read and write to points, verts, and primitive attributes simultaneously. 

In per primitive batch mode, runs the shader once per primitive batch. 

The number of threads mode defines how many threads are used. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[glsladvancedPOP_Class](</GlsladvancedPOP_Class> "GlsladvancedPOP Class")

## 

Parameters - Main Page

Compute Shader`computedat`\- Points to the DAT holding the Compute Shader. Drag & Drop a DAT here, or manually enter the path to the DAT. 

Shader Dispatch Mode`shaderdispatchmode`\- ⊞ \- Specifies the compute shader dispatch mode. 
* Single Shader Dispatch`single`-
* Per Primitive Batch`perprimbatch`-


Number of Elements`numelems`\- The number of elements when setting it manually with a parameter. 

POP`numelemspop`\- POP reference when setting the number of elements from an attribute. 

Num Elements Attrib`numelemsclass`\- ⊞ \- Sets the attribute class where the number of elements can be found. 
* Num Elements Attrib`numelemsclass`-
* Num Elements Attrib`numelemsattr`\- The attribute to use for the number of elements. The first value is used.


Work Group Size`workgroupsize`\- ⊞ \- Specifies the workgroup size when manually setting the number of threads. 
* Work Group Size`workgroupsizex`-
* Work Group Size`workgroupsizey`-
* Work Group Size`workgroupsizez`-


Dispatch Size`dispatchsize`\- ⊞ \- Determines the number of thread groups to launch in each dimension. 
* Dispatch Size`dispatchsizex`-
* Dispatch Size`dispatchsizey`-
* Dispatch Size`dispatchsizez`-


Number of Threads per Batch Mode`numthreadsbatchmode`\- ⊞ \- Sets how the number of threads per primitive batch is determined. 
* Per Input Vertex`inputvert`-
* Per Input Primitive`inputprim`-
* Per Output Vertex`outputvert`-
* Per Output Primitive`outputprim`-


Point Output Attributes`ptoutputattrs`\- ⊞ \- Input point attributes modified by the shader. 
* *`*`-


Prim Output Attributes`primoutputattrs`\- ⊞ \- Input primitive attributes modified by the shader. 
* *`*`-


Vert Output Attributes`vertoutputattrs`\- ⊞ \- The vertex attributes to output. 
* *`*`-


Output Access`outputaccess`\- ⊞ \- Controls whether the attribute buffers can only be read from or read from and written to. 
* Write Only`writeonly`-
* Read-Write`readwrite`-


Initialize Output Attributes`initoutputattrs`\- Copy input attributes values for existing attributes, set the attributes values to their defaults for new attributes. It's a separate compute shader dispatch happening before the POP custom compute shader dispatch. 

Copy Previous Pass Output to Input`prevpassoutput`\- Enable copying the previous pass outputs to the next pass inputs. 

Passes`npasses`\- Number of shader passes. 

Input`input`\- Start of Sequential Parameter Blocks managing the inputs of the POP. 

In POPs`input0pops`\- Allows to specify additional input POPs besides connected POPs. 

TDSimplexNoise()`simplexnoise`\- ⊞ \- Sets the implementation to use for a simplex noise method that can be called in the shader. 
* Performance`performance`-
* Quality`quality`-


Number of Threads`numthreadsmode`\- ⊞ \- Selects how to set the number of threads for the custom compute shader dispatch. 
* Per Input Point`inputpoint`-
* Per Input Vertex`inputvert`-
* Per Input Primitive`inputprim`-
* Per Max Output Point`outputpoint`-
* Per Max Output Vertex`outputvert`-
* Per Max Output Primitive`outputprim`-
* Manual Number of Elements`numelems`-
* Number of Elements from Attribute`numelemsattrib`-
* Manual Number of Threads`manual`-

## 

Parameters - Output Page

Render`render`\- Enables rendering in the viewer. Disable when output data is in an intermediate or non-renderable state 

Max Points`maxpointsmode`\- ⊞ \- Determines if the maximum number of points is determined by the input or by a custom value. 
* Max Points`maxpointsmode`-
* Max Points`maxpoints`\- Sets the max number of points. If the POP point count info is on the CPU, that's the actual number of points.


Point Count Info`pointcountinfo`\- ⊞ \- Input point count source. 
* From Input`input`-
* From Attributes`fromattrs`-
* From Max Parameters`fromparams`-


Point Count`pointcountmode`\- ⊞ \- Output point count source. 
* From Input`input`-
* Zero`zero`-
* Set`set`-


Point Count POP`pointcountpop`\- POP that holds the point count. 

Point Count Attribute`pointcountclass`\- ⊞ \- Attribute class of the attribute that holds the point count. 
* Point Count Attribute`pointcountclass`-
* Point Count Attribute`pointcountattr`\- Attribute that holds the point count.


Max Triangles`maxtrianglesmode`\- ⊞ \- Specifies how to set the max number of triangle primitives. If the POP topology info is on the CPU, that's the actual number of triangle primitives. 
* Max Triangles`maxtrianglesmode`-
* Max Triangles`maxtriangles`\- Sets the max number of triangle primitives. If the POP topology info is on the CPU, that's the actual number of triangle primitives.


Max Quads`maxquadsmode`\- ⊞ \- Specifies how to set the max number of quadrilaterals primitives. If the POP topology info is on the CPU, that's the actual number of quadrilateral primitives. 
* Max Quads`maxquadsmode`-
* Max Quads`maxquads`\- Sets the max number of quad primitives. If the POP topology info is on the CPU, that's the actual number of quad primitives.


Max Line Strips`maxlinestripsmode`\- ⊞ \- Specifies how to set the maximum number of line strips. 
* Max Line Strips`maxlinestripsmode`-
* Max Line Strips`maxlinestrips`\- Sets the max number of line strip primitives. If the POP topology info is on the CPU, that's the actual number of line strip primitives.


Max Line Strip Verts`maxlsvertsmode`\- ⊞ \- Sets the max number of line strip vertices. If the POP topology is on the CPU, that's the actual number of line strip vertices. 
* Max Line Strip Verts`maxlsvertsmode`-
* Max Line Strip Verts`maxlsverts`\- Sets the max number of line strip vertices. If the POP topology is on the CPU, that's the actual number of line strip vertices.


Max Lines`maxlinesmode`\- ⊞ \- Specifies how to set the maximum number of line primitives. 
* Max Lines`maxlinesmode`-
* Max Lines`maxlines`\- Sets the max number of line primitives. If the POP topology info is on the CPU, that's the actual number of line primitives.


Max Point Prims`maxpointprimsmode`\- ⊞ \- Specifies how to set the max number of point primitives. 
* Max Point Prims`maxpointprimsmode`-
* Max Point Prims`maxpointprims`\- Sets the max number of point primitives. If the POP topology info is on the CPU, that's the actual number of point primitives.


Line Strip Info Update`lsinfoupdate`\- ⊞ \- Allows you to choose how the Line Strip Info buffers get updated. 
* Auto`auto`-
* Zero`zero`-
* Manual`manual`-


Line Strip Info POP`lsinfopop`\- POP with the attribute to use for the Line Strip Info buffer. 

Line Strip Info Attribute`lsinfoclass`\- ⊞ \- Sets the attribute class where the line strip info attribute can be found. 
* Line Strip Info Attribute`lsinfoclass`-
* Line Strip Info Attribute`lsinfoattr`\- Attribute to use for the Line Strip Info buffer.


Line Strip Index per Vert POP`lsindexpop`\- POP with the attribute to use for the Line Strip Index per Vert buffer. 

Line Strip Index per Vert Attribute`lsindexclass`\- ⊞ \- Sets the attribute class where the line strip index per vertex attribute can be found. 
* Line Strip Index per Vert Attribute`lsindexclass`-
* Line Strip Index per Vert Attrib`lsindexattr`\- Attribute to use for the Line Strip Index per Vert buffer.


Max Verts per Line Strip`lsmaxvertsoverride`\- ⊞ \- Specifies you want to set the max number of verts per line strip.allocation. 
* Max Verts per Line Strip`lsmaxvertsoverride`-
* Max Verts per Line Strip`lsmaxverts`\- Sets the max number of verts per line strip. Used by some downstream POPs for GPU memory allocation.


Initialize Output Primitives`initoutputprims`\- ⊞ \- Copy input primitives (point index values) and set point index for new primitives to 0. 
* Don't Initialize`none`-
* Copy input primitives (extra verts 0)`copy`-
* Set vertices to 0`zero`-


Topology Info`topoinfo`\- ⊞ \- Sets the topology information source. 
* From Input`input`-
* From Attributes`fromattrs`-
* From Max Parameters`fromparams`-


Topology Info POP`topoinfopop`\- Sets reference to a POP where the info attribute can be found. 

Topology Info Attributes Class`topoinfoclass`\- ⊞ \- Sets the attribute class where the info attribute can be found. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Triangle Count`trianglecountmode`\- ⊞ \- The triangle count when setting it manually with a parameter. 
* Triangle Count`trianglecountmode`-
* Triangle Count Attribute`trianglecountattr`\- Specifies the attribute to use to set the triangles count.


Quad Count`quadcountmode`\- ⊞ \- Whether to get the count of quad primitives from the source, set it to 0, or set its value manually. 
* Quad Count`quadcountmode`-
* Quad Count Attribute`quadcountattr`\- Specifies the attribute to use to set the quadrilaterals count.


Line Strip Count`linestripcountmode`\- ⊞ \- Whether to get the count of line strips from the source, set it to 0, or set its value manually. 
* Line Strip Count`linestripcountmode`-
* Line Strip Count Attribute`linestripcountattr`\- Specifies the attribute to use to set the line count.


Line Strip Vert Count`lsvertcountmode`\- ⊞ \- Whether to get the vertex count of line strips from the source, set it to 0, or set its value manually. 
* Line Strip Vert Count`lsvertcountmode`-
* Line Strip Vert Count Attribute`lsvertcountattr`\- Specifies the attribute to use for the line strip vertex count.


Line Count`linecountmode`\- ⊞ \- Whether to get the count of line primitives from the source, set it to 0, or set its value manually. 
* Line Count`linecountmode`-
* Line Count Attribute`linecountattr`\- Specifies the attribute to use to set the line count.


Point Prim Count`pointprimcountmode`\- ⊞ \- Whether to get the count of point primitives from the source, set it to 0, or set its value manually. 
* Point Prim Count`pointprimcountmode`-
* Point Prim Count Attrib`pointprimcountattr`\- Specifies the attribute to use for the point primitive count.

## 

Parameters - Extra Outputs Page

Extra Output`extraout`\- Start of Sequential Parameter Blocks to declare additional POP outputs that can be picked with GLSL Select. 

Name`extraout0name`\- The name of the extra output. 

POP`extraout0pop`\- POP reference. 

Point Output Attributes`extraout0ptattrs`\- Input point attributes modified by the shader. 

Prim Output Attributes`extraout0primattrs`\- Input primitive attributes modified by the shader. 

Vert Output Attributes`extraout0vertattrs`\- Input vertex attributes modified by the shader. 

Output Access`extraout0outputaccess`\- ⊞ \- Controls whether the attribute buffers can only be read from or read from and written to. 
* Write Only`writeonly`-
* Read-Write`readwrite`-


Copy Previous Pass Output to Input`extraout0prevpassoutput`\- Enable copying the previous pass outputs to the next pass inputs. 

Copy Input Attributes`extraout0copyinputattrs`\- For allocated output attributes, whether to initialize them with the input values. 

## 

Parameters - Create Attribs Page

New Attribute`attr`\- Start of Sequential Parameter Blocks to create new attributes. 

New Attribute Class`attr0class`\- ⊞ \- The attribute class for the new attribute. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


New Attribute Name`attr0name`\- ⊞ \- Choose to create a predefined attribute or a custom attribute. 
* New Attribute Name`attr0name`-
* Custom Name`attr0customname`\- The name of the new cutom attribute.


New Attribute Type`attr0type`\- ⊞ \- Determines the type. 
* New Attribute Type`attr0type`-
* New Attribute Number of Components`attr0numcomps`\- Number of components of the new attribute.


Array`attr0isarray`\- Attribute is an array, for example 5 float3 values is an array of size 5. 

Array Size`attr0arraysize`\- Array Size of the new attribute. 

Value`attr0value`\- ⊞ \- Attribute value. 
* Value`attr0value0`\- Attribute value(s).
* Value`attr0value1`\- Attribute value(s).
* Value`attr0value2`\- Attribute value(s).
* Value`attr0value3`\- Attribute value(s).


Matrix Attribute`matattr`\- Start of Sequential Parameter Blocks to create new matrix attributes. 

Matrix Attribute Class`matattr0class`\- ⊞ \- Determines the attribute class where the matrix attribute can be created. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Custom Matrix Name`matattr0name`\- Determines the new matrix attribute name. 

Rows`matattr0numrows`\- Number of rows in the matrix - 2, 3 or 4. 

Columns`matattr0numcols`\- Number of columns in the matrix - 2, 3 or 4. 

Array`matattr0isarray`\- Attribute is an array, for example 5 float3 values is an array of size 5. 

Array Size`matattr0arraysize`\- Nunber of elements in the array of matrices. 

Qualifier`matattr0qualifier`\- ⊞ \- Additional detail on how the attribute should be interpreted. 
* None`none`-
* Transform Matrix`transformMatrix`-

## 

Parameters - Colors Page

Pre-Multiply RGB by Alpha`premultcolor`\- Enable RGB values pre-multiplication with the Alpha. 

Color`color`\- Start of Sequential Parameter Blocks for color uniforms. 

Name`color0name`\- The name of the color uniform. 

RGB`color0rgb`\- ⊞ \- RGB Color. 
* RGB`color0rgbr`-
* RGB`color0rgbg`-
* RGB`color0rgbb`-


Alpha`color0alpha`\- Alpha value. 

## 

Parameters - Vectors Page

Vector`vec`\- Start of Sequential Parameter Blocks to define uniform variables. 

Name`vec0name`\- The name of the vector uniform. 

Type`vec0type`\- ⊞ \- The numeric representation of the attribute values. 
* float`float`-
* vec2`vec2`-
* vec3`vec3`-
* vec4`vec4`-
* double`double`-
* dvec2`dvec2`-
* dvec3`dvec3`-
* dvec4`dvec4`-
* int`int`-
* ivec2`ivec2`-
* ivec3`ivec3`-
* ivec4`ivec4`-
* uint`uint`-
* uvec2`uvec2`-
* uvec3`uvec3`-
* uvec4`uvec4`-


Value`vec0value`\- ⊞ \- Vector value. 
* Value`vec0valuex`-
* Value`vec0valuey`-
* Value`vec0valuez`-
* Value`vec0valuew`-

## 

Parameters - Samplers Page

Sampler`sampler`\- Start of Sequential Parameter Blocks for Samplers to read from the shader. 

Name`sampler0name`\- The name of the sampler uniform. 

TOP`sampler0top`\- ⊞ \- Sets reference to a TOP to sample. 

Extend U`sampler0extendu`\- ⊞ \- Controls what is returned from the texture sampling functions when the U texture coordinates are outside [0-1] range. 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Extend V`sampler0extendv`\- ⊞ \- Controls what is returned from the texture sampling functions when the V texture coordinates are outside [0-1] range. 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Extend W`sampler0extendw`\- ⊞ \- Controls what is returned from the texture sampling functions when the W texture coordinates are outside [0-1] range. 
* Hold`hold`-
* Zero`zero`-
* Repeat`repeat`-
* Mirror`mirror`-


Filter`sampler0filter`\- ⊞ \- Controls the pixel filtering on the input image of the TOP. 
* Nearest Pixel`nearest`-
* Interpolate Pixels`linear`-

## 

Parameters - Arrays Page

Array`array`\- Start of Sequential Parameter Blocks for array uniforms. 

Name`array0name`\- The name of the array uniform. 

Type`array0type`\- ⊞ \- The number of components for the array. 
* float`float`-
* vec2`vec2`-
* vec3`vec3`-
* vec4`vec4`-


CHOP`array0chop`\- The CHOP for the current uniform. 

Array Type`array0arraytype`\- ⊞ \- The type of uniform array, array or sampler. 
* Uniform Array`uniformarray`-
* Texture Buffer`texturebuffer`-

## 

Parameters - Matrices Page

Matrix`matrix`\- Start of Sequential Parameter Blocks of matrix uniforms. 

Name`matrix0name`\- The name of the matrix uniform. 

Matrix`matrix0value`\- The value to assign the matrix. For valid ways to specify this, see the Matrix Parameters article. 

## 

Parameters - Temp Buffers Page

Temp Buffer`tempbuffer`\- Start of Sequential Parameter Blocks for Temporary buffers used to pass information to the shader as uniforms. 

Name`tempbuffer0name`\- The name of the temporary buffer. 

Initial Value`tempbuffer0initval`\- Initial value for the current temporary buffer. 

Constant`const`\- Start of Sequential Parameter Blocks for Specialization Constants. 

Name`const0name`\- The name of the constant. 

Value`const0value`\- Constant value. 

## 

Parameters - Page

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

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

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the GLSL Advanced POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common POP Info Channels

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


  
TouchDesigner Build: Latest\nwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• GLSL Advanced • [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
