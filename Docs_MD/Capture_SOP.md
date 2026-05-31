# Capture SOP

##   
  
Summary

The Capture SOP is used to weight points in a geometry to capture regions. The weighting scheme is described in the next section, [Capture Region SOP](<./Capture_Region_SOP.md> "Capture Region SOP"). 

The weights and the regions they correspond to are transferred down the SOP chain as point and detail attributes. 

The Capture SOP can take an optional second input to specify extra capture regions to use in the capture process. Any capture regions that are in this second input are processed after the capture regions that are in the object hierarchy specified by the Hierarchy parameter. You can also specify a second input and not specify a Parent Object at all. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[captureSOP_Class](<./CaptureSOP_Class.md> "CaptureSOP Class")

## 

Parameters - Capture Page

Group`group`\- Specify the point groups from the first input (input0) to operate on. 

Hierarchy`rootbone`\- An object hierarchy is traversed to find the Capture Regions with which to do the weighting. This parameter specifies the top of the traversal hierarchy. 

Weight from`weightfrom`\- ⊞ \- Use this menu to specify where to get the weight from. 
* Surface`surface`\- (default) Uses the surface to compute the weight of a point (or CV in the case of NURBS). This is very helpful for NURBS surfaces when the CV's may be far off the surface. By using Weight From Surface, each CV is weight based on the surface's location within a Capture Region. This is determined by calculating the CVs "most influenced point" on the NURBS surface and computing the weight of that position.
* Points`cv`\- Using the Weight From Points choice, the location of the point within the region is used for the weighting.


Capture Frame`captframe`\- Specifies the frame number to do the capture computations. Every time TouchDesigner reaches this frame, the geometry will be re-captured. It is a common practice to set the Capture Frame to an frame outside of your animation range, -1 for example. Specifies the frame number to do the capture computations. Every time TouchDesigner reaches this frame, the geometry will be re-captured. It is a common practice to set the Capture Frame to an frame outside of your animation range, -1 for example. 

**Note:** When a .toe file is loaded, all of the associated capture regions are evaluated at the Capture Frame. Keyframes must be set to position the capture regions properly at the Capture Frame, otherwise the geometry will be weighted incorrectly upon the subsequent file loads. __

Point Coloring`color`\- ⊞ \- This option colors each point by capture region (using point attributes) according to its capture weight. The points inherit their colors from the Capture Region(s) in which they lie. For example, if a point falls within a blue capture region and also a yellow capture region, the point will be colored green (more blue near if the blue weighting dominates, and more yellow if the yellow weight dominates). In addition, the points become darker as the weighting gets lighter. For example, near the edge of a blue region, a caught point will appear dark blue. Near the centre, it will appear bright blue. If a point is not caught by any region, it is colored bright red. 
* Default Source Color`coldefault`-
* Color by Capture Region`colregion`-


Override File`captfile`\- The name of the capture override file (`*.ocapt`). This file is loaded after TouchDesigner completes its point weighting. Each line of the override file lists a point number, a region (path and primitive number) and a weight. The points on the geometry are modified to use these custom weights. 

**Override File Format** \- Each line in the override file must have the following format: 

For example: 
[code] 
    0 /obj/chain_bone1/cregion 0 0.0 			
    0 /obj/chain_bone2/cregion 0 3.757989 			
    0 /obj/chain_bone3/cregion 0 1.757989			
    
[/code]

  
This weights point 0 to three regions (actually only two because the first entry has a weight of zero). Remember that the Override File is read after TouchDesigner does it's own capture weight computation, so in this case, if point 0 was originally assigned to region`/obj/chain_bone4/cregion 0`, this part of its weighting would be unchanged. There is no upper limit to the number of regions that can be weighted to a point. If a point/region combination is in the file twice, the second one is used. 

For example: 
[code] 
    0 /obj/chain_bone1/cregion 0 1.0			
    0 /obj/chain_bone1/cregion 0 2.0			
    
[/code]

This causes the first entry to be ignored (a weighting of 2.0 is used). 

The weight field is used to prescribe the relative amount of influence a region has on a point. It can be any number. The range of the weights computed by TouchDesigner are specified by the Inner/Outer Weight parameter of each Capture Region (please see [Capture Region SOP](<./Capture_Region_SOP.md> "Capture Region SOP")). The easiest way to a capture Override File is to use the Save Override File button (see below) and start from the file produced by TouchDesigner. __

## 

Parameters - Override Page

Save File`savefile`\- The file specified here can be used as a "working file" to save the point weighting of all the points or a selected subset of points. The file format for the capture override files is fairly straight-forward (see above), so this is a good place to start if you need to do custom overriding. 

Increment Save File`autoincr`\- This increments the Save File name before saving. Be careful about turning this option off because there is no warning or confirm dialog to prevent you from overwriting an .ocapt file. 

Save All Data to File`savecaptfile`\- This saves the point weighting of all points to the Save File. 

Save Selected Points to File`savesel`\- This saves the point weighting only for the points that are selected in the viewport. 

Note: you must be editing this particular SOP in the Viewport for this selection to apply to this SOP. __

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Capture SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• Capture • [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
