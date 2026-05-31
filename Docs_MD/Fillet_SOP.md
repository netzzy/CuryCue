# Fillet SOP

## 

Summary

The Fillet SOP is used to create smooth bridging geometry between two curves / polygons or two surfaces / meshes. 

Filleting creates a new primitive between each input pair and never affects the original shapes. This is in contrast to the [Join](<./Join_SOP.md> "Join SOP") and [Stitch SOPs](<./Stitch_SOP.md> "Stitch SOP"). The [Join SOP](<./Join_SOP.md> "Join SOP") converts and possibly changes the connected ends of primitives, and stitching changes the original shapes but does not change the number of resulting primitives. 

Please refer to the [Align SOP](<./Align_SOP.md> "Align SOP") for a discussion of "left" and "right" primitives as well as the option of an auxiliary input. 

Note: Trim curves are not taken into account by a fillet. To do this, use the Join SOP. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[filletSOP_Class](<./FilletSOP_Class.md> "FilletSOP Class")

## 

Parameters - Page

Group`group`\- Which primitives to fillet. If blank, it fillets the entire input. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Fillet`fillet`\- ⊞ \- Can optionally fillet subgroups of N primitives or every nth primitive in a cyclical manner. 

**Example** : Assume there are six primitives numbered for 0 - 5, and N = 2. Then: 
1. Groups will fillet 0-1 2-3 4-5
  2. Skipping will fillet 0-2-6 and 1-3-5.
* All Primitives`all`-
* Groups of N Primitives`group`-
* Skip Every Nth Primitive`skip`-


N`inc`\- Determines the number of primitives to be either grouped or skipped. 

Wrap Last to First`loop`\- Connects the beginning of the first primitive to the end of the last primitive filleted, or, if only one primitive exists, it creates a fillet between its ends. 

Direction`dir`\- ⊞ \- This menu determines the parametric direction of the filleting operation, which can be in U or in V, and is meaningful only when the inputs are surfaces. The U direction is associated with columns; the V direction refers to rows. 
* in U`ujoin`-
* in V`vjoin`-


Fillet Type`fillettype`\- ⊞ \- Select which type of fillet to use in this menu. 
* Freeform`freeform`\- Allows full specifications of the fillet.
* Convex`convex`\- May negate scale values to ensure convex fillets.
* Circular`circular`\- Attempts to build a fillet as close to a radial arc as the shape and orientation of the inputs permit. You do not need to specify a radius - it is automatically determined to ensure a smooth connection between the inputs. As the two inputs come into proximity of each other, the fillet radius decreases. The tangent scales are ignored (as in the [Bridge SOP](<./Bridge_SOP.md> "Bridge SOP")); only the sign of the tangent is taken into account in order to save you from needing to flip the normals of either input.


Primitive Type`primtype`\- ⊞ \- Select what type of primitive will be created by the fillet in this menu. 
* Input Geometry Type`input`\- Builds a fillet of the matching type between pairs of primitives. If the pair of primitives are different types, then the most general type is used (i.e. NURBS over Bzier, Bzier over polygons).
* Polygon`polygon`\- Builds a polygonal fillet between pairs of primitives.
* NURBS`nurbs`\- Builds a NURBS fillet between pairs of primitives at the given order.
* Bezier`bezier`\- Builds a Bzier fillet between pairs of primitives at the given order.


Order`order`\- Order at which to build the spline fillets. 

Left UV`leftuv`\- ⊞ \- Parametric point on each left primitive at which to begin the fillet. 

  *`leftuv1`-


  *`leftuv2`-


Right UV`rightuv`\- ⊞ \- Parametric point on each right primitive at which to begin the fillet. 

  *`rightuv1`-


  *`rightuv2`-


LR Width`lrwidth`\- ⊞ \- The first value represents the proportion of the left primitive that the left end of the fillet spans. The second value represents the proportion of the right primitive that the right end of the fillet spans. 

  *`lrwidth1`-


  *`lrwidth2`-


LR Scale`lrscale`\- ⊞ \- Use to control the direction and scale of the first and last segments of the fillet. 

  *`lrscale1`-


  *`lrscale2`-


LR Offset`lroffset`\- ⊞ \- Controls the position of the first and last segments of the fillet. 

  *`lroffset1`-


  *`lroffset2`-


Match Input to Fillets`seamless`\- If selected, then the inputs are modified in such a way that the isoparms appear continuous from one primitive, through the fillet to the other primitive. Also, the primitives are promoted to the same type and order. This will minimize if not eliminate any artifacts introduced in rendering at the cost of more refined geometry. 

Cut Primitives`cut`\- If selected, the primitives are trimmed at the point the fillet begins. 

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Fillet SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• Fillet • [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
