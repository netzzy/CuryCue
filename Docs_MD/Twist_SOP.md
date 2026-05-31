# Twist SOP

##   
  
Summary

The Twist SOP performs non-linear deformations such as bend, linear taper, shear, squash and stretch, taper and twist. Each deformation will distort the object in one or more axes. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[twistSOP_Class](</TwistSOP_Class> "TwistSOP Class")

## 

Parameters - Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Operation`op`\- ⊞ \- This menu allows you to select a type of non-linear deformation. Select from the following options: 
* Twist`twist`\- Rotates the input geometry around the Primary Axis.
* Bend`bend`\- Bends the input geometry about the Primary Axis while keeping points on the Secondary Axis stationary.
* Shear`shear`\- Shears the input geometry along the Secondary Axis while looking down the Primary Axis.
* Taper`taper`\- Tapers the input geometry along the Secondary Axis while looking down the Primary Axis.
* Linear Taper`ltaper`\- Tapers the input geometry as with the Taper option; however, only the edges remain straight through the Taper operation.
* Squash & Stretch`squash`\- Traditional animator's bounce tools.


Primary Axis`paxis`\- ⊞ \- These menus allows you to select the primary and secondary axes for the deformation. The selected deformation will first occur in the Primary Axis and then the Secondary Axis. 
* X Axis`x`\- This field allows you to choose the origin of the deformation.
* Y Axis`y`\- This field allows you to choose the origin of the deformation.
* Z Axis`z`\- This field allows you to choose the origin of the deformation.


Secondary Axis`saxis`\- ⊞ \- These menus allows you to select the primary and secondary axes for the deformation. The selected deformation will first occur in the Primary Axis and then the Secondary Axis. 
* X Axis`x`\- This field allows you to choose the origin of the deformation.
* Y Axis`y`\- This field allows you to choose the origin of the deformation.
* Z Axis`z`\- This field allows you to choose the origin of the deformation.


Pivot`p`\- ⊞ \- This field allows you to choose the origin of the deformation. 
* X`px`-
* Y`py`-
* Z`pz`-


Strength`strength`\- The Strength of the effect being applied. The Rolloff determines an accentuation of the effect being applied. When you are using different types of transformations this Strength / Roll will have different effects: 
* Bend - Strength and Roll are used to control the extremities of the geometry (try a value of 0.5).
  * Twist - Strength and Roll are used to affect the twist amount based on the distance.
  * Shear - Strength and Roll are used to affect the shear amount based on distance.
  * Taper - Strength and Roll are used to affect the direction of the bow (inwards vs. outwards).
  * Linear Taper - Strength and Roll have no effect for this option.
  * Squash and Stretch - Strength and Roll are used to maintain the apparent volume of the source geometry.


Typically, Rolloff should equal`1`\- which spreads the effect evenly (although not being limited to) across the bounds of the geometry. Values higher than`1`iterate the effect multiple times through the same range. If Rolloff equals`0`, then the effect may be localised to a small segment at the centre of the deformed geometry and Strength may not appear to work properly. 

**Note:** To be certain to see the effects of the Twist SOP, make sure you have enough divisions along the edges. By using a centre that is different from that of the object you can improve your control of the object. Try moving the pivot point to the bottom of an object that you are squashing and stretching. __

Rolloff`roll`\- The Strength of the effect being applied. The Rolloff determines an accentuation of the effect being applied. When you are using different types of transformations this Strength / Roll will have different effects: 
* Bend - Strength and Roll are used to control the extremities of the geometry (try a value of 0.5).
  * Twist - Strength and Roll are used to affect the twist amount based on the distance.
  * Shear - Strength and Roll are used to affect the shear amount based on distance.
  * Taper - Strength and Roll are used to affect the direction of the bow (inwards vs. outwards).
  * Linear Taper - Strength and Roll have no effect for this option.
  * Squash and Stretch - Strength and Roll are used to maintain the apparent volume of the source geometry.


Typically, Rolloff should equal`1`\- which spreads the effect evenly (although not being limited to) across the bounds of the geometry. Values higher than`1`iterate the effect multiple times through the same range. If Rolloff equals`0`, then the effect may be localised to a small segment at the centre of the deformed geometry and Strength may not appear to work properly. 

**Note:** To be certain to see the effects of the Twist SOP, make sure you have enough divisions along the edges. By using a centre that is different from that of the object you can improve your control of the object. Try moving the pivot point to the bottom of an object that you are squashing and stretching. __

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Twist SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\n2021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• Twist • [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
