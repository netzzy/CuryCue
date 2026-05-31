# Clay SOP

## 

Summary

The Clay SOP deforms faces and surfaces by pulling points that lie directly on them. As opposed to the Point SOP or other SOPs that manipulate control points (CVs), the Clay SOP operates on the primitive contours themselves, providing a direct, intuitive, and unconstrained way of reshaping geometry. Thus, rather than translating CVs to change the aspect of the primitive, the Clay SOP takes the inverse approach of manipulating the primitive's skin to reposition the CVs. 

The point that defines the area to be modified is called a "target point" or "target" for short. It is expressed as a (u,v) pair in the parametric space of the primitive and ranges between 0 and 1 in both U and V. The image of the target point on the primitive is a 3D point which Clay can displace in several ways. Furthermore, if the primitive is a surface, there is are options to pull only the point or a whole isoparametric curve in either U or V. 

Clay does not refine the faces and surfaces unless asked to, so the complexity of the geometry does not increase. The area affected by the change varies with each primitive type and topology. In all cases it is possible to reduce to amount of change by inserting a Refine SOP before the Clay SOP and inserting detail around the target point. For other ways to increase the locality of the deformation as well as its sharpness, see U and V Sharpness below. 

If a second input is present, it is possible to snap the target (u,v) point to an (s,t) point on the first primitive of the second input. Without a second input, the primitives can be made to snap to themselves. Moreover, the Clay SOP is able to snap the target to arbitrary points in space. 

Both this SOP and the Align SOP can be used effectively as snapping tools and building blocks for curve networks. The main difference between the two SOPs is that Clay deforms the inputs partially, while Align translates and/or rotates the whole primitive. 

The Clay SOP accepts a mix of any combination of face and surface types. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[claySOP_Class](<./ClaySOP_Class.md> "ClaySOP Class")

## 

Parameters - Clay Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in Pattern Matching in the [Scripting Guide]. 

Warp Method`method`\- ⊞ \- The following describe the four types of transformations the Clay SOP can apply to the target (U, V) points or isoparametric curves (U or V). All the transformations are exclusive, and all reduce to a signed translation along a direction. The difference between the various transformations is the way the translation and the direction are specified. 
* Matrix`mat`\- The matrix method relocates the target point based on a transformation matrix. For a description of transforms, see the [Transform SOP](<./Transform_SOP.md> "Transform SOP").
* Vector`vec`\- The vector method provides a distance and a vector to translate along.
* Point`point`\- The point method provides a 3D point in object space that the target point must snap to.
* Primitive`prim`\- The primitive method allows the target point to be snapped to a point on another primitive. Any primitive type is allowed, including metaballs, all quadrics, and even particle systems. The point on the destination primitive is expressed parametrically as a (U, V) pair.


If the Clay SOP has a second input, then the destination primitive is going to be the first primitive in that input. If there is no second input, the primitives in the first input will snap to themselves (each face or surface to itself). 

Transform Order`xord`\- ⊞ \- Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`rord`\- ⊞ \- Sets the order of the rotations within the overall transform order. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`t`\- ⊞ \- These three fields move the Source geometry in the three axes. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- These three fields rotate the Source geometry in the three axes. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Scale`s`\- ⊞ \- These three fields scale the Source geometry in the three axes. 
* X`sx`-
* Y`sy`-
* Z`sz`-


Pivot`p`\- ⊞ \- The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object. 

For example, during a scaling operation, if the pivot point of an object is located at:`-1, -1, 0`and you wanted to scale the object by`0.5`(reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left. 

In the example above, rotations performed on an object with different pivot points produce very different results. 
* X`px`-
* Y`py`-
* Z`pz`-


Distance`dist`\- Specifies the translation distance along the given vector. 

Normal`normal`\- When On, the translation will be performed along the primitive normal at the target (U, V) point. Otherwise an explicit direction is required, see Direction parameter below. If the input contains face primitives, the primitive normal is independent of the target (U) point. Primitive normals can be displayed from the Display Options dialog. 

Direction`dir`\- ⊞ \- The direction of the vector is the Normal parameter above is Off. 
* X`dirx`-
* Y`diry`-
* Z`dirz`-


Coordinates`coord`\- ⊞ \- Specifies the absolute 3D location the (U, V) target must translate to. 
* X`coordx`-
* Y`coordy`-
* Z`coordz`-


U and V`uvsnap`\- ⊞ \- The primitive method allows the target point to be snapped to a point on another primitive specified by U and V here. See Warp Method parameter for details. 

  *`uvsnap1`-


  *`uvsnap2`-


[code] 
       |opFamily=SOP
    
[/code]

}} 

