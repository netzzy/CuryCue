# Ray POP

## 

Summary

The Ray POP casts a ray from each points of the input, in the direction defined by the Ray Attribute, and outputs new attributes that report what each ray hits. 

The second input is the set of triangles and quads that the rays are tested against. The Ray POP can count the number of primitives it hit as it transmits through all primitive in its line, and the distance to the closest primitive. 

It can output properties of the primitive it hit - its primitive index, the barymetric position on the primitive it hit, and the values of any attributes on the primitive it hit. 

It an also output information about rays that are reflected. Assuming the Collision Geometry is a closed surface, the Ray POP can report whether it is located inside or outside the volume. 

It can be put into a mode where it outputs line strips representing the rays that it casts, intersects and reflects. 

By default, the Ray POP projects the points on the collision mesh, Scale is a 0 to 1 multiplier between original position and projected position, Lift is also a control to move the point along the ray but in absolute units (to move points inside or outside a bit from the collision surface. 

See also [Math Mix POP](<./Math_Mix_POP.md> "Math Mix POP") (has ray functions) 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[rayPOP_Class](</RayPOP_Class> "RayPOP Class")

## 

Parameters - Ray Page

Ray Attribute`rayattrib`\- Ray direction attribute. 

Negate Ray`negateray`\- Negates the direction of the ray. 

Number of Bounces`numbounces`\- The number of bounces for the rays. 

Connect Points`connectpoints`\- When doing multiple bounces, for each input point whether to connect the intersections as a line strip. 

Limit Ray Length`limitraylength`\- ⊞ \- The ray length will be limited. 
* Limit Ray Length`limitraylength`-
* Ray Distance Max Attrib`raydistancemaxattr`\- Help Not Available.


Trim Ray`trimray`\- ⊞ \- Option to trim ray line strip. 
* Trim Ray`trimray`-
* Trim Distance Attrib`trimdistanceattr`\- Specifies the attribute to use to trim rays.


Hardware Ray Tracing`hwraytracing`\- ⊞ \- Selects mode for Hardware Ray Tracing if supported 
* Off`off`-
* Fast Build (Dynamic Geometry)`fastbuild`-
* Fast Trace (Static Geometry)`fasttrace`-


Opaque Geometry`opaque`\- When using hardware raytracing, specify whether the collision geometry is treated as opaque (only the closest or the first hit is returned) or not. 

Any Hit`anyhit`\- Whether to return the first hit, not guaranteed to be the closest or the farthest one. 

Hit Normal`hitnormal`\- ⊞ \- Generate normal attribute at hit locations. 
* Hit Normal`hitnormal`-
* Hit Normal Name`hitnormalname`\- Name of the normal attribute for the ray hit location on the surface.


Reflected Ray`doreflectedray`\- ⊞ \- Whether to output an attribute containing the reflected ray direction. 
* Reflected Ray`doreflectedray`-
* Reflected Ray Name`reflectedrayname`\- Reflected ray attribute name.


Point Intersection Distance`dist`\- ⊞ \- Whether to output an attribute with the distance between the original point and the intersection with the collision geometry. 
* Point Intersection Distance`dist`-
* Point Intersection Distance Name`distname`\- Intersection distance output attribute name.


Farthest Hit`farhit`\- ⊞ \- Whether to output an attribute with the farthest hit position. 
* Farthest Hit`farhit`-
* Farthest Hit Name`farhitname`\- Determines the scope of the attribute used to output the farthest hit position.


Number of Hits`numhits`\- ⊞ \- The Number of hits for rays passing through all the primitives in the ray direction. 
* Number of Hits`numhits`-
* Number of Hits Name`numhitsname`\- The name of the Number of Hits attribute.


Inside`inside`\- ⊞ \- Outputs an attribute containing 0 for rays stating outside a volume (a closed polygon surface), or 1 for rays originating inside a volume. 
* Inside`inside`-
* Inside Name`insidename`\- Inside attribute name. Value is 0 if inside closed mesh, 1 if outside.


Hit Primitive Index`hitprimindex`\- ⊞ \- Generate primitive index at hit locations. 
* Hit Primitive Index`hitprimindex`-
* Hit Primitive Index Name`hitprimindexname`\- Name of the primitive index attribute.


Barycentric Coordinates`barycoords`\- ⊞ \- Whether to output an attribute with the barycentric coordinates of the intersection point. 
* Barycentric Coordinates`barycoords`-
* Barycentric Coordinates Name`barycoordsname`\- Barycentric coordinates name.


Scale`scale`\- Intersection scaling factor. 

Lift`lift`\- This value offsets the point from the collision geometry in the direction of its normal. 

Hit Point Attr Scope`hitpointattrscope`\- ⊞ \- Point attributes to sample on the collision geometry. 
* *`*`-


Hit Primitive Attr Scope`hitprimattrscope`\- ⊞ \- Primitive attributes to sample on the collision geometry. 
* *`*`-


Hit Vertex Attr Scope`hitvertattrscope`\- ⊞ \- Vertex attributes to sample on the collision geometry. 
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

Extra Information for the Ray POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• Ray • [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
