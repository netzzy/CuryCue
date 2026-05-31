# Depth MAT

## 

Summary

The Depth Only MAT can be used to prevent objects from being drawn by making an invisible barrier in Z. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[depthMAT_Class](<./DepthMAT_Class.md> "DepthMAT Class")

## 

Parameters - Deform Page

Refer to the [ Deform Article](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)") for more information on doing deforms in TouchDesigner. 

Deform`dodeform`\- Enables deforms on this material. 

Get Bone Data:`deformdata`\- ⊞ \- Specifies where the deform bone data will be obtained. 
* From a SOP`sop`-
* From another MAT`mat`-
* From a DeformIn MAT`deformin`-


SOP with Capture Data`targetsop`\- Specifies the SOP that contains the deform capture attributes. 

pCaptPath Attrib`pcaptpath`\- Specifies the name of the pCaptPath attribute to use. When your geometry has been put through a [Bone Group SOP](<./Bone_Group_SOP.md> "Bone Group SOP"), the attributes will be split into names like pCaptPath0, pCaptPath1. You can only render 1 bone group at a time, so this should match the group you are rendering with this material. 

pCaptData Attrib`pcaptdata`\- Much like pCaptPath Attrib. 

Skeleton Root Path`skelrootpath`\- Specifies the path to the COMP where the root of the skeleton is located. 

MAT`mat`\- When obtaining deform data from a MAT or a Deform In MAT, this is where that MAT is specified. 

## 

Parameters - Common Page

### 

Blending

[Blending](<./Blending.md> "Blending") is summing the color value of the pixel being drawn and the pixel currently present in the Color-Buffer. Blending is typically used to simulate [Transparency](<./Transparency.md> "Transparency"). The blending equation is:`Final Pixel Value = (Source Blend * Source Color) + (Dest Blend * Destination Color)`Blending (Transparency)`blending`\- This toggle enables and disables blending. However see the wiki article [Transparency](<./Transparency.md> "Transparency"). 

Blend Operation`blendop`\- ⊞ \- 
* Add`add`-
* Subtract`subtract`-
* Reverse Subtract`revsubtract`-
* Minimum`minimum`-
* Maximum`maximum`-


Source Color *`srcblend`\- ⊞ \- This value is multiplied by the color value of the pixel that is being written to the Color-Buffer (also know as the Source Color). 
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Source Alpha Saturate`sas`-
* One`one`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Destination Color *`destblend`\- ⊞ \- This value is multiplied by the color value of the pixel currently in the Color-Buffer (also known as the Destination Color). 
* One`one`-
* Src Color`scol`-
* One Minus Src Color`omscol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha Saturate`sas`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Separate Alpha Function`separatealphafunc`\- This toggle enables and disables separate blending options for the alpha values. 

Alpha Blend Operation`blendopa`\- ⊞ \- 
* Add`add`-
* Subtract`subtract`-
* Reverse Subtract`revsubtract`-
* Minimum`minimum`-
* Maximum`maximum`-


Source Alpha *`srcblenda`\- ⊞ \- This value is multiplied by the alpha value of the pixel that is being written to the Color-Buffer (also know as the Source Alpha). 
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Source Alpha Saturate`sas`-
* One`one`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Destination Alpha *`destblenda`\- ⊞ \- This value is multiplied by the alpha value of the pixel currently in the Color-Buffer (also known as the Destination Alpha). 
* One`one`-
* Src Color`scol`-
* One Minus Src Color`omscol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Zero`zero`-
* Dest Color`dcol`-
* One Minus Dest Color`omdcol`-
* Source Alpha Saturate`sas`-
* Constant Color`constantcol`-
* One Minus Constant Color`omconstantcol`-
* Constant Alpha`constanta`-
* One Minus Constant Alpha`omconstanta`-


Blend Constant Color`blendconstant`\- ⊞ \- 
* Blend Constant Color`blendconstantr`-
* Blend Constant Color`blendconstantg`-
* Blend Constant Color`blendconstantb`-


Blend Constant Alpha`blendconstanta`\- 

Legacy Alpha Behavior`legacyalphabehavior`\- 

Post-Mult Color by Alpha`postmultalpha`\- Multiplies the color by alpha after all other operations have taken place. 

Point Color Pre-Multiply`pointcolorpremult`\- ⊞ \- 
* Already Pre-Multiplied By Alpha`alreadypremult`-
* Pre-Multiply By Alpha in Shader`premultinshader`-


Depth Test`depthtest`\- Enables and disables the Depth-Test. If the depth-test is disabled, depths values aren't written to the Depth-Buffer. 

Depth Test Function`depthfunc`\- ⊞ \- The depth value of the pixel being drawn is compared to the depth value currently in the depth-buffer using this function. If the test passes then the pixel is drawn to the Frame-Buffer. If the test fails the pixel is discarded and no changes are made to the Frame-Buffer. 
* Less Than`less`-
* Less Than or Equal`lessorequal`-
* Equal`equal`-
* Greater Than`greater`-
* Greater Than or Equal`greaterorequal`-
* Not Equal`notequal`-
* Always`always`-

### 

Depth Test

