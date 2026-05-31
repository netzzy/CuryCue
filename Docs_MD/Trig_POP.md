# Trig POP

##   
  
Summary

The Trig POP is a simple operator that converts attributes that are angles into the trigonometry representation of angles (sine, cosine, tangent). Alternately, the Trig POP can convert from the sine, cosine, tangent representation back to angles using the asin, acos and atan functions. asin(x) can be thought of as "the angle whose sine value is x". 

You can choose the units your angles are expressed in - degrees (360 per rotation), radians (2 * 3.14157 per rotation) or simply rotations (1 means 1 rotation) 

For example if an attribute has a value of 30 (degrees) and the Operation is set to sin(A), the Trig POP will output .5 to a new attribute. 

sinh, cosh and tanh are the hyperbolic functions. 

This POP does the same thing as the sin, cos... , asin, acos ... functions in the [Math Mix POP](<./Math_Mix_POP.md> "Math Mix POP"), [Math Combine POP](<./Math_Combine_POP.md> "Math Combine POP"), [Math POP](<./Math_POP.md> "Math POP"). where you can also choose the units of your angles. 

sin and cos are true "functions" because for every value of angle A, there is one and only one value for sin(A). However asin(A) etc are not functions as values of A may have an infinite number or zero numbers of values for asin(A)). 

The function atan2(A,B) requires that you provide two attribute values. 

Note: the other trig functions not included are cot(x) is equal to 1/tan(x). sec(x) = 1/cos(x), and csc(x) = 1/sin(x). 

See also [Math Mix POP](<./Math_Mix_POP.md> "Math Mix POP"), [LFO CHOP](<./LFO_CHOP.md> "LFO CHOP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[trigPOP_Class](</TrigPOP_Class> "TrigPOP Class")

## 

Parameters - Trigonometry Page

Attribute Class`attrclass`\- ⊞ \- Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Group`group`\- If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified. 

Input Attribute Scope A`inputattrscopea`\- Input attribute or attribute components for functions argument A. 

Input Attribute Scope B`inputattrscopeb`\- Input attribute or attribute components for functions argument B. 

Operation`operation`\- ⊞ \- Selects the operation to perform. 
* None`none`-
* cos(A)`cos`-
* sin(A)`sin`-
* tan(A)`tan`-
* acos(A)`acos`-
* asin(A)`asin`-
* atan(A)`atan`-
* atan2(A,B)`atan2`-
* cosh(A)`cosh`-
* sinh(A)`sinh`-
* tanh(A)`tanh`-
* None`none`-
* cos(A)`cos`-
* sin(A)`sin`-
* tan(A)`tan`-
* acos(A)`acos`-
* asin(A)`asin`-
* atan(A)`atan`-
* atan2(A,B)`atan2`-
* cosh(A)`cosh`-
* sinh(A)`sinh`-
* tanh(A)`tanh`-


From Angle Units`fromunit`\- ⊞ \- Controls the angle unit when the selected operation takes an angle as argument. 
* Degrees`deg`-
* Radians`rad`-
* Cycles`cycle`-


To Angle Units`tounit`\- ⊞ \- Determines the angles units after the operation. 
* Degrees`deg`-
* Radians`rad`-
* Cycles`cycle`-


Output Attribute Scope`outputattrscope`\- ⊞ \- Name of attribute to output (can choose components of attribute), can choose from menu. 
* P`P`-
* N`N`-
* Color`Color`-
* Color.rgb`Color.rgb`-
* Tex`Tex`-
* PointScale`PointScale`-
* LineWidth`LineWidth`-


Override Automatic Attribute`overrideautoattr`\- Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute. 

Attribute Type`attrtype`\- ⊞ \- The output attribute's data type, default float. 
* float`float`-
* double`double`-
* int`int`-
* uint`uint`-
* Color`color`-
* Color (double)`dcolor`-
* Direction`dir`-
* Direction (double)`ddir`-


Components`attrnumcomps`\- ⊞ \- The number of components in the new custom attribute. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Default Value`attrdefaultval`\- ⊞ \- Default values of the output attribute components if they cannot be computed. 
* Default Value`attrdefaultval0`\- Default value(s) of the attribute.
* Default Value`attrdefaultval1`\- Default value(s) of the attribute.
* Default Value`attrdefaultval2`\- Default value(s) of the attribute.
* Default Value`attrdefaultval3`\- Default value(s) of the attribute.

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

Extra Information for the Trig POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• Trig • [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
