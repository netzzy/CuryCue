# Neighbor POP

## 

Summary

The Neighbor POP uses the`P`attribute to find, for each point of the input, the closest points to it. It puts the indexes of the closest points in an array attribute`Nebr`. You specify the max number of neighbors, and you choose the Max Neighbors Distance to look for neighbors. 

The size of the attribute`Nebr`is the Max Neighbors parameter. If fewer than that number is found, it puts a special number`4294967295`as the value for the neighbor index. The attribute`NumNebrs`holds the number of neighbors found for each point. 

You can output the average distance to the found neighbors, optionally including the point's position. Alternately you can output the Inverse Distance Weighted Average, where the closest points have the highest influence on the average. 

Instead of outputting the indexes of the neighbors, you can output any set of attributes of the neighbors (careful, this can produce a lot of data). 

An alternate form of the Neighbor POP takes a second input, where the each point of the first input is compared to points of the second input. 

Neighbors are determined by distance between points, but via the Neighbors Type menu, they can also be determined by connectivity along any primitive connecting edges to neighboring points (only one step currently). For example, two points adjacent to each other in a line strip or quad are neighbors of each other. 

( Distribution - Default, Unique, Closest ) 

Internally it is using a unbounded spatial hashing algorithm nad put into one of Num Hash Buckets. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[neighborPOP_Class](</NeighborPOP_Class> "NeighborPOP Class")

## 

Parameters - Neighbor Page

Neighbors Type`nebrtype`\- ⊞ \- When checking for neighbors, choose to use edge connectivity or only distance to neighbor points. 
* By Distance`distance`-
* Connected`connected`-


Max Neighbors Distance`maxdistance`\- Specifies the distance below which a point is considered a neighbor of the current point. 

Distribution`distribution`\- ⊞ \- Determines what kind of neighbor sets are returned. 
* Default`default`-
* Unique`unique`-
* Closest`closest`-


Num Hash Buckets`numhashbuckets`\- The number of buckets the points will be sorted in based on their position. A good heuristic is to choose it to be close to the number of points. 

Output Hash Attrib`outputhash`\- Whether to output an attribute with the Spatial Hash values, which can be useful to debug and optimize performance. 

Output`nebroutput`\- ⊞ \- Whether to output the individual neighbors and their attributes in array attributes, or their average or distance weighted average. 
* Neighbors`nebr`-
* Average`avg`-
* Inverse Distance Weighted Average`weightedavg`-


Max Neighbors`maxneighbors`\- Specifies the max number of neighbors. This sets the array size of all the attributes storing neighbors information. 

Neighbors`nebrs`\- ⊞ \- Enable addition of the neighbors attribute. 
* Neighbors`nebrs`-
* Neighbor Attr Name`nebrattrname`\- Name for the attribute containing the point indices of the neighbors.


Num Neighbors`numnebrs`\- ⊞ \- Enable the addition of the number of neighbors attribute. 
* Num Neighbors`numnebrs`-
* Num Neighbors Attr Name`numnbrsattrname`\- The attribute name for the number of neighbors.


Add Distance Attribute`dodist`\- ⊞ \- Whether to output an attribute containing the distance to the query point. 
* Add Distance Attribute`dodist`-
* Distance Attribute Name`distattrname`\- Specifies the scope of the attribute that stores the distance values


Max Neighbors for Average`maxnebrsavg`\- Specifies the max number of neighbors considered when averaging neighbor attributes. 

Include Query Point`incquerypt`\- When on, includes the query point when calculating average when output is average. 

Add Prefix`addprefix`\- Whether to add Nebr prefix when outputting neighbor attributes. 

Cast Integers to Floats`castintstofloats`\- When averaging the neighbor attribute values, whether to cast integer attributes to float. 

Neighbor Point Attributes`nebrptattrs`\- ⊞ \- Creates array attributes the size of max neighbors with the neighbor attributes for each point in the first input. 
* *`*`-

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Neighbor POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• Neighbor • [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
