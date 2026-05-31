# Blend SOP

##   
  
Summary

The Blend SOP provides 3D metamorphosis between shapes with the same topology. It can blend between sixteen input SOPs using the average weight of each input's respective channel. It will also interpolate point colors and/or texture co-ordinates between shapes. 

For best results, there should be the same number of points / CVs (and faces) in the geometry of each SOP. The points should have a similar order; if point 17 in one source is on the left side, and point 17 in another Source is on the right side, it will move across the object during the blend, which may create distorted and twisted shapes. To ensure that this doesn't happen, you can make all the pieces to be blended by editing point positions of one common base shape. Each of the pieces to be morphed must be in different SOPs. 

For example, when editing the shapes in the Model Editor, each particular geometry can be saved and then read in, or input the Model SOP directly into the Blend SOP. You would then have the base model geometry entering the Blend SOP in the first Blend, then up to 15 Model SOPs feeding from the SOP containing the base model geometry, which in turn would feed into the Blend SOP. Remember that Model SOPs cannot be unlocked and, therefore, are a safe way to store data without using a File In SOP. 

The Blend SOP now only cooks non-zero-weighted inputs. 

See also [Sequence Blend SOP](<./Sequence_Blend_SOP.md> "Sequence Blend SOP"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[blendSOP_Class](<./BlendSOP_Class.md> "BlendSOP Class")

## 

Parameters - Blend Page

Group`group`\- Specifies a point or primitive group in the first input. If, for example, a group is specified containing the first and third points, then the first and third point of every input will be blended whereas the second, fourth, fifth, etc. points will be set to match the first input source. Accepts patterns, as described in: [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Differencing`diff`\- Generates exaggerated blends between objects where values above 1 or less than 0 will result in over-scaled blends. 

When this option is checked, the above channel values are not summed and scaled to 1. The first input is considered a reference; Blend computes the difference between the first input and the others for each point; values greater than 1 and less than 0 produce exaggerations of the shapes for inputs 2 and higher. The first input, however, cannot be exaggerated by its blend channel, /blend1, and it is considered to be the "base". When using Differencing, the /blend1 channel has no effect. If the geometry in the first input must be deformed, feed it into another input, where the blend channels have an effect. __

Blend Position`dopos`\- When checked, the point positions of the inputs will be blended based on the weights of the blend channels. If not checked, the input geometry will not change, only allowing Blending of Colors, Normals and Textures if selected. 

Blend Colors`doclr`\- When checked, the point colors of the geometry inputs will be blended based on the weights of the blend channels. 

Blend Normals`donml`\- When checked, the point normals of the geometry inputs will be blended based on the weights of the blend channels. 

Blend Texture`douvw`\- When checked, the point texture co-ordinates of the geometry inputs will be blended based on the weights of the blend channels. 

Blend Up`doup`\- When checked, the Up Vector of the geometry inputs will be blended based on the weights of the blend channels. 

## 

Parameters - Weights Page

Channels controlling the contribution of the geometry inputs to the output geometry. Add parameters below as needed for the number of inputs connected. 

Input`input`\- Sequence of input weights 

Weight`input0weight`\- The weight or contribution of this input. 0 has no contribution, 1 is full contribution. 

## 

Uses

This SOP can be used as a form of geometry deformation. Model your geometry, such as the mouth on the head of a character. This will become your first input. 

## 

Example

Set the input to the first SOP to be blended. For example, if there are five shapes to be blended, the simplest set-up is the following: 

Use four Model SOPs, and import the geometry from the base geometry to be deformed / morphed. In each of the Model SOPs, edit the geometry to suit. 

Append a Blend SOP off of the SOP containing the base geometry and then proceed to connect up the four Model SOPs into the Blend SOP. 

The amount that each input contributes to the resulting shape is controlled by each input's blend channel. Editing the values of the blend channels will result in each input to determine the final shape based on ratios. 

For example, if the /blend3 channel's value is 1, and the rest of the channels are set to 0, the resulting shape is the geometry in the third input SOP. Now change the value in the /blend5 channel to 1, the resulting shape will be a 50/50 percent blend of the geometry contained in the input SOPs' three and five. You would get the exact same result by setting both channels to 0.3, or to any number if the numbers are the same in both channels, there will be equal contribution to the shape. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Blend SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2022.241402021.100002020.200002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• Blend • [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