## 

Parameters - U Page

Deform along U`uwarp`\- Determines whether the clay operation affects the U parametric direction. Both faces and surfaces respond to this option. If the primitives are face types and the toggle is off, clay doesn't change the inputs at all. If the inputs are surfaces and U is off, clay will pull the surfaces along the entire V direction (if V is on) or not at all. 

U`u`\- This value defines a point in the parametric space of a face, representing the location to be affected by the clay operation. This location is referred to as the "target". For surfaces, U defines a line of constant value in the parametric space of the primitive and requires a second coordinate - V - to specify a unique location (see the V> Page below). Spline faces and surfaces have explicit parametric spaces known as domains; since domains are not restricted to the unit range [0, 1], the Clay SOP maps U to the real domain value of the primitive. For polygons and meshes, U is expressed in terms of the number or vertices and columns respectively and in terms of their relative positions. 

U Bias`uusebias`\- Indicates whether the clay algorithm should use the bias it thinks works best for the given U parameter, or take the value explicitly stated beside the toggle. Since clay affects the CVs in the neighbourhood of the given parametric location, the bias can influence the amount of pull applied to the CVs on either side of this location. The effect is a slant of the "wave" the parametric point rides on - towards one side or the other. 

U Bias`ubias`\- 

U Sharpness`usharp`\- This parameter affects only NURBS curves and surfaces. The pull generated by clay on these primitives can be smooth or sharp depending on the position of the target relative to the underlying domain (the farther away from a knot, the rounded the bulge) and the knot multiplicity near the target (the higher the multiplicity the sharper the pull). If the pull is too round or affects too big an area in U, the U Sharpness parameter can reduce it by inserting one or more knots at the target U value. When the U Sharpness is zero no knots are inserted. When the U Sharpness is 1, all "degree" knots are inserted and the shape becomes very sharp. The U Sharpness varies in discrete steps; the number of steps equals the U degree of the spline. 

**Note:** The range of the U Sharpness slider varies with the degree of the spline (i.e. the closer it is to 1, the more knots it adds). Since the number of knots added forms a discrete sequence, the slider will automatically jump to the valid positions. __

## 

Parameters - V Page

Deform along V`vwarp`\- Determines whether the clay operation affects the V parametric direction of the surface. If the inputs are surfaces and V if off, clay will pull the surfaces along the entire U direction (if U is on) or not at all. If both U and V are on, clay will pull the surface at the target (U, V) point specified in the U and V folders below. This option does not affect face types. 

V`v`\- This value affects only surface types. V defines a line of constant value in the parametric space of the surface and together with U specifies a unique location in that space. Spline surfaces have explicit parametric spaces known as domains; since domains are not restricted to the unit range [0, 1], the Clay SOP maps V to the real domain value of the surface. For meshes, V is expressed in terms of the number or rows and their relative positions. 

V Bias`vusebias`\- Indicates whether the clay algorithm should use the bias it thinks works best for the given V parameter, or take the value explicitly stated beside the toggle. Since clay affects the CVs in the neighbourhood of the given parametric location, the bias can influence the amount of pull applied to the CVs on either side of this location. The effect is a slant of the "wave" the parametric point rides on -- towards one side or the other. 

V Bias`vbias`\- 

V Sharpness`vsharp`\- This parameter affects only NURBS surfaces. The pull generated by clay on these primitives can be smooth or sharp depending on the position of the target relative to the underlying domain (the farther away from a knot, the rounded the bulge) and the knot multiplicity near the target (the higher the multiplicity the sharper the pull). If the pull is too round or affects too big an area in V, the V Sharpness parameter can reduce it by inserting one or more knots at the target V value. When the V Sharpness is zero no knots are inserted. When the V Sharpness is 1, all "degree" knots are inserted and the surface becomes very sharp. The V Sharpness varies in discrete steps; the number of steps equals the V degree of the spline. 

**Note:** The range of the V Sharpness slider varies with the degree of the spline (i.e. the closer it is to 1, the more knots it adds). Since the number of knots added forms a discrete sequence, the slider will automatically jump to the valid positions. __

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Clay SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• Clay • [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
