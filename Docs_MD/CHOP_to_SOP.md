# CHOP to SOP

##   
  
Summary

The CHOP to SOP takes CHOP channels and generates 3D polygons in a SOP. It reads sample data from a [CHOP](<./CHOP.md> "CHOP") and converts it into point positions and point attributes. This makes it complementary to the [SOP to CHOP](<./SOP_to_CHOP.md> "SOP to CHOP"). The Channels created by the [SOP to CHOP](<./SOP_to_CHOP.md> "SOP to CHOP") can be modified and then re-inserted into the SOP network via a CHOP to SOP. 

By default, the SOP is a line from (`-1 0 0`) to (`1 0 0`) containing one point for every sample in the CHOP. 

It matches the input channels to the Channel Scope (`tx ty tz`) where possible. If`tx`or`ty`or`tz`don’t match anything, it just uses the value from the default line, and it only shows a Warning. 

The simplest thing to do is to send it a channel named`ty`, which will make a 3D curve that looks like the CHOP curve. 

This does what a [Point SOP](<./Point_SOP.md> "Point SOP") with a`op('wave1')['chan1'].eval(0)`function can do, but is much faster. 

By using point groups from the incoming SOP, the channels can be inserted only into the group's points. 

The CHOP to SOP also supports custom attributes. If the user maps a channel to an attribute that is not found, that attribute is added to the points. Currently, all custom attributes are floats and of size = 1. 

In its default state it will attempt to replace the point positions (`P(0) P(1) P(2)`) with the channels named`tx ty`and`tz`. 

The channel and attribute scope are first expanded into individual names and matched on a 1 to 1 basis. If you are filling P it doesn't matter if you specify`t[xyz]`or`tx ty tz`, both will replace`P(0) P(1) P(2)`, which can be collapsed to`P`. 

For example: Add custom attributes "Scale", "Twist" or "Roll" to the backbone's points with a CHOP to SOP. 

If you connect a SOP to its input, it will use the SOP as a starting geometry versus the default line. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[choptoSOP_Class](<./ChoptoSOP_Class.md> "ChoptoSOP Class")

## 

Parameters - Page

Group`group`\- Modify only the points within this point group. If blank, all points are modified. Accepts patterns, as described in: [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

CHOP`chop`\- Specifies which CHOP Network / CHOP contains the sample data to fetch. 

Start Position`startpos`\- ⊞ \- Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes. 
* X`startposx`-
* Y`startposy`-
* Z`startposz`-


End Position`endpos`\- ⊞ \- Sets the bounds for positions that are not defined by a channel, ie. a channel is not set to one of the P attributes. 
* X`endposx`-
* Y`endposy`-
* Z`endposz`-


Channel Scope`chanscope`\- The names to use to modify the attributes. 

Attribute Scope`attscope`\- A string list of attributes to modify in the SOP. List of Common Attributes: 

  *`**P**`\- Point position (X, Y, Z) - 3 values
  *`**Pw**`\- Point weight - 1 value
  *`**Cd**`\- Point color (red, green, blue, alpha) - 4 values
  *`**N**`\- Point normal (X, Y, Z) - 3 values
  *`**uv**`\- Point texture coordinates (U, V, W) - 3 values


See [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)") for a complete listing of attributes. __

Organize by Attribute`organize`\- Instead of using the point index, use the value of this attribute as the index to use when looking up into the CHOP. 

Mapping`mapping`\- ⊞ \- Determines how the CHOP samples are mapped to the geometry points. 
* One Sample to Each Point`onetoone`\- The samples are simply mapped 1-to-1, each sample is mapped to the next point in order.
* Resample CHOP to Fit SOP`scale`\- If there are more or less CHOP samples than points in the geometry, then the CHOP channels are resampled to interpolate values for all the geometry points.


Compute Normals`compnml`\- Creates normals on the geometry. 

Compute Tangents`comptang`\- Creates tangents on the geometry. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the CHOP to SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• CHOP to • [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
