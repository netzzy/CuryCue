# Force Radial POP

## 

Summary

The Force Radial POP is used in a [Particle POP](<./Particle_POP.md> "Particle POP") loop and outputs a float3 attribute named`PartForce`that sums a set of forces defined in the Force Radial POP. 

The forces include, first on the Global page, a single global force, plus a Wind Speed converted to a wind force. 

These forces are by default uniform for all particles, but because it can be affected by attributes on the Map page, each particle (point) can have a different global force or wind speed applied to it. 

Currently the conversion of wind speed to wind force is hard-wired in the Force Radial POP, but more detailed control will be provided in a future build. 

On the Force (Local) page, you can choose between Radial, Axial, Spiral and Planar local fore types, with position (Translate), Direction, rolloff (Radius) and Strength controls. 

The global and local forces are added together. 

In one Force Radial POP, the local force is added to the global and wind forces to generate a`PartForce`attribute. If the input of the Force Radial POP already exists, then the Force Radial POP's sum of forces is added to the input's`PartForce`. 

Thus you can string a bunch of Force Radial POPs together and optionally mask each one with a [Field POP](<./Field_POP.md> "Field POP") by multiplying its`Weight`attribute by Force Radial's`PartForce`attribute. 

Assuming`PartForce`is in the (usually Null) POP at the end of the Particle POP's feedback loop,`PartForce`feeds back to the Particle POP where it is used to calculate all particles' velocity and position on the next frame of the simulation. 

However you can define multiple local forces in one Force Radial POP: To enable many forces to be included in one Force Radial POP, the parameter called Specification POP is a pointer to, usually, a [Point POP](<./Point_POP.md> "Point POP"), where each point of the Point POP defines a separate local force, where the attribute names are matched to the the parameter names (for example, attribute`strength`represents the Strength parameter). In the Point POP you need to create the appropriate matching attributes. 

Then the sum of the local forces are added to the global and wind forces to generate the`PartForce`attribute. 

Note that you can create the`PartForce`attribute any way you want - using Noise, Math Mix, Pattern, Lookup, GLSL POPs etc. You don't need the Force POP \- it is just a convenience. 

See also [Particle POP](<./Particle_POP.md> "Particle POP"), [Field POP](<./Field_POP.md> "Field POP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[forceradialPOP_Class](<./ForceradialPOP_Class.md> "ForceradialPOP Class")

## 

Parameters - Force Page

Specification POP`specpop`\- Reference to a POP where each point is a specification defining a separate force. 

Position`pos`\- ⊞ \- Forces center position. 
* Position`posx`-
* Position`posy`-
* Position`posz`-


Direction`direction`\- ⊞ \- Determines the radial force main direction. 
* Direction`directionx`-
* Direction`directiony`-
* Direction`directionz`-


Enable Radial`radial`\- Enable the radial force. 

Radial Strength`radialstrength`\- Radial force magnitude. 

Enable Axial`axial`\- Enable the axial force. 

Axis Rotation`axialr`\- ⊞ \- 3D rotation for the axial force direction. The base axis is the Direction. 
* Axis Rotation`axialrx`-
* Axis Rotation`axialry`-
* Axis Rotation`axialrz`-


Axial Strength`axialstrength`\- The strength of the force along the Direction axis. 

Enable Spiral`spiral`\- Enable the spiral force. 

Spiral Rotation`spiralr`\- ⊞ \- 3D rotation for the spiral force axis. The base axis is the Direction. 
* Spiral Rotation`spiralrx`-
* Spiral Rotation`spiralry`-
* Spiral Rotation`spiralrz`-


Spiral Strength`spiralstrength`\- Spiral force magnitude. 

Enable Planar`planar`\- Enable the planar force. 

Planar Exponent`planarexponent`\- Planar force distance exponent. 

Planar Strength`planarstrength`\- Planar force factor. 

Falloff`falloff`\- ⊞ \- Sets the falloff type on the forces. 
* S Curve`scurve`-
* Bias Power`power`-
* Inverse Distance`inversedistance`-
* None`none`-


Steepness`falloffsteepness`\- Controls the steepness of the S-Curve falloff. 

Bias`falloffbias`\- In the S Curve falloff, this biases the curve to fall off closer to its inner limit or its outer limit. 

Exponent`falloffexponent`\- Sets the exponent on the distance when enabling falloff by inverse distance. 

Radius`falloffradius`\- The radius of the falloff. 

Plateau`falloffplateau`\- The plateau of the falloff. 

Limit Near-Range`fallofflimitrange`\- The near-range limit of the falloff. 

## 

Parameters - Global Page

Global Force`globforce`\- ⊞ \- Global force direction. 
* Global Force`globforcex`-
* Global Force`globforcey`-
* Global Force`globforcez`-


Global Force Multiplier`globforcemult`\- Multiplier for the global force. 

Wind Speed`windspeed`\- ⊞ \- Global wind speed. 
* Wind Speed`windspeedx`-
* Wind Speed`windspeedy`-
* Wind Speed`windspeedz`-


Wind Speed Multiplier`windspeedmult`\- Multiplier for global wind speed. 

## 

Parameters - Map Page

Mapping`map`\- Start of Sequential Parameter Blocks for attribute-to-parameter mapping. 

OP`map0op`\- Source OP for parameter mapping. The default of _in0 means the input POP. 

Element`map0element`\- The attribute (or component of an attribute) that will be mapped to a parameter per-point. 

Parameter`map0parm`\- ⊞ \- Parameter on the current POP that will be mapped from the Element (the attribute). 
* globforce (Global Force)`globforce`-
* globforcex`globforcex`-
* globforcey`globforcey`-
* globforcez`globforcez`-
* globforcemult (Global Force Multiplier)`globforcemult`-
* windspeed (Wind Speed)`windspeed`-
* windspeedx`windspeedx`-
* windspeedy`windspeedy`-
* windspeedz`windspeedz`-
* windspeedmult (Wind Speed Multiplier)`windspeedmult`-


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

Extra Information for the Force POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditormw-revertedmw-new-redirectmw-manual-revertmw-changed-redirect-targetmw-changed-redirect-target2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• Force Radial • [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
