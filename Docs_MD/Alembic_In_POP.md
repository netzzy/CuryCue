# Alembic In POP

## 

Summary

The Alembic In POP loads and plays back [Alembic](<http://www.alembic.io/>) file geometry sequences. 

The supported Alembic primitives are polymesh, curves, and points for geometry. As well, Alembic transformations are supported. 

Polymesh primitives are imported as triangles or quads for faces of 3 or 4 vertices respectively, and as a close lined strip for faces with greater than 4 vertices. 

For Alembic files that contain animation, use the Time parameter and pay attention to the Unit menu to control it in frames, seconds, or whatever you like. 

An Alembic archive may contain one or more object paths for one or multiple geometries. It is possible to view these objects all at once or select them separately using the 'Object Path' parameter menu. If separate selected objects contain duplicate attributes (ie. sharing a name) but associated with a different attribute class (eg. vertex vs. point), then the duplicate attribute will be converted to a vertex attribute. 

Each object in an Alembic file schema may possess standard or custom attributes. The standard attributes are normal (`N`), velocity (`V`), and texture coordinates (`Tex`). Multiple custom attributes may live in an Alembic schema with more flexible names and types. Most Alembic attributes are supported but not all convert one-to-one into a POP format: 
* 16-bit int attributes (eg. Int16, V2s, P3s, etc.) are converted to 32-bit int.
  * 64-bit attributes (eg. Uint64, Int64, V2d, etc.) are converted to double, which is the only 64-bit attribute that POPs currently support.
  * Attributes with > 4 components (eg. Box3f, M33f, M44f etc.) are packed as an array of vec4's. If there is an array of these attributes then they will be packed together back-to-back. Eg. M44f has 16 components and will be imported as float4[4], and M44f[2] will be imported as float4[8] with M44f[0] first followed by M44f[1].


List of **unsupported** attributes: 
* String/WString
  * 8-bit and 16-bit float color
  * Bool
  * UChar/Char


The conversion between the Alembic geometries scopes to the TouchDesigner attributes types are shown in the table below:   
  
---  
**Alembic Scope** | **TouchDesigner Attribute**  
Varying, Vertex | Point  
Facevarying | Vertex  
Uniform, Constant | Primitive  
  
[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[alembicPOP_Class](<./AlembicPOP_Class.md> "AlembicPOP Class")

## 

Parameters - Alembic Page

Alembic File`file`\- The file path to the Alembic file. 

Object Path`objectpath`\- ⊞ \- Specify which geometry object to be loaded. Each geometry object can represent a hierarchies of multiple geometries. It is also possible to choose the "All Objects" (ie. "*") option from the list of available objects. This option is selected by default. 
* *`*`-
* /box_object1/color1`/box_object1/color1`-


Transform`xform`\- ⊞ \- Select which transform is applied if the transform data is available from the input Alembic file. 
* None`none`\- No transformation is applied to the geometry(s), they reside at the origin.
* Static Local Transformation`staticlocalxform`\- Applies the static local transformation for the selected geometry objects from the Object Path.
* Static World Transformation`staticworldxform`\- Applies the static world transformation of the selected geometry objects from the Object Path up to their parents transformation.
* Dynamic Transformation`dynamicxform`\- In the case that the Alembic file includes dynamic or animated geometries the transformation is applied to the selected geometries. This option performs both local and world transformation (if available) for the given geometry.


Time`time`\- ⊞ \- Specify which part of the Alembic samples sequence is loaded. The time unit menu converts the current time units to the selected unit. The available options are Frames, Seconds, Indices, and Fraction. 
* Time`time`\- Specify which part of the Alembic samples sequence is loaded.
* Time Unit`timeunit`\- The time unit menu converts the current time units to the selected unit. The available options are Frames, Seconds, Indices, and Fraction.


FPS`fps`\- Specify the rate used for sample calculation for reading from the Alembic file. 

Interpolation`interp`\- ⊞ \- Interpolate between the samples/keyframes in the Alembic file. This parameter only works if the selected geometries are defined as dynamic and the transformation information are available from the input Alembic file. 
* None`none`\- No interpolation is performed between each samples.
* Linear Interpolation`interp`\- Smooth interpolation between each two samples is calculated.


Unload`loadfile`\- Toggling the unload to "on" will unload the file and close it. By setting it to "off", the file will be loaded again. When the file is unloaded it can be overwritten by other applications or deleted. 

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Info CHOP Channels

Extra Information for the Alembic In POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• Alembic In • [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
