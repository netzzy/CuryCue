# Copy POP

##   
  
Summary

The Copy POP makes copies of its input using (1) the Number of Copies parameter that specifies the number of copies to make with the transform applied to each copy, and (2) a second-input Template POP where a copy is placed at each point of the template. 

For each copy in (1), the transforms are cumulative, that is, the transform is applied to the transform of the previous copy, with no transform applied to the first copy. 

Once (1) is done, then (2) is applied to the result. 

The Template page chooses which attributes of the template are used to define the transform for each copy-per-template point. 

The Template Attributes page determines what attributes are added to the output, and how the attributes are combinations of the first input and the template input, multiplying or adding them together. 

If the number of copies is greater than 1, The Dimension of the first input is increased by one, and the number of dimensions is increased by the second (template) input's dimension. See [Dimension](<./Dimension.md> "Dimension"). 

See also: [GLSL Copy POP](<./GLSL_Copy_POP.md> "GLSL Copy POP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[copyPOP_Class](</CopyPOP_Class> "CopyPOP Class")

## 

Parameters - Copy Page

Number of Copies`ncy`\- Sets the number of copies. If the template input is used, that's the number of copies per template point. 

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


Translate`t`\- ⊞ \- Translate the points in the three axes. 
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


Uniform Scale`scale`\- Specifies a uniform scale factor in all axes. 

CopyId Attribute`copyid`\- ⊞ \- Whether to output an attribute containing the copy index and where. 
* CopyId Attribute`copyid`-
* CopyId Attrib Name`copyidname`\- Sets the attribute scope when outputting the Copy Id attribute.


Look At`lookat`\- Orients the copied geometry (Z axis) to look at, or point to, the object component specified in the parameter. 

Up Vector`upvector`\- ⊞ \- Sets the up vector when setting up the look at transform. 
* Up Vector`upvectorx`-
* Up Vector`upvectory`-
* Up Vector`upvectorz`-


Forward Direction`forwarddir`\- ⊞ \- Determines the forward direction for look at transformation. 
* +X`posx`-
* -X`negx`-
* +Y`posy`-
* -Y`negy`-
* +Z`posz`-
* -Z`negz`-


Vectors Maintain Length`vlength`\- Enable preserving the original vector length after applying transformations. 

Append Dimension`dimension`\- ⊞ \- Always add a dimension, or only add a dimesion when its size is 2 or more. 
* When Template Points / Copies > 1`morethanone`-
* Always`always`-

## 

Parameters - Template Page

Template Matrix Transform`dotemplatematrix`\- ⊞ \- Whether to use a transform matrix attribute on the template points. 
* Template Matrix Transform`dotemplatematrix`-
* Transform Attribute`transformattr`\- Specifies the scope of the template attribute that holds the transform matrices.


Template Transform Order`templatexord`\- ⊞ \- Sets the overall transform order for the template transformations. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Template Rotate Order`templaterord`\- ⊞ \- Sets the order of the X, Y and Z rotations within the overall template transform. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Template Translate`dotemplatetranslate`\- ⊞ \- Whether to use a translate attribute on the template points. 
* Template Translate`dotemplatetranslate`-
* Template Translate Attribute`translateattr`\- The attribute scope for the translation base on the template input.


Template Rotate`dotemplaterotate`\- ⊞ \- Whether to use a rotate attribute on the template points. 
* Template Rotate`dotemplaterotate`-
* Template Rotate Attribute`rotateattr`\- The attribute scope for the rotation base on the template input.


Template Scale`dotemplatescale`\- ⊞ \- Whether to use a scale attribute on the template points. 
* Template Scale`dotemplatescale`-
* Scale Attribute`scaleattrib`\- Input attribute scope for scaling.


Template Pivot`dotemplatepivot`\- ⊞ \- Whether to use a pivot attribute on the template points. 
* Template Pivot`dotemplatepivot`-
* Template Pivot Attribute`pivotattr`\- The attribute scope for the pivot base on the template input.


Template Rotate to Vector`dotemplaterotateto`\- Enable align to vector rotation, using the template input as a reference. 

Template Rotate to Order`templaterottoord`\- ⊞ \- Sets the order of axis and align to vector rotations within the overall template transform. 
* Rotate to Vector, then Transform`rottoxform`-
* Rotate, then Rotate to Vector`rotaterotto`-
* Rotate to Vector, then Rotate`rottorotate`-


Rotate to Vector : Forward Direction`instanceforward`\- ⊞ \- Base forward direction used to compute the rotation to vector. 
* +X`posx`-
* -X`negx`-
* +Y`posy`-
* -Y`negy`-
* +Z`posz`-
* -Z`negz`-


Rotate to Vector Attribute`vecattr`\- Input attribute used to compute the rotation to vector. 

Up Vector Type`upvectoratype`\- ⊞ \- Specifies the up vector source. 
* Attribute`attribute`-
* Constant`constant`-


Up Attribute`upattr`\- Defines the scope of the up attribute used for alignment with template vectors. 

Up Constant`upconstant`\- ⊞ \- Sets the up vector to align with the template vectors. 
* Up Constant`upconstantx`-
* Up Constant`upconstanty`-
* Up Constant`upconstantz`-


TemplateId Attribute`templateid`\- ⊞ \- Output a template ID attribute to points, vertices or primitives. 
* TemplateId Attribute`templateid`-
* TemplateId Attrib Name`templateidname`\- Output attribute scope for the template Id.

## 

Parameters - Template Attributes Page

Use Template Point Attribs`doattr`\- Enable additional operations on template input attributes. 

Template Attribute`templateattr`\- Start of Sequential Parameter Blocks for attributes as combinations of the first input and the template input. 

Operation`templateattr0op`\- ⊞ \- Choose how to combine the template attribute with the matching attribute on the copy if it exists. 
* Copy`copy`-
* Multiply`mul`-
* Add`add`-
* Subtract`subtract`-


Destination`templateattr0dest`\- ⊞ \- Sets the attribute class where the template point attribute operation will happen. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Names`templateattr0names`\- ⊞ \- Names of the attributes on the template input to use. 
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

Extra Information for the Copy POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• Copy • [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
