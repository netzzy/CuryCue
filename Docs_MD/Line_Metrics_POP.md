# Line Metrics POP

##   
  
Summary

You can add metrics attributes to Line Strips. They can be created as point attribute or the vertex attributes. 

This gives good information about the points and the context they are in. For each point you can get the direction to the next and previous points, or the distance back to the start of the line strip, or the line strip number it is in… things useful for Math POPs or Lookup POPs. 

A convenience of the Line Metrics POP is to give nice values to awkward situations like co-incident points (two or more consecutive points in the same location), especially direction vectors. That’s what the Continuous Direction parameter does. It would work with Direction to Next, Direction to Previous, and do nice things to the Tangent vectors by keeping them in line. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[linemetricsPOP_Class](</LinemetricsPOP_Class> "LinemetricsPOP Class")

## 

Parameters - Neighbor Page

Attribute Class`attrclass`\- ⊞ \- Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable. 
* Point`point`-
* Vertex`vertex`-


Displacement to Next`dispnext`\- ⊞ \- Whether to output an attribute with the displacement to the next vertex in the line strip. 
* Displacement to Next`dispnext`-
* Displacement to Next Attrib Name`dispnextname`\- Specifies the attribute scope used to output the Displacement to Next attribute


Displacement to Previous`dispprev`\- ⊞ \- Whether to output an attribute with the displacement to the previous vertex in the line strip. 
* Displacement to Previous`dispprev`-
* Displacement to Previous Attrib Name`dispprevname`\- Specifies the attribute scope used to output the Displacement to Previous attribute


Distance to Next`distnext`\- ⊞ \- Whether to output an attribute with the distance to the next vertex in the line strip. 
* Distance to Next`distnext`-
* Distance to Next Attrib Name`distnextname`\- Specifies the attribute scope used to output the Distance to Next attribute


Distance to Previous`distprev`\- ⊞ \- Whether to output an attribute with the distance to the previous vertex in the line strip. 
* Distance to Previous`distprev`-
* Distance to Previous Attrib Name`distprevname`\- Specifies the attribute scope used to output the Distance to Previous attribute


Direction to Next`dirnext`\- ⊞ \- Whether to output an attribute with the direction to the next vertex in the line strip. 
* Direction to Next`dirnext`-
* Direction to Next Attrib Name`dirnextname`\- Specifies the attribute scope used to output the Direction to Next attribute


Direction to Previous`dirprev`\- ⊞ \- Whether to output an attribute with the direction to the previous vertex in the line strip. 
* Direction to Previous`dirprev`-
* Direction to Previous Attrib Name`dirprevname`\- Specifies the attribute scope used to output the Direction to Previous attribute


Tangent`tangent`\- ⊞ \- Output a tangent attribute for each point. 
* Tangent`tangent`-
* Tangent Attrib Name`tangentname`\- Attribute scope for the tangent.


Curvature`curvature`\- ⊞ \- Whether to output an attribute containing the curvature. 
* Curvature`curvature`-
* Curvature Attrib Name`curvaturename`\- Sets the attribute scope when computing curvature


Angle per Distance`angleperdist`\- ⊞ \- Whether to output Angle per Distance. 
* Angle per Distance`angleperdist`-
* Angle per Distance Attrib Name`angleperdistname`\- Attribute Name for Angle per Distance.


Continuous Direction`continuousdir`\- Enable returning continuous directions for co-incident points 

Max Neighbors`maxneighbors`\- When computing Direction vector, how far to look when points are in same position as next or previous points. 

## 

Parameters - Line Strip Page

Distance from Start`diststart`\- ⊞ \- Whether to output an attribute with the distance from the start of the line strip. 
* Distance from Start`diststart`-
* Distance from Start Attrib Name`diststartname`\- Specifies the attribute scope used to output the Distance from Start attribute


Distance from End`distend`\- ⊞ \- Whether to output an attribute with the distance from the end of the line strip. 
* Distance from End`distend`-
* Distance from End Attrib Name`distendname`\- Specifies the attribute scope used to output the Distance from End attribute


Distance from Start Normalized`diststartnorm`\- ⊞ \- Whether to output an attribute with the normalized distance from the start of the line strip. 
* Distance from Start Normalized`diststartnorm`-
* Distance from Start Normalized Attrib Name`diststartnormname`\- Specifies the attribute scope used to output the Distance from Start Normalized attribute


Distance from End Normalized`distendnorm`\- ⊞ \- Whether to output an attribute with the normalized distance from the end of the line strip. 
* Distance from End Normalized`distendnorm`-
* Distance from End Normalized Attrib Name`distendnormname`\- Specifies the attribute scope used to output the Distance from End Normalized attribute


Line Strip Length`primlen`\- ⊞ \- Enable addition of line strip length attribute. 
* Line Strip Length`primlen`-
* Line Strip Length Attrib Name`primlenname`\- Name of the attribute for the line strip length.


Length Attrib Primitive Attribute`primlenprim`\- When on, the attribute created for the length of the line strip is a primitive attribute. 

## 

Parameters - Index Page

Vert Index in Line Strip`pointindex`\- ⊞ \- Output the vertex index for each point, assuming unique. 
* Vert Index in Line Strip`pointindex`-
* Vert Index Attrib Name`pointindexname`\- The name of the vertex index attribute.


Number of Verts in Line Strip`numverts`\- ⊞ \- Outputs attribute for number of vertices in current point's like strip. 
* Number of Verts in Line Strip`numverts`-
* Number of Verts Attrib Name`numvertsname`\- Name for the Number of Verts in Line Strip attribute.


Vert Index in Line Strip Normalized`vertindexnorm`\- ⊞ \- Output the vertex index normalized to 0-1 for each point, assuming unique. 
* Vert Index in Line Strip Normalized`vertindexnorm`-
* Vert Index Normalized Attrib Name`vertindexnormname`\- The name of the vertex index normalized attribute.


Line Strip Index`linestripindex`\- ⊞ \- Enable addition of line strip index attribute. 
* Line Strip Index`linestripindex`-
* Line Strip Index Attrib Name`linestripindexname`\- Attribute name for the index of the line strip.


Line Strip Index Normalized`lsindexnorm`\- ⊞ \- Enable addition of normalized line strip index attribute. 
* Line Strip Index Normalized`lsindexnorm`-
* Line Strip Index Normalized Attrib Name`lsindexnormname`\- Attribute name for the normalized index of the line strip.

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

Extra Information for the Line Metrics POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• Line Metrics • [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
