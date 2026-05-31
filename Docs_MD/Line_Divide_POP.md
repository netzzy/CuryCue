# Line Divide POP

##   
  
Summary

The Line Divide POP takes any set of line strips, and for each it generates a new line strip that is subdivided using various interpolation methods. The default is linear interpolation with 4 divisions between incoming points. 

You can choose the Interpolation Method, the default being Linear interpolation, but you can also choose spline types like Cardinal, BSpline, Beziers and Quadratic. With the spline types, it can use incoming attributes (like those set in the [Line POP](<./Line_POP.md> "Line POP")) that specify the spline properties like`Weight`, tangents (`TanIn`and`TanOut`), tangent constraints (`TanInConstraint`) and/or tension. It will also interpret an interpolation method per-point if a`SegMethod`attribute exists. 

There are two stages of doing divisions, The first stage allows setting the total divisions for the line strip, or divisions per-segment, dividing by distance along the curves, or by curvature of the line strip. It interpolates all the attributes. 

The second stage lets you further re-sample the line strip with one of three methods: Divisions per Line Strip, Distance between Points, or Points as Keyframes. 

Points as Keyframes interpolates by treating one attribute as an independent variable (like`Time`, or`U`), like a`y = f(x)`mathematical function. (For example, if you have an attribute`Time`on the points, you can resample curves at equal steps of time, assuming you curves express values over time.) 

NOTE: The Maximum Number of Vertices parameter is required because it is not known on the GPU how many points you will end up with, and the GPU needs to pre-allocate enough memory to do the job. Oherwise line strips will be truncated. 

To add: distinguish the different beziers, explain`TanInConstraint`.`ControlPoint`attribute (laser) 

See also [Line POP](<./Line_POP.md> "Line POP"), [Curve POP](<./Curve_POP.md> "Curve POP"), [Point POP](<./Point_POP.md> "Point POP"), [Primitive POP](<./Primitive_POP.md> "Primitive POP"), [Pattern POP](<./Pattern_POP.md> "Pattern POP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[linedividePOP_Class](</LinedividePOP_Class> "LinedividePOP Class")

## 

Parameters - Divide Page

Divisions Method`divmethod`\- ⊞ \- The method to apply the divisions. 
* None`none`-
* Divisions per Line Strip`linestrip`-
* Divisions per Segment`segment`-
* Distance between Points`dist`-
* Distance by Curvature`curvature`-


Divisions`divs`\- The number of divisions. 

Min Distance`mindist`\- The minimum distance between points in the output line strips. 

Max Distance`maxdist`\- Divide the line so there are no two adjacent points farther apart than this distance - max distance between points. 

Min Max Bias`minmaxbias`\- Bias of point creation - more near the minimum or more near the maximum distance. 

By Edge`byedge`\- When dividing using the distance between points, whether to restart at each segment (edge). 

Add ControlPoint Attribute`addctrlpointattr`\- Whether to output a ControlPoint attribute set to 1 for control points. 

Maximum Number of Vertices`maxverts`\- Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory. 

## 

Parameters - Interpolate Page

Interpolation Method per Segment`interpmethodpersegment`\- ⊞ \- When toggle is on, it uses a separate interpolation method for each segment in the input line strips. 
* Interpolation Method per Segment`interpmethodpersegment`-
* Segment Method Attribute`segmethodattr`\- Attribute scope for the segment method index.


Interpolation Method`interpmethod`\- ⊞ \- Method to use for interpolation. 
* Linear`linear`-
* Cardinal (Interpolating)`cardinal`-
* BSpline`bspline`-
* Cubic Bezier With Tangents`cubicbeziertang`-
* Cubic Bezier`cubicbezier`-
* Quadratic Bezier`quadraticbezier`-


Weight Attribute`useweight`\- ⊞ \- When on, the points will have a weight attribute affecting the tightness of the curve around the point. 
* Weight Attribute`useweight`-
* Weight Attribute Name`weightattr`\- Specifies the scope of the attribute that stores weight values


In Tangent Attribute`usetanin`\- ⊞ \- When on, the points will have a attribute to be the tangent going into the point. 
* In Tangent Attribute`usetanin`-
* In Tangent Attribute Name`taninattr`\- Name of the incoming tangent attribute.


Out Tangent Attribute`usetanout`\- ⊞ \- When on, the points will have a attribute to be the tangent going out of the point. 
* Out Tangent Attribute`usetanout`-
* Out Tangent Attribute Name`tanoutattr`\- Name of the output tangent attribute.


In Tangent Constraint Attribute`usetaninconst`\- ⊞ \- When on, the points will have an attribute to be constraints of a curve at that point.. 
* In Tangent Constraint Attribute`usetaninconst`-
* In Tangent Constraint Attribute Name`taninconstattr`\- Name of the in tangent constraint attribute.


Clamped`clamped`\- When using Cardinal or BSpline interpolation, whether to duplicate the start and end control points so the resulting curve start and end at the control points. Only has an effect on open line strips. 

Tension`tension`\- Controls how tightly the cardinal line strip bends through the control points 

## 

Parameters - Resample Page

Post-Resample Method`resamplemethod`\- ⊞ \- Resampling method used after division. 
* None`none`-
* Divisions per Line Strip`linestrip`-
* Distance between Points`dist`-
* Points as Keyframes`keyframes`-


Divisions`resampledivs`\- The number of divisions. 

Independant Variable Attribute`indvarattr`\- Attribute to use as the independent variable. 

Independant Variable Step`indvarstep`\- Step size to use for the independent variable, usually a fraction of the independent variable range. 

Maximum Number of Vertices`resamplemaxverts`\- Sets the number of vertices to be allocated. It should be bigger than the actual number of vertices created (visible in info popup). More vertices allocated use more GPU memory. 

Max Tries for Binary Search`maxtries`\- Max number of iterations for binary search when linearly resampling. 

Remove Unused Points`rmvunusedpts`\- Removes unused points not referenced by primitives. 

Max Distance`resamplemaxdist`\- Maximum Distance between Points 

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

Extra Information for the Line Divide POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• Line Divide • [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
