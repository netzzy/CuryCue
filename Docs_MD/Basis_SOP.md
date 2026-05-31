# Basis SOP

## 

Summary

The Basis SOP provides a set of operations applicable to the parametric space of spline curves and surfaces. The parametric space, also known as the "domain" of a NURBS or Bzier primitive, is defined by one basis in the U direction and, if the primitive is a surface, another basis in the V direction. The size of the domain is given by the values of the knots that make up the basis. 

[![BasisSOP.gif](./images/b/b8/BasisSOP.gif)](</File:BasisSOP.gif>)

The Basis SOP contains both ratio-preserving and non ratio-preserving operations. 

If the basis reparameterization does not change the distance ratios between knots, the shape of a NURBS primitive is not affected. If the ratios are not preserved, however, a NURBS primitive will change shape in the area influenced by the modified knots; furthermore, if the primitive is a NURBS or Bzier surface, any profiles it may contain will be affected as well. 

For more information about bases and knots see Breakpoints, Knots, and Spline Basis in the [Primitive](<./Primitive.md> "Primitive") and [Spline](<./Spline.md> "Spline") articles. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[basisSOP_Class](<./BasisSOP_Class.md> "BasisSOP Class")

## 

Parameters - Basis Page

Group`group`\- Group of spline primitives (accepts patterns, as described in: Scripting Guide). Non-spline types are ignored. 

Two sets of pages follow, one for each parametric direction (U and V). In each set the operations are applied in tab order, starting from the left: Parameterization, Mapping, and then raising the spline Order. To disable all the operations of a set, toggle off the U or V check mark above it. The V set is meaningful only for spline surfaces, and is ignored otherwise. Channel names are given for both the U and V pages. __

## 

Parameters - U Page

Edit the U Basis`ubasis`\- Enable editing of the U Basis. 

Parameterization`uparmtype`\- ⊞ \- Select the method of parameterization in u from the options below. 
* Unchanged`nochange`\- Does not change the basis.
* Uniform`uniform`\- Distributes all the knots evenly, maintaining the basis origin and length. Recommended only for regular shapes.
* Chord Length`chord`\- Computes the knot ratios based on the distances between successive CVs. This is the most common and most effective parameterization method.
* Centripetal`centripetal`\- Similar to the chord length method. Recommended for shapes containing sharp turns.
* Manual: Single`manualone`\- Loads the basis with the knots listed in the "Knot Sequence" below. If the SOP input contains several primitives, only the basis of the first spline primitive will be affected.
* Manual: Propagated`manualall`\- Same as above + it copies the basis to the basis of all the other spline primitives in the model or in the group. Using this feature on curves that have the point count and degree will generate cleaner surfaces, i.e. surfaces with fewer isoparms.
* Knotslide`slide`\- Shift clusters of knots within the basis. See Knotslide (From Paramaterization Menu) for discussion.


Knot Sequence`uknots`\- The basis of the first spline primitive in the input loads its knot sequence with the data specified in this field when the Parameterization is set to Manual. The values must be in ascending order, and their total count must match the number of knots in the basis. To ensure an exact count, click on the Read Basis button to read the original knot sequence into this field. 

**Note:** Bezier bases cannot have repeated knots. NURBS bases accept repeated knots as long as the knot multiplicity does not exceed the degree of the basis. The first two and last two knots of a NURBS basis must be identical. __

Read Basis`uread`\- Loads the original knots of the basis into the Knot Sequence field when the Parameterization type is Manual. 

Range`urange`\- ⊞ \- Range specifies the domain interval to be shifted. All the knots captured in this range are shifted by the same amount as far as the closest neighbouring knot on either side. 

  *`urange1`-


  *`urange2`-


Bias`ubias`\- Bias indicates the direction and the amount of translation. A Bias of 0.5 does not displace the knots at all. As the Bias decreases, the knot cluster migrates closer to its left-neighbouring knot. A Bias greater than 0.5 forces a migration to the right. 

Sometimes a Bias of 0 or 1 does not clamp the knot cluster to the closest neighbouring knot. The reason for this behaviour is that the knot multiplicity cannot be allowed to exceed the degree of the basis. For example, an order 4 (degree 3, or "cubic") spline can have at most 3 identical knots in sequence. When sliding the knot of a NURBS basis, a larger area of that spline is affected. This may create the impression than more knots than those in the cluster are being displaced. __

Concatenate`uconcat`\- Indicates whether the bases of the input spline primitives should be concatenated such that the last knot of the first primitive coincides with the first knot of the second primitive, and so on. This operation is performed before the ones below it, thus allowing a whole set of bases to be mapped onto a given interval (usually [0,1]) while enforcing basis continuity. 

