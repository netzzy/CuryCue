# Circle SOP

##   
  
Summary

The Circle SOP creates open or closed arcs, circles and ellipses. 

If two NURBS circles that are non-rational (i.e. their X and Y radii are unequal) are skinned, more isoparms may be generated than expected. This is because non-rational NURBS circles parameterise their knots based on chord length, and the Skin SOP must consolidate the total number of knots between the two circles before skinning. 

To remedy this, you may want to use a Refine SOP, and unrefine the resulting skin, or better yet - before unrefining, start with the same circle and use a Primitive or Transform SOP to deform the second copy before skinning. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[circleSOP_Class](<./CircleSOP_Class.md> "CircleSOP Class")

## 

Parameters - Page

Primitive Type`type`\- ⊞ \- For information on the different types, see the [Primitive](<./Primitive.md> "Primitive") and [Spline](<./Spline.md> "Spline") articles. Depending on the primitive type chosen, some SOP options may not apply. Using the 'Primitive' primitive type is not recommended when using instancing. 
* Primitive`prim`-
* Polygon`poly`-
* NURBS Curve`nurbs`-
* Bezier Curve`bezier`-


Orientation`orient`\- ⊞ \- The plane on which the circle lies. 
* XY Plane`xy`-
* YZ Plane`yz`-
* ZX Plane`zx`-


Modify Bounds`modifybounds`\- Available only when an input is connected to the Curcle SOP to set bounds for the sphere. When Modify Bounds = On the transform parameters below will further modify the radius and position of the bounds. 

Radius`rad`\- ⊞ \- The Radius of the Circle in the X and Y directions. 
* X`radx`-
* Y`rady`-


Center`t`\- ⊞ \- The Center of the Circle in X, Y and Z. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Reverse Anchors`reverseanchors`\- Invert the direction of anchors. 

Anchor U`anchoru`\- Set the point in X about which the geometry is positioned, scaled and rotated. 

Anchor V`anchorv`\- Set the point in Y about which the geometry is positioned, scaled and rotated. 

Order`order`\- If a spline curve is selected, it is built at this order. 

Divisions`divs`\- The number of edges (points +1) used to describe the circle. This option applies to polygons and imperfect splines. The more Divisions a circle has, the smoother it looks. Using three divisions makes a triangle, four divisions a diamond, five divisions a pentagon, and so on. Also, for open arc types, the number of points will equal Divisions \+ 1, and for closed arc types, Divisions \+ 2. 

Arc Type`arc`\- ⊞ \- Determines how the circle should be drawn. Applies to polygons and imperfect splines only. 
* Closed`closed`\- An enclosed curve.
* Open Arc`openarc`\- An open curve segment.
* Closed Arc`closedarc`\- An Open Arc with connecting edges to the centre resembling a slice of pie.
* Sliced Arc`slicedarc`\- Same as Closed Arc, but connects every single point to the center of the circle.Same as Closed Arc, but connects every single point to the center of the circle.


Arc options are available for polygonal circles and some spline types. The difference between the choices: Open, Closed, and Slice are illustrated below for the polygonal case: 

[![TouchGeometry220.gif](./images/9/93/TouchGeometry220.gif)](</File:TouchGeometry220.gif>)

Arc Angles`angle`\- ⊞ \- The beginning and ending angles of the arc. An arc will start at the beginning angle, and proceed towards the ending angle. If beginning=0 and end=360 it will be a full circle. As a reference: 

[![TouchGeometry222.gif](./images/d/db/TouchGeometry222.gif)](</File:TouchGeometry222.gif>)

**Note:** The total angle can exceed 360, making multiple wraps of the circle. 

  *`beginangle`-


  *`endangle`-


Imperfect`imperfect`\- This option applies only to Bezier and NURBS circles. If selected, the circles are approximated non-rational curves, otherwise they are perfect rational closed curves. 

Texture Coordinates`texture`\- ⊞ \- Option to include texture cooordinates or not. 
* Off`off`\- No texture coordinates are created.
* Face`face`\- Default texture coordinates are created. To modify texture coordinates, see [Texture SOP](<./Texture_SOP.md> "Texture SOP").


Compute Normals`normals`\- When On, normals are created for the surface. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Circle SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2022.241402021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• Circle • [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
