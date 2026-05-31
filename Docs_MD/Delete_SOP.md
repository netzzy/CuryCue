# Delete SOP

##   
  
Summary

The Delete SOP deletes input geometry as selected by a group specification or a geometry selection by using either of the three selection options: by entity number, by a bounding volume, and by entity (primitive/point) normals. You can choose to delete the selected or the non-selected geometry. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[deleteSOP_Class](<./DeleteSOP_Class.md> "DeleteSOP Class")

## 

Parameters - Page

Group`group`\- The name of the group to be created. The default name is set to match the name of the SOP. 

Operation`negate`\- ⊞ \- Choose to Delete the Selected Geometry or Delete the Non-Selected Geometry. 
* Delete Selected`dele`-
* Delete Non-Selected`keep`-


Entity`entity`\- ⊞ \- Choose to delete primitives or points. 
* Primitives`primitive`-
* Points`point`-


Geometry Type`geotype`\- ⊞ \- Select the geometry type group. The selection will only pertain to the geometry type specified. e.g. If you only wanted to group polygons. 
* All Types`all`\- All geometry will be selected.
* Bezier Curve`bezierc`-
* Bezier Surface`bezier`-
* Circle`circle`-
* Mesh`mesh`-
* Metaball`meta`-
* NURBS Curve`nurbc`-
* NURBS Surface`nurb`-
* Particles`part`-
* Polygon`poly`-
* Sphere`sphere`-
* Tube`tube`-
* Triangle Strip`tristrip`-
* Triangle Fan`trifan`-

## 

Parameters - Number Page

Allows selection of grouping of entities by number. When checked, the options relative to this selection option are displayed. 

Use Number`usenumber`\- When the Enable button is checked under the Number button, the selection options become active and can be used to select entities. The fields available are listed below. 

Operation`groupop`\- ⊞ \- When the Number Enable button is checked, this option groups entities based on a defined Pattern or by a Range. 
* Delete by Pattern`pattern`\- Select a pattern in the Pattern field below.
* Delete by Range`range`\- Select a Range using the Start/End and Select_of_ fields below.
* Delete by Expression`filter`\- Select a range using the Filter Expression field below.


Pattern`pattern`\- Activated when Operation is set to Group by Pattern. In this field, enter the range of primitives to select. The required syntax is "**S.P** ", where **S** is the index of the parent surface, and **P** the profile index on that surface. You can mix primitives with profiles in the list. A mixed group is automatically ordered. 

**For example** ;`0.4 2 4 2.5 3.7`selects three profiles and two primitives`0-100:2`selects every other number from 0 to 100`0-10:2,3`selects every two of three`0.0-6`selects six profiles on primitive 0`0.*`selects all profiles on primitive 0`!4`selects every primitive or point except the fourth`9-0`selects first ten (in reverse if ordered flag is on)`!0.*`selects all profiles except those on primitive 0`*`selects all primitives or points, and no profiles 

See Pattern Matching in the [Scripting Guide] __

Start / End`range`\- ⊞ \- Activated when Operation is set to Group by Range. Select the start and end of the primitive/point number selection. 

  *`rangestart`-


  *`rangeend`-


Select _ of _`select`\- ⊞ \- Activated when Operation is set to Group by Range. Select every nth occurrence of every mth entity in the above Start/End range. 

**For example** ; entering 1 and 2 selects 1 out of every 2 entities 

  *`select1`-


  *`select2`-


Filter Expression`filter`\- The Filter Expression provided is evaluated for every point/primitive. Wherever it is true, the entity is added to the selection. 

## 

Parameters - Bounding Volume Page

This option is used for selecting entities based on bounding volumes: **Bounding Box** , or **Bounding Sphere**. When checked, the options relative to this selection option are displayed. 

Use Bounds`usebounds`\- When the Enable button is checked under the Bounding button, the selection options become active and can be used to select entities. The fields available are listed below. The bounding volume can be seen in the viewport as guide geometry. 

Bounding Type`boundtype`\- ⊞ \- Selects the type of bounding volume to use: 
* Bounding Box`usebbox`\- Bounding Box entities contained within the box are selected.
* Bounding Sphere`usebsphere`\- Bounding Sphere entities contained within the sphere are selected.


Size`size`\- ⊞ \- Dimensions of either the Bounding Box or Bounding Sphere in X, Y and Z. 
* X`sizex`-
* Y`sizey`-
* Z`sizez`-


Center`t`\- ⊞ \- The X, Y, and Z coordinates of the center of the bounding volume. 
* X`tx`-
* Y`ty`-
* Z`tz`-

## 

Parameters - Normal Page

This option is used for selecting entities based on the angle of the entity normals. When checked, the options relative to this selection option are displayed. 

Use Normal`usenormal`\- When the Enable button is checked under the Normal button, the selection options become active and can be used to select entities. The fields available are listed below. 

The primary axis and the spread angle from the defined axis define a range of angles. If any entity normals lie within this range, then the associated entity is selected. 

**For example** ; if you want to select the polygons that are very steep in a polygon mountain terrain on the XZ axis. You would set the Direction to be`0, 1, 0`and the spread angle to around 75. This selects all the polygons with normals that lie flat to fairly sloped. You will have grouped all of the polygons that lie flat up to polys that are at a 75 angle from the axis. You are left with all of the polygons that are 76 or greater. __

Direction`dir`\- ⊞ \- The default values of`0, 1, 0`create a normal vector straight up in Y, which is perpendicular to the XZ plane, which becomes the primary axis. The`1, 0, 0`points the normal in positive X, giving a normal axis perpendicular to the YZ. The plane may be positioned at an angle by using values typed in (`1, 1, 0`gives a 45 angle plane) or interactively by using the direction vector jack. Values between 0 and 1 should be used. 
* X`dirx`-
* Y`diry`-
* Z`dirz`-


Spread Angle`angle`\- The value entered in this field generates an angle of deviation from the primary axis. This can be visualized as a cone where the radius of the base of the cone is defined by the Spread Angle and the axis of the cone is determined by the Direction axis. Viewing the primitive normals in the viewport, you can see that any primitives with normals that have an angle that lies in the range of angles defined by the cone will be selected and grouped. 

Backface from`camera`\- This menu allows you to select an object. Typically, a camera object would be chosen. The primitives which are backface when viewed from the object specified will be grouped or selected. 

Delete Unused Groups`removegrp`\- If any group has 0 entries and if this parameter is enabled, then those groups are removed. If you want to keep empty groups, disable this parameter. 

Delete Geometry, Keep Points`keeppoints`\- Deletes the geometry but keeps the points. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Delete SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• Delete • [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
