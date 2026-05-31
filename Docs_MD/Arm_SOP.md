# Arm SOP

## 

Summary

The Arm SOP creates all the necessary geometry for an arm, and provides a smooth, untwisted skin that connects the arm to the body. It is controlled through inverse kinematics linked to a handprint. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[armSOP_Class](<./ArmSOP_Class.md> "ArmSOP Class")

## 

Parameters - Arm Page

Capture Type`capttype`\- ⊞ \- You can use either **Ellipses** or **Capture Regions** as deformation geometry. Ellipses are for use with the Skeleton SOP. Capture Regions are for use with the Capture SOP. 
* Ellipses`ellipses`-
* Capture Regions`cregions`-


Arm Axis`axis`\- ⊞ \- Position the model along the +X or -X axis. 
* \+ X`posx`-
* \- X`negx`-


Radius`bonerad`\- Controls the scale of the circle radii. 

Rotate Hand`rotatehand`\- This parameter rotates the hand and the wrist joint to match the orientation of the hand-print object. In order to operate correctly, the end-affector (hand print) scale transformations must remain at 1. 

**Note:** If the channel is set to 0, then the hand rotations are relative to the forearm. If the channel is set to 1, the hand rotations are the same orientation as the end affector. __

Auto Elbow Twist`autoelbow`\- This parameter affects the default twist of the elbow joint to a more natural position. 

Elbow Twist`elbowtwist`\- Specifies the rotation angle of the elbow joint. 

Flip Elbow`flipelbow`\- This toggle positions the arm using an alternative elbow position solution. 

## 

Parameters - Lengths Page

[![TouchGeometry216.gif](./images/9/9e/TouchGeometry216.gif)](</File:TouchGeometry216.gif>)

Clavicle`clavlength`\- Control bone lengths, as illustrated above. 

Humerous`humlength`\- Control bone lengths, as illustrated above. 

Ulna`ulnalength`\- Control bone lengths, as illustrated above. 

Hand`handlength`\- Control bone lengths, as illustrated above. 

Shoulder Joint`shoulder`\- Control the joint lengths, as illustrated above. 

Elbow Joint`elbow`\- Control the joint lengths, as illustrated above. 

Wrist Joint`wrist`\- Control the joint lengths, as illustrated above. 

## 

Parameters - Transforms Page

When the arm is positioned to reach the end affector (hand print), the shoulder, elbow and wrist joints may produce unnatural looking bends. The transform fields allow manual adjustment of each controlling circle of each joint to fix this. 

Each joint circle (e.g. Shoulder 1) is given three transform fields (two translates and one scale). These values are scaled by the amount of bend applied to the particular joint. In other words, when the arm is fully extended, the transforms have no effect. When the arm joint angles are at 90, they have maximum effect. Thus, set the joints to 90 before adjusting these values. 

Shoulder 1`shoulder1t`\- ⊞ \- The X, Z position of the first shoulder circle, as well as its overall scale. 
* X`shoulder1tx`\- The X position of the first shoulder circle.
* Y`shoulder1ty`\- The Z position of the first shoulder circle. (**Note:** the parameter is labelled Y).
* Z`shoulder1tz`\- The overall scale of the first shoulder circle. (**Note:** the parameter is labelled Z).


Shoulder 2`shoulder2t`\- ⊞ \- The X, Z position of the second shoulder circle, as well as its overall scale. 
* X`shoulder2tx`\- The X position of the second shoulder circle.
* Y`shoulder2ty`\- The Z position of the second shoulder circle. (**Note:** the parameter is labelled Y).
* Z`shoulder2tz`\- The overall scale of the second shoulder circle. (**Note:** the parameter is labelled Z).


Shoulder 3`shoulder3t`\- ⊞ \- The X, Z position of the third shoulder circle, as well as its overall scale. 
* X`shoulder3tx`\- The X position of the third shoulder circle.
* Y`shoulder3ty`\- The Z position of the third shoulder circle. (**Note:** the parameter is labelled Y).
* Z`shoulder3tz`\- The overall scale of the third shoulder circle. (**Note:** the parameter is labelled Z).


Shoulder 4`shoulder4t`\- ⊞ \- The X, Z position of the fourth shoulder circle, as well as its overall scale. 
* X`shoulder4tx`\- The X position of the fourth shoulder circle.
* Y`shoulder4ty`\- The Z position of the fourth shoulder circle. (**Note:** the parameter is labelled Y).
* Z`shoulder4tz`\- The overall scale of the fourth shoulder circle. (**Note:** the parameter is labelled Z).


Shoulder 5`shoulder5t`\- ⊞ \- The X, Z position of the fifth shoulder circle, as well as its overall scale. 
* X`shoulder5tx`\- The X position of the fifth shoulder circle.
* Y`shoulder5ty`\- The Z position of the fifth shoulder circle. (**Note:** the parameter is labelled Y).
* Z`shoulder5tz`\- The overall scale of the fifth shoulder circle. (**Note:** the parameter is labelled Z).