Depth-Testing is comparing the depth value of the pixel being drawn with the pixel currently in the [Frame-Buffer](</index.php?title=Frame-Buffer&action=edit&redlink=1> "Frame-Buffer \(page does not exist\)"). A pixel that is determined to be in-front of the pixel currently in the Frame-Buffer will be drawn over it. Pixels that are determined to be behind the pixel currently in the Frame-Buffer will not be drawn. Depth-Testing allows geometry in a 3D scene to occlude geometry behind it, and be occluded by geometry in-front of it regardless of the order the geometry was drawn. 

For a more detailed description of Depth-Testing, refer to the [Depth-Test](<./Depth-Test.md> "Depth-Test") article. 

Write Depth Values`depthwriting`\- If Write Depth Values is on, pixels that pass the depth-test will write their depth value to the Depth-Buffer. If this isn't on then no changes will be made to the Depth-Buffer, regardless of if the pixels drawn pass or fail the depth-test. 

Discard Pixels Based on Alpha`alphatest`\- This enables or disables the pixel alpha test. 

Keep Pixels with Alpha`alphafunc`\- ⊞ \- This menu works in conjunction with the Alpha Threshold parameter below in determining which pixels to keep based on their alpha value. 
* Less Than`less`-
* Less Than or Equal`lessorequal`-
* Greater Than`greater`-
* Greater Than or Equal`greaterorequal`-


Alpha Threshold`alphathreshold`\- This value is what the pixel's alpha is compared to to determine if the pixel should be drawn. Pixels with alpha greater than the Alpha Threshold will be drawn. Pixels with alpha less than or equal to the Alpha Threshold will not be drawn. 

Wire Frame`wireframe`\- ⊞ \- Enables and disables wire-frame rendering with the option of OpenGL Tesselated or Topology based wireframes. 
* Off`off`-
* OpenGL Tesselated Wire Frame`tesselated`-
* Topology Wire Frame`topology`-

### 

Alpha Test

Alpha-testing allows you to choose to draw or not draw a pixel based on its alpha value. 

Line Width`wirewidth`\- This value is the width that the wires will be. This value is in pixels. 

Cull Face`cullface`\- ⊞ \- Selects which faces to render. 
* Use Render Setting`userender`\- Use the render settings found in the Render or Render Pass TOP.
* Neither`neither`\- Do not cull any faces, render everything.
* Back Faces`backfaces`\- Cull back faces, render front faces.
* Front Faces`frontfaces`\- Cull front faces, render back faces.
* Both Faces`bothfaces`\- Cull both faces, render nothing.


Polygon Depth Offset`polygonoffset`\- Turns on the polygon offset feature. 

Offset Factor`polygonoffsetfactor`\- 

Offset Units`polygonoffsetunits`\- 

### 

Wire Frame

The wire-frame feature will render the geometry as wire-frame, using the actual primitive type used in the render. What this means is surfaces like Metaballs, NURBs and Beziers will become a wire-frame of the triangles/triangle-strips used to render them (since these types of primitives can't be natively rendered in OpenGL). 

### 

Cull Face

The cull face parameter will cull faces from the render output. This can be used as an optimization or sometimes to remove artifacts. See [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling") for more infomation. 

### 

Polygon Depth Offset

This feature pushes the polygons back into space a tiny fraction. This is useful when you are rendering two polygons directly on-top of each other and are experiencing [Z-Fighting](<./Z-Fighting.md> "Z-Fighting"). Refer to [Polygon Depth Offset](<./Polygon_Depth_Offset.md> "Polygon Depth Offset") for more information. This is also an important feature when doing [shadows](<./Shadows.md> "Shadows"). 

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

Extra Information for the Depth MAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common MAT Info Channels

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


  
TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070

MATs   
---  
[Constant ](<./Constant_MAT.md> "Constant MAT")• [Experimental:Constant ](</Experimental:Constant_MAT> "Experimental:Constant MAT")• Depth • [GLSL ](<./GLSL_MAT.md> "GLSL MAT")• [Experimental:GLSL ](</Experimental:GLSL_MAT> "Experimental:GLSL MAT")• [In ](<./In_MAT.md> "In MAT")• [Line ](<./Line_MAT.md> "Line MAT")• [MAT ](<./MAT.md> "MAT")• [Experimental:MAT ](</Experimental:MAT> "Experimental:MAT")• [MAT Common Page ](<./MAT_Common_Page.md> "MAT Common Page")• [Null ](<./Null_MAT.md> "Null MAT")• [Out ](<./Out_MAT.md> "Out MAT")• [PBR ](<./PBR_MAT.md> "PBR MAT")• [Experimental:PBR ](</Experimental:PBR_MAT> "Experimental:PBR MAT")• [Phong ](<./Phong_MAT.md> "Phong MAT")• [Experimental:Phong ](</Experimental:Phong_MAT> "Experimental:Phong MAT")• [Point Sprite ](<./Point_Sprite_MAT.md> "Point Sprite MAT")• [Experimental:Point Sprite ](</Experimental:Point_Sprite_MAT> "Experimental:Point Sprite MAT")• [Select ](<./Select_MAT.md> "Select MAT")• [Switch ](<./Switch_MAT.md> "Switch MAT")• [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Wireframe ](<./Wireframe_MAT.md> "Wireframe MAT")
