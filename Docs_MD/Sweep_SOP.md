# Sweep SOP

## 

Summary

The Sweep SOP sweeps primitives in the Cross-section input along Backbone Source primitive(s), creating ribbon and tube-like shapes. The cross-section primitives are placed at each point of the backbone perpendicular to it. The Backbone Source can have one or several primitives. If there is more than one, Sweep will sweep the cross section along each one. 

A backbone is a primitive curve that can be open or closed, but must have at least two points. The cross section input can also have multiple primitives, and can be assigned to the backbone in various ways. The origin of the cross section primitive is placed at a point on the backbone by default, but you can also choose a point number of the cross section to place. In most cases, it is best to build 1the cross section primitives in the XY plane; Sweep will automatically orient them properly along the backbone. The orientation of the cross section is based on the direction of the backbone line segment and the positive Z axis. So vertical movement in the backbone will result in the cross section rotating around backbone axis. For example, if you create the cross section in the XY plane, you can maintain its orientation (+Y Up) by building the backbone in the XZ plane. 

If the backbone primitive(s) have point colors or texture coordinates, they will be maintained and applied to the cross section primitives. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[sweepSOP_Class](</SweepSOP_Class> "SweepSOP Class")

## 

Parameters - Sweep Page

X-Section Group`xgrp`\- You can use only a subset of primitives from the Cross-section inputs by specifying a group here. 

Path Group`pathgrp`\- You can use only a subset of primitives from the Backbone inputs by specifying a group here. 

Reference Group`refgrp`\- You can use only a subset of primitives from the Reference inputs by specifying a group here. 

Cycle Type`cycle`\- ⊞ \- Determines the Cycle Type based on these menu options. 
* All Primitives at Each Point`all`\- Places all the primitives from the Cross-section input at each point on the Backbone.
* One Primitive at a Time`each`\- Similar to the above, except the transformation is applied to individual primitives rather than to the whole.
* Cycle Primitives`cycle`\- This cycles through incoming primitives when placing them on a backbone. i.e. Start with 0 at vertex 0, primitive 1 > vertex 1, etc.


Angle Fix`angle`\- Attempts to fix buckling twists that may occur when sweeping. 

Fix Flipping`noflip`\- Attempts to fix buckling twists that may occur when sweeping by fixing flipped normals. 

Remove Coincident Points on Path`skipcoin`\- When selected, any points right on top of one another will be ignored. 

Aim at Reference Points`aimatref`\- Reference Points are used in conjunction with the backbone to control the orientation of the elements along the sweep. This is done by drawing a line between the reference point and corresponding backbone point in order to determine an angle vector which determines the orientation of the cross-section profiles. Enable this parameter to allow this behaviour. 

**Note:** In order for this to work, you must supply **Reference Points** via the third input, and there must be exactly the same number of **Reference Points** as there are points in the **Backbone**. __

Use Vertex`usevtx`\- Use vertex number of the incoming cross-section to place the cross-section on the backbone. 

Connection Vertex`vertex`\- Specify a specific vertex to connect to the backbone. 

Scale`scale`\- Scales the cross sections globally. 

Twist`twist`\- Cumulative rotation of the cross sections around the backbone. If a value of five is specified, the cross section at the first point of the backbone is rotated five degrees, the next ten degrees, the next fifteen degrees and so on. 

Roll`roll`\- Non-cumulative rotation of the cross sections around the backbone. All cross sections get the same rotation. 

**Note:** The **Scale** , **Twist** and **Roll** parameters can now be controlled directly by points' attributes of the same names. Thus, combined with the [Channel SOP](<./CHOP_to_SOP.md> "CHOP to SOP"), those parameters can now be controlled dynamically. You can use scale and other attributes coming in to taper. __

## 

Parameters - Output Page

Create Groups`newg`\- Selecting this option enables the creation of groups. A group is created for each backbone that is incoming. This allows for easy skinning in the [Skin SOP](<./Skin_SOP.md> "Skin SOP"). 

Sweep Groups`sweepgrp`\- Specify the name of your output groups in this field. 

Skin Output`skin`\- ⊞ \- Determines the output based on these menu options. 
* Off`off`\- Doesn't skin the output.
* On`on`\- Skins the output.
* On with Auto Close`auto`\- Closes the skinned mesh if the path curve which it follows is also closed. This allows you to close primitives properly.


**Tip:** There is a way of speeding the skinning of many points using the second input of the [Point SOP](<./Point_SOP.md> "Point SOP"). Suppose you have Thousands of proceedurally animated curves you wish to skin with the Sweep SOP \- rather than performing a skining operation after the animation, make a second set of unanimated geometry that is preskinned. Then assuming your have a matching number of points you can just swap in the animated points into the skinned geometry. 

This technique is significantly faster than using the Skin Output option of the Sweep SOP, or a Skin SOP following the Sweep SOP. 

Fast Sweep`fast`\- Enables an optimized skinning technique which speeds up output from 2 - 4 times in many cases at the expense of accuracy. In order for it to work correctly, the input topologies must remain consistent between cooks and each cross-section must have the same number of vertices. 

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -
  * Input 2:  -

## 

Info CHOP Channels

Extra Information for the Sweep SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• Sweep • [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