Elbow 1`elbow1t`\- ⊞ \- The X, Z position of the first elbow circle, as well as its overall scale. 
* X`elbow1tx`\- The X position of the first elbow circle.
* Y`elbow1ty`\- The Z position of the first elbow circle. (**Note:** the parameter is labelled Y).
* Z`elbow1tz`\- The overall scale of the first elbow circle. (**Note:** the parameter is labelled Z).


Elbow 2`elbow2t`\- ⊞ \- The X, Z position of the second elbow circle, as well as its overall scale. 
* X`elbow2tx`\- The X position of the second elbow circle.
* Y`elbow2ty`\- The Z position of the second elbow circle. (**Note:** the parameter is labelled Y).
* Z`elbow2tz`\- The overall scale of the second elbow circle. (**Note:** the parameter is labelled Z).


Elbow 3`elbow3t`\- ⊞ \- The X, Z position of the third elbow circle, as well as its overall scale. 
* X`elbow3tx`\- The X position of the third elbow circle.
* Y`elbow3ty`\- The Z position of the third elbow circle. (**Note:** the parameter is labelled Y).
* Z`elbow3tz`\- The overall scale of the third elbow circle. (**Note:** the parameter is labelled Z).


Elbow 4`elbow4t`\- ⊞ \- The X, Z position of the fourth elbow circle, as well as its overall scale. 
* X`elbow4tx`\- The X position of the fourth elbow circle.
* Y`elbow4ty`\- The overall scale of the fourth elbow circle. (**Note:** the parameter is labelled Z).
* Z`elbow4tz`\- The overall scale of the fourth elbow circle. (**Note:** the parameter is labelled Z).


Elbow 5`elbow5t`\- ⊞ \- The X, Z position of the fifth elbow circle, as well as its overall scale. 
* X`elbow5tx`\- The X position of the fifth elbow circle.
* Y`elbow5ty`\- The overall scale of the fifth elbow circle. (**Note:** the parameter is labelled Z).
* Z`elbow5tz`\- The overall scale of the fifth elbow circle. (**Note:** the parameter is labelled Z).


Wrist 1`wrist1t`\- ⊞ \- The X, Z position of the first wrist circle, as well as its overall scale. 
* X`wrist1tx`\- The X position of the first wrist circle.
* Y`wrist1ty`\- The overall scale of the first wrist circle. (**Note:** the parameter is labelled Z).
* Z`wrist1tz`\- The overall scale of the first wrist circle. (**Note:** the parameter is labelled Z).


Wrist 2`wrist2t`\- ⊞ \- The X, Z position of the second wrist circle, as well as its overall scale. 
* X`wrist2tx`\- The X position of the second wrist circle.
* Y`wrist2ty`\- The overall scale of the second wrist circle. (**Note:** the parameter is labelled Z).
* Z`wrist2tz`\- The overall scale of the second wrist circle. (**Note:** the parameter is labelled Z).


Wrist 3`wrist3t`\- ⊞ \- The X, Z position of the third wrist circle, as well as its overall scale. 
* X`wrist3tx`\- The X position of the third wrist circle.
* Y`wrist3ty`\- The overall scale of the third wrist circle. (**Note:** the parameter is labelled Z).
* Z`wrist3tz`\- The overall scale of the third wrist circle. (**Note:** the parameter is labelled Z).


Wrist 4`wrist4t`\- ⊞ \- The X, Z position of the fourth wrist circle, as well as its overall scale. 
* X`wrist4tx`\- The X position of the fourth wrist circle.
* Y`wrist4ty`\- The overall scale of the fourth wrist circle. (**Note:** the parameter is labelled Z).
* Z`wrist4tz`\- The overall scale of the fourth wrist circle. (**Note:** the parameter is labelled Z).


Wrist 5`wrist5t`\- ⊞ \- The X, Z position of the fifth wrist circle, as well as its overall scale. 
* X`wrist5tx`\- The X position of the fifth wrist circle.
* Y`wrist5ty`\- The overall scale of the fifth wrist circle. (**Note:** the parameter is labelled Z).
* Z`wrist5tz`\- The overall scale of the fifth wrist circle. (**Note:** the parameter is labelled Z).

## 

Parameters - End Affector Page

Affector Object`affector`\- Allows the end affector to be another object, or simply defined by a default box, which is controlled by the transformations below. 

Translate`t`\- ⊞ \- End Affector Translation. For a full explanation of transforms, see the [Transform SOP](<./Transform_SOP.md> "Transform SOP"). 
* X`tx`\- End Affector X Translate.
* Y`ty`\- End Affector Y Translate.
* Z`tz`\- End Affector Z Translate.


Rotate`r`\- ⊞ \- End Affector Rotation. For a full explanation of transforms, see the [Transform SOP](<./Transform_SOP.md> "Transform SOP"). 
* X`rx`\- End Affector X Rotate.
* Y`ry`\- End Affector Y Rotate.
* Z`rz`\- End Affector Z Rotate.


Scale`s`\- ⊞ \- End Affector Scale. For a full explanation of transforms, see the [Transform SOP](<./Transform_SOP.md> "Transform SOP"). 
* X`sx`\- End Affector X Scale.
* Y`sy`\- End Affector Y Scale.
* Z`sz`\- End Affector Z Scale.

## 

Info CHOP Channels

Extra Information for the Arm SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\n2022.241402021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• Arm • [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
