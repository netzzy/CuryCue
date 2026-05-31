# Switch MAT

##   
  
Summary

The Switch MAT allows you to switch between multiple materials. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[switchMAT_Class](</SwitchMAT_Class> "SwitchMAT Class")

## 

Parameters - Switch Page

Index`index`\- Selects which input to use. The first input is 0. 

Extend`extend`\- ⊞ \- Determines extend behaviour when index is out of range. Allows negative indices. 
* Clamp`clamp`-
* Loop`loop`-
* ZigZag`zigzag`-

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

[Blending](<./Blending.md> "Blending") is summing the color value of the pixel being drawn and the pixel currently present in the Color-Buffer. Blending is typically used to simulate [Transparency](<./Transparency.md> "Transparency"). The blending equation is: Final Pixel Value = (Source Blend * Source Color) + (Dest Blend * Destination Color) 

Blending(Transparency)`blending`\- This toggle enables and disables blending. However see the wiki article [Transparency](<./Transparency.md> "Transparency"). 

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


Destination Color *`destblend`\- ⊞ \- This value is multiplied by the color value of the pixel currently in the Color-Buffer (also known as the Destination Color). 
* One`one`-
* Src Color`scol`-
* One Minus Src Color`omscol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Zero`zero`-


Separate Alpha Function`separatealphafunc`\- This toggle enables and disables separate blending options for the alpha values. 

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


Destination Alpha *`destblenda`\- ⊞ \- This value is multiplied by the alpha value of the pixel currently in the Color-Buffer (also known as the Destination Alpha). 
* One`one`-
* Src Color`scol`-
* One Minus Src Color`omscol`-
* Source Alpha`sa`-
* One Minus Source Alpha`omsa`-
* Dest Alpha`da`-
* One Minus Dest Alpha`omda`-
* Zero`zero`-

### 

Depth Test

Depth-Testing is comparing the depth value of the pixel being drawn with the pixel currently in the [Frame-Buffer](</index.php?title=Frame-Buffer&action=edit&redlink=1> "Frame-Buffer \(page does not exist\)"). A pixel that is determined to be in-front of the pixel currently in the Frame-Buffer will be drawn over it. Pixels that are determined to be behind the pixel currently in the Frame-Buffer will not be drawn. Depth-Testing allows geometry in a 3D scene to occlude geometry behind it, and be occluded by geometry in-front of it regardless of the order the geometry was drawn. 

For a more detailed description of Depth-Testing, refer to the [Depth-Test](<./Depth-Test.md> "Depth-Test") article. 

Depth Test`depthtest`\- Enables and disables the Depth-Test. If the depth-test is disabled, depths values aren't written to the Depth-Buffer. 

Depth Test Function`depthfunc`\- ⊞ \- The depth value of the pixel being drawn is compared to the depth value currently in the depth-buffer using this function. If the test passes then the pixel is drawn to the Frame-Buffer. If the test fails the pixel is discarded and no changes are made to the Frame-Buffer. 
* Less Than`less`-
* Less Than or Equal`lessorequal`-
* Equal`equal`-
* Greater Than`greater`-
* Greater Than or Equal`greaterorequal`-
* Not Equal`notequal`-
* Always`always`-


Write Depth Values`depthwriting`\- If Write Depth Values is on, pixels that pass the depth-test will write their depth value to the Depth-Buffer. If this isn't on then no changes will be made to the Depth-Buffer, regardless of if the pixels drawn pass or fail the depth-test. 

### 

Alpha Test

Alpha-testing allows you to choose to draw or not draw a pixel based on its alpha value. 

Discard Pixels Based on Alpha`alphatest`\- This enables or disables the pixel alpha test. 

Keep Pixels with Alpha`alphafunc`\- ⊞ \- This menu works in conjunction with the Alpha Threshold parameter below in determining which pixels to keep based on their alpha value. 
* Less Than`less`-
* Less Than or Equal`lessorequal`-
* Greater Than`greater`-
* Greater Than or Equal`greaterorequal`-


Alpha Threshold`alphathreshold`\- This value is what the pixel's alpha is compared to to determine if the pixel should be drawn. Pixels with alpha greater than the Alpha Threshold will be drawn. Pixels with alpha less than or equal to the Alpha Threshold will not be drawn. 

### 

Wire Frame

The wire-frame feature will render the geometry as wire-frame, using the actual primitive type used in the render. What this means is surfaces like Metaballs, NURBs and Beziers will become a wire-frame of the triangles/triangle-strips used to render them (since these types of primitives can't be natively rendered in OpenGL). 

Wire Frame`wireframe`\- ⊞ \- Enables and disables wire-frame rendering with the option of OpenGL Tesselated or Topology based wireframes. 
* Off`off`-
* OpenGL Tesselated Wire Frame`tesselated`-
* Topology Wire Frame`topology`-


Line Width`wirewidth`\- This value is the width that the wires will be. This value is in pixels. 

### 

Cull Face

The cull face parameter will cull faces from the render output. This can be used as an optimization or sometimes to remove artifacts. See [Back-Face Culling](<./Back-Face_Culling.md> "Back-Face Culling") for more infomation. 

Cull Face`cullface`\- ⊞ \- Selects which faces to render. 
* Use Render Setting`userender`\- Use the render settings found in the Render or Render Pass TOP.
* Neither`neither`\- Do not cull any faces, render everything.
* Back Faces`backfaces`\- Cull back faces, render front faces.
* Front Faces`frontfaces`\- Cull front faces, render back faces.
* Both Faces`bothfaces`\- Cull both faces, render nothing.

### 

Polygon Depth Offset

This feature pushes the polygons back into space a tiny fraction. This is useful when you are rendering two polygons directly on-top of each other and are experiencing [Z-Fighting](<./Z-Fighting.md> "Z-Fighting"). Refer to [Polygon Depth Offset](<./Polygon_Depth_Offset.md> "Polygon Depth Offset") for more information. This is also an important feature when doing [shadows](<./Shadows.md> "Shadows"). 

Polygon Depth Offset`polygonoffset`\- Turns on the polygon offset feature. 

Offset Factor`polygonoffsetfactor`\- 

Offset Units`polygonoffsetunits`\- 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Switch MAT can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070

MATs   
---  
[Constant ](<./Constant_MAT.md> "Constant MAT")• [Depth ](<./Depth_MAT.md> "Depth MAT")• [GLSL ](<./GLSL_MAT.md> "GLSL MAT")• [In ](<./In_MAT.md> "In MAT")• [Line ](<./Line_MAT.md> "Line MAT")• [MAT ](<./MAT.md> "MAT")• [MAT Common Page ](<./MAT_Common_Page.md> "MAT Common Page")• [Null ](<./Null_MAT.md> "Null MAT")• [Out ](<./Out_MAT.md> "Out MAT")• [PBR ](<./PBR_MAT.md> "PBR MAT")• [Phong ](<./Phong_MAT.md> "Phong MAT")• [Point Sprite ](<./Point_Sprite_MAT.md> "Point Sprite MAT")• [Select ](<./Select_MAT.md> "Select MAT")• Switch • [Texture Sampling Parameters ](<./Texture_Sampling_Parameters.md> "Texture Sampling Parameters")• [Wireframe ](<./Wireframe_MAT.md> "Wireframe MAT")
