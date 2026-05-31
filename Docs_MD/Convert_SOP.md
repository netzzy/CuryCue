# Convert SOP

##   
  
Summary

The Convert SOP converts geometry from one geometry type to another type. Types include polygon, mesh, Bezier patche, particle and sphere primitive. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[convertSOP_Class](<./ConvertSOP_Class.md> "ConvertSOP Class")

## 

Parameters - Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

From Type`fromtype`\- ⊞ \- Determines which geometry by type will be converted. The default is All Types: 
* All Types`all`\- All geometry will be converted.
* Sphere`sphere`-
* Tube`tube`-
* Particles`part`-
* Meta-ball`metaball`-
* Polygon`poly`-
* Mesh`mesh`-
* Bezier Curve`bezcurve`-
* Bezier Surface`bezsurf`-
* NURBS Curve`nurbcurve`-
* NURBS Surface`nurbsurf`-
* Circle`circle`-
* Triangle Strip`tristrip`-
* Triangle Fan`trifan`-


Convert to`totype`\- ⊞ \- Determines what the above From Type geometry will be converted to. Conversion to Polygons is the default: 

  
**Notes** : Not all geometry can be converted to specific types. For example, a triangulated polygon surface to a single NURBS surface, or a Mesh sphere into a primitive sphere. Also, certain conversions will preserve shapes. For example, converting a Bzier curve to a NURBS curve or a polygonal mesh to a NURBS Surface. 

**Circle Notes** : Converting to primitive circles is available for action users who are used to working with polygon circles so that you can convert them to primitive circles for the TouchDesigner Skeleton, Arm, and Limb SOPs. 

**Trimmed Surface Notes** : If the primitive to be converted is a curve (NURBS or Bezier) and is flat, a trimmed surface will be generated such that the visible piece coincides with the curve. If the curve is not flat, it will be converted to a non-trimmed surface. The advantage of the trimmed solution is that it yields a very clean surface and handles concave curves perfectly. 
* Polygon`poly`-
* Mesh`mesh`-
* Bezier Curve`bezcurve`-
* Bezier Surface`bezsurf`-
* NURBS Curve`nurbcurve`-
* NURBS Surface`nurbsurf`-
* Circle`circle`-
* Trimmed Bezier Surface`trimbezsurf`-
* Trimmed NURBS Surface`trimnurbsurf`-
* Particles`part`-


Connectivity`surftype`\- ⊞ \- This option is used to select how the points of the created surface are connected. 
* Rows`rows`\- Creates horizontal lines.
* Columns`cols`\- Creates vertical lines.
* Rows and Columns`rowcol`\- Both Rows and Columns. Looks like Quadrilaterals in wire frame display, but all polygons are open (if the primitive type is polygon).
* Triangles`triangles`\- Build the grid with Triangles.
* Quadrilaterals`quads`\- Generates sides composed of quadrilaterals (default).
* Alternating Triangles`alttriangles`\- Generates triangles that are opposed; similar to the Triangles option.

## 

Parameters - Level of Detail Page

This affects the use of the U/V/Trim Curve fields: 
* For Level of Detail: U, V, Trim Curve Level of Detail


In a spline's case, the span is the curve arc between two breakpoints. The number of divisions per span specifies how many points to be created between the two breakpoints. If the number of divisions = 0, a single segment will connect the two breakpoints; if number of divisions = 1, two edges will be created; etc. The advantage of Divisions over the Level of Detail is that it tells you exactly how many points you'll end up with - extremely useful for polygonal modeling. 

U`lodu`\- When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh. 

When set to Divisions per Span, specificies the number of divisions per span. 

**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the`primdist()`expression. Then the detail will increase/decrease as the camera gets closer/further away. __

V`lodv`\- When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh. 

When set to Divisions per Span, specificies the number of divisions per span. 

**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the`primdist()`expression. Then the detail will increase/decrease as the camera gets closer/further away. __

Trim-Curve`lodtrim`\- The trimmed part of a surface will be converted using this Trim lod (level of detail) instead of using an implicit "1" constant. 

## 

