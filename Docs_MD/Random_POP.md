# Random POP

## 

Summary

The Random POP takes its input and either (1) generates a new attribute containing random values, or (2) sets, adds or multiplies an existing attribute by a random value for each point. 

The random values can be applied to point, vertex or primitive attributes. 

By default, the random values are uniformly distributed between 0 and 1, but there is a variety of alternate distributions controlled with the Type menu. These include Gaussian (also known as Normal) distribution (where most points are near the center of the range), two values randomly chosen with a fraction probability of each (Two Values), a random Direction vector (within a certain cone angle) which always has length of 1, random float3 vectors within a unit Sphere, and Exponential which is an exponential dropoff above 0 separately in each axis. 

The random values can be generated within a specified range (Value A and Value B), and then optionally clamped between two values. 

There is an option to generate 2 or more points for every input point to increase the density of points around the source points. (Extra Points per Source Point) 

The random values can also be restricted to certain point, vertex or primitive Groups. 

Tip: You can get random distributions radially around a point by using the [Projection POP](<./Projection_POP.md> "Projection POP") by generating random numbers in polar space and converting to Cartesian. 

**Per-point mapping of parameters** \- The Random POP has a Map page, which allows every point to get a different value for Amplitude, Offset, Exponent, Period, Value A and B and other parameters. In this mechanism, a separate attribute in the input contains values that override (or add to / multiply by) the parameter value. See [Mapping POP Attributes to Parameters](<./Mapping_POP_Attributes_to_Parameters.md> "Mapping POP Attributes to Parameters"). 

See also [Point Generator POP](<./Point_Generator_POP.md> "Point Generator POP"), [Noise POP](<./Noise_POP.md> "Noise POP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[randomPOP_Class](<./RandomPOP_Class.md> "RandomPOP Class")

## 

Parameters - Random Page

Extra Points per Source Point`extrapts`\- Determines how many additional random points are generated per input point. 

Type`type`\- ⊞ \- Determines the random type. 
* Constant`constant`-
* Two Values`twovalues`-
* Uniform (Continuous)`uniform`-
* Uniform (Discrete)`uniformdiscrete`-
* Direction`direction`-
* Inside Sphere`insidesphere`-
* Normal (Gaussian)`normal`-
* Exponential`exponential`-
* Log-Normal`lognormal`-
* Cauchy-Lorentz`cauchylorentz`-
* Custom Ramp`customramp`-
* None`none`-
* Gaussian (Normal)`gaussian`-


CHOP`chop`\- When the distribution type is Custom Ramp, the CHOP to use for the custom ramp. 

Random Size`randomsize`\- ⊞ \- Number of random components. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Seed`seed`\- Numerical value that initializes the randomization. 

Parameter Size`parsize`\- ⊞ \- Number of independent configurable parameter values. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Amplitude`amp`\- For certain types of random values, the random values amplitude (a scale on the values output). 

Exponent`exp`\- Sets the exponent. The internal value is raised by the power of the exponent 

Offset`offset`\- Adds an offset to the resulting value. 

Value A`valuea`\- One of two values determining the random numbers that are output. 

Value B`valueb`\- One of two values determining the random numbers that are output. 

Value B Probability`valuebproba`\- The probability that the numbers will be biased toward value B vs A. 

Clamp Value`clamp`\- Whether to clamp the output value between a minimum and a maximum. 

Clamp Min`minval`\- Minimum output value. 

Clamp Max`maxval`\- Maximum output value. 

Cone Direction`conedir`\- ⊞ \- When random distribution is direction, specifies the cone direction. 
* Cone Direction`conedirx`-
* Cone Direction`conediry`-
* Cone Direction`conedirz`-


Cone Angle`coneangle`\- When random distribution is direction, specifies the cone angle around the cone direction. 

Combine Operation`combineop`\- ⊞ \- Specify how to combine the output value with the combine attribute value. 
* Set`set`-
* Add`add`-
* Multiply`mult`-
* Translate along Normal`translatealongnormal`-


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

Compute Point Normals`computenormals`\- Whether to compute point normals as a post operation. 

## 

Parameters - Map Page

Mapping`map`\- Start of Sequential Parameter Blocks for attribute-to-parameter mapping. 

OP`map0op`\- Source OP for parameter mapping. The default of _in0 means the input POP. 

Element`map0element`\- The attribute (or component of an attribute) that will be mapped to a parameter per-point. 

Parameter`map0parm`\- ⊞ \- Parameter on the current POP that will be mapped from the Element (the attribute). 
* amp (Amplitude)`amp`-
* exp (Exponent)`exp`-
* offset (Offset)`offset`-
* valuea (Value A)`valuea`-
* valueb (Value B)`valueb`-
* valuebproba (Value B Probability)`valuebproba`-
* stepval (Step Value)`stepval`\- The minimum difference between two random values for uniform discrete mode.
* minval (Clamp Min)`minval`-
* maxval (Clamp Max)`maxval`-
* conedir (Cone Direction)`conedir`-
* conedirx`conedirx`-
* conediry`conediry`-
* conedirz`conedirz`-
* coneangle (Cone Angle)`coneangle`-


Combine Operation`map0combineop`\- ⊞ \- Combine operation for attribute value with parameter value. 
* Set`set`-
* Multiply`mult`-
* Add`add`-

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

Extra Information for the Random POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• Random • [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
