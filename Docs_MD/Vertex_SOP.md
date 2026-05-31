# Vertex SOP

## 

Summary

The Vertex SOP allows you to edit/create attributes on a per-vertex (rather than per-point) basis. It is similar to the [Point SOP](<./Point_SOP.md> "Point SOP") in this respect. It supports two inputs, and will inherit the first input source by default. If the second input have less primitives than the first input, it will cycle through the primitives and match the vertices. If the primitive in the first input has more vertices than the matching primitive in the second input, the extra vertices are ignored. 

There are currently three vertex attributes supported: 
* Diffuse Color
  * Alpha
  * Texture Coordinates


When the attribute is defined, it can only occur on either points or vertices, but not both. Thus, if the input geometry has a point attribute for diffuse color, the attribute will automatically be "elevated" to be a vertex attribute (if diffuse colors are added in the Vertex SOP). 

The SOP processes every vertex of every primitive. For each vertex processed, there are variables which allow you to know the: 
* Vertex number of the primitive being processed
  * The number of vertices in the primitive being processed
  * The point which is referenced by the vertex
  * The primitive which contains the vertex
  * The total number of points
  * The total number of primitives


There are also local variables to find out the values of some point attributes (i.e. position, normal - if they exist), in addition to vertex attributes. To access the attributes of the second input source, append a 2 to the variable. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[vertexSOP_Class](</VertexSOP_Class> "VertexSOP Class")

## 

Parameters - Vertex Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this`SOP`to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Color`doclr`\- ⊞ \- Select between keeping the color, adding new color, or using no color for vertex color attributes from incoming geometry. 
* Keep Color`off`-
* Add Color`on`-
* No Color`remove`-


Color`diff`\- ⊞ \- If you select 'Add Color' from the menu above, Cd color vertex attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are:`me.inputColor[0]`for red,`me.inputColor[1]`for green,`me.inputColor[2]`for blue, and`me.inputColor[3]`for alpha. If you select 'No Color' from the menu above, the Cd color vertex attribute will be removed from the SOP. 
* Color`diffr`-
* Color`diffg`-
* Color`diffb`-


Alpha`alpha`\- Control the alpha attribute in the same manner as the rgb colors above. Alpha is Cd[3] and comes from input via`me.inputColor[3]`Texture`douvw`\- ⊞ \- Select between keeping the texture coordinates, adding new texture coordinates, or using no texture coordinates for the vertex texture attributes from incoming geometry. 
* Keep Texture`off`-
* Add Texture`on`-
* No Texture`remove`-


Texture`map`\- ⊞ \- If you select 'Add Texture' from the menu above, uv texture coordinate vertex attributes will be added/modified in the SOP. Enter expressions here to control the values of the vertex texture coordinates here. The attributes to modify are:`me.inputTexture[0]`,`me.inputTexture[1]`and`me.inputTexture[2]`. If you select 'No Texture' from the menu above, the uv texture coordinates vertex attribute will be removed from the SOP. 
* Texture`mapu`-
* Texture`mapv`-
* Texture`mapw`-


Crease`docrease`\- ⊞ \- Select between keeping the crease, adding new crease, or using no crease for creaseweight attribute from incoming geometry. 

The`Crease Weight`attribute can be used to set individual edge crease weights for sub-division surfaces (see [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP") ). This vertex attribute defines the weight for the edge which goes from that vertex to the next vertex in the polygon. For example, with a triangle (which has vertices 0, 1, 2), the attribute for vertex 1 defines the crease weight for the edge (1, 2). The attribute for vertex 2 defines the crease weight for edge (2, 0). The crease weight should be greater than 0. The larger the value for crease weights, the sharper the edge will be when sub-divided. 

Crease attributes can be visualized by passing them into a [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP"). 
* Keep Crease`off`-
* Add Crease`on`-
* No Crease`remove`-


Crease`crease`\- If you select 'Add Crease' from the menu above, enter expressions here to control the values of the creaseweights here. The attribute to modify is: me.inputVertex.creaseWeight[0]. Values for the weight of the vertex can range from 0.0001 to infinity. 

## 

Parameters - Attributes Page

Custom Attribute`attr`\- Sequence of custom attributes to be added to the geometry created. 

Name`attr0name`\- Creates a custom attribute with this name. 

Type`attr0type`\- ⊞ \- The type of attribute created can be selected from this menu. 
* float`float`-
* vec2`vec2`-
* vec3`vec3`-
* vec4`vec4`-
* int`int`-
* ivec2`ivec2`-
* ivec3`ivec3`-
* ivec4`ivec4`-


Value`attr0value`\- ⊞ \- Set the values of the Custom Attrib using these parameters. 
* Value`attr0value1`-
* Value`attr0value2`-
* Value`attr0value3`-
* Value`attr0value4`-

## 

Examples

### 

Texture Offsets

You can have set of images in a TOP, and apply all of them in one material to different parts of an object. This allows you to have a pre-rendered animation clip with the clip playing at different speeds and time offsets on different surfaces. 

You can adjust the material frame time by the first vertex/point texture W component (texture coordinated are U (horizontal), V (vertical) and W (one of a set of texture images). A texture (W) value of -1 moves back in time 1 frame. This lets you apply different frames to many polygons simultaneously using the Vertex SOP, or [Point SOP](<./Point_SOP.md> "Point SOP"). 

## 

Operator Inputs
* Input 0:  -
  * Input 1:  -

## 

Info CHOP Channels

Extra Information for the Vertex SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditor2021.100002020.200002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• Vertex • [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
