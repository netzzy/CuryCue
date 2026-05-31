# Palette:depthProjection

##   
  
Summary

The depthProjection component uses the given camera intrinsic properties to project a 2D depth map image into a 3D point cloud. The resulting point cloud is stored in a floating point texture which can be used as an instancing source for rendering point clouds. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[Pallette:depthProjection Ext](<./Pallette-depthProjection_Ext.md> "Pallette:depthProjection Ext")

## 

Parameters - Projection Page

Depth Type`Depthtype`\- ⊞ \- Determines what kind of depth is stored in the source depth image i.e. whether the point cloud is projected in rays from a single camera point, or from the image plane. 
* Distance to Camera Point`distance`\- The depth in the source image is the radial distance from the real world object position and the camera point. This method is more common in lidar scanners.
* Z Depth`zpos`\- The values in the source image are the distances from the real work object position and the corresponding point on the image plane.


From Range`Fromrange`\- ⊞ \- Used for scaling the point cloud depth. This parameter defines the range of depths in the source image. Depths outside this range are extrapolated. 
* From Range`Fromrange1`-
* From Range`Fromrange2`-


To Range`Torange`\- ⊞ \- Determines the output range for the depth values. The range of input values is mapped linearly to the output range and values outside of the range are extrapolated. 
* To Range`Torange1`-
* To Range`Torange2`-


View Angle Method`Viewanglemethod`\- ⊞ \- Determines how the field of view is defined for the projection. 
* Horizontal FOV`horzfov`\- The field of view is determined by the horizontal angle. The vertical field of view is based on the aspect ratio of the input
* Focal Lengths`focallengths`\- The field of view is determined by the vertical and horizontal focal lengths. The focal lengths are give in normalized values relative to the resolution of the source image, so camera intrinsics provided in pixels should generally be divided by the horizontal resolution.


FOV Angle`Fov`\- The field of view measured in degrees when using Horizontal FOV mode. 

Focal Lengths (Fx, Fy)`Focallengths`\- ⊞ \- The normalized focal length values when using the Focal Length view angle method. 
* Focal Lengths (Fx, Fy)`Focallengths1`-
* Focal Lengths (Fx, Fy)`Focallengths2`-


Optical Center (Cx, Cy)`Center`\- ⊞ \- The position of the camera relative to the image plane in normalized values i.e. (0.5, 0.5) assumes the camera point is directly in the center of the image plane. 
* Optical Center (Cx, Cy)`Center1`-
* Optical Center (Cx, Cy)`Center2`-

## 

Parameters - About Page

Help`Help`\- 

Version`Version`\- 

.tox Save Build`Toxsavebuild`\- 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). _[Info Channels Common Page](</index.php?title=Info_Channels_Common_Page&action=edit&redlink=1> "Info Channels Common Page \(page does not exist\)")_

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


  
TouchDesigner Build: Latest\nwikieditorbefore wikieditor

COMPs   
---  
[Actor ](<./Actor_COMP.md> "Actor COMP")• [Ambient Light ](<./Ambient_Light_COMP.md> "Ambient Light COMP")• [Animation ](<./Animation_COMP.md> "Animation COMP")• [Annotate ](<./Annotate_COMP.md> "Annotate COMP")• [Base ](<./Base_COMP.md> "Base COMP")• [Blend ](<./Blend_COMP.md> "Blend COMP")• [Bone ](<./Bone_COMP.md> "Bone COMP")• [Bullet Solver ](<./Bullet_Solver_COMP.md> "Bullet Solver COMP")• [Button ](<./Button_COMP.md> "Button COMP")• [Camera Blend ](<./Camera_Blend_COMP.md> "Camera Blend COMP")• [Camera ](<./Camera_COMP.md> "Camera COMP")• [MediaWiki:Common.js ](<./MediaWiki-Common.md> "MediaWiki:Common.js")• [COMP ](<./COMP.md> "COMP")• [Component ](<./Component.md> "Component")• [Constraint ](<./Constraint_COMP.md> "Constraint COMP")• [Container ](<./Container_COMP.md> "Container COMP")• [Engine ](<./Engine_COMP.md> "Engine COMP")• [Environment Light ](<./Environment_Light_COMP.md> "Environment Light COMP")• [FBX ](<./FBX_COMP.md> "FBX COMP")• [Field ](<./Field_COMP.md> "Field COMP")• [Force ](<./Force_COMP.md> "Force COMP")• [Geo Text ](<./Geo_Text_COMP.md> "Geo Text COMP")• [Geometry ](<./Geometry_COMP.md> "Geometry COMP")• [GLSL ](<./GLSL_COMP.md> "GLSL COMP")• [Handle ](<./Handle_COMP.md> "Handle COMP")• [Impulse Force ](<./Impulse_Force_COMP.md> "Impulse Force COMP")• [Light ](<./Light_COMP.md> "Light COMP")• [List ](<./List_COMP.md> "List COMP")• [Null ](<./Null_COMP.md> "Null COMP")• [NVIDIA Flex Solver ](<./NVIDIA_Flex_Solver_COMP.md> "NVIDIA Flex Solver COMP")• [NVIDIA Flow Emitter ](<./NVIDIA_Flow_Emitter_COMP.md> "NVIDIA Flow Emitter COMP")• [OP Viewer ](<./OP_Viewer_COMP.md> "OP Viewer COMP")• [Parameter ](<./Parameter_COMP.md> "Parameter COMP")• [Replicator ](<./Replicator_COMP.md> "Replicator COMP")• [Select ](<./Select_COMP.md> "Select COMP")• [Shared Mem In ](<./Shared_Mem_In_COMP.md> "Shared Mem In COMP")• [Shared Mem Out ](<./Shared_Mem_Out_COMP.md> "Shared Mem Out COMP")• [Slider ](<./Slider_COMP.md> "Slider COMP")• [Table ](<./Table_COMP.md> "Table COMP")• [Text ](<./Text_COMP.md> "Text COMP")• [Time ](<./Time_COMP.md> "Time COMP")• [USD ](<./USD_COMP.md> "USD COMP")• [Widget ](<./Widget_COMP.md> "Widget COMP")• [Window ](<./Window_COMP.md> "Window COMP")
