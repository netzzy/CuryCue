# Trim SOP

##   
  
Summary

The Trim SOP cuts out parts of a spline surface, or uncuts previously cut pieces. When a portion of the surface is trimmed, it is not actually removed from the surface; instead, that part is made invisible. This means that you can still modify the surface (modify the position of its points, for instance) that is not displayed in order to affect the part that is displayed. 

The surface can be trimmed by specifying open or closed profiles as inside or outside regions. The profiles need not be contained within the domain (UV space) of the surface; they can also be nested. 

Open profiles are treated as follows: if both ends of the profile are inside the surface, the ends are connected to one another; if the profile's ends are outside the domain of the surface they are projected onto, that part of the surface appears to be cut away. 

You will usually need a Trim SOP, [Bridge SOP](<./Bridge_SOP.md> "Bridge SOP"), or [Profile SOP](<./Profile_SOP.md> "Profile SOP") after a [Project SOP](<./Project_SOP.md> "Project SOP"). 
* Use a Trim SOP to cut a hole in the projected surface.
  * Use a [Bridge SOP](<./Bridge_SOP.md> "Bridge SOP") to skin the profile curve to another profile curve.
  * Use a [Profile SOP](<./Profile_SOP.md> "Profile SOP") to extract the curve on surface or remap it's position.

### 

Selection Method - Winding Rule

The selection method employed for clarifying overlapping trim loops is the winding rule, which executes overlapping commands instead of having them cancel each other out. 

**Tip:** Since only surfaces containing profile curves can be trimmed, you will always need a Project or [Carve SOP](<./Carve_SOP.md> "Carve SOP") in the chain above the Trim SOP. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[trimSOP_Class](</TrimSOP_Class> "TrimSOP Class")

## 

Parameters - Page

Group`group`\- This field allows you to specify the group that you would like to trim. You can select the group from the pop-up menu, or specify a points and primitives range. 

You can specify profile curves within the group by providing a profile pattern (e.g.`*.3`specifies the fourth profile in all spline surfaces). __`optype`\- ⊞ \- The types of trimming operations available. 
* Keep Outside`keepout`\- Trims the interior of the curve, or makes a hole in the display of the surface. Keeping what's outside the profile curve generates an outer trim loop in order to define the limits of the surface to be displayed-the surface that's outside of the profile curve.
* Keep Inside`keepin`\- Keeps the interior of the curve and removes the display of everything else.
* Keep Natural`keepnatural`\- Trim based on the natural orientation of the profiles, be they open or not. Counter-clockwise profiles keep their interior, generating a result similar to Keep Inside. Clockwise profiles discard their interior, similar to Keep Outside, and may require an explicit outer trim-loop if none is present.
* Untrim`untrim`\- Turns the trim curve into a plain profile.
* Change Altitude`chgalt`-


Process Profiles Individually`individual`\- When this option is off, the trim loops in the group (or all the loops on the surfaces if no group has been specified) will be considered together to form a region. It will report the first region that is found. That is, if more than one closed loop could be formed by joining the lines, there is no guarantee that the region is trimmed. Also, if there is a closed loop in the group of loops, then just that loop is used. 

If the loops on the surface don't form a closed loop, then the SOP will attempt to form a region by using the boundary of the region. If all the loops make a total of two intersections with the boundary, then it will attempt to form the loop by forming it around the boundary. 

**For example:** Use the [Carve SOP](<./Carve_SOP.md> "Carve SOP") to extract four profiles: two in U, and two in V. Pipe that into a Trim SOP and turn this option off. The four profiles will define a region to be trimmed. Notice that the profile end-points do not coincide, and the profiles are not parametrically continuous, nor are they created in the proper order. Despite all this, the Trim SOP is able to figure out the hole. __

Build outer Trim-Loop Explicitly`bigloop`\- This option allows you to specify that an outer trim loop be built. It is useful where you have more than one profile curve on the surface and are performing several successive trim operations involving both the Keep Inside and Keep Outside options (see example, below). 

**Tip:** An outer trim loop must be generated the first time you punch a hole in the surface, but not if you just keep the contents of that hole and throw away the rest. By default, the outer loop (which goes all around the domain boundary) is built for you automatically. Sometimes, however, you first do a **Keep Inside** , then a **Keep Outside** with an area that's not inside the preserved regions, so you may want the outer curve at that point. That is when this parameter is useful. __

Trimming Tolerance`trimtol`\- How close two trim curves must be to each other or to the edge of the patch in order to be considered an intersection. 

Altitude`altitude`\- You can specify the altitude of the trim. The`$ALTITUDE`variable is the surface's current altitude. This marks the transition for the surface from trimmed in to trimmed out. 

## 

Example

The following results were obtained by using a [Project SOP](<./Project_SOP.md> "Project SOP") to project two NURBS circles onto a NURBS grid. Then two Trim SOPs were added, one after the other, to the [Project SOP](<./Project_SOP.md> "Project SOP") . The first Trim SOP was set to Keep Inside, while the second Trim SOP had it's operation changed as indicated. 

The illustrations show a Gouraud shaded view of the resulting geometry. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Trim SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• Trim • [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
