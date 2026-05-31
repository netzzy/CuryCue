# Sort SOP

##   
  
Summary

The Sort SOP allows you to sort points and primitives in different ways. Sometimes the primitives are arranged in the desired order, but the point order is not. There are many possible combinations. To sort vertices, use the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[sortSOP_Class](</SortSOP_Class> "SortSOP Class")

## 

Parameters - Point Page

Point Sort`ptsort`\- ⊞ \- Sort the points in the input geometry, according to the following criteria: 
* No change`none`\- No sorting is applied.
* By vertex order`vtxord`\- Order points in same order as vertices.
* By x`byx`\- Sort according to X position.
* By y`byy`\- Sort according to Y position.
* By z`byz`\- Sort according to Z position.
* Reverse`rev`\- Reverse the point order.
* Random`seed`\- Randomize point order using the specified seed without changing the point positions.
* Shift`shift`\- Shift points by the amount specified on the Offset parameter.
* Proximity to Point`prox`\- Sort points by their proximity to the specified point.
* Along Vector`vector`\- Sorts points along either a user or object-defined vector.
* Distance to Object`object`\- Sorts points based on distance to the object specified in the Vector Object parameter.
* Closest Neighbour`neighbour`\- Reorders points based on next closest. Slow nxn search.


Seed`pointseed`\- The random seed when Point Sort is set to Random. 

Offset`pointoffset`\- Shift point order by the amount specified on the offset line. 

Point`pointprox`\- ⊞ \- The X, Y and Z coordinates to reference when sorting by Proximity to Point. 
* X`pointproxx`-
* Y`pointproxy`-
* Z`pointproxz`-


Vector Object`pointobj`\- Sort points along a vector defined by the object's transformation values. 

Vector`pointdir`\- ⊞ \- Allows you to specify a unique vector along which points can be sorted. 
* X`pointdirx`-
* Y`pointdiry`-
* Z`pointdirz`-

## 

Parameters - Primitive Page

Primitive Sort`primsort`\- ⊞ \- Sort the primitives according to the following criteria: 
* No change`none`\- No sorting is applied.
* By x`byx`\- Sort according to X position.
* By y`byy`\- Sort according to Y position.
* By z`byz`\- Sort according to Z position.
* By Type`bytype`-
* Reverse`rev`\- Reverse primitive order.
* Random`seed`\- Randomize primitive order using the specified seed without changing the primitive positions.
* Shift`shift`\- Shift primitives by the amount the specified on the Offset parameter.
* Proximity to Point`prox`\- Sort primitives by their proximity to the specified point.
* Along Vector`vector`\- Sorts primitives along either a user or object-defined vector.
* Distance to Object`object`\- Sorts primitive based on distance to the object specified in the Vector Object parameter.


Seed`primseed`\- Random seed when sorting by Random. 

Offset`primoffset`\- Shift primitive order by the amount specified on the offset line. 

Point`primprox`\- ⊞ \- The X, Y and Z coordinates to reference when sorting by Proximity to Point. 
* X`primproxx`-
* Y`primproxy`-
* Z`primproxz`-


Vector Object`primobj`\- Sort primitives along a vector defined by the object's translation. 

Vector`primdir`\- ⊞ \- Allows you to specify a unique vector along which primitives can be sorted. 
* X`primdirx`-
* Y`primdiry`-
* Z`primdirz`-

## 

Parameters - Particle Page

Particles are sorted on a per-particle system basis. That is if you have a SOP with 2 different particle system primitives, they are sorted independently of each other. 

Particle Sort`partsort`\- ⊞ \- Sort the primitives according to the following criteria: 
* No change`none`\- No sorting is applied.
* By x`byx`\- Sort according to X position.
* By y`byy`\- Sort according to Y position.
* By z`byz`\- Sort according to Z position.
* Reverse`rev`\- Reverse particle order.
* Shift`shift`\- Shift particles by the amount the specified on the Offset parameter.
* Proximity to Point`prox`\- Sort particle by their proximity to the specified point.
* Along Vector`vector`\- Sorts particles along either a user or object-defined vector.
* Distance to Object`object`\- Sorts particles based on distance to the object specified in the Vector Object parameter.


Reverse Results`partreverse`\- Reverses the result from the Particle Sort as defined above. 

Offset`partoffset`\- Shift particle order by the amount specified on the offset line. 

Point`partprox`\- ⊞ \- The X, Y and Z coordinates to reference when sorting by Proximity to Point. 
* X`partproxx`-
* Y`partproxy`-
* Z`partproxz`-


Vector Object`partobj`\- Sort particles along a vector defined by the object's translation. 

Vector`partdir`\- ⊞ \- Allows you to specify a unique vector along which particles can be sorted. 
* X`partdirx`-
* Y`partdiry`-
* Z`partdirz`-

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Sort SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• Sort • [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