Parameters - Divisions per Span Page

This affects the use of the U/V/Trim Curve fields: 
* For Divisions per Span: U, V, Number of Trim Curve Divisions.


In a spline's case, the span is the curve arc between two breakpoints. The number of divisions per span specifies how many points to be created between the two breakpoints. If the number of divisions = 0, a single segment will connect the two breakpoints; if number of divisions = 1, two edges will be created; etc. The advantage of Divisions over the Level of Detail is that it tells you exactly how many points you'll end up with - extremely useful for polygonal modeling. 

U`divu`\- When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh. 

When set to Divisions per Span, specificies the number of divisions per span. 

**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the`primdist()`expression. Then the detail will increase/decrease as the camera gets closer/further away. __

V`divv`\- When set to Level of Detail, controls the number of points or CVs that are used in the newly generated geometry depending on the above setting. Converting a NURBS surface into a polygon mesh with a Level of Detail of 1 results in a fair approximation of the NURBS surface whereas a value of 2 generates a very dense polygonal mesh. 

When set to Divisions per Span, specificies the number of divisions per span. 

**Tip:** Animate the Level of Detail based on how close your character or geometry is to the camera by using the`primdist()`expression. Then the detail will increase/decrease as the camera gets closer/further away. __

Trim-Curve`divtrim`\- The trimmed part of a surface will be converted using this Trim lod (level of detail) instead of using an implicit "1" constant. 

U Order`orderu`\- When converting to a spline type, this specifies the degree + 1 of the U or V basis function. 

Paste Coordinates 
* From Feature Surfaces - The resulting mesh will have the shape of the paste hierarchy (i.e. the top-most features will determine the shape).
  * From Base Surface - The resulting mesh will take the shape of the bottom-most surface.


Paste Attributes
* From Feature Surfaces - Each mesh point has the attributes of the top-most feature at that location.
  * From Base Surface - The resulting mesh will inherit the primitive attributes of the root surface (e.g. the material), and the point attributes will be those of the root surface as well.


By using base coordinates and feature attributes you are, in fact, pasting attributes onto the surface. __

V Order`orderv`\- When converting to a spline type, this specifies the degree + 1 of the U or V basis function. 

Paste Coordinates 
* From Feature Surfaces - The resulting mesh will have the shape of the paste hierarchy (i.e. the top-most features will determine the shape).
  * From Base Surface - The resulting mesh will take the shape of the bottom-most surface.


Paste Attributes
* From Feature Surfaces - Each mesh point has the attributes of the top-most feature at that location.
  * From Base Surface - The resulting mesh will inherit the primitive attributes of the root surface (e.g. the material), and the point attributes will be those of the root surface as well.


By using base coordinates and feature attributes you are, in fact, pasting attributes onto the surface. __

Preserve Original`new`\- When checked, the original geometry will be retained along with the converted geometry. 

Interpolate Through Hulls`interphull`\- This option applies to the conversion between polygonal faces and grids to NURBS and Bzier surfaces and curves. When selected, the resulting curves retain the same topology as the original polygon. When not selected, the polygon points are used as a hull to define the new curve or surface. 

Particle Type`prtype`\- ⊞ \- Selects how the particles are rendered. 
* Render as Lines`lines`\- Each particle will be rendered as a 2-point line, with the length determined based on the particles velocity. If the particle has no velocity it will just be a single pixel in size.
* Render as Point Sprites`pointprites`\- For use with the [Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT"). Each particle is a square of pixels that always face the camera. The size of the square is determined by parameters in the Point Sprite and the`pscale`vertex/point attribute. The point sprites will have texture coordinates generated for them automatically also ((0,0) in the bottom left and (1,1) in the top right).

## 

Notes

Face to Surface Conversion - When converting from a set of polygons to a mesh, a single mesh will result only if [Facet SOP](<./Facet_SOP.md> "Facet SOP"). 

Otherwise, each polygon is converted individually into a mesh. In fact, any individual face can be converted to any surface. This is accomplished by cutting the face into three or four adjacent sections, and then creating a patch from them. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Convert SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• Convert • [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
