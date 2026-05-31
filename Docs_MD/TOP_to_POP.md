# TOP to POP

##   
  
Summary

Position and Active is a shortcut for P in RGB, and alpha is set to 1 for active pixels (pixels with a valid attribute value). 

Using Custom you specify which attribute and components you want in the RGBA of the TOP, so max 4 could be`P(0) Color(2) N(1) P(2)`. 

When you Use Dimension all pixels are active since the resolution matches the TOP When using the other modes you can end up with unused pixels (you have 40 points, fit to square gives you 7x7, so you end up with 9 unused pixels), alpha is only set to 1 for used pixels. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[toptoPOP_Class](<./ToptoPOP_Class.md> "ToptoPOP Class")

## 

Parameters - Inputs Page

First RGBA Contains`rgba`\- ⊞ \- Determines how the TOP's pixels should be interpreted. 
* Color (RGBA)`color`-
* Position and Active (RGBA)`pactive`-
* Position (RGB)`pos`-
* Depth`depth`-
* Height (R)`height`-
* Custom`custom`-


Max Number of Points`maxpointsenable`\- ⊞ \- Enable the setting of the max number of points when First RGBA Contains is set to Position. 
* Max Number of Points`maxpointsenable`-
* Number of Points`maxpoints`\- Sets the max number of points when the automatic max number of points is overriden.


TOP`input`\- Start of Sequential Parameter Blocks for TOPs to convert. 

TOP`input0top`\- Sets reference to a TOP to convert. 

Channel Scope`input0chanscope`\- ⊞ \- Color channels to sample. 
* r`r`-
* g`g`-
* b`b`-
* a`a`-


Attribute Scope`input0attrscope`\- ⊞ \- A list of attributes to be created according to the channel scope. 
* P`P`-
* P.i01`P.i01`-


Filter`input0filter`\- ⊞ \- The TOP pixel filtering. 
* Nearest Pixel`nearest`-
* Interpolate Pixels`linear`-
* High Quality Resize`highquality`-


New Attribute`attr`\- Start of Sequential Parameter Blocks to create new attributes. 

New Attribute Name`attr0name`\- ⊞ \- Choose to create a predefined attribute or a custom attribute. 
* New Attribute Name`attr0name`-
* Custom Name`attr0customname`\- The name of the new cutom attribute.


Attribute Type`attr0type`\- ⊞ \- Determines the type. 
* Attribute Type`attr0type`-
* Components`attr0numcomps`\- The number of components in the new custom attribute.


Default Value`attr0defaultval`\- ⊞ \- The value of the new custom attribute if it cannot be computed. 
* Default Value`attr0defaultval0`-
* Default Value`attr0defaultval1`-
* Default Value`attr0defaultval2`-
* Default Value`attr0defaultval3`-

## 

Parameters - Detail Page

Connectivity`surftype`\- ⊞ \- Determines the primitive used to connect the points. 
* None`none`-
* Point Primitives`points`-
* Lines`lines`-
* Line Strips`linestrips`-
* Triangles`triangles`-
* Alternating Triangles`alttriangles`-
* Quadrilaterals`quads`-


Line X/Y/Z`line`\- ⊞ \- Specifies whether to enable Lines in the X/Y/Z axis. 
* Line X/Y/Z`linex`-
* Line X/Y/Z`liney`-
* Line X/Y/Z`linez`-


Plane XY/YZ/ZX`plane`\- ⊞ \- Plane orientation. 
* Plane XY/YZ/ZX`planex`-
* Plane XY/YZ/ZX`planey`-
* Plane XY/YZ/ZX`planez`-


Unique Points`uniquepoints`\- Enable not sharing points between primitives. 

Center`t`\- ⊞ \- The center of the output geometry. 
* Center`tx`-
* Center`ty`-
* Center`tz`-


Override Size`overridesize`\- ⊞ \- When on, overrides the automatic size, which is 1 in X with the size in Y respecting the input TOP aspect ratio. 
* Override Size`overridesizex`-
* Override Size`overridesizey`-
* Override Size`overridesizez`-


Size`size`\- ⊞ \- The geometry 3D size. 
* Size`sizex`-
* Size`sizey`-
* Size`sizez`-


Override Resolution`overrideres`\- ⊞ \- When on, overrides the automatic resolution, which is the input TOP resolution. 
* Override Resolution`overrideresx`-
* Override Resolution`overrideresy`-
* Override Resolution`overrideresz`-


Resolution`res`\- ⊞ \- Overriden resolution. 
* Resolution`resx`-
* Resolution`resy`-
* Resolution`resz`-


Pixel Sampling Location`pixelsamplingloc`\- ⊞ \- Sets where the pixels are sampled. 
* Edge to Edge`edgetoedge`-
* Pixel Centered`pixelcentered`-


Texture Coordinates`texture`\- ⊞ \- Sets the attribute class where the texture coordinates should be created. 
* None`none`-
* Point`point`-
* Vertex`vert`-


Append Dimension`dimension`\- ⊞ \- Always add a dimension, or only add a dimesion when its size is 2 or more. 
* When Rows Cols Slices > 1`morethanone`-
* Always for Rows Cols`rowscolsalways`-
* Always for Rows Cols Slices`rowscolsslicesalways`-

## 

Parameters - Depth Page

Rerange from Low High`rerangefromlow`\- ⊞ \- Range for input values. 
* Rerange from Low High`rerangefromlow`-
* Rerange from High`rerangefromhigh`-


Rerange to Low High`rerangetolow`\- ⊞ \- Range for output values. 
* Rerange to Low High`rerangetolow`-
* Rerange to High`rerangetohigh`-


Camera`camera`\- Specify the camera component. 

Override Camera View`overridecamera`\- When on, overrides the View settings from the selected camera object. 

View Angle Method`viewanglemethod`\- ⊞ \- Sets the method to convert the depth TOP. 
* Horizontal FOV`horfov`-
* Vertical FOV`vertfov`-
* Focal Lengths`focallengths`\- Determines the camera's focal lengths.


FOV Angle`fov`\- Determines the camera's field of view angle. 

Focal Length (Fx, Fy)`focallengths`\- ⊞ \- 
* Focal Length (Fx, Fy)`focallengthsx`-
* Focal Length (Fx, Fy)`focallengthsy`-


Optical Center (Cx, Cy)`center`\- ⊞ \- The location of the center of the camera for the depth projection. 
* Optical Center (Cx, Cy)`centerx`-
* Optical Center (Cx, Cy)`centery`-


Delete Near Points`deletenear`\- Enable removal of points that are close to the camera. 

Near Depth`depthnear`\- Depth of the near clipping plane. 

Delete Far Points`deletefar`\- Enable removal of points that are far from the camera. 

Far Depth`depthfar`\- Depth of the far clipping plane. 

Line Strip Behavior`linestripbehavior`\- ⊞ \- What to do when points of a line strip are deleted. 
* Delete Point of Line Strip`delpointoflinestrip`-
* Split Line Strip`splitlinestrip`-
* Delete Line Strip`dellinestrip`-

## 

Parameters - Height Page

Displacement Scale`dispscale`\- Sets the displacement scale when the pixels are interpreted as heights values 

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

Extra Information for the TOP to POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• TOP to • [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
