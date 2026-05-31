# Alembic SOP

##   
  
Summary

The Alembic SOP loads and plays back [Alembic](<http://www.alembic.io/>) file geometry sequences. 

The supported Alembic primitives are polymesh, curves, and points for geometry. As well, Alembic transformations are supported. 

For Alembic files that contain animation, use the Time parameter and pay attention to the Unit menu to control it in frames, seconds, or whatever you like. 

An Alembic archive may contain one or more object paths for one or multiple geometries. It is possible to view these objects all at once or select them separately using the 'Object Path' parameter menu. 

Each object in an Alembic file schema may possess standard or custom attributes. The standard attributes are normal (`N`), velocity (`V`), and texture coordinates (`UV`). Multiple custom attributes may live in an Alembic schema with more flexible names and types. The custom attribute types can be any of the following: 
* float arrays
  * integer arrays
  * 2d or 3d vectors of floats
  * matrix with 16 float elements


The conversion between the Alembic geometries scopes to the TouchDesigner attributes types are shown in the table below:   
  
---  
**Alembic Scope** | **TouchDesigner Attribute**  
Varying, Vertex | Point  
Facevarying | Vertex  
Uniform, Constant | Primitive  
  
The Alembic SOP lets you load geometry to either the CPU or the GPU. While using the GPU is much faster, it has some limitations: 
* In GPU direct mode you can not connect additional SOPs downstream.
  * In GPU direct mode, when there are multiple objects with different sets of attributes, a default value is used for the missing attributes of each objects. For example, if one geometry has normal data and another one doesn’t, the x, y, and z elements of normal vector for the geometry with the missing normal attribute will be set to 0, 0, 1 respectively.


[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[alembicSOP_Class](<./AlembicSOP_Class.md> "AlembicSOP Class")

## 

Parameters - Page

Alembic File`file`\- The file path to the Alembic file. 

Object Path`objectpath`\- Specify which geometry object to be loaded. Each geometry object can represent a hierarchies of multiple geometries. It is also possible to choose the "All Objects" option from the list of available objects. This option is selected by default. 

Time`time`\- Specify which part of the Alembic samples sequence is loaded. The time unit menu converts the current time units to the selected unit. The available options are Frames, Seconds, and Fraction. 

Time Unit`timeunit`\- 

Transform`xform`\- ⊞ \- Select which transform is applied if the transform data is available from the input Alembic file. 
* None`none`\- No transformation is applied to the geometry(s), they reside at the origin.
* Static Local Transformation`transform`\- Applies the static local transformation for the selected geometry objects from the Object Path.
* Static World Transformation`transform`\- Applies the static world transformation of the selected geometry objects from the Object Path up to their parents transformation.
* Dynamic Transformation`transform`\- In the case that the Alembic file includes dynamic or animated geometries the transformation is applied to the selected geometries. This option performs both local and world transformation (if available) for the given geometry.


Interpolation`interp`\- ⊞ \- Interpolate between the samples/keyframes in the Alembic file. This parameter only works if the selected geometries are defined as dynamic and the transformation information are available from the input Alembic file. 
* None`none`\- No interpolation is performed between each samples.
* Smooth Interpolation`interpT`\- Smooth interpolation between each two samples is calculated.


Straight to GPU`straightgpu`\- Load the geometry directly to the GPU. This options is much faster than the default loading to CPU, however you can not use the geometry output to other SOPs or access the geometry data in the [SOP to CHOP](<./SOP_to_CHOP.md> "SOP to CHOP") or [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"). It is recommended that the Alembic file have the normals and UVs baked into the file since you can not add them via SOPs in TouchDesigner. 

Compute Normal`compnml`\- Creates normals for the input geometry. 

Unload`loadfile`\- Toggling the unload to "on" will unload the file and close it. By setting it to "off", the file will be loaded again. When the file is unloaded it can be overwritten by other applications or deleted. 

## 

Info CHOP Channels

Extra Information for the Alembic SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). 

### 

Specific Alembic SOP Info Channels
* start_time -
* end_time -

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
[Add ](<./Add_SOP.md> "Add SOP")• Alembic • [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Experimental:Face Track ](</Experimental:Face_Track_SOP> "Experimental:Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [Experimental:POP to ](</Experimental:POP_to_SOP> "Experimental:POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")• [Experimental:ZED ](</Experimental:ZED_SOP> "Experimental:ZED SOP")
