# Texture SOP

##   
  
Summary

The Texture SOP assigns texture UV and W coordinates to the Source geometry for use in texture and bump mapping. It generates multi-layers of texture coordinates. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[textureSOP_Class](</TextureSOP_Class> "TextureSOP Class")

## 

Fixing Seams & Unrolling Geometry

**NOTE:** the following discussing pertains only to face and hull primitives. 

If a texture type requires fixing of seams and the texture is applied to vertices, the wrapped primitives are unrolled before computing the texture coordinates. Unrolling a wrapped primitive turns it into an open primitive whose new vertices use the same points as the vertices they have been uniqued from. Thus, unrolling does not change the point count, nor does it allow cracks to appear further down the road. Explicit unrolling, using the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP"), is not required. 

The seam fixing is done after computing the texture coordinates. It is required whether textures are applied to vertices or points, and it's done in u, v, or both. 

The following texture types require fixing of seams: 
* Cylindrical \- seams fixed in u.
  * Polar \- seams fixed in u and v.
  * Row/col \- seams fixed in u and v.
  * Spline types: Uniform, Chord Length, and Average \- seams fixed in u and v.


**Note:** When the projection type is **Cylindrical** or **Polar** , closed meshes, Bzier & NURBS surfaces will be opened. At least one row/column of vertices will be added (possibly more for NURBS<). This is to prevent poor interpolation of texture coordinates at the seam of the join. 

## 

Parameters - Page

Primitive Group`group`\- If there are input primitive groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Does not work with point or vertex groups. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

## 

Parameters - Texture Page

Texture Layer`texlayer`\- If the geometry has multiple textures layers applied to it, this parameter determines which layer of UV coordinates this Texture SOP will effect. 

Texture Type`type`\- ⊞ \- The Face, Uniform Spline, and Arc-Length Spline texturing methods accept spline curves as well as polygons. 

When using one of the spline-based methods, specifying a paste hierarchy in the Group field will propagate the computation of texture coordinates to all of its nodes. Projection methods will typically yield smoother texture continuity between pasted surfaces than any of the spline methods. Sometimes it helps ensuring that pasted features are Chord-length parameterized with the [Basis SOP](<./Basis_SOP.md> "Basis SOP"). 
* Orthographic`texture`\- Direct projection from Projection Axis.
* XYZ Position`xyzposition`\- The XYZ position of the vertices will be copied into the UVW values.
* Equirectangular Inside (Spherical Polar)`equirectangularin`\- Applies corrdinates to properly apply an equirectangular texture map to the inside of an object. Useful for skyboxes for example.
* Equirectangular Outside (Spherical Polar)`equirectangularout`\- Applies corrdinates to properly apply an equirectangular texture map to the outside of an object.
* Cylindrical`cylin`\- Wrap cylindrically in Projection Axis direction.
* Row & Columns`rowcol`\- For geometry constructed as a mesh (Grid, Sphere, Tube, Skin, and Sweep). The U coordinates are placed along rows, and the V coordinates along columns. This is good for texturing curved meshes such as car fenders where you cannot project from any one axis.
* Face`face`\- Maps a copy of the texture onto every face. You should make points unique using a [Facet SOP](<./Facet_SOP.md> "Facet SOP"), before using this function in the Texture SOP. The map is graphically projected to each face along its normal, so the texture is oriented properly for each face. However, the map is not scaled to fit each polygon, nor is it distorted by the shape of each polygon. If the geometry changes in size in object space, the texture does not "stick" to the geometry. It is best suited to texturing objects that represent chunks of rock and brick, as the textures will likely not match at the edges between polygons.
* Modify Source`modify`\- If the Source already has texture UV coordinates, they are maintained. You can offset and scale them, however, using Scale and Offset.
* Uniform Spline`suniform`\- This projection type operates only on NURBS and Bzier surfaces. It samples the domain space (i.e. the basis) of each surface uniformly in U and V and assigns those (u,v) values as texture coordinates to the surface points or vertices. To ensure continuity between the texture space of adjacent surfaces insert a [Basis SOP](<./Basis_SOP.md> "Basis SOP") before the Texture SOP and toggle Concatenate on to merge the spline bases in U and/or V.
* Average Spline`saverage`\- Stores the average of degree successive knots into the texture attribute. These averages are known as **Greville points**. This method and Uniform Spline are recommended for pasted surfaces.
* Arc Length Spline`sarclen`\- This method is similar to the Uniform Spline method since it relies on the underlying spline basis when computing the texture coordinates. Both methods generate texture coordinates in the same range, bounded by the minimum and maximum knot values. The difference between the two spline methods lies in the spacing between successive texture coordinates. The uniform method samples the parameter space uniformly. The Arc-Length Spline method chooses the texture coordinates based on surface arc-lengths.


