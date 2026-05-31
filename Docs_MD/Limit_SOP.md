# Limit SOP

##   
  
Summary

The Limit SOP creates geometry from samples fed to it by [CHOPs](<./CHOP.md> "CHOP"). It creates geometry at every point in the sample. Different types of geometry can be created using the Output Type parameter on the **Channels Page**. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[limitSOP_Class](<./LimitSOP_Class.md> "LimitSOP Class")

## 

Parameters - Channels Page

CHOP`chop`\- Specifies which CHOP Network / CHOP contains the sample data to fetch. 

Rotate Order`rord`\- ⊞ \- Specifies the order in which the Rotate Channel X / Y / Z channels are applied. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


X Channel`chanx`\- Channels used to specify the point's positions, tx. 

Y Channel`chany`\- Channels used to specify the point's positions, ty. 

Z Channel`chanz`\- Channels used to specify the point's positions, tz. 

Rotate Channel X`chanrx`\- Channels used to specify the rotational data of the geomtery created at each point. Only used when Output Type is "Polygon at Each Point" or "Primitive Circle at Each Point". 

Rotate Channel Y`chanry`\- Channels used to specify the rotational data of the geomtery created at each point. Only used when Output Type is "Polygon at Each Point" or "Primitive Circle at Each Point". 

Rotate Channel Z`chanrz`\- Channels used to specify the rotational data of the geomtery created at each point. Only used when Output Type is "Polygon at Each Point" or "Primitive Circle at Each Point". 

Radius Channel`chanrad`\- Uniformly controls the radius of the geometry created at each point. The Radius channels are multiplied with the Radius parameter on the **Output Page**. 

Radius Channel X`chanradx`\- Channels that control the radius on the respective axis. The Radius channels are multiplied with the Radius parameter on the **Output Page**. 

Radius Channel Y`chanrady`\- Channels that control the radius on the respective axis. The Radius channels are multiplied with the Radius parameter on the **Output Page**. 

Radius Channel Z`chanradz`\- Channels that control the radius on the respective axis. The Radius channels are multiplied with the Radius parameter on the **Output Page**. 

Alpha Channel`chanalpha`\- Controls the point alpha, giving you alpha control of any geometry created at those points. 

**Note:** If using a [Copy SOP](<./Copy_SOP.md> "Copy SOP"), turn on the Use Template Point Attributes option in the Copy SOP's **Attributes Page** to allow the geometry to inherit the point attributes. __

Red Channel`chanr`\- These channels control the point color, or the color of any geometry created at those points. 

Green Channel`chang`\- These channels control the point color, or the color of any geometry created at those points. 

Blue Channel`chanb`\- These channels control the point color, or the color of any geometry created at those points. 

Texture W`texturew`\- Controls the w texture-offset for the point(s) This is most often used as a frame-offset or time-offset, expressed in # of frames from the current frame or frame 1 of an image sequence. 

## 

Parameters - Custom Page

Allows custom attributes to be added to the geometry created. Use the + button to add additional parameters to add more custom attributes. 

Custom Attribute`customattr`\- Sequence of custom attributes to be added to the geometry created. 

Name`customattr0name`\- Specify the name of the custom attribute, for example pscale, age, or any custom name. 

Channel Zero`customattr0chan0`\- Select which channel to assign to the [0] index of the attribute. ie. pscale[0] 

Channel One`customattr0chan1`\- Select which channel to assign to the [1] index of the attribute. ie. pscale[1] 

Channel Two`customattr0chan2`\- Select which channel to assign to the [2] index of the attribute. ie. pscale[2] 

Channel Three`customattr0chan3`\- Select which channel to assign to the [3] index of the attribute. ie. pscale[3] 

## 

Parameters - Output Page

