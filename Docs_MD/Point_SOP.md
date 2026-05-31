# Point SOP

##   
  
Summary

The Point SOP allows you to get right into the geometry and manipulate the position, color, texture coordinates, and normals of the points in the Source, and other attributes. The Point SOP also lets you create custom point attributes. It is the complement to the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP"). Using a second input allows for combining of two SOPs using their respective expressions (see: [PointSOP Class](<./PointSOP_Class.md> "PointSOP Class")). If the second input has less points than the first input, the points in the second input will be cycled. 

For example, you can create point coloring, or flip the normals of incoming geometry. Using expressions in Position X, Y and Z, you can move any given input point to a new place as defined by the expression with any standard attributes. 

The Width (width) attribute affects the line width in the [Line MAT](<./Line_MAT.md> "Line MAT"). The Scale attribute (pscale) affects particle size, and in the [Line MAT](<./Line_MAT.md> "Line MAT") it affects the dot size at each point. 

**Tip** : For greater flexibility, use the [Script SOP](<./Script_SOP.md> "Script SOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[pointSOP_Class](<./PointSOP_Class.md> "PointSOP Class")

## 

Parameters - Point Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this`SOP`to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Position`t`\- ⊞ \- Expressions to translate the XYZ coordinates of a given point can be entered here. The attributes to modify here are:`me.inputPoint.x`,`me.inputPoint.y`and`me.inputPoint.z`. 

Simply entering`me.inputPoint.x`into the Position X field means that the X coordinate of each point that comes in is passed straight through with no modification. 

Changing this entry to`me.inputPoint.x+5`means that the X coordinate of each point that comes in will be displaced by 5 units. This expression can be expanded to produce many useful effects. Transformations can also be effected in the Y and Z fields. 
* Position`tx`-
* Position`ty`-
* Position`tz`-


Weight`doweight`\- ⊞ \- Select between keeping the weight or adding a new weight. 
* Keep Weight`off`-
* New Weight`on`-


Weight`weight`\- If you select 'New Weight' from the menu above, enter expressions here to control the values of the point weights here. The attribute to modify is:`me.inputPoint.w`. Values for the weight of the point can range from 0.0001 to infinity. 

Color`doclr`\- ⊞ \- Select between keeping the color, adding new color, or using no color. 
* Keep Color`off`-
* Add Color`on`-
* No Color`remove`-


Color`diff`\- ⊞ \- If you select 'Add Color' from the menu above, Cd color attributes will be added/modified in the SOP. Enter expressions below to control the values of the point colors. The attributes to modify are:`me.inputColor[0]`for red,`me.inputColor[1]`for green,`me.inputColor[2]`for blue, and`me.inputColor[3]`for alpha. 

If you select 'No Color' from the menu above, the Cd color attribute will be removed from the SOP. 
* Color`diffr`-
* Color`diffg`-
* Color`diffb`-


Alpha`alpha`\- Control the alpha attribute in the same manner as the rgb colors above. Alpha is Cd[3] and comes from input via`me.inputColor[3]`Normal`donml`\- ⊞ \- Select between keeping the normals, adding new normals, or using no normals. 
* Keep Normal`off`-
* Add Normal`on`-
* No Normal`remove`-


Normals`n`\- ⊞ \- If you select 'Add Normal' from the menu above, N normal attributes will be added/modified in the SOP. Enter expressions to change a given point normal here. Point normals are directional vectors used by other SOPs, such as Turbulence, Facet and Copy. See [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)") article for detailed information. The attributes to modify are:`me.inputNormal[0]`,`me.inputNormal[1]`and`me.inputNormal[2]`. 

If you select 'No Normal' from the menu above, the N normal attribute will be removed from the SOP. 
* Normals`nx`-
* Normals`ny`-
* Normals`nz`-

### 

Flipping Normals

You can flip the point normals of incoming geometry by entering: 
[code](-me.inputNormal[0] -me.inputNormal[1] -me.inputNormal[2])
    
[/code]

in the fields with this parameter set to Add Normals. This works, because it takes the existing normals 
[code](me.inputNormal[0] me.inputNormal[1] me.inputNormal[2])
    
[/code]

and inverts them (the preceding - ). 

Texture`douvw`\- ⊞ \- Select between keeping the texture coordinates, adding new texture coordinates, or using no texture coordinates. 
* Keep Texture`off`-
* Add Texture`on`-
* No Texture`remove`-


Texture`map`\- ⊞ \- If you select 'Add Texture' from the menu above, uv texture coordinate attributes will be added/modified in the SOP. Enter expressions here to control the values of the texture coordinates here. The attributes to modify are:`me.inputTexture[0]`,`me.inputTexture[1]`and`me.inputTexture[2]`. 

If you select 'No Texture' from the menu above, the uv texture coordinate attribute will be removed from the SOP. 
* Texture`mapu`-
* Texture`mapv`-
* Texture`mapw`-


Width(Line MAT)`dowidth`\- ⊞ \- Select between keeping the width attribute or adding a new width. This Width (width) attribute is used exclusively with [Line MAT](<./Line_MAT.md> "Line MAT") to control line width when the material is rendered. 
* Keep Width`off`-
* New Width`on`-


Width(Line MAT)`width`\- If you select 'New Width' from the menu above, width attribute will be added/modified in the SOP. Enter expressions here to control the values of the point widths here. The attribute to modify is:`me.inputPoint.width[0]`. 

Scale`dopscale`\- ⊞ \- Select between keeping the scale attribute, adding new scale, or using no scale. This scale (pscale) attribute is used with the [Particle SOP](<./Particle_SOP.md> "Particle SOP") and acts as a multiplier for the size of particles. The value of this attribute is multiplied by the size specified in the [Particle SOP](<./Particle_SOP.md> "Particle SOP")'s render attributes to scale each particle. This attribute is used by the [Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT") when rendering point sprites. 
* Keep Scale`off`-
* Add Scale`on`-
* No Scale`remove`-


Scale`pscale`\- If you select 'Add Scale' from the menu above, pscale attribute will be added/modified in the SOP. Enter expressions here to control the values of the point particle scales here. The attribute to modify is:`me.inputPoint.pscale[0]`. 

If you select 'No Scale' from the menu above, the pscale attribute will be removed from the SOP. __

## 

Parameters - Custom Page

Custom Attribute`attr`\- Sequence of custom attributes to add 

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

Parameters - Particle Page

Point Mass/Drag`domass`\- ⊞ \- Retains, adds, or removes mass and drag attributes for points. 
* Keep Mass/Drag`off`-
* Add Mass/Drag`on`-
* No Mass/Drag`remove`-


Mass`mass`\- If you select 'Add Mass/Drag' from the menu above, mass attribute will be added/modified in the SOP. If you select 'No Mass/Drag' from the menu above, the mass attribute will be removed from the SOP. 

Drag`drag`\- If you select 'Add Mass/Drag' from the menu above, drag attribute will be added/modified in the SOP. If you select 'No Mass/Drag' from the menu above, the drag attribute will be removed from the SOP. 

Tension`dotension`\- Tension affects the elasticity of the edges the point is connected to. 

Tension`tension`\- If you select 'Add Tension' from the menu above, tension attribute will be added/modified in the SOP. Enter expressions here to control the values of the tension here. The attribute to modify is:`me.inputPoint.tension[0]`. If you select 'No Tension' from the menu above, the tension attribute will be removed from the SOP. 

Spring K`dospringk`\- ⊞ \- Retains, adds, or removes spring constant attributes for points. The Spring Constant is a well known physical property affecting each point. 
* Keep Spring K`off`-
* Add Spring K`on`-
* No Spring K`remove`-


Spring K`springk`\- If you select 'Add Spring K' from the menu above, springk attribute will be added/modified in the SOP. Enter expressions here to control the values of the springk here. The attribute to modify is:`me.inputPoint.springk[0]`. If you select 'No Spring K' from the menu above, the springk attribute will be removed from the SOP. 

Velocity`dovel`\- ⊞ \- Retains, adds, or removes the velocity of points. Defines the magnitude of the particle's velocity in the X, Y and Z directions. 
* Keep Velocity`off`-
* Add Velocity`on`-
* No Velocity`remove`-


Velocity`v`\- ⊞ \- If you select 'Add Velocity' from the menu above, v velocity attributes will be added/modified in the SOP. Enter expressions to change a given point velocity here. The attributes to modify here are:`me.inputPoint.v[0]`,`me.inputPoint.v[1]`and`me.inputPoint.v[2]`. If you select 'No Velocity' from the menu above, the v velocity attribute will be removed from the SOP. 
* X`vx`-
* Y`vy`-
* Z`vz`-


Up Vector`doup`\- ⊞ \- Creates/Removes the "up" attribute for points. This attribute defines an up vector which is used to fully define the space around a point (for particle instancing or copying geometry). The up vector can be used in conjunction with the copy template's normals to control the orientation of the copies in the [Copy SOP](<./Copy_SOP.md> "Copy SOP"). 
* Keep Up Vector`off`-
* Add Up Vector`on`-
* No Up Vector`remove`-


Up Vector`up`\- ⊞ \- If you select 'Add Up Vector' from the menu above, up attributes will be added/modified in the SOP. Enter expressions to change a given point up vector here. The attributes to modify here are:`me.inputPoint.up[0]`,`me.inputPoint.up[1]`and`me.inputPoint.up[2]`. If you select 'No Up Vector' from the menu above, the up attribute will be removed from the SOP. 
* X`upx`-
* Y`upy`-
* Z`upz`-

## 

Parameters - Force Page

Radius`doradius`\- ⊞ \- Retains, adds, or removes radiusf attributes for points, used to modify the distance roll-off effect. The roll-off is:`r /(r+d^2)`Where`r`is radius, and`d`is distance from attractor point. If no radius is set, no attenuation is performed. 
* Keep Radius`off`-
* Add Radius`on`-
* No Radius`remove`-


Radius`radiusf`\- If you select 'Add Radius' from the menu above, radiusf attribute will be added/modified in the SOP. Enter expressions here to control the values of the distance roll-off here. If you select 'No Radius' from the menu above, the radiusf attribute will be removed from the SOP. 

F Scale`doscale`\- ⊞ \- Retains, adds, or removes scalef attributes for points, a multiplier for total force associated with this attractor point. 

Both Radius and Force Scale will default to 1 if not created as point attributes. 

**Radial / Normal / Edge / Directional Force** \- These four parameters introduce a type of force when created and each has a corresponding multiplier associated with it. 
* Keep F Scale`off`-
* Add F Scale`on`-
* No F Scale`remove`-


F Scale`scalef`\- If you select 'Add F Scale' from the menu above, scalef attribute will be added/modified in the SOP. Enter expressions here to control the values of the force multiplier here. If you select 'No F scale' from the menu above, the scalef attribute will be removed from the SOP. 

Radial F`doradialf`\- ⊞ \- Retains, adds, or removes radialf attributes for points, the force directed towards the attractor point. Positive multipliers are towards while negative are away. 
* Keep Radial F`off`-
* Add Radial F`on`-
* No Radial F`remove`-


Radial F`radialf`\- If you select 'Add Radial F' from the menu above, radialf attribute will be added/modified in the SOP. Enter expressions here to control the values of the directed force here. If you select 'No Radial F' from the menu above, the radialf attribute will be removed from the SOP. 

Normal F`donormalf`\- ⊞ \- Retains, adds, or removes normalf attributes for points, the force directed along the point normal direction. 
* Keep Normal F`off`-
* Add Normal F`on`-
* No Normal F`remove`-


Normal F`normalf`\- If you select 'Add Normal F' from the menu above, normalf attribute will be added/modified in the SOP. Enter expressions here to control the values of the force in the normal direction here. If you select 'No Normal F' from the menu above, the normalf attribute will be removed from the SOP. 

Edge F`doedgef`\- ⊞ \- Retains, adds, or removes edgef attributes for points, which only works on primitive face types. The force is directed in the direction of the edge leading from that point. If multiple vertices reference the same point, then the direction is the edge direction of the last primitive referencing the point. 

If the face open, then the end point has an edge direction equal to that of the preceding point in that primitive. 

**Note:** When edge forces are added using the Point SOP, the force directions are computed in the Point SOP itself. Thus, any following transformations do not effect these. If you wish for the edge directions to be transformed as well, all transformations must be done before the Point SOP. Only the edge forces function like this. 
* Keep Edge F`off`-
* Add Edge F`on`-
* No Edge F`remove`-


Edge F`edgef`\- If you select 'Add Edge F' from the menu above, edgef attribute will be added/modified in the SOP. Enter expressions here to control the values of the force in the normal direction here. If you select 'No Edge F' from the menu above, the edgef attribute will be removed from the SOP. 

Dir. F`dodirf`\- ⊞ \- Retains, adds, or removes dirf attributes for points, an arbitrary directional force still affected by the distance roll-off function. 
* Keep Dir. F`off`-
* Add Dir. F`on`-
* No Dir. F`remove`-


Dir. F`dirf`\- ⊞ \- If you select 'Add Dir. F' from the menu above, dirf attribute will be added/modified in the SOP. Enter expressions here to control the values of the force in the arbitrary direction here. If you select 'No Dir. F' from the menu above, the dirf attribute will be removed from the SOP. 
* X`dirfx`-
* Y`dirfy`-
* Z`dirfz`-

## 

Operator Inputs
* Input 0: Source 1 -
  * Input 1: Source 2 -

## 

Info CHOP Channels

Extra Information for the Point SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• Point • [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
