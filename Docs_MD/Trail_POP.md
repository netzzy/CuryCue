# Trail POP

##   
  
Summary

The Trail POP captures and retains all the points of the input for the most recent N frames or N "slices", being a time-history of the input's points. It then optionally creates primitives that connects the points in various ways. 

If the number of points of the input is the same for all the slices, then it can easily skin points together using the Connectivity menu, such as maling a line strip for each point over time. 

If the number of points is changing per-frame, as it would with a particle system, it can still connect time-related dots by using an`Id`attribute on the points, and making sure the Id of a particle stays the same through its life. You can select which attribute it co-relates to using the Match by Attribute parameter. 

It ignores and does not use the connectivity (primitives) of the input. 

If the number of points of the input is the same for all the slices, it adds one new [Dimension](<./Dimension.md> "Dimension") whose size is the number of slices. 

Trail Length can be expressed in Seconds or Frames. Seconds is preferable as it will remain the same if you move the Trail POP to another project with a different frame rate. Trail Increment lets you skip frames - capture a slice every Mth frame. 

Reset clears and restarts the trail. Oldest Point First reverses the order of the slices. 

The Trail POP deals with frame drops elegantly by (optionally) filling in data for missing frames and creating stand-in slices, and (optionally) tagging each slice with an`Age`attribute. This can give smoother frame-drop-resistant trail curves. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[trailPOP_Class](</TrailPOP_Class> "TrailPOP Class")

## 

Parameters - Trail Page

Active`active`\- When enabled, the trail POP will append the input POP to the current trails. 

Always Cook`alwayscook`\- Forces the operator to cook every frame. 

Trail Length`length`\- ⊞ \- Length of trail expressed in time units. 
* Trail Length`length`-
* Trail Length Unit`lengthunit`\- The time unit.


Trail Increment`inc`\- ⊞ \- The spacing between trail points. 
* Trail Increment`inc`-
* Trail Increment Unit`incunit`\- The time unit.


Reset`reset`\- ⊞ \- Resets tail and holds one snapshot. 
* Reset`reset`-
* Reset Pulse`resetpulse`\- Reset trail.


Age Attribute`ageattr`\- ⊞ \- Whether to outpt an Age attribute. 
* None`none`-
* Seconds`seconds`-
* Frames`frames`-


Oldest Point First`oldestpointfirst`\- Changes the point order: older points are first instead of last. 

Fill Missed Frames`fillmissedframes`\- Enable frame reconstruction for dropped frames using interpolation. 

Match by Attribute`attrmatch`\- Connect points sharing the same attribute value. 

Attribute Name`attrname`\- Attribute to use when connecting points by attribute. 

Attrib is UInt`uintmax`\- ⊞ \- When connecting trails by attribute, allows to specify whether the attribute is an unsigned integer and what the max value is. Smaller max UInt require fewer passes for the internal sort. 
* 4 bits UInt (max 16)`uint4`-
* 8 bits UInt (max 256)`uint8`-
* 12 bits UInt (max 4096)`uint12`-
* 16 bits UInt (max 65,536)`uint16`-
* 20 bits UInt (max 1 M)`uint20`-
* 24 bits UInt (max 16 M)`uint24`-
* 28 bits UInt (max 268 M)`uint28`-
* 32 bits UInt (max 4 B)`uint32`-


Max Number of Line Strips`maxls`\- Sets the max number of line strips to be allocated. This number should be bigger than the actual number of line strips (visible in info popup) for all the trail line strips to be created. 

Connectivity`surftype`\- ⊞ \- Determines the primitive used to connect the points. 
* None`none`-
* Point Primitives`points`-
* Rows`rows`-
* Columns`cols`-
* Rows and Columns`rowcol`-
* Triangles`triangles`-
* Alternating Triangles`alttriangles`-
* Quadrilaterals`quads`-


Closed`closed`\- The last vertex is connected to the first vertex. 

## 

Parameters - Transform Page

Transform Order`xord`\- ⊞ \- Sets the overall transform order for the transformations. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`rord`\- ⊞ \- Sets the order of the rotations within the overall transform order. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`t`\- ⊞ \- Translate the points in the three axes over time. 
* Translate`tx`-
* Translate`ty`-
* Translate`tz`-


Rotate`r`\- ⊞ \- Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees. 
* Rotate`rx`-
* Rotate`ry`-
* Rotate`rz`-


Scale`s`\- ⊞ \- These three fields scale the Source geometry in the three axes. 
* Scale`sx`-
* Scale`sy`-
* Scale`sz`-


Pivot`p`\- ⊞ \- The pivot point for the transform rotates and scales. 
* Pivot`px`-
* Pivot`py`-
* Pivot`pz`-

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

Extra Information for the Trail POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• Trail • [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