Since the Uniform Spline method relies heavily on the parametric fabric of the surface, the resulting texture will tend to squash and stretch given uneven surface parameterizations. The Arc-Length Spline method reduces this effect by relating the texture space directly to the world space of the surface, while ensuring that the size and origin of the generated texture space coincide with those of the underlying domain. 
* Edge Length`edgelength`\- Applies to hulls + faces (NURBs/Bezier/Polygon).
* Perspective From Camera`persp`\- The texture coordinates are assigned so that the world space of the object can be textured to fit the projection of the camera exactly. If any points are behind the near clipping plane or beyond the far clipping plane, the texture coordinates (`0, 0, 0`) are assigned. Note: Unless a Custom Projection matrix is used in the [Camera COMP](<./Camera_COMP.md> "Camera COMP"), the aspect ratio of the projection is assumed to be 1:1. You may need to scale the UVs to match the aspect ratio of your render.
* Equidistant Azimuth (Fish Eye 180)`equiazimuth`\- Applies coordinates for using 180 degree Fish Eye maps.
* Equidistant Azimuth (Fish Eye 360)`equiazimuth360`\- Applies coordinates for using 360 degree Fish Eye maps.


Projection Axis`axis`\- ⊞ \- Axis to project along, or projection method from splines. X, Y, or Z axes. 
* X Axis`x`-
* Y Axis`y`-
* Z Axis`z`-


Camera Name`camera`\- This is used when the Perspective From Camera Texture Type is selected. The menu is used to select which light or camera to project the perspective coordinates from. 

Apply to`coord`\- ⊞ \- Select to apply texture coordinates to their Natural Location, Point textures, or Vertex textures. 

When Natural location is selected, the UV's will be applied to the verticies when using Polar, Cylindrical, Rows and Columns, and Face texture types. Orthographic, Uniform Spline, Average Spline and Arc Length Spline will always generate point UV's when you choose Natural. 

Natural Location will also create vertex uvs when creating new texture layers, if a vertex uv already exists for layer 0. 

IIf the primitive is open in both directions like a grid or a surface (so that the ends do not touch), then the advantage of vertex UV's does not apply since there are no matched seams on the single surface to worry about. 

Using vertex UVs gives you unique points at the closed seam whereas point UVs are shared at seams and are, by default given a value of 0 for either U or V depending on the closed direction of the surface. If you want to make a closed surface open, simply insert a [Carve SOP](<./Carve_SOP.md> "Carve SOP") in the chain and place a single carve in the surface of the direction that the surface is closed. 
* Natural location`natural`-
* Point texture`point`-
* Vertex texture (fix seams)`vertex`-


Scale`s`\- ⊞ \- Scales the texture coordinates a specific amount. 

  *`su`-


  *`sv`-


  *`sw`-


Offset`offset`\- ⊞ \- Offsets the texture coordinates a specific amount. 

  *`offsetu`-


  *`offsetv`-


  *`offsetw`-


Rotate`angle`\- Rotates the texture coordinates the specified value. 

**Tip:** Before applying a spline-based texture projection with the Texture SOP, remap the U and/or V bases of the spline surface (using a [Basis SOP](<./Basis_SOP.md> "Basis SOP")) between 0 and 1 to ensure a complete mapping of the texture. If a single texture map must be shared by several surfaces, the surface bases should be concatenated prior to being remapped. __

Fix Face Seams`fixseams`\- Attempts to correct texture continuity at face seams. 

## 

Parameters - Transform Page

Add further transformations to the texture coordinate space. 

Transform Order`xord`\- ⊞ \- Sets the overall transform order for the transformations. The transform order determines the order in which transformations take place. Depending on the order, you can achieve different results using the exact same values. Choose the appropriate order from the menu. 
* Scale Rotate Translate`srt`-
* Scale Translate Rotate`str`-
* Rotate Scale Translate`rst`-
* Rotate Translate Scale`rts`-
* Translate Scale Rotate`tsr`-
* Translate Rotate Scale`trs`-


Rotate Order`rord`\- ⊞ \- Sets the order of the rotations within the overall transform order. 
* Rx Ry Rz`xyz`-
* Rx Rz Ry`xzy`-
* Ry Rx Rz`yxz`-
* Ry Rz Rx`yzx`-
* Rz Rx Ry`zxy`-
* Rz Ry Rx`zyx`-


Translate`t`\- ⊞ \- These three fields move the texture coordinates in the three axes. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- These three fields rotate the texture coordinates in the three axes. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Scale`scaletwo`\- ⊞ \- These three fields scale the texture coordinates in the three axes. 
* X`scaletwox`-
* Y`scaletwoy`-
* Z`scaletwoz`-


Pivot`p`\- ⊞ \- The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which the texture coordinates scale and rotate. Altering the pivot point produces different results depending on the transformation performed. 

For example, during a scaling operation, if the pivot point of the texture coordinates is located at:`-1, -1, 0`and you wanted to scale by`0.5`(reduce its size by 50%) the texture would scale toward the pivot point and appear to slide down and to the left. 

In the example above, rotations performed on a texture coordinates with different pivot points produce very different results. 
* X`px`-
* Y`py`-
* Z`pz`-

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Texture SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Experimental:Face Track ](</Experimental:Face_Track_SOP> "Experimental:Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [Experimental:POP to ](</Experimental:POP_to_SOP> "Experimental:POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• Texture • [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")• [Experimental:ZED ](</Experimental:ZED_SOP> "Experimental:ZED SOP")
