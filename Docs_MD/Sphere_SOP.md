# Sphere SOP

##   
  
Summary

The Sphere SOP generates spherical objects of different geometry types. It is capable of creating non-uniform scalable spheres of all geometry types. 

If an input is provided, the sphere's radius is automatically determined as a function of the input's bounding geometry. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[sphereSOP_Class](<./SphereSOP_Class.md> "SphereSOP Class")

## 

Parameters - Page

Primitive Type`type`\- ⊞ \- Select from the following types. For information on the different types, see the [Geometry](<./Category-Geometry.md> "Category:Geometry") category articles. Depending on the primitive type chosen, some SOP options may not apply. Using the 'Primitive' primitive type is not recommended when using instancing. 
* Primitive`prim`-
* Polygon`poly`-
* Mesh`mesh`-
* NURBS`nurbs`-
* Bezier`bezier`-


Connectivity`surftype`\- ⊞ \- This option is used to select the type of surface, when using a Mesh Primitive Type. 
* Rows`rows`\- Creates horizontal lines.
* Columns`cols`\- Creates vertical lines.
* Rows and Columns`rowcol`\- Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon).
* Triangles`triangles`\- Build the grid with Triangles.
* Quadrilaterals`quads`\- Generates sides composed of quadrilaterals (default).
* Alternating Triangles`alttriangles`\- Generates triangles that are opposed; similar to the Triangles option.


Orient Bounds`orientbounds`\- Available only when an input is connected to the Sphere SOP to set bounds for the sphere. When Orient Bounds = On it will rotate the geometry to match the orientation of the input SOP used for bounds. 

Modify Bounds`modifybounds`\- Available only when an input is connected to the Sphere SOP to set bounds for the sphere. When Modify Bounds = On the transform parameters below will further modify the rotation, position, and radius of the bounds. 

Rotate Order`rord`\- ⊞ \- Sets the order in which the rotations are applied. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Radius`rad`\- ⊞ \- The radius of the sphere in X, Y and Z. 
* X`radx`-
* Y`rady`-
* Z`radz`-


Center`t`\- ⊞ \- Offset of sphere center from object center. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- These three fields rotate the Sphere along the X, Y, and Z axes. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Reverse Anchors`reverseanchors`\- Invert the direction of anchors. 

Anchor U`anchoru`\- Set the point in X about which the geometry is positioned, scaled and rotated. 

Anchor V`anchorv`\- Set the point in Y about which the geometry is positioned, scaled and rotated. 

Anchor W`anchorw`\- Set the point in Z about which the geometry is positioned, scaled and rotated. 

Orientation`orient`\- ⊞ \- Determines axis for sphere. Poles of sphere align with orientation axis. 
* X Axis`x`-
* Y Axis`y`-
* Z Axis`z`-


Frequency`freq`\- This controls the level of polygons used to create the sphere, when using the Polygon Primitive Type. 

Rows`rows`\- Number of rows in a sphere when using the mesh, imperfect NURBS and imperfect Bzier. 

Columns`cols`\- Number of columns in a sphere when using the mesh, imperfect NURBS and imperfect Bzier. 

U Order`orderu`\- If a spline curve is selected, it is built at this order for U. 

V Order`orderv`\- If a spline curve is selected, it is built at this order for V. 

Imperfect`imperfect`\- This option applies only to Bzier and NURBS spheres. If selected, the spheres are approximated nonrational curves, otherwise they are perfect rational curves. 

Unique Points per Pole`upole`\- Applies to Mesh, NURBS and Bzier surfaces only. This option determines whether points at the poles are shared or are individual to the columns. 

Accurate Bounds`accurate`\- If the SOP is being used to generate a bounding sphere for it's input geometry, this parameter tells the SOP to use a more accurate (but slower) bounding sphere calculation. 

Texture Coordinates`texture`\- ⊞ \- Adds UV texture coordinates to the sphere. 
* Off`off`\- No UV coordinates added to surface.
* By Primitive Type`byprimtype`\- Adds vertex UV coordinates.
* Equirectangular Inside (Spherical Polar)`equirectangularin`-
* Equirectangular Outside (Spherical Polar)`equirectangularout`-
* Equidistant Azimuth (Fish Eye 180)`equiazimuth`-
* Equidistant Azimuth (Fish Eye 360)`equiazimuth360`-


Compute Normals`normals`\- Creates normals on the geometry. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Sphere SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2022.241402021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• Sphere • [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
