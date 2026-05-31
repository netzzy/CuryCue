# Point File In POP

## 

Summary

The Point File In POP loads 3D point data into POPs from either a single file or a sequence of files. The Point File In POP will load all available point data after you select field names and give them attribute names. Fields include standard ones like XYZ position, normal vectors, texture coordinates and RGBA color. More specialized fields are read in via any number of sequential blocks that map fields to attributes. 

By default, field`x`,`y`and`z`are placed into the`P`attribute, and`r g b a`into the`Color`attribute, but that can be all re-assigned. The sequential blocks can create float, float2, float3 and float4 attributes, as well as arrays of values (no matrices or double at the moment). 

The Thin page lets you skip points in the file, either randomly or in patterns. The ReRange page lets you scale/offset attribute values without having to create a temporary version of an attribute. 

The Point File In POP will read point data from various mesh and floating point data files including:`.obj`,`.ply`,`.fits`(astronomy format), and`.exr`. It can also load ASCII point files (`.xyz`,`.pts`,`.csv`,`.txt`, etc) with one point per line and comma- or space-separated fields. The first line in ASCII point files can either be the number of points, the names of the point fields or the first point in the file. 

For a complete list, see [File Types](<./File_Types.md> "File Types"). The OpenEXR file format is generally best to use as it is binary, can be read in multi-frame file sequences that uses TouchDesigner's movie file pre-reading and buffering, and can be written from TouchDesigner's [Movie File Out TOP](<./Movie_File_Out_TOP.md> "Movie File Out TOP") with unlimited numbers of channels. 

**Gaussian Splat files** : The Point File In POP can read in all the specialized attributes of Gaussian Splat files. Give there are over 45 components of attributes, there is an example file in POPs`Examples / GaussianSplats/`with a full setup, and there is an example in Help -> Browse Samples :`PointClouds/`(TBD: Examine the state of a Point File In POP by attaching an Info CHOP. This will show information like the number of points, fields per point and the number of frames. It also shows dynamic information like the file open status, current frame, readahead frames and queue size, dropped frame count, CPU decode time and GPU upload time.) 

Headers: If the file contains any additional header data, this can be viewed by attaching an [Info DAT](<./Info_DAT.md> "Info DAT"). Header data is stored as key-value pairs with the keys in the first column and the corresponding data in the second column, which can easily be interpreted with python. 

All of the ASCII point list formats are loaded the same way whether their extension is`txt`,`csv`,`xyz`, etc. The parser looks for the first separating character (comma, space or tab) and then uses that to delimit the rest of the file. It will ignore delimiters that are inside single or double quotes. There are a few special rules depending on the delimiter style e.g. multiple spaces are merged together, but a comma at the end of a line indicates a blank field afterwards. Once a delimiter is established, The first line can be the number of points, but it is ignored. If the next line are strings then it is treated as a row of headers (channel names). Each row after that is considered the attributes of point. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[pointfileinPOP_Class](<./PointfileinPOP_Class.md> "PointfileinPOP Class")

## 

Parameters - Point File In Page

File`file`\- The path and name of the point file to load. 

Reload`reload`\- ⊞ \- Re-import and load the geometry. 
* Reload`reload`-
* Reload Pulse`reloadpulse`\- Force reload.


Create Point Primitives`createpointprim`\- Enable creating point primitives 

Max Number of Points`maxpointsenable`\- Enable the setting of the max number of points. 

Max Number of Points`maxpoints`\- Sets the max number of points when the automatic max number of points is overriden. 

Position Fields`positionfields`\- ⊞ \- Fields mapped to the position. 
* x`x`-
* y`y`-
* z`z`-
* nx`nx`-
* ny`ny`-
* nz`nz`-
* r`r`-
* g`g`-
* b`b`-
* a`a`-


Normal Fields`normalfields`\- ⊞ \- Fields for the normal attribute. 
* x`x`-
* y`y`-
* z`z`-
* nx`nx`-
* ny`ny`-
* nz`nz`-
* r`r`-
* g`g`-
* b`b`-
* a`a`-


