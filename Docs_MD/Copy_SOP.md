# Copy SOP

##   
  
Summary

The Copy SOP lets you make copies of the geometry of other SOPs and apply a transformation to each copy. 

It also allows you to copy geometry to points on an input template. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[copySOP_Class](<./CopySOP_Class.md> "CopySOP Class")

## 

Parameters - Copy Page

Specifies a subset of template primitives from which to copy onto. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Source Group`sourcegrp`\- Specifies a subset of input primitives to copy from. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Template Group`templategrp`\- Specifies a subset of template primitives from which to copy onto. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Number of Copies`ncy`\- Sets number of Copies to be made of the source. For a template input, it specifies the number of copies to be placed at each point of the template. 

Primitives per Point`nprims`\- Defines how many primitives to copy from each point. 

Rotate to Normal`nml`\- Only used when a template input is specified. If the template is a sphere, and the first input is a circle, a circle is placed at each point of the sphere. With this option on, all the circles will re-orient to face the surface of the sphere (a default sphere has normals radiating outwards from the center). 

If an up attribute exists on the template geometry, then this will be used (along with the normal) to fully define the rotates for the copies. An up attribute is created with the Point SOP. __

Transform Cumulative`cum`\- Each transformation "builds" on the location left by the one before it. Transformations are cumulative as the Copy SOP produces new copies. 

Transform Order`xord`\- ⊞ \- Sets the overall transform order for the transformations. The Transform Order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu. 
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


Translate`t`\- ⊞ \- These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Scale`s`\- ⊞ \- These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference. 
* X`sx`-
* Y`sy`-
* Z`sz`-


Pivot`p`\- ⊞ \- These allow you to specify the Translation (how much it moves over in a given direction), Rotation, and the Scale between each copy. Three columns are given for X, Y, and Z coordinates. Guide geometry is provided for the Pivot's translations. The Pivot is represented by a single red dot in the Viewport. Changing the Pivot parameters moves this point of reference. 
* X`px`-
* Y`py`-
* Z`pz`-


Uniform Scale`scale`\- Uniform Scale allows you to shrink or enlarge geometry along all three axes simultaneously. 

Normals Maintain Length`vlength`\- Vector type attributes (i.e. normals, velocity) maintain the same length under transforms. i.e. When geometry is scaled, the normals remain constant in length. 

Create Output Groups`newg`\- If selected, this creates a group for each copy number, and places each primitive created at that stage into it. 

Copy Groups`copyg`\- Defines the base name of the groups created. 

Look At`lookat`\- Orients the copied geometry to lookat, or point to, the [object](<./Object.md> "Object") component specified in the parameter. 

Up Vector`upvector`\- ⊞ \- When specifying a Look At, it is possible to specify an up vector for the lookat. Without using an up vector, it is possible to get poor animation when the lookat object passes through the Y axis of the target object. 
* X`upvectorx`-
* Y`upvectory`-
* Z`upvectorz`-

## 

Parameters - Stamp Page

Stamping is allowed in any parameter in TouchDesigner. The only requirement is that the stamped parameter is upstream in some fashion from the Copy SOP doing the stamping. 

Stamp Inputs`stamp`\- When enabled, it will Stamp proceeding variables for each input copied. 

Copy`copy`\- Sequence of stamp variables 

Param`copy0param`\- Token of each stamp variable. Stamped parameters are accessible via the global`fetchStamp()`method in the [td Module](<./Td_Module.md> "Td Module") in python, or`param()`in tscript. See the example, below. 

Value`copy0value`\- Value of each stamp variable. Stamped parameters are accessible via the global`fetchStamp()`method in the [td Module](<./Td_Module.md> "Td Module") in python, or`param()`in tscript. See the example, below. 

## 

Parameters - Attributes Page

This page allows you to determine how point attributes on template geometry affect attributes on the source geometry. The template attribute can modify the source in four ways: 
* Set - Override the source attribute.
  * Multiply - Multiply the source attribute.
  * Add - Get Added to the source attribute.
  * Sub - Get Subtracted from the source attribute.


