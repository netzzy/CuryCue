# Refine SOP

## 

Summary

The Refine SOP allows you to increase the number of CVs in any NURBS, Bzier, or polygonal surface or face without changing its shape. It is also used to decrease the number of CVs within a given tolerance (i.e. a simple but fast method of data reduction). 

### 

The Difference Between Refinement and Unrefinement

Refinement and unrefinement work both on faces (polygons, Bzier curves and NURBS curves) and surfaces (primitive meshes, Bzier surfaces and NURBS surfaces). To unrefine a face or a surface you need to specify a parametric interval (not just a single value as in refinement). This allows you to unrefine primitives within arbitrary intervals, either locally or globally. For example, to unrefine the whole primitive choose 0 and 1 as the two parametric boundaries; [0,0.5] will unrefine only the first parametric half of the primitive. 

The interval boundaries are given by the First/Second U/V fields. Since refinement does not need an interval, the Second U/V fields are disabled by default. 

The Tolerance control is only available for unrefinement, and not for refinement. Refinement does not need tolerances because it generates a curve or a surface that is mathematically identical to the original. Unrefinement, however, may tend to smooth out (or "melt") the original in a given area. In short, unrefinement is lossy; refinement isn't. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[refineSOP_Class](<./RefineSOP_Class.md> "RefineSOP Class")

## 

Parameters - Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

First U`firstu`\- Enable or disable the First U controls. 

First U`domainu1`\- This specifies a starting / ending location to complete the operation. Select this and a parametric U location between 0 and 1. 

Second U`secondu`\- Enable or disable the Second U controls. 

Second U`domainu2`\- This specifies a starting / ending location to complete the operation. Select this and a parametric U location between 0 and 1. 

U Divisions`divsu`\- If refining or sub-dividing, this option specifies the number of refines to be performed between First U and Second U. 

First V`firstv`\- Enable or disable the First V controls. 

First V`domainv1`\- This specifies a starting / ending location to complete the operation. Select this and a parametric V location between 0 and 1. 

Second V`secondv`\- Enable or disable the Second V controls. 

Second V`domainv2`\- This specifies a starting / ending location to complete the operation. Select this and a parametric V location between 0 and 1. 

V Divisions`divsv`\- If refining or sub-dividing, this option specifies the number of refines to be performed between First V and Second V. 

## 

Parameters - Refine Page

If enabled, will refine the primitive at the locations specified above. If the primitive is a NURBS, then a knot is inserted multiple times as described below. 

NURB Count U`refineu`\- Number of knots to insert at each location in the U / V basis when refining NURBS. 

NURB Count V`refinev`\- Number of knots to insert at each location in the U / V basis when refining NURBS. 

Spacing`space`\- ⊞ \- Specify how to measure along splines / curves. 
* Uniform Domain Lengths`domain`\- Refine at equal basis intervals if refining a spline.
* Uniform Arc Lengths`arc`\- Each refinement is done at the centre of the maximum knot span (splines) or edge length (polygons).


**Note:** **Uniform Domain Lengths** should be selected if the domain ranges are animating, otherwise the inserted points will be undeterminable as different maximum lengths are encountered.

## 

Parameters - Unrefine Page

If enabled, will remove CVs from any NURBS curve or surface, polygon or mesh (points/ rows removed) between First U and Second U, and First V and Second V. 

NURB Count U`unrefineu`\- Number of knots to remove at each location in the U / V basis if refining NURBS. 

NURB Count V`unrefinev`\- Number of knots to remove at each location in the U / V basis if refining NURBS. 

Tolerance U`tolu`\- Only remove knots that do change the curve, polygon, or surface by more than this distance. 

Tolerance V`tolv`\- Only remove knots that do change the curve, polygon, or surface by more than this distance. 

## 

Parameters - Subdivide Page

Subdivide refines a primitive such that the subdivision causes a sharp discontinuity if ever displaced. In essence subdivide is equivalent to refine for polygons and Bziers, since any refinement causes a potential discontinuity. In the case of a NURBS it is equivalent to a maximum refinement (i.e. count = primitive basis order - 1). 

Spacing`subdivspace`\- ⊞ \- Subdivide refines a primitive such that the subdivision causes a sharp discontinuity if ever displaced. In essence subdivide is equivalent to refine for polygons and Bziers, since any refinement causes a potential discontinuity. In the case of a NURBS it is equivalent to a maximum refinement (i.e. count = primitive basis order - 1). 
* Uniform Domain Lengths`domain`\- Refine at equal basis intervals if refining a spline.
* Uniform Arc Lengths`arc`\- Each refinement is done at the centre of the maximum knot span (splines) or edge length (polygons).


**Note:** **Uniform Domain Lengths** should be selected if the domain ranges are animating, otherwise the inserted points will be undeterminable as different maximum lengths are encountered. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Refine SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• Refine • [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
