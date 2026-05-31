# Add SOP

## 

Summary

The Add SOP can both create new Points and Polygons on its own, or it can be used to add Points and Polygons to an existing input. 

If an input is specified, this SOP adds points and polygons to it as specified below. If no input is specified, then it generates the points and polygons below as a new entity. It can read points and vertices from DATs. See also [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[addSOP_Class](<./AddSOP_Class.md> "AddSOP Class")

## 

Parameters - Points Page

Points DAT`pointdat`\- Path to a [Table DAT](<./Table_DAT.md> "Table DAT") containing point data. By default, x, y, z, and w can be defined in the first 4 columns of the table using un-named columns. 

If the`Named Attributes`parameter below is turned on, the following attributes can be defined in the Points Table DAT using named columns: 

  *`P(0) P(1) P(2) P(3)`*`N(0) N(1) N(2)`*`Cd(0) Cd(1) Cd(2) Cd(3)`*`uv(0) uv(1) uv(2)`Any other columns are added as single-float attributes. 

**NOTE:** Turn off`Compute Normals`on the Polygon parameter page when supplying`N(0) N(1) N(2)`in the Points Table DAT. __

Named Attributes`namedattribs`\- Allows extra attributes to be defined in the Point Table DAT above. 

Delete Geometry, Keep Points`keep`\- Use this option to remove any unused points. When checked, existing geometry in the input are discarded, but the polygons created by this SOP are kept, as well as any points in the input. 

Add Points`addpts`\- When On you can add individual points with position and weight of your choosing by using the parameters below. 

Point`point`\- Sequence of points to add 

Position`point0pos`\- ⊞ \- The three input fields represent the X, Y and Z coordinates of the point. These values can be constants (numbers) or variables. Below are three examples: 
[code]
    0.2    0.42    1.3
    
[/code]
[code] 
    0.2    op('xform1').par.tx    1.36
    
[/code]
[code] 
    # read the sixth point (first point is 0) from the SOP, grid1
    op('grid1').points[5].x    op('grid1').points[5].y    op('grid1').points[5].z
    
[/code]
* Position`point0posx`-
* Position`point0posy`-
* Position`point0posz`-


Weight`point0weight`\- The spline weight of the point. If the point is later used to create a spline (nurbs or Bezier) primitive, the weight will influence the shape of the primitive and may cause that primitive to become rational. Polygons and metaballs are not affected by this weight. 

## 

Parameters - Polygons Page

Method`method`\- ⊞ \- Specify to create polygons from the points by using a Group method or Pattern Method. 
* By Group`group`\- Create as many polygons as determined by the group field and by the grouping / skipping rules.
* By Pattern`pattern`\- Specify the points to use to create polygons using the parameters Polygon Table or Polygon 0 below.


Group`group`\- Subset of points to be connected. 

Add`add`\- ⊞ \- Optionally join subgroups of points. 
* All Points`all`\- Adds all points just as if you added them manually in the Points page.
* Groups of N Points`group`\- Adds only the number of points specified.
* Skip Every Nth Point`skip`\- Adds points, buts skips every Nth one.
* Each Group Separately`sep`\- Creates separate polygons for each group specified in the`Group`parameter. For example, if you have a Group SOP creating a group called group1 and using the`Create Boundary Groups`option, you can connect this to an Add SOP and enter group1__* in the`Group`parameter. If`Each Group Separately`is chosen, polygons will be created for each boundary on the surface.


**Tip: The Each Group Separately option is useful when pasting surfaces. Boundary groups can be created for the boundaries of two adjacent surfaces, and then the PolyLoft SOP (using the Points option) can be used to stitch these surfaces together.**

N`inc`\- Increment / skip amount to use for adding points. 

Closed`closedall`\- Closes the generated polygons. 

Polygons Table`polydat`\- Path to a Table DAT containing polygon data. Accepts rows of polygons specified by point number in the first column. The second column indicates if the polygons are closed (1) or open (0). 

Polygon`poly`\- Sequence of polygon patterns 

Pattern`poly0pattern`\- Create a fixed number of polygons by specifying a point pattern for each polygon. Enter connection lists here to add polygons. These consist of a list of point numbers to define the order in which the points are to be connected. The form is: {from}-{to}[:{every}][,{of}]. 

Examples of Valid Connection Lists:`1 2 3 4`\- Makes a polygon by connecting point numbers 1,2,3,4.`1 3-15 16 8`\- All points from 3-15 are included.`1-234 820-410 235-409`\- Points from 1-820 are included, in the specified order.`0-15:2`\- Every other point from 0 to 15 is included.`0-15:2,3`\- Every 2 of 3 points are included (i.e. 0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15).`!4`\- Every point except 4 is included.`!100-200`\- Every point <100 and >200 is included.`*`\- Include all points.`9-0`\- The first ten points are included in reverse order.`!9-0`\- All but the first ten points are included in reverse order.

Closed`poly0closed`\- To create a closed polygon, check the Closed button. 

## 

Parameters - Post Page

Remove Unused Points`remove`\- Keep only the connected points, and discard unused points. 

Compute Normals`normals`\- Creates normals on the geometry. 

## 

Uses

Used in conjunction with a point expression, the Add SOP can be useful for extracting a specific point from another SOP. For example, to extract the X, Y and Z value of the fifth point, from a Grid SOP in geo1: 
[code] 
    op('geo1/grid1').points[5].x
    op('geo1/grid1').points[5].y
    op('geo1/grid1').points[5].z
    
[/code]

Points added in this way are appended to the end of the point list if a Source is specified. Middle-mouse click on the SOP node to find out how many points there are. For example, if you have added two points and there are 347 points (from 0 to 346), you have added the last two point numbers: 345 and 346. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Add SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2022.241402021.100002020.200002018.28070before 2018.28070

SOPs   
---  
Add • [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
