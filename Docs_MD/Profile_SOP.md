# Profile SOP

## 

Summary

The Profile SOP enables the extraction and manipulation of profiles. 

You will usually need a [Trim SOP](<./Trim_SOP.md> "Trim SOP"), [Bridge SOP](<./Bridge_SOP.md> "Bridge SOP"), or Profile SOP after a [Project SOP](<./Project_SOP.md> "Project SOP"). Use a Trim SOP to cut a hole in the projected surface. Use a Bridge SOP to skin the profile curve to another profile curve. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[profileSOP_Class](<./ProfileSOP_Class.md> "ProfileSOP Class")

## 

Parameters - Profile Page

Group`group`\- This field allows you to specify the particular group of curves on the surface. Other primitives are ignored. You can specify profile curves within the group by providing a profile pattern (e.g. *.3 specifies the fourth profile in all spline surfaces). 

Method`method`\- ⊞ \- This menu allows you to extract a stand-alone 3D curve as the world or parametric image of the profile. The non-parametric option will yield a curve whose shape and position in space are identical or very similar to those of the chosen profile. The parametric option will produce a planar, XY face whose vertices and type will be identical to those of the profile in 2D; also, if the profile is a spline it will have the same basis as the extracted curve. 
* Extract`extract`\- Use the extraction parameters below to extract a 3D curve from the profile.
* Remap`remap`\- Use parametric parameters below to produce a planar face from the profile.


Parametrically to X Y`parametric`\- If Fitted (this option not checked), the profile will be a spatial NURBS curve whose position and shape in space will be identical to the curve on surface. It may very well be non-planar. If Extracted Parametrically (this option checked), the result will extract the profile's parametric image as a 3D face, which will be a planar face in XY whose type (polygon, Bzier, NURBS) will the same as the profile's, and whose vertices match the profile CVs. This, however, does not guarantee spatial coincidence between profile and extracted curve, and is more of an analytical tool. 

**Tip:** A profile extracted parametrically can be reapplied to the surface identically with the Project SOP by choosing the **Parametric** option with no Mapping to Range. Use this method to extract the profile, pull its points or edit it as you would any 3D face, then re-project it on the surface at the same location. __

Smooth Curve`smooth`\- If enabled, it will fit a spline through the extracted points. This parameter is disabled when extracting the profile parametrically. Disable this parameter in order to bypass the fitting process which might be both expensive (in processing speed) and unnecessary when extracting profiles produced by boolean operations (see [Surfsect SOP](<./Surfsect_SOP.md> "Surfsect SOP")). 

Divisions per Span`sdivs`\- The number of points per span to be computed on the profile. A span is the line connecting two consecutive CVs on a polygon, or the arc between two breakpoints on a spline curve. The profile tends to become more accurate as the number of divisions is higher. 

Tolerance`tolerance`\- This parameter specifies the precision of the fitting process for the extracted 3D data, and is typically less than 0.01. 

Order`order`\- The spline order of the resulting 3D curve. The type of curve (Bzier or NURBS) is inherited from the spatial curve. The order, however, is not inherited because the spline order provides useful control over the quality of the fit. If the profile is a polygon, the spatial curve will be a NURBS curve. 

Preserve Sharp Corners`csharp`\- Controls the precision with which sharp corners in the profile curve are interpolated. It should be on when the profile has areas of high changes in curvature. 

Keep Surface`keepsurf`\- Specifies whether the parent surface should be removed after the extraction or not. 

Delete Original Profile`delprof`\- When Keep Surface parameter is On, select whether to leave or delete the original profile. 

Mapping Type`maptype`\- ⊞ \- Select how to reposition and scale an existing profile to fit within the specified domain range. It is a good means of bringing an invisible profile into view by setting the mapping range between 0 and 1 in the U and V parametric directions. A profile mapped outside the unit domain becomes invisible but is not removed from the surface. Other ways to change a profile are available through the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP"). 
* Uniform`unif`\- Uniform converts the spatial coordinates of the profile to (U,V) points in the domain of the surface without taking into account the parameterization of the surface.
* Chord Length`chordlen`\- Chord Length takes into account the surface parameterization and attempts to compute a profile best suited to the spatial and parametric determinants of the model.


U Range`urange`\- ⊞ \- Indicates in percentages what part of the U surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the U parametric direction. The range is not restricted to the 0-1 interval. 

  *`urange1`-


  *`urange2`-


V Range`vrange`\- ⊞ \- Indicates in percentages what part of the V surface domain is the mapping area. A full range of 0-1 will cause the profiles to be mapped to the entire domain in the V parametric direction. The range is not restricted to the 0-1 interval. 

  *`vrange1`-


  *`vrange2`-

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Profile SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• Profile • [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
