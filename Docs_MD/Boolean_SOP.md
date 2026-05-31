# Boolean SOP

## 

Summary

The Boolean SOP takes two closed polygonal sets, A and B. Set these Sources to the SOPs with the 3D shapes that you wish to operate on. There are two important requirements for input geometry: 
* Shapes must be completely closed. A tube with open ends is not an acceptable input. You can close Tube ends with an end-cap. An extruded letter with no back polygons output is also unacceptable (even with backs output it can be unacceptable because of the second requirement).
  * All polygons must be convex and coplanar. In the case of the Extrude SOP, you must select Output Convex Faces for front and back faces. It will now be a usable input for Boolean. The Divide SOP also offers a convexing function for geometry not created with the Extrude SOP.


Other caveats for Boolean are the following: 
* Point colors and texture UV coordinates are not interpolated correctly.
  * In some cases polygons can be reversed so that all normals point outwards. The polygon reversal should not usually present much of a problem (use a Primitive SOP > Face/Hull page > Vertex > Reverse to reverse them if necessary).
* A [Facet SOP](<./Facet_SOP.md> "Facet SOP") can be used to prepare inputs when the Boolean SOP complaints they are not closed. In that case, use both the Consolidate Points and Orient Polygons options.


This SOP is quite visual and intuitive; you can experiment with the different combinations on screen to see the effects. 

**Note:** The Boolean SOP handles polygonal geometry types. For boolean-type operations with nurbs and Bezier surfaces - see [Surfsect SOP](<./Surfsect_SOP.md> "Surfsect SOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[booleanSOP_Class](<./BooleanSOP_Class.md> "BooleanSOP Class")

## 

Parameters - Page

Operation`booleanop`\- ⊞ \- Some of the operations below produce guide geometry to give you visual feedback on the results of the operation being performed. The appearance of the geometry is context sensitive - if you are performing an intersect operation, or either of the edge operations the guide will be both inputs; if you are doing A minus B then the guide will be B and if B minus A then the guide will be A. If you are doing union then there will be no guide geometry. 

If the guide geometry is too distracting, you can disable it by entering the Viewport options dialog and clicking on the Guide geometry button so that it no longer appears indented. This procedure is global and will disable the guide geometry of other SOPs as well. 

The Boolean SOP will automatically orient polygons so they face the same way. This may not be enough in some cases because Boolean results in some unshared edges where the intersection cut took place. If the shading is still not good enough, you are best to follow Boolean with a Facet SOP. In it, Consolidate Points, Orient Polygons and finally Cusp. 

If you have really strange shaped polygons, you can first triangulate one or both of the inputs with the Divide SOP. 
* Union`union`\- Geometry from the two inputs is combined, and interior polygons are removed. The result is a closed shape. This can be very useful for joining pipes or other shapes that the camera will travel inside, or where the intersecting shapes must be transparent. Points at the intersection of the shapes are not consolidated.
* Intersect`intersect`\- The resulting geometry is a closed shape where the two input shapes overlap or intersect. Geometry outside the common area is discarded.
* A minus B`aminusb`\- The result is a closed shape in which the geometry from B is cut away or subtracted from the geometry in A.
* B minus A`bminusa`\- All operations same as previous three, but resulting shape is Part B with Part A cut away from it.
* A Edge`aedge`\- Closed face(s) are produced, at the edges where the two parts meet. The face(s) can be twisted (not planar). The point order is unpredictable; append a Polygon SOP with the Order Points option enabled to sort them out if you want to make connections to the face.
* B Edge`bedge`\- Closed face(s) are produced, at the edges where the two parts meet. The face(s) can be twisted (not planar). The point order is unpredictable; append a Polygon SOP with the Order Points option enabled to sort them out if you want to make connections to the face.


Accurate Attributes Interpolation`accattrib`\- If selected, all inputs are convexed to triangles, otherwise they are convexed to quadrilaterals. 

Create Groups`creategroup`\- If selected, a group is created containing all faces pertaining to the first input, and a second group containing all faces of the second input. 

Group A`groupa`\- When Create Groups = On, specify a name for Group A. 

Group B`groupb`\- When Create Groups = On, specify a name for Group B. 

## 

Uses
* Cutting a 3D shape from another 3D shape.
  * Joining a 3D shape to another 3D shape, removing interior polygons.
  * Creating a 3D shape where two 3D shapes intersect.
  * Creating holes or planes where 3D shapes intersect.
  * Animating any of the above effects.

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Boolean SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• Boolean • [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
