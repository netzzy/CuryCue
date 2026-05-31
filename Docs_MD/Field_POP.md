# Field POP

##   
  
Summary

The Field POP adds a`Weight`attribute that represents, for each point of the input, how much a shape defined by the Field POP overlaps with each point. It is often used to cut out sections of points in point clouds. Its shapes include spheres (ellipsoids), cylinders, planes, paraboloids, etc, where all points within the shape (or on one side of the shape) are given a Weight of 1 and all other points are 0. 

It also can output a`Dist`attribute, which is a distance to the surface for points that are outside the shape. 

There are parameters that soften the`Weight`transition from 0 to 1: The Transition range is the distance over which the weight goes from 1 to 0, Transition Align determines if the transition from 1 to 0 starts at the field shape surface, or ends at the surface (default is half-way). The Transition Type allows for linear, ease-in ease-out, or smooth step transitions. 

**Multiple fields in one Field POP**: A parameter called Specification POP is a pointer to a POP where each point is a specification defining a separate field - one point per field. The attributes of the specification POP are named the same as parameters tokens in the Field POP, and override the parameters for each field. Menus and toggles are represented as integers, starting at 0 for the first menu entry. You need only to create a Point POP with attributes named as the Field POP parameters, and then add a point per field, and set their values. (An attribute`sizex`will override the Size X (`sizex`) parameter.) Alternately you can generate points procedurally with attributes that match the Field POP parameter names. The workflow is the same as multiple strings defined in a specification DAT of the [Geo Text COMP](<./Geo_Text_COMP.md> "Geo Text COMP") and the [Text COMP](<./Text_COMP.md> "Text COMP"). 

**Using P as field position** : Although the rule is that the attribute name must be the same as the name of the parameter of the Field POP,`P`(position attribute) is a special case as it overrides`tx`,`ty`and`tz`parameters of the Field POP. If the node`point1`has attributes`radx`and`P`, they override the Field POP's`radx`,`tx`,`ty`and`tz`parameters. 

**Multiple weights raw or mixed** : When you specify multiple fields, their weights are mixed together into the`Weight`attribute (using a blend mode like Screen of the [Composite TOP](<./Composite_TOP.md> "Composite TOP") \- combining multi-fields increase the`Weight`but it never exceeds 1). Alternately the weight for each field can be output raw in a multi-value`Weights`array attribute. 

The`Weight`or`Distance`attribute can be added/multiplied with any another attribute, like a`PartForce`attribute to confine forces to certain regions. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[fieldPOP_Class](<./FieldPOP_Class.md> "FieldPOP Class")

## 

Parameters - Field Page

Attribute Class`attrclass`\- ⊞ \- Makes the POP operate on point attributes, vertex attributes or primitive attributes where applicable. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Field Attribute Scope`fieldattrscope`\- Determines the scope of the attribute used to output the weight. 

Specification POP`specpop`\- Reference to a POP where each point is a specification defining a separate field. 

Mode`mode`\- ⊞ \- Select the shape of the field. 
* Sphere`sphere`-
* Box`box`-
* Torus`torus`-
* Tube Infinite`tubeinfinite`-
* Tube Capped`tubecapped`-
* Tube Rounded`tuberounded`-
* Capsule`capsule`-
* X-Plane`xplane`-
* Y-Plane`yplane`-
* Z-Plane`zplane`-
* Parabola`parabola`-
* Line Projection`lineprojection`-


Size`size`\- ⊞ \- The geometry 3D size. 
* Size`sizex`-
* Size`sizey`-
* Size`sizez`-


Radius`rad`\- ⊞ \- Radius of field. 
* Radius`radx`-
* Radius`rady`-
* Radius`radz`-


Height`height`\- The height of the tube. 

Roundness`roundness`\- Roundness factor for rounded fields modes. 

Point A`pointa`\- ⊞ \- Shape first point. 
* Point A`pointax`-
* Point A`pointay`-
* Point A`pointaz`-


