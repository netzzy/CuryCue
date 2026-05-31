# SOP

##   
  
Summary

See [Category:SOPs](</index.php?title=Category:SOPs&action=edit&redlink=1> "Category:SOPs \(page does not exist\)") for a full list of articles related to SOPs. 

**Surface Operators** , also known as **SOPs** , are operators that can generate, import, modify and combine 3D surfaces (also called geometry). The surface types include 3D points, polygons, lines, particles, surfaces, spheres and meatballs. Particles and point clouds are now done primarily on the GPU using TOPs - see`particlesGpu`in the palette and components in the`PointClouds`folder of the palette. 

See also: [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point](<./Point.md> "Point"), [Point List](<./Point_List.md> "Point List"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Prims Class](<./Prims_Class.md> "Prims Class"), [Polygon](<./Polygon.md> "Polygon"), [Vertex](<./Vertex.md> "Vertex"), [SOP Class](<./SOP_Class.md> "SOP Class"), [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](<./Point_Group.md> "Point Group"), [Primitive Groups](<./Primitive_Group.md> "Primitive Group"), [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[SOP Class](<./SOP_Class.md> "SOP Class")

## Sweet 16 SOPs

The following 16 SOPs are commonly used, we recommend familiarizing yourself with them. 

SOP | Purpose | Related SOP  
---|---|---  
[Circle](<./Circle_SOP.md> "Circle SOP") | Circle, sphere, torus primitives. | [Sphere](<./Sphere_SOP.md> "Sphere SOP"), [Torus](<./Torus_SOP.md> "Torus SOP")  
[Grid](<./Grid_SOP.md> "Grid SOP") | Grid, box, rectangle. | [Box](<./Box_SOP.md> "Box SOP"), [Rectangle](<./Rectangle_SOP.md> "Rectangle SOP")  
[Merge](<./Merge_SOP.md> "Merge SOP") | Merge and delete. | [Object Merge](<./Object_Merge_SOP.md> "Object Merge SOP"), [Delete](<./Delete_SOP.md> "Delete SOP")  
[Copy](<./Copy_SOP.md> "Copy SOP") | Copy or replicate. | [Limit](<./Limit_SOP.md> "Limit SOP")  
[Switch](<./Switch_SOP.md> "Switch SOP") | Switch or blend multi-inputs. | [Blend](<./Blend_SOP.md> "Blend SOP"), [Sequence Blend](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")  
[Texture](<./Texture_SOP.md> "Texture SOP") | Apply texture coordinated to points or vertices. | [Material](<./Material_SOP.md> "Material SOP")  
[Noise](<./Noise_SOP.md> "Noise SOP") | Apply noise, twist and deform. | [Twist](<./Twist_SOP.md> "Twist SOP"), [Deform](<./Deform_SOP.md> "Deform SOP")  
[Transform](<./Transform_SOP.md> "Transform SOP") | Transform point positions. | [Script](<./Script_SOP.md> "Script SOP")  
[DAT to](<./DAT_to_SOP.md> "DAT to SOP") | DAT table to SOP points. | [Add](<./Add_SOP.md> "Add SOP")  
[CHOP to](<./CHOP_to_SOP.md> "CHOP to SOP") | CHOP channel samples to SOP points. | [Line](<./Line_SOP.md> "Line SOP")  
[Trace](<./Trace_SOP.md> "Trace SOP") | Trace a TOP image to polygons. | [File In](<./File_In_SOP.md> "File In SOP")  
[Clip](<./Clip_SOP.md> "Clip SOP") | Clip and carve. | [Carve](<./Carve_SOP.md> "Carve SOP")  
[Facet](<./Facet_SOP.md> "Facet SOP") | Facet, subdivide, convert. | [Subdivide](<./Subdivide_SOP.md> "Subdivide SOP"), [Convert](<./Convert_SOP.md> "Convert SOP")  
[Particle](<./Particle_SOP.md> "Particle SOP") | Particles. |   
[Sweep](<./Sweep_SOP.md> "Sweep SOP") | Sweep, skin, rails. | [Skin](<./Skin_SOP.md> "Skin SOP"), [Rails](<./Rails_SOP.md> "Rails SOP")  
[Sort](<./Sort_SOP.md> "Sort SOP") | Sort and reorder. |   
  
## Using SOPs
* 3D geometry data, processed on CPU
  * FBX Import: .fbx importer, File In SOP \- recommend importing geometry from more mature modelers
  * FBX Export: Right-click and select **Save Geometry...** In the File Browser that opens, change the file type to .fbx to create a FBX file of that geometry.

## See Also

[Category:SOPs](</index.php?title=Category:SOPs&action=edit&redlink=1> "Category:SOPs \(page does not exist\)")  
[Geometry Detail](<./Geometry_Detail.md> "Geometry Detail")  
[Primitive](<./Primitive.md> "Primitive")  
[Point](<./Point.md> "Point")

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• SOP • [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