The template point attributes are able to affect point, primitive, or vertex attributes in the source geometry simply by entering values in the appropriate fields. 

Use Template Point Attribs`doattr`\- Enables the parameters below to allow template point attributes to be applied to the copied source geometry. 

Copy to Point`setpt`\- ⊞ \- Copy the attributes to the source geometry's points. 
* *`*`-


Copy to Primitive`setprim`\- ⊞ \- Copy the attributes to the source geometry's primitives. 
* *`*`-


Copy to Vertex`setvtx`\- ⊞ \- Copy the attributes to the source geometry's vertices. 
* *`*`-


Multiply Point`mulpt`\- ⊞ \- Multiply the attributes with the source geometry's point attributes. 
* *`*`-


Multiply Primitive`mulprim`\- ⊞ \- Multiply the attributes with the source geometry's primitive attributes. 
* *`*`-


Multiply Vertex`mulvtx`\- ⊞ \- Multiply the attributes with the source geometry's vertex attributes. 
* *`*`-


Add Point`addpt`\- ⊞ \- Add the attributes to the source geometry's point attributes. 
* *`*`-


Add Primitive`addprim`\- ⊞ \- Add the attributes to the source geometry's primitive attributes. 
* *`*`-


Add Vertex`addvtx`\- ⊞ \- Add the attributes to the source geometry's vertex attributes. 
* *`*`-


Subtract Point`subpt`\- ⊞ \- Subtract the attributes from the source geometry's point attributes. 
* *`*`-


Subtract Primitive`subprim`\- ⊞ \- Subtract the attributes from the source geometry's primitive attributes. 
* *`*`-


Subtract Vertex`subvtx`\- ⊞ \- Subtract the attributes from the source geometry's vertex attributes. 
* *`*`-

## 

Tips

You can use the`me.copyTotal`python member to calculate the degrees of rotation for a given number of copies. For example, if you have 28 copies, you can set the rotation to be:`360/me.copyTotal`\- this would automatically give you 12.8571 degrees, evenly spacing your 28 copies around the full circumference of the circle. 

Using a Particle SOP as the Template object, you can copy objects defined in the Copy Data input to each particle template. This allows you, for example, to copy a Bee to each particle to create a swarm of bees. 

Make a series of copies about an axis, and skin them to achieve lathe-like effects, similar to the results achieved with the Revolve SOP. 

## 

Examples

### 

Creating Stamped Geometry
1. Place a Circle SOP, and set its type to Polygon.
  2. Set the number of Divisions in the Circle to:`fetchStamp("sides",3)`The method`fetchStamp()`returns the value of the global parameter sides. If it is not yet defined it will return a value of 3.
  3. Append a Copy SOP, and set the Number of Copies to`5`; and set Translate X to:`2.5`.
  4. In the Stamp page of the Copy SOP, turn on Stamp Inputs. Set Param 1 to:`sides`and`me.copyIndex+3`[![CopySOPStampPage.png](./images/d/d9/CopySOPStampPage.png)](</File:CopySOPStampPage.png>)
  5. This creates a triangle on the first stamped copy; a square on the next; a pentagon on the third, and so on. The geometry for each copy is cooked separately.


You can set multiple stamp Params at once and they can be used anywhere in the ancestry of the copy's input. 

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Copy SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common SOP Info Channels
* num_points \- Number of points in this SOP.
* num_prims \- Number of primitives in this SOP.
* num_particles \- Number of particles in this SOP.
* last_vbo_update_time \- Time spent in another thread updating geometry data on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.
* last_meta_vbo_update_time \- Time spent in another thread updating meta surface geometry data (such as metaballs or nurbs) on the GPU from the SOP's CPU data. As it is part of another thread, this time is not part of the usual frame time.

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditor2022.241402021.100002020.200002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• Copy • [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
