# ZED POP

##   
  
Summary

**NOTE**

**OS:** This operator is only supported under the **Microsoft Windows** operating system.  


The ZED POP uses the [ZED](<./ZED.md> "ZED") StereoLabs SDK to scan and create geometry meshes (triangles) by moving it around the room or an object of interest or generate live point clouds from on-camera depth data. 

After pressing start the ZED POP uses each frame of video to build up the mesh, with the preview of the captured points in the viewer. 

To know what ZED SDK we are using, refer to the [ZED](<./ZED.md> "ZED") page. See also [ZED](<./ZED.md> "ZED"), [ZED TOP](<./ZED_TOP.md> "ZED TOP"), [ZED CHOP](<./ZED_CHOP.md> "ZED CHOP") and [ZED SOP](<./ZED_SOP.md> "ZED SOP")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[zedPOP_Class](<./ZedPOP_Class.md> "ZedPOP Class")

## 

Parameters - Zed Page

Active`active`\- Extra pass to free unused GPU memory. 

ZED TOP`zedtop`\- Reference to a ZED TOP. 

Output Mode`outputmode`\- ⊞ \- Whether to output a mesh or a point cloud. 
* Mesh`mesh`-
* Point Cloud`pointcloud`-


Connectivity`connectivity`\- ⊞ \- Determines whether and how to connect the points. 
* None`none`-
* Point Primitives`points`-
* Triangles`triangles`-


Initialize`initialize`\- Clears the extracted geometry and resets spatial mapping. 

Start`startpulse`\- Start playback. 

Play`play`\- Enable playback. 

Go to Done`donepulse`\- Will immediately go to the done state. 

Preview`preview`\- ⊞ \- Camera preview mode. 
* No Preview`nopreview`-
* Limited Preview`limited`-
* Full Preview`limited`-


Maximum Memory`maxmemory`\- Sets the maximum memory used for spatial mapping. 

Resolution`resolution`\- Spatial mapping resolution in meters. 

Range`range`\- Depth range in meters. 

Normals`normals`\- When enabled, the extracted geometry will have normals. 

Color`color`\- Output color information as an attribute. 

Filter`filter`\- ⊞ \- The greater the filtering, the more the resulting mesh is smoothed, small holes are filled, and small blobs of non-connected triangles are deleted. 
* Low`low`-
* Medium`medium`-
* High`high`-


Perspective`perspective`\- ⊞ \- Camera perspective. 
* Left`left`-
* Right`right`-


Rerange from Low High`rerangefromlow`\- ⊞ \- Range for input values. 
* Rerange from Low High`rerangefromlow`\- Re-ranging low values.
* Rerange from High`rerangefromhigh`\- Re-ranging from high value.


Rerange to Low High`rerangetolow`\- ⊞ \- Range for output values. 
* Rerange to Low High`rerangetolow`\- Re-ranging to low value.
* Rerange to High`rerangetohigh`\- Re-ranging to high value.


Mirror Image`mirrorimage`\- Mirrors the input image. 

Camera`camera`\- Specify the camera component. 

Override Camera View`overridecamera`\- When on, overrides the View settings from the selected camera object. 

View Angle Method`viewanglemethod`\- ⊞ \- Sets the method to convert the depth TOP. 
* Horizontal FOV`horfov`-
* Vertical FOV`vertfov`-
* Focal Lengths`focallengths`\- Determines the camera's focal lengths.


FOV Angle`fov`\- Determines the camera's field of view angle. 

Focal Length (Fx, Fy)`focallengths`\- ⊞ \- 
* Focal Length (Fx, Fy)`focallengthsx`-
* Focal Length (Fx, Fy)`focallengthsy`-


Optical Center (Cx, Cy)`center`\- ⊞ \- The location of the center of the camera for the depth projection. 
* Optical Center (Cx, Cy)`centerx`-
* Optical Center (Cx, Cy)`centery`-


Delete Near Points`deletenear`\- Enable removal of points that are close to the camera. 

Near Depth`depthnear`\- Depth of the near clipping plane. 

Delete Far Points`deletefar`\- Enable removal of points that are far from the camera. 

Far Depth`depthfar`\- Depth of the far clipping plane. 

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Info CHOP Channels

Extra Information for the ZED POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

### 

Common POP Info Channels

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditorwikieditorwikieditorwikieditorwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• ZED
