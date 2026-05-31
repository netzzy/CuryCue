# Bridge SOP

## 

Summary

The Bridge SOP is useful for skinning trimmed surfaces, holes, creating highly controllable joins between arms and body, branches or tube intersections. 

The Bridge SOP is similar to the Skin SOP but with much greater control over the resulting surface. Given a set of profiles (i.e. curves on surface) and/or spatial faces, the Bridge SOP builds a NURBS skin with specified tangent and curvature characteristics. The precision of the resulting surface is highly dependent on the number of required cross-sections and on the quality of the profile extraction. High precisions will generate a very dense surface with, potentially, many multiple knots. 

In general, the higher the order of the curve, the better the fit the Bridge SOP will be able to provide. However, it is generally better to stick to cubics (order 4) curves, as the software is optimized for cubics. 

Because the Bridge SOP can join both a set of spatial curves and trim curves, it can be used much like the Skin SOP and/or the Fillet SOP. However, bridging trimmed surfaces is more expensive than bridging carved surfaces. 

You will usually need a Trim, Bridge, or Profile SOP after a Project SOP. 
* Use a Trim SOP to cut a hole in the projected surface
  * Use a Bridge SOPto skin the profile curve to another profile curve.
  * Use a Profile SOP to extract the curve on surface or remap it's position.


**Note:** To texture-map the resulting skin, use an Orthographic projection rather than a Spline-based projection. This results in better continuity across the surfaces. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[bridgeSOP_Class](<./BridgeSOP_Class.md> "BridgeSOP Class")

## 

Parameters - Page

Group`group`\- The Group edit field allows you to enter profile groups for profiles and/or faces to bridge. This is optional if you have regular geometric curves or surfaces, however, you must enter something here in order for Bridge to work with profile curves. For example`*.0`will Bridge the 0th (first) profiles of all incoming primitives. 

**Note:** Always specify the curves on surface if you want the Bridge SOP bridge curves on surfaces; otherwise it will attempt to bridge free-floating curves. __

Bridge`bridge`\- ⊞ \- Allows bridging of subgroups of N primitives or patterns of primitives. 
* All Primitives`all`-
* Groups of N Primitives`group`-
* Skip Every Nth Primitive`skip`-


N`inc`\- Determines the pattern of primitives to bridge using this SOP. 

Order`order`\- Sets the spline order for both profile extraction and skinning operations. 

## 

Parameters - Surface Properties Page

Min X-Sections`isodivs`\- The minimum number of cross-sections in the resulting skin. If you create a high-density surface, TouchDesigner's level of detail may display the surface less smoothly than it actually is. You can increase the level of detail by adjusting the viewdisplay options (e.g.`viewdisplay -l 1.5 SOPmain.persp1`) for the Viewport. 

**Production Tip:** If, in generating a smooth surface, you create an extremely complex surface, some of the complexity can be removed without damaging the appearance of the surface by appending a Refine SOP, and using its **Unrefine** option. In the Refine SOP, set the **First U** parameter to zero and, in the **Unrefine** option's parameters, set the **U** value close to the order of the surface created in the Bridge SOP. __

Use`frenet`\- ⊞ \- Specifies the type of normal to use for computing direction: 
* The Frenet Frame of the Face`frenet`\- The Frenet Frame of the face. This option uses a local coordinate system on the curve to compute the direction.
* The Normal of the Face`normal`\- The Normal of the face.


Circular Arc Fillet`circular`\- Tells TouchDesigner to try to generate a round fillet rather than a free-form fillet. Only the sign (positive or negative) of the tangent scales is used; the scale magnitude is ignored when building a circular fillet. 

The radius of the fillet is computed automatically and adjusted according to the distance between the rails (curves and/or profiles) and their tangents. __

Rotate Tangents`rotatet`\- ⊞ \- The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents. 

  *`rotatet1`\- Applies to the first face in the input.


  *`rotatet2`\- Applies to all intermediate faces.


  *`rotatet3`\- Applies to the last face in the input.


