# Curve POP

## 

Summary

The Curve POP is used to generate a curve in XY (Z=0) that can be used as a lookup curve for a [Lookup Attribute POP](<./Lookup_Attribute_POP.md> "Lookup Attribute POP") or elsewhere. It is a "function" in that the`P(0)`X-value steps forward uniformly from point to point, while the`P(1)`Y-value takes on different interpolated shapes. The curve it generates is also in an attribute`Curve`, which you can use instead of`P(1)`for clarity. 

Like the [S Curve CHOP](<./S_Curve_CHOP.md> "S Curve CHOP"), it defaults to an ease-in ease-out curve, but the Curve POP lets you add multiple segments (sequential blocks) that enable a greater range of curves. The curve can be made of several segments defined by [Sequential Blocks](</index.php?title=Sequential_Blocks&action=edit&redlink=1> "Sequential Blocks \(page does not exist\)") of parameters, each with its own start and end values and Curve Type. 

The Curve Type includes Constant, Linear, the Eases and Bezier. 

The Alpha and Beta values affect the curve, where Alpha makes it more- or less-sloped, and Beta makes it more biased to the start or end of the segment. When Bezier is selected, Slope In and Slope Out affect the slopes at the end-points of the segment. 

More generally, we treat the 2 axes as U and V. The curves can output as points-only, a linestrip, or as an RGBA color curves. 

Because the U values can start and end at any value, you can normalize the curve so the U values (`P(0)`) are between 0 and 1. 

The curve can be extended to double length and made symmetric using the Symmetric toggle. 

The Lookup page lets you apply the curve as a lookup without first converting anything to points. This preerves maximum accuracy, and avoids interpolation problems when a lookup curve sharply steps from one value to another as may occur between two segments. In this case you attach an input POP where you want to modify one or more attributes with the curve. In this mode it behaves similar to the [Lookup Attribute POP](<./Lookup_Attribute_POP.md> "Lookup Attribute POP"). 

Tip: If you want specific points to exactly hit your U keyframe values, make sure your (Number of Points - 1) is divisible evenly by your U values. 

See also [S Curve CHOP](<./S_Curve_CHOP.md> "S Curve CHOP"), [Line POP](<./Line_POP.md> "Line POP"), [Lookup Attribute POP](<./Lookup_Attribute_POP.md> "Lookup Attribute POP"), [Pattern POP](<./Pattern_POP.md> "Pattern POP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[curvePOP_Class](</CurvePOP_Class> "CurvePOP Class")

## 

Parameters - Curve Page

Total Length`totallength`\- Determines the number of points. 

Output Curve`outputcurve`\- ⊞ \- Selects the type of primitive to output. 
* Points`points`-
* Line Strips`linestrip`-
* Color Strip`colorstrip`-


Normalize U`normalizeu`\- Normalize all the U values so their range is 0 to 1. 

Symmetric`symmetric`\- Enable mirroring the curve segments. 

Parameter Size`parsize`\- ⊞ \- Number of independent configurable parameter values. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Start U`startu`\- Start U position for the first segment. 

Segment`seg`\- Start of Sequential Parameter Blocks for creating curve segments. 

Curve Type`seg0type`\- ⊞ \- The interponation type of the curve between the start and end of the segment. 
* Constant`constant`-
* Linear`linear`-
* Ease In`easein`-
* Ease Out`easeout`-
* Ease In Ease Out`easeinout`-
* Bezier`bezier`-


U`seg0u`\- Sets the segments end U. 

Specify Start Value`seg0specstartval`\- When set, the segment has a start value, otherwise it is a continuation of the previous segment. 

Start Value`seg0startval`\- When set, the segment has a start value, otherwise it is a continuation of the previous segment. 

End Value`seg0endval`\- The value at the end of a curve segment. 

Alpha`seg0alpha`\- One paramter that affects the curve, usually a form of steepness. 

Beta`seg0beta`\- A second paramter that affects the curve, usually a form of bias to the start or end of a curve segment. 

Slope in`seg0slopein`\- Bezier slope factor for the incoming curve segment. 

Slope Out`seg0slopeout`\- Bezier slope factor for the outgoing curve segment. 

## 

Parameters - Lookup Page

Apply Lookup`applylookup`\- The Lookup page lets you apply the curve as a lookup without first converting anything to points. 

Lookup Index Attribute`lookupindexattr`\- Attribute to use as the index for the lookup. 

From Low High`fromlow`\- ⊞ \- Reranges the attribute value. 
* From Low High`fromlow`-
* From High`fromhigh`\- Reranges the index attribute value.


To Low High`tolow`\- ⊞ \- Reranges the input lookup attribute value. 
* To Low High`tolow`-
* To High`tohigh`\- Sets high value on the output range.


Extend Left and Right`extendleft`\- ⊞ \- What happens when the lookup samples outside of the range. 
* Hold`hold`-
* Slope`slope`-
* Cycle`cycle`-
* Mirror`mirror`-
* Extend Left and Right`extendleft`-
* Extend Right`extendright`\- What happens when the lookup samples the curves outside its U range.


Lookup`lookup`\- Start of Sequential Parameter Blocks of lookups. 

Multiply`lookup0multiply`\- A multiplier that is applied to the lookup result. 

Add`lookup0add`\- A value you add to the result of a lookup. 

Combine Operation`lookup0combineop`\- ⊞ \- After a value is retrieved doing the lookup, it can be added or multiplied with an attribute. 
* Set`set`-
* Add`add`-
* Multiply`mult`-
* Minimum`min`-
* Maximum`max`-


Output Attribute Scope`lookup0outputattrscope`\- ⊞ \- Name of attribute to output (can choose components of attribute), can choose from menu. 
* P`P`-
* N`N`-
* Color`Color`-
* Color.rgb`Color.rgb`-
* Tex`Tex`-
* PointScale`PointScale`-
* LineWidth`LineWidth`-


Override Automatic Attribute`lookup0overrideautoattr`\- Whether to override the kind of attribute automatically created based on the POP input and parameters. Allows to specify manually the type and number of components of the new attribute. 

Attribute Type`lookup0attrtype`\- ⊞ \- The lookup attribute type. 
* float`float`-
* double`double`-
* int`int`-
* uint`uint`-
* dir`dir`-
* dbl dir`ddir`-


Components`lookup0attrnumcomps`\- ⊞ \- The number of components in the new custom attribute. 
* 1`1`-
* 2`2`-
* 3`3`-
* 4`4`-


Default Value`lookup0attrdefaultval`\- ⊞ \- Default values of the output attribute components if they cannot be computed. 
* Default Value`lookup0attrdefaultval0`-
* Default Value`lookup0attrdefaultval1`-
* Default Value`lookup0attrdefaultval2`-
* Default Value`lookup0attrdefaultval3`-


Extend Right`extendright`\- ⊞ \- 
* Hold`hold`-
* Slope`slope`-
* Cycle`cycle`-
* Mirror`mirror`-

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

Extra Information for the Curve POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• Curve • [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