Point B`pointb`\- ⊞ \- Shape second point. 
* Point B`pointbx`-
* Point B`pointby`-
* Point B`pointbz`-


Strength`strength`\- ⊞ \- Sets the field strength. 
* Strength`strengthx`-
* Strength`strengthy`-


Exponent`exponent`\- Sets the exponent on parabola fields. 

Transition Range`transitionrange`\- Determines a transition range for weights. 

Transition Align`transitionalign`\- Determines a transition offset for weights. 

Transition Type`transitiontype`\- ⊞ \- Determines a transition function for weights. 
* Linear`linear`-
* Smooth Step`smoothstep`-
* Ease In Ease Out`easeinout`-


Absolute Value`absvalue`\- Enable using the absolute value on the transitioned weight. 

Invert`invert`\- Invert the attribute value resulting from the field. 

To Range`torange`\- ⊞ \- Sets the output range on the weigths. 
* To Range`torangemin`\- Sets low value on the output range.
* To Range`torangemax`\- Sets high value on the output range.


Delete Zeros`deletezeros`\- Enable removal of points with weigth zero. 

Line Strip Behavior`linestripbehavior`\- ⊞ \- What to do when points of a line strip are deleted. 
* Delete Point of Line Strip`delpointoflinestrip`-
* Split Line Strip`splitlinestrip`-
* Delete Line Strip`dellinestrip`-

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


Translate`t`\- ⊞ \- Translate the field in the three axes. 
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

Parameters - Output Page

Weight`weight`\- ⊞ \- Output a field weight attribute. 
* Weight`weight`-
* Weight Output Attribute`outputattr`\- Specifies the weight output attribute scope.


Signed Distance`signeddistance`\- ⊞ \- Output a signed distance attribute for each point. 
* Signed Distance`signeddistance`-
* Signed Distance Output Attribute`sdoutputattr`\- Attribute scope for the signed distance field output.


Per-Field Weights`perfieldweights`\- ⊞ \- Output an attribute array value for each field in the Specification POP. 
* Per-Field Weights`perfieldweights`-
* Weights`perfieldweightsoutputattr`\- Specifies the per-field weights output attribute scope.


Per-Field Distances`perfielddistances`\- ⊞ \- Output an attribute array value for each field in the Specification POP. 
* Per-Field Distances`perfielddistances`-
* Distances`perfielddistancesoutputattr`\- Specifies the attribute scope used to output per field distances.


Combine Operation`combineop`\- ⊞ \- Specify how to combine the output value with the combine attribute value. 
* None`none`-
* Add`add`-
* Multiply`mult`-


Combine Entity`combineentity`\- ⊞ \- Specify which computed value to use for the combine operation. 
* Weight`weight`-
* Signed Distance`signeddistance`-


Combine Attribute`combineattr`\- Input attribute scope for the combine operation. 

Combine Output Attribute`combineoutputattr`\- ⊞ \- Output attribute scope for the combine operation. 
* P`P`-
* N`N`-
* Color`Color`-
* Color.rgb`Color.rgb`-
* Tex`Tex`-
* PointScale`PointScale`-
* LineWidth`LineWidth`-


Override Automatic Attribute`combineoverrideautoattr`\- Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute. 

Attribute Type`combineattrtype`\- ⊞ \- The combined output attribute's data type, default float. 
* float`float`-
* double`double`-
* int`int`-
* uint`uint`-
* Color`color`-
* Color (double)`dcolor`-
* Direction`dir`-
* Direction (double)`ddir`-


Components`combineattrnumcomps`\- ⊞ \- The number of components in the new custom attribute. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Default Value`combineattrdefaultval`\- ⊞ \- Default values of the output attribute components if they cannot be computed. 
* Default Value`combineattrdefaultval0`-
* Default Value`combineattrdefaultval1`-
* Default Value`combineattrdefaultval2`-
* Default Value`combineattrdefaultval3`-

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

Extra Information for the Field POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• Field • [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
