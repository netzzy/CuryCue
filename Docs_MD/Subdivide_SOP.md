# Subdivide SOP

##   
  
Summary

The Subdivide SOP takes an input polygon surface (which can be piped into one or both inputs), and divides each face to create a smoothed polygon surface using a Catmull-Clark subdivision algorithm. Especially useful for avoiding the angular appearance often associated with polygonal models - without adding lots of extra geometry to the entire object. For best results, polygons should be convex and relatively uniform in distribution. 

Subdivision surfaces also allows you to create the smoothed surface based on a polygon control shape. As the control shape changes, so does the smooth shape within. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[subdivideSOP_Class](</SubdivideSOP_Class> "SubdivideSOP Class")

## 

Creases and Cracks

### 

Creases

Creases control the strength of pull of the polygon faces on the subdivision surfaces, much like a magnet drawing the surface towards the reference polygon. They can be applied selectively using the Creases field to specify an input group to use. 

Creases work by controlling the strength of the pull of the polygon faces on the subdivision surfaces, like a magnet drawing the surface towards the reference polygon. The figure below shows the result of setting the Crease Weight to`0, 1, 2`reading from left to right. As the weight increases so the pull effect strengthens and the shape approaches the reference polygon. 

### 

The Crease Algorithm

If there is a second input: 

    If the Override button is enabled, each edge defined in the second input will have its edge crease weight set to the value of the override.
    If the vertex attribute "`creaseweight`" exists on the second input, each matching edge in the input will have its crease weight set to the maximum of the vertex attributes for any shared edges.
    If the primitive attribute "`creaseweight`" exists on the second input, each polygon in the second input will set matching edges to the appropriate weights.

If there is no second input: 

    If an override is specified, the value of the override is used for all edges in the sub-divided surface.
    If the vertex attribute "`creaseweight`" exists, this attribute will be used to define the crease weights on the edges of the surface.
    If the primitive attribute "`creaseweight`" exists, this attribute will be used to define the crease weights for the subdivision surface.

When defining crease weights on shared edges, the maximum of the weights of the shared edges is used. For example, if two polygons share an edge and the primitive attribute is used, the maximum of the crease weight will be used for the shared edge. 

### 

Closing Cracks

Cracks can be closed by either Pull Cracks Closed or Stitch Cracks Together, so only one of these two options can be chosen at a time from the Surrounding Faces parameter. Bias applies only to Pulling, and is disabled when Stitching is chosen. 

A crack is formed by a single edge on the non-subdivided area and multiple edges on the subdivided area. The Surrounding Faces menu determines what will will happen to the single edge on the non-subdivided area, and in more generally, to the polygon containing this edge. 

If No Edge Division is chosen and cracks are pulled closed, all the points on the subdivided edges are pulled (i.e. moved) to the closest points on the non-subdivided edges. Bias is disabled, when No Edge Division is specified. 

If cracks are pulled with the Divide Edges option, the non-subdivided edge is split into many sections, so that each each point on the non-subdivided edge now corresponds to a new point on the subdivided edge. Then, points on the newly divided edge are joined with the points on the subdivided boundary. A Bias of`1`will place these joined points along the subdivided boundary. A Bias of`0`will place them along the non- subdivided boundary (and values between 0 and 1 will place them somewhere inbetween). 

Pulling cracks with the Triangulate option will do exactly the same thing as Divide Edges, except it will also triangulate the non-subdivided polygon. This is desirable because pulling the non-subdivided boundary towards the curved subdivided boundary will likely generate a non-planar polygon, so Triangulate will divide this polygon into smaller (planar) ones. Pulling cracks with a Bias of`1`and triangulating usually produces the nicest results. 

The Triangulate option is necessary because the [Divide SOP](<./Divide_SOP.md> "Divide SOP") is not designed to handle (very) non-planar polygons. 

The Stitch Cracks Together option, on the other hand, inserts new polygons (triangles) to close up the cracks. When No Edge Division is chosen, many triangles are created, each having one vertex on one point of the non-subdivided edge. 

When Divide Boundary Edges is chosen, the non-subdivided edge is divided, so there are more points available to be used for triangles. The resulting triangles are more regularly shaped (not as long and skinny). The Triangulate option will again triangulate the non-subdivided polygon, although this option is less likely to be used becuase this polygon should remain planar during stitching. 

## 

Parameters - Page

Group`subdivide`\- Subset of input to use as a polygonal mesh to subdivide. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Creases`creases`\- This field allows you to specify a subset of the second input to use as creases. The elements of the second input specified by the Creases field are used as creases. Each edge in a crease polygon corresponds to the edge in the polygon mesh which has the same point numbers. Point position is irrelevant. For polygon edges to be classified as the same edge, they must share the same points. Merely being physically close is not sufficient. 

The primitive attribute`creasesharpness`is used to determine the sharpness of the specified creases unless overridden. __

Depth`iterations`\- How many iterations to subdivide. Higher numbers give a smoother surface. 

Override Crease Weight Attribute`overridecrease`\- Determine if the crease sharpness should be determined by the primitive or vertex`creaseweight`attribute or by overridden by this SOP. 

Crease Weight`creaseweight`\- If the crease weight is overriden, this is the weight used. 

**Tip:** The default is to have the **Override Crease Weight Attribute** enabled. So you can simply set a value which applies to all the creases. You can, however, set a crease attribute using the Vertex or Primitive SOPs which allows for more control. __

Generate Resulting Creases`outputcrease`\- If any creases are sharper than the Depth, they will be left over in the resulting geometry. With this parameter enabled, these left over creases are created with the appropriate primitive attribute values, and placed in the specified group. 

New Group`outcreasegroup`\- Name of the group to place the generated creases into. 

Close Cracks`closeholes`\- ⊞ \- Choose how gaps are handled in the output geometry. 
* Do Not Close`noclose`\- Don't close cracks.
* Pull Cracks Closed`pull`\- Move points on boundary of subdivided area in order to close cracks formed during the subdivision.
* Stitch Cracks Together`stitch`\- Add polygons (triangles) to close the cracks caused by subdividing.


Surrounding Faces`surroundpoly`\- ⊞ \- Choose how to handle the polygons on either side of a crack when pulling or stitching it closed. 
* No Edge Division`nodiv`\- When No Edge Division is chosen, many triangles are created, each having one vertex on one point of the non-subdivided edge.
* Divide Edges`edges`\- Divides edges surrounding the subdivided area when pulling or stitching cracks by inserting new polygons (triangles) to close up the cracks.
* Triangulate`triangulate`\- Does exactly the same thing as Divide Edges, except it also triangulates the non-subdivided polygon. This is desirable because pulling the non-subdivided boundary towards the curved subdivided boundary will likely generate a non-planar polygon, so Triangulate will divide this polygon into smaller (planar) ones. Pulling cracks with a Bias of 1 and triangulating usually produces the nicest results.


Bias`bias`\- Determines which points are moved when pulling crack closed. 
* 0 means move points on subdivided area to meet boundary.
  * 1 means move points on boundary to meet subdivided area.

## 

Example

Below, a Subdivide SOP is used to create a subdivision surface from a [Box SOP](<./Box_SOP.md> "Box SOP"). The Depth of the subdivision is set to 2. The [Facet SOP](<./Facet_SOP.md> "Facet SOP") consolidates the points so that the box faces are treated as a unit. 

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Subdivide SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• Subdivide • [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