Texture Fields`texturefields`\- ⊞ \- Fields mapped to the texture coordinates. 
* x`x`-
* y`y`-
* z`z`-
* nx`nx`-
* ny`ny`-
* nz`nz`-
* r`r`-
* g`g`-
* b`b`-
* a`a`-


Color Fields`colorfields`\- ⊞ \- The fields to use for the color attribute. 
* x`x`-
* y`y`-
* z`z`-
* nx`nx`-
* ny`ny`-
* nz`nz`-
* r`r`-
* g`g`-
* b`b`-
* a`a`-


Attribute`attr`\- Start of Sequential Parameter Blocks for attribute conditions. 

Fields`attr0fields`\- ⊞ \- Determines fields that can be used to create additional attributes. 
* x`x`-
* y`y`-
* z`z`-
* nx`nx`-
* ny`ny`-
* nz`nz`-
* r`r`-
* g`g`-
* b`b`-
* a`a`-


Attribute Name`attr0name`\- Name of attribute 

Array`attr0isarray`\- Attribute is an array, for example 5 float3 values is an array of size 5. 

Array Size`attr0arraysize`\- Nunber of elements in the array. 

Qualifier`attr0qualifier`\- ⊞ \- Whether the new attribute is generic attribute or not. Qualifiers are taken into account for some operations. 
* None`none`-
* Color`color`-
* Direction`dir`-


Input Color Space`inputcolorspace`\- ⊞ \- Override / set the color space, or use the color space in the file, or assume default if there is none. 
* Automatic`automatic`-
* sRGB`srgb`-
* sRGB - Linear`srgblinear`-
* Rec.601 (NTSC)`rec601ntsc`-
* Rec.709`rec709`-
* Rec.2020`rec2020`-
* Rec.2020 ST2084PQ`rec2020st2084pq`-
* Rec.2020 HLG`rec2020hlg`-
* DCI-P3`dcip3`-
* DCI-P3 (D60)`dcip3d60`-
* Display P3 (D65)`displayp3d65`-
* Display P3 (D65) - Linear`displayp3d65linear`-
* ACES2065-1`aces2065-1`-
* ACEScg`acescg`-
* ACESproxy`acesproxy`-
* Passthrough`passthrough`-


Input Reference White`inputreferencewhite`\- ⊞ \- Color space to use for the incoming data. 
* Default For Color Space`default`-
* Standard (SDR)`sdr`-
* High (HDR)`hdr`-
* UI`ui`-

## 

Parameters - Thin Page

Thin Out Range`thinoutrange`\- Enable index-based point filtering. 

Thin Range Start`thinrangestart`\- Determines the starting index for range-based point filtering. 

Thin Range Length`thinrangelength`\- Determines the number of points being filtered by index range. 

Thin Step`thinstep`\- Filters every Nth point. 

Thin Random`thinrandom`\- Determines the proportion of points randomly filtered. 

Thin Random Seed`thinrandomseed`\- Sets the random seed for points being randomly filtered. 

## 

Parameters - ReRange Page

Rerange`rerange`\- Start of Sequential Parameter Blocks to re-range created attributes. 

Scope`rerange0scope`\- ⊞ \- Rerange any attribute from the file. 
* P`P`-
* P.i01`P.i01`-
* Color`Color`-
* Color.rgb`Color.rgb`-
* N`N`-


Parameter Size`rerange0parsize`\- ⊞ \- Number of independent configurable parameter values. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Map from Low`rerange0fromlow`\- Reranges the attribute value. 

Map from High`rerange0fromhigh`\- Reranges the attribute value. 

Map to Low`rerange0tolow`\- Reranges the attribute value. 

Map to High`rerange0tohigh`\- Reranges the attribute value. 

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

## 

Info CHOP Channels

Extra Information for the Point File In POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• Point File In • [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