Origin`udoorigin`\- Enables the Origin parameter. 

Origin`uorigin`\- The new origin of the basis, or the origin of the cummulated bases if Concatenation is On. 

Length`udolength`\- Enables the Length parameter. 

Length`ulength`\- The new length of the basis, or the total length of the cummulated bases if Concatenation is On. The Length, which represents the distance between the first and last knot, must be greater than zero. 

Scale`udoscale`\- Enables the Scale parameter. 

Scale`uscale`\- The multiplier applied to the basis starting at the basis origin. The Scale must be greater than zero. 

Raise to`uraise`\- Enables the Raise to parameter. 

Raise U to`orderu`\- The only operation here is raising the order (or degree) of the spline basis. Valid orders range from 2 to 11. Orders lower than the current spline order are ignored. The operation preserves the shape of the primitive. 

**Production Tip:** Before applying a spline-based texture projection with the Texture SOP, remap the U and/or V bases of the spline surface between 0 and 1 to ensure a complete mapping of the texture. If a single texture map must be shared by several surfaces, the surface bases should be concatenated prior to being remapped. __

## 

Parameters - V Page

Edit the V Basis`vbasis`\- Enable editing of the V Basis. 

Parameterization`vparmtype`\- ⊞ \- Select the method of parameterization in v from the options below. 
* Unchanged`nochange`-
* Uniform`uniform`-
* Chord Length`chord`-
* Centripetal`centripetal`-
* Manual: Single`manualone`-
* Manual: Propagated`manualall`-
* Knotslide`slide`-


Knot Sequence`vknots`\- The basis of the first spline primitive in the input loads its knot sequence with the data specified in this field when the Parameterization is set to Manual. The values must be in ascending order, and their total count must match the number of knots in the basis. To ensure an exact count, click on the Read Basis button to read the original knot sequence into this field. 

**Note:** Bezier bases cannot have repeated knots. NURBS bases accept repeated knots as long as the knot multiplicity does not exceed the degree of the basis. The first two and last two knots of a NURBS basis must be identical. __

Read Basis`vread`\- Loads the original knots of the basis into the Knot Sequence field when the Parameterization type is Manual

Range`vrange`\- ⊞ \- Range specifies the domain interval to be shifted. All the knots captured in this range are shifted by the same amount as far as the closest neighbouring knot on either side. 

  *`vrange1`-


  *`vrange2`-


Bias`vbias`\- Bias indicates the direction and the amount of translation. A Bias of 0.5 does not displace the knots at all. As the Bias decreases, the knot cluster migrates closer to its left-neighbouring knot. A Bias greater than 0.5 forces a migration to the right. 

Sometimes a Bias of 0 or 1 does not clamp the knot cluster to the closest neighbouring knot. The reason for this behaviour is that the knot multiplicity cannot be allowed to exceed the degree of the basis. For example, an order 4 (degree 3, or "cubic") spline can have at most 3 identical knots in sequence. When sliding the knot of a NURBS basis, a larger area of that spline is affected. This may create the impression than more knots than those in the cluster are being displaced. __

Concatenate`vconcat`\- Indicates whether the bases of the input spline primitives should be concatenated such that the last knot of the first primitive coincides with the first knot of the second primitive, and so on. This operation is performed before the ones below it, thus allowing a whole set of bases to be mapped onto a given interval (usually [0,1]) while enforcing basis continuity. 

Origin`vdoorigin`\- Enables the Origin parameter. 

Origin`vorigin`\- The new origin of the basis, or the origin of the cummulated bases if Concatenation is On. 

Length`vdolength`\- Enables the Length parameter. 

Length`vlength`\- The new length of the basis, or the total length of the cummulated bases if Concatenation is On. The Length, which represents the distance between the first and last knot, must be greater than zero. 

Scale`vdoscale`\- Enables the Scale parameter. 

Scale`vscale`\- The multiplier applied to the basis starting at the basis origin. The Scale must be greater than zero. 

Raise to`vraise`\- Enables the Raise to parameter. 

Raise V to`orderv`\- The only operation here is raising the order (or degree) of the spline basis. Valid orders range from 2 to 11. Orders lower than the current spline order are ignored. The operation preserves the shape of the primitive. 

**Production Tip:** Before applying a spline-based texture projection with the Texture SOP, remap the U and/or V bases of the spline surface between 0 and 1 to ensure a complete mapping of the texture. If a single texture map must be shared by several surfaces, the surface bases should be concatenated prior to being remapped. __

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Basis SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• Basis • [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
