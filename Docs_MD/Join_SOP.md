# Join SOP

##   
  
Summary

The Join SOP connects a sequence of faces or surfaces into a single primitive that inherits their attributes. Faces of different types can be joined together, and so can surfaces. Mixed face-surface types are not allowed. The surfaces do not have to have the same number of rows or columns in the side being joined. Spline types of different orders and parameterization are all valid inputs. The Join SOP converts simpler primitives such as polygons into Bziers and NURBS if necessary. 

Joining is different from filleting (see [Fillet SOP](<./Fillet_SOP.md> "Fillet SOP")) or stitching (see [Stitch SOP](<./Stitch_SOP.md> "Stitch SOP")) because it takes n primitives and converts them into one after possibly changing the connected ends of the primitives. Filleting creates a new primitive between each input pair and never affects the original shapes. Stitching changes the original shapes but does not change the number of resulting primitives. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[joinSOP_Class](<./JoinSOP_Class.md> "JoinSOP Class")

## 

Parameters - Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Blend`blend`\- Determines the way the primitives are joined. A blended face or surface will typically reposition the ends to be joined and convert them into a single, common point, row or column respectively. The amount of change can be reduced or eliminated by lowering the tolerance (see Tolerance below). When not blended, the original shapes remain unaffected. Instead, the chosen ends are joined by an arc-like fillet. In either case, the result is a single primitive. 

Tolerance`tolerance`\- The meaning of the tolerance varies with the type of join. The shapes of blended primitives will change less if the tolerance is low. If the tolerance is <`1`, a new point, knot, row or column is inserted between the last and before-last point, row or column. The lower the tolerance, the closer the insertion to the ends being pulled together, and thus the smaller the region affected. When the tolerance is zero the blended inputs do not change at all: the faces are connected by a straight line and the surfaces by a flatish, linear patch. 

Tolerance also affects the size and roundness of the fillet built between non-blended primitives. A zero tolerance yields a short, flat fillet; a unit tolerance generates pointed, non self-intersected fillet. __

Bias`bias`\- Affects only blended primitives by varying the position of the common point, row or column linearly between the two original ends. If the bias is zero, the common part will coincide with the end of the second primitive and the end of the first primitive will be stretched all the way to it. If the bias is one, the common part will coincide with the end of the first primitive and the second primitive will be stretched. 

The bias is irrelevant when the blend tolerance is 0. __

Multiplicity`knotmult`\- Affects the number of knots inserted at the blend point and thus allows for smooth or pointed connections. The connection will be pointed when the Multiplicity is on. When Blend is not on, an active multiplicity influences the shape and the tightness of the fillet by forcing a multiple knot insertion when on. 

The fillet tends to be better behaved when multiplicity in on. However, this means that the resulting face or surface is built with a discontinuity at the connection points and might not lend itself to point modeling in that area too well. 

Multiplicity has no effect on polygons and meshes. __

Connect Closest Ends`proximity`\- The Join SOP connects the tail of the first primitive with the head on the next primitive, and so on unless this toggle is on, in which case the closest ends are chosen instead. For surfaces, this option enables the proximity test in U or V, as specified in the Direction parameter below. 

Direction`dir`\- ⊞ \- This menu determines the parametric direction of the joining operation, which can be in U or in V, and is meaningful only when the inputs are surfaces. The U direction is associated with columns; the V direction refers to rows. For example, joining two surfaces in U will generate a surface with more columns than either input. The number of rows might be higher too, but only if the two inputs have a different number of rows or a different V basis. 
* in U`ujoin`-
* in V`vjoin`-


Join`joinop`\- ⊞ \- Can optionally join subgroups of n primitives or every nth primitive in a cyclical manner. 

**For Example** ; assume there are six primitives numbered for 0 - 5, and N = 2. Then, 
1. Groups will generate 0-1 2-3 4-5
  2. Skipping will generate 0-2-6 and 1-3-5.
* All Primitives`all`-
* Groups of N Primitives`group`-
* Skip Every Nth Primitive`skip`-


N`inc`\- Determines the number of primitives to be either grouped or skipped. N2. 

Wrap Last to First`loop`\- If enabled, it connects the beginning of the first primitive to the end of the last primitive, thus forming a single, closed face or hull. If a single, open primitive exists in the input, it will be closed. The [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP") provides a more direct way of closing primitives but offers almost no shape controls. 

Keep Primitives`prim`\- If this button is not checked, the input primitives will be deleted after being joined. If checked, they will be preserved. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Join SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• Join • [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