Scale Tangents`scalet`\- ⊞ \- The scaling and rotation parameters contain three fields. The rotation fields (degrees) apply further rotation to the tangents, while the scale parameter further scales the tangents. 

  *`scalet1`\- Applies to the first face in the input.


  *`scalet2`\- Applies to all intermediate faces.


  *`scalet3`\- Applies to the last face in the input.


Use Curvature`curvature`\- Takes curvature into consideration as well. 

Scale Curvatures`scalec`\- ⊞ \- Further scaling of the curvature. 

**Note:** If the resulting skin bulges too greatly, you can achieve a smooth resulting transition between surfaces by disabling the Preserve Tangent & Preserve Curvature Magnitude parameters, and manually tweaking the Tangent Scales and the Curvature Scales. In general, avoid tweaking the Rotations of the Tangents unless you wish to deform the resulting surface. 

If the bridge bulges on one side but not the other, try increasing the Min. Number of Cross sections in the bridge. 

  *`scalec1`-


  *`scalec2`-


  *`scalec3`-

## 

Parameters - Profile Extraction Page

This page's parameters are similar to those found in the Fit and Project SOPs. 

Divisions per Span`sdivs`\- Number of 2-D points evaluated in each span. 

Tolerance`tolerance`\- Precision of 2-D fitting algorithm. 

Preserve Sharp Corners`csharp`\- Enables or disables fitting of sharp turns. If cracks appear in the resulting skin, Preserve Sharp Corners is usually a good solution; however, it may add additional knots which can create undesirable "ripples" in some cases. 

If this option is disabled, fewer isoparms are generated and the surface may not follow the contours of the profile curves perfectly unless the profile curves were built using the`Preserve Sharp Corners`option. __

## 

Example
1. Place a Circle SOP. Primitive Type: NURBS; Radius = 0.2, 0.2
  2. Place a Grid SOP. Primitive Type: NURBS.
  3. Feed both the Circle and Grid SOPs into a Project SOP. Make it the display SOP. You notice the projected circle on the grid - our trim curve.
  4. Append a Trim SOP and make it the display SOP. Turn on Gouraud shading for the Viewport - you now see the trimmed holes in the surface of the grid.
  5. Append a Copy SOP. Number of Copies: 2; Translation Z: 1.0; Rotation X: 30. Make it the display SOP. Now we have two grids with trimmed holes in them.
  6. Append a Bridge SOP, and make it the display SOP. Scale Tangents:`0, 0, 0`; Use Curvature: On; Preserve Curvature Magnitudes: Off; Scale Curvatures:`3, 3, 3`. Nothing happens. Why?
  7. We need to specify which profile curves to skin. Turn on Profile Numbers in the Viewport options (click M at the bottom-right of Viewport, and enable the icon). We can see the profile numbers of the two trim curves are 0.0 and 1.0 - meaning the 0th profile of the 0th primitive and the 0th profile of the 1st primitive). The strange numbering is because primitive numbers start at 0 instead of 1.
  8. In the Bridge SOP's Group field enter:`.0`\- this means to include the 0th (first) curve from all (the _*_ wildcard character) primitives in the skin. You now see the resulting bridge between the two trim curves. The skin bulges outwards.
  9. We can control the bulge by playing with the Scale Curvatures and the Tangent Magnitudes. Set the Scale Curvatures to:`-3, -3, -3`. Now we have an inward-bulging tube connecting the two holes.  


[![BridgeSOPExample.gif](./images/a/a3/BridgeSOPExample.gif)](</File:BridgeSOPExample.gif>)
10. Experiment with moving the location and size of the holes (change the Translation and Radius in the Circle SOP). The Bridge SOP dynamically updates the geometry connecting the two surfaces. Setting the Scale Curvature to:`0, 0, 0`produces a straight-through connection between the two holes.

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Bridge SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• Bridge • [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
