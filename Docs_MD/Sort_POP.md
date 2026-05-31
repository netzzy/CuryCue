# Sort POP

##   
  
Summary

The Sort POP sorts the point list and/or the primitive list based on the position`P`or any attribute component. When sorting by`P`it can sort the points relative to a vector, or proximity to a point, or relative to a Geometry COMP's Z axis. 

The Sort POP can also randomize the point order, or shift the point order (circularly in the point list, like first point becomes the second point and the last point becomes the first). 

It can do the same operations to primitives. 

It implements <https://gpuopen.com/fidelityfx-parallel-sort/>

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[sortPOP_Class](</SortPOP_Class> "SortPOP Class")

## 

Parameters - Point Page

Point Method`ptmethod`\- ⊞ \- Point sorting criteria. 
* No Change`none`-
* By Attribute`byattrib`-
* Random`seed`-
* Proximity to Point`prox`-
* Along Vector`vector`-
* Relative to Object Z-axis`object`-


Attribute`pointattr`\- Attribute to use for sorting. 

Attrib is UInt`pointuint`\- ⊞ \- When sorting by attribute, allows to specify whether the attribute is an unsigned integer and what the max value is. Smaller max UInt require fewer passes to sort. 
* Not UInt Attrib`notuint`-
* 4 bits UInt (max 16)`uint4`-
* 8 bits UInt (max 256)`uint8`-
* 12 bits UInt (max 4096)`uint12`-
* 16 bits UInt (max 65,536)`uint16`-
* 20 bits UInt (max 1 M)`uint20`-
* 24 bits UInt (max 16 M)`uint24`-
* 28 bits UInt (max 268 M)`uint28`-
* 32 bits UInt (max 4 B)`uint32`-


Seed`pointseed`\- Seed for random number generator for randomly-ordered points. 

Point`pointprox`\- ⊞ \- Proximity Point. 
* Point`pointproxx`-
* Point`pointproxy`-
* Point`pointproxz`-


Vector`pointdir`\- ⊞ \- When sorting points Along Vector, it takes the point position, finds the the closest point on a line through 0,0,0 in the direction of the vector, and then sorts along that line. 
* Vector`pointdirx`-
* Vector`pointdiry`-
* Vector`pointdirz`-


Object`pointobj`\- 3D Object to use when sorting points relative to Object Z-axis. 

Reverse`pointrev`\- After sorting points, reverse their order. 

Shift`pointshift`\- Enables offsetting on sorted points. 

Offset`pointoffset`\- Shifts the point order by this offset. 

## 

Parameters - Primitive Page

Primitive Method`primmethod`\- ⊞ \- Primitive sorting criteria. 
* No Change`none`-
* By Point Attribute`byptattrib`-
* By Primitive Attribute`byprimattrib`-
* Random`seed`-
* Proximity to Point`prox`-
* Along Vector`vector`-
* Relative to Object Z-axis`object`-


Attribute`primattr`\- Attribute to use for sorting. 

Attrib is UInt`primuint`\- ⊞ \- When sorting by attribute, allows to specify whether the attribute is an unsigned integer and what the max value is. Smaller max UInt require fewer passes to sort. 
* Not UInt Attrib`notuint`-
* 4 bits UInt (max 16)`uint4`-
* 8 bits UInt (max 256)`uint8`-
* 12 bits UInt (max 4096)`uint12`-
* 16 bits UInt (max 65,536)`uint16`-
* 20 bits UInt (max 1 M)`uint20`-
* 24 bits UInt (max 16 M)`uint24`-
* 28 bits UInt (max 268 M)`uint28`-
* 32 bits UInt (max 4 B)`uint32`-


Seed`primseed`\- Seed for primitive ranomizer. 

Point`primprox`\- ⊞ \- Position when sorting by proximity to point. 
* Point`primproxx`-
* Point`primproxy`-
* Point`primproxz`-


Vector`primdir`\- ⊞ \- When sorting primitives Along Vector, it takes the center of the primitive, finds the closest point on a line through 0,0,0 in the direction of the vector, and then sorts along that line. 
* Vector`primdirx`-
* Vector`primdiry`-
* Vector`primdirz`-


Object`primobj`\- 3D Object to use when sorting primitives relative to Object Z-axis. 

Reverse`primrev`\- Reverse the order of primitives. 

Shift`primshift`\- Enables offsetting on sorted primitives. 

Offset`primoffset`\- Shifts the primitive order by this offset. 

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Sort POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• Sort • [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