Output Type`output`\- ⊞ \- The type of geometry the Limit SOP produces from its sample data. 
* Polygonal Line`line`\- Creates a point for each sample and connects them with a polygonal line.
* Polygon at Each Point`polys`\- Places a polygon at each sample point. Number of points in polygon defined by Divisions.
* Primitive Circle at Each Point`circles`\- Places a primitive circle at each sample point.
* Sphere at Each Point`spheres`\- Places a primitive sphere at each smaple point.
* Poly Sphere at Each Point`polyspheres`\- Places a polygonal sphere at each sample point. Sphere's frequency defined by Divisions.
* Tubes`tubes`\- Creates a tube down the path. Tubes cross-section defined by Divisions.
* Strips`strips`\- Creates a strip down the path. Number of points in strip defined by Divisions.


Divisions`divisions`\- Only works on the following Output Types. 
* Polygon at Each Point - Number of points per polygon.
  * Poly Sphere at Each Point - Frequency of each Polygonal Sphere.
  * Tubes - Number of points in cross-section of the tube.
  * Strips - Number of points in cross-section of the strip.


Radius`rad`\- Radius of geometry created. Disabled for "Polygonal Line". 

Smooth Flip`flipsmooth`\- Dynamically controls the twist of each instance of geometry on a series of points to avoid frame-by-frame flipping, which can sometimes occur when geometry is oriented along a path. 

Limit`dolimit`\- ⊞ \- Creates a bounding box for the position of the output geometry. Drop down menu determines behavior when outside bounded region. 
* Off`off`\- Bounding region off.
* Clamp`clamp`\- Clamps position to specified value.
* Loop`loop`\- Loops position between bounded region.
* Zigzag`zigzag`\- Zigzags position back and forth between bounded region.


X Limit`xlimit`\- ⊞ \- Parameters to set edges of bounding region when Limit is active. 

  *`xlimitmin`-


  *`xlimitmax`-


Y Limit`ylimit`\- ⊞ \- Parameters to set edges of bounding region when Limit is active. 

  *`ylimitmin`-


  *`ylimitmax`-


Z Limit`zlimit`\- ⊞ \- Parameters to set edges of bounding region when Limit is active. 

  *`zlimitmin`-


  *`zlimitmax`-


Apply Texture`texture`\- Applys u, v, and w texture coordinates to the created geometry. 

Scale`texscale`\- ⊞ \- Scales the texture coordinates a specific amount. 

  *`texscale1`-


  *`texscale2`-


Offset`texoffset`\- ⊞ \- Offsets the texture coordinates a specific amount. 

  *`texoffset1`-


  *`texoffset2`-


Orient to Path`orient`\- If this option is selected, the object will be oriented along the path. To see what the path looks like, change the Output Type to "Polygonal Line". When the Output Type is "Polygon/Primitive Circle at Each Point", the positive Z axis of each object will be pointing down the path. When the Output Type is "Tubes/Strips" then the cross-section of the geometry created will be pointing down the path. 

Lookat Object`lookat`\- Orient to Path must be checked for Lookat Object to have any effect. This allows you to orient your geometry by naming the object you would like it to Look At, or point to. Once you have designated this object to look at, it will continue to face that object, even if you move it. The Look At parameter points the each piece of geometry at the other object's origin individually. 

Rotate Polys`dorotate`\- ⊞ \- Rotate the geometry at each point using the Rotate parameter (below). Only works for Output Type is "Polygon/Primitive Circle at Each Point". 
* Off`off`\- Do not rotate polys. Rotate parameter is greyed out.
* On`on`\- Add value of Rotate to polys equally.
* Cumulative`cum`\- Add value of Rotate to polys cumulatively (ie. increasing with each poly).


Rotate`rotate`\- ⊞ \- Rotation channels rx, ry, and rz for Rotate Polys parameter. 
* X`rotatex`-
* Y`rotatey`-
* Z`rotatez`-


Compute Normals`normals`\- Computes normals for the geometry created. 

## 

Info CHOP Channels

Extra Information for the Limit SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2021.100002020.200002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• Limit • [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
