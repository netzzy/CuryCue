# Pattern POP

## 

Summary

The Pattern POP is a generator that makes simple line strip shapes using elementary math functions in X, Y and Z. Alternately it can add a new attribute to an input POP using the elementary math functions. 

The math functions include sine, cos, triangles, square waves, as well as ease in/out and random. Parameters control phase, repeats and re-ranging. 

The Pattern POP can: 
* make one or more 3D line strips generating a`P`attribute containing a different curve in X, Y and Z. (it can create`Tex`at the same time). (generator)
  * add a new attribute (1-4 components) to an input POP, each component containing a separate type of curve. (filter)
  * modify an existing attribute of an input POP by adding/multiplying the curve to it. (filter)
  * create a POP that has no P attribute - just a curve in a new attribute. (generator)


See also: [Curve POP](<./Curve_POP.md> "Curve POP"), [Math Mix POP](<./Math_Mix_POP.md> "Math Mix POP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[patternPOP_Class](</PatternPOP_Class> "PatternPOP Class")

## 

Parameters - Pattern Page

Number of Points`numpoints`\- Sets the number of points. 

Cyclic`cyclic`\- Enable having completes cycle correspond to Number of Points + 1 values. 

Connectivity`connectivity`\- ⊞ \- Determines whether and how to connect the points. 
* None`none`-
* Line Strip`linestrip`-
* Lines`lines`-
* Point Prims`points`-


Parameter Size`parsize`\- ⊞ \- Number of independent configurable parameter values. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Type`type`\- ⊞ \- Determines the pattern type. 
* Type`type0`\- Determine the pattern type.
* Type`type1`-
* Type`type2`-


Seed`seed`\- Numerical value that initializes the randomization. 

Number of Cycles`numcycles`\- ⊞ \- Set the number of repeating cycles of the Type shapes over the Length, except for Random. 
* Number of Cycles`numcycles0`\- Number of cycles.
* Number of Cycles`numcycles1`\- Number of cycles.
* Number of Cycles`numcycles2`\- Number of cycles.


Step per Cycle`steppercycle`\- ⊞ \- Step added to each cycle. 
* Step per Cycle`steppercycle0`-
* Step per Cycle`steppercycle1`-
* Step per Cycle`steppercycle2`-


Bias`bias`\- ⊞ \- Makes Triangle type into a sawtooth wave, and sets the Square type variable-width. 
* Bias`bias0`-
* Bias`bias1`-
* Bias`bias2`-


Phase`phase`\- ⊞ \- Shifts the cycle. 
* Phase`phase0`\- Shifts the cycle.
* Phase`phase1`\- Phase shift of pattern.
* Phase`phase2`\- Phase shift of pattern.


Exponent`exp`\- ⊞ \- Sets the exponent. The internal value is raised by the power of the exponent 
* Exponent`exp0`-
* Exponent`exp1`-
* Exponent`exp2`-


Map from Low`fromlow`\- ⊞ \- Reranges the attribute value. 
* Map from Low`fromlow0`-
* Map from Low`fromlow1`-
* Map from Low`fromlow2`-


Map from High`fromhigh`\- ⊞ \- Reranges the attribute value. 
* Map from High`fromhigh0`-
* Map from High`fromhigh1`-
* Map from High`fromhigh2`-


Map to Low`tolow`\- ⊞ \- Reranges the attribute value. 
* Map to Low`tolow0`-
* Map to Low`tolow1`-
* Map to Low`tolow2`-


Map to High`tohigh`\- ⊞ \- Reranges the attribute value. 
* Map to High`tohigh0`-
* Map to High`tohigh1`-
* Map to High`tohigh2`-


Reverse`reverse`\- ⊞ \- Enable reverse order. 
* Reverse`reverse0`-
* Reverse`reverse1`-
* Reverse`reverse2`-


Line Break Each Cycle`linebreakcycle`\- ⊞ \- When on, creates a line break at each cycle. 
* Line Break Each Cycle`linebreakcycle0`-
* Line Break Each Cycle`linebreakcycle1`-
* Line Break Each Cycle`linebreakcycle2`-


Closed`closed`\- The last vertex is connected to the first vertex. 

Output Line Break Attribute`outputlinebreakattr`\- Whether to output a LineBreak attribute. 

Texture Coordinates`texture`\- ⊞ \- Sets the texture coordinate mode relative to the cylcles. 
* Off`off`-
* Ramp Start to End`rampstartend`-
* Ramp Per Cycle`ramppercycle`-


Combine Operation`combineop`\- ⊞ \- Specify how to combine the output value with the combine attribute value. 
* Set`set`-
* Add`add`-
* Multiply`mult`-


Combine Attribute Scope`combineattrscope`\- Input attribute scope for the combine operation. 

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


Attribute Class`attrclass`\- ⊞ \- Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Group`group`\- If there are input groups, specifying a group name in this field will cause this POP to act only upon the group specified. 

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

Extra Information for the Pattern POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• Pattern • [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
