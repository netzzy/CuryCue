# Fit SOP

## 

Summary

The Fit SOP fits a Spline curve to a sequence of points or a Spline surface to an m X n mesh of points. 

Any type of face or surface represents a valid input. The Fit SOP looks only at the control vertices (CVs) of the primitives, treating the CVs as data points to run the fit through. For example, if a cubic NURBS surface and a mesh have the same number of rows and columns and identical points, they will yield an identical fit because the Spline bases of the input NURBS surface are ignored. 

The Fit SOP generates two types of outputs: primitives that roughly follow the path of the data points without necessarily going through the data points; and primitives that touch all the data points. The first type, known as "approximation", is used primarily to extract a lean, smooth shape from a heavy data set, lending itself well to data reduction. The second type, known as "interpolation", often serves as a smoothing tool for paths that must go through specified target positions. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[fitSOP_Class](<./FitSOP_Class.md> "FitSOP Class")

## 

Parameters - Page

Group`group`\- If there are input groups, specifying a group name in this field will cause this SOP to act only upon the group specified. Accepts patterns, as described in [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

## 

Parameters - Fit Page

This is the main page of the SOP. Its purpose is to specify the type of fitting and the characteristics of the output primitive. 

Method`method`\- ⊞ \- Specifies one of two fitting styles: approximation or interpolation. Each style has a number of parameters that are accessible from the respective folder. For more information see the Approximation and Interpolation pages below. 
* Approximation`approx`-
* Interpolation`interp`-


Primitive Type`type`\- ⊞ \- The output of the Fit SOP is a NURBS or Bzier primitive. All input faces are fitted to Spline curves, and all input surfaces are fitted to spline surfaces. The resulting shapes are identical whether created as NURBS or as Bzier primitives. 
* NURBS`nurbs`-
* Bezier`bezier`-


Connectivity`surftype`\- ⊞ \- This option is used to select the type of surface, when using a Mesh Primitive Type. 
* Rows`rows`\- Creates horizontal lines.
* Columns`cols`\- Creates vertical lines.
* Rows and Columns`rowcol`\- Both Rows and Columns. Looks like Quads in wire frame display, but all polygons are open (if the primitive type is polygon).
* Triangles`triangles`\- Build the grid with Triangles.
* Quadrilaterals`quads`\- Generates sides composed of quadrilaterals (default).
* Alternating Triangles`alttriangles`\- Generates triangles that are opposed; similar to the Triangles option.


U Order`orderu`\- If the input is a face, this is the order of the Spline curve to be generated. If the input is a surface, this is the order of the fitted spline surface in the U parametric direction. 

V Order`orderv`\- If the input is a surface, this is the order of the fitted Spline surface in the V parametric direction. The V order is irrelevant if the input is a face. 

## 

Parameters - Approximation Page

Approximation fitting is used primarily to generate a lean, smooth shape from a dense data set. The result is a primitive that approximates the positions and attributes of the data points but does not necessarily touch these points. The only points the fitted curve or surface goes through are the end-points of the data set. If the fitted primitive is required to go through all the points, fitting by interpolation is the answer. 

The approximation fit is capable of producing very reasonable shapes with far fewer control vertices than the number of data points. Although the result is unlikely to match the original shape identically, it can come very close to it, depending on the parameters it is set to. For this reason, approximation fitting is often used as a data reduction tool and performs best when the size of the data set is large. 

The fitted primitives are generated open or wrapped based on the "open" property of the inputs. For best results, the input primitives should be open. 

Tolerance`tol`\- This is the primary precision factor in approximation fitting. The smaller the tolerance, the closer the fit and the higher the number of generated vertices. If a small tolerance causes unwanted twists or contortions in the fitted primitive, it may help to vary the Spline order and/or enable the Multiple Knots flag. 

Smoothness`smooth`\- For a set tolerance, the smoothness factor allows for more or less roundness in the generated shape. If this parameter is zero, it does not mean that the fit will be sharp. It simply indicates that no additional smoothing is required past the level of smoothness already achieved with the given tolerance. 

U Multiple Knots`multipleu`\- Sometimes the data set has sharp bends that must be preserved in the fitted shape. In this case, inserting multiple knots in the areas of sharp curvature will usually produce the right effect. Sometimes, however, the simulated sharpness induces unwanted twists immediately before or after the corner. Lowering the Spline order and/or reducing the tolerance may help diminish this side-effect. 

V Multiple Knots`multiplev`\- Sometimes the data set has sharp bends that must be preserved in the fitted shape. In this case, inserting multiple knots in the areas of sharp curvature will usually produce the right effect. Sometimes, however, the simulated sharpness induces unwanted twists immediately before or after the corner. Lowering the Spline order and/or reducing the tolerance may help diminish this side-effect. 

## 

Parameters - Interpolation Page

Interpolation fitting is used primarily to generate a shape that goes through (i.e. interpolates) a complete set of data points and their attributes. As opposed to approximation fitting, interpolation thrives on small data sets. Moreover, unlike the approximation method, this one does not produce a leaner structure than the input it fits. In certain cases it even generates a higher CV count than its input. For this reason, the use of interpolation fitting should be limited to those cases where point interpolation is paramount, such as building precise animation paths. 

Scope`scope`\- ⊞ \- Scope establishes the interpolation method. 
* Global`global`\- Global interpolation take the whole data set into account at once and generates exactly as many CVs as data points is it given.
* Local (Curves Only)`local`\- Local interpolation takes a more geometric approach, building the curve or surface one span at a time, using only local data at each step. The local method generates more CVs than the number of data points it is given, but it usually yields a tighter fit than the global method. The local approach is also less computationally expensive than the global one, and handles cusps and local perturbations better. Local interpolation is available only for curves.
* Breakpoints`breakpnt`\- Breakpoint interpolation is a variant of global interpolation that satisfies the requirement that the locations of data points coincide with the breakpoints of the generated curve. The breakpoints of a Spline curve are the image of the Spline basis on the curve. Breakpoint interpolation is available only for curves.


U Data Parameter`dataparmu`\- ⊞ \- Specifies the parameterization of the data in the U direction (the only direction if the input is a curve). The data parameterization can be uniform, chord length, or centripetal. 

    Uniform Uniform parameterization uses equally spaced parameter values. It works best when the geometry is very regular. When the data is unevenly spaced, this approach can produce very unintuitive shapes, and is not recommended.
    Chord Length Chord length computes the parameterization of the data based on the relative distances between successive data points. It is the most commonly used approach because is tends to produce the most accurate results.
    Centripetal Centripetal parameterization is similar to chord length, but yields better results when the data has very sharp corners.
* Uniform`uniform`-
* Chord Length`chrdlen`-
* Centripetal`centrip`-


V Data Parameter`dataparmv`\- ⊞ \- V data parameterization is identical to U data parameterization, but it affects the V direction when the input is a surface. It is not used when the input is a face. 
* Uniform`uniform`-
* Chord Length`chrdlen`-
* Centripetal`centrip`-


U Wrap`closeu`\- ⊞ \- This menu determines whether the fitted curve should be closed, or whether the fitted surface should be wrapped in the U parametric direction. The options are to open (Off), close (On), or inherit the closure type from the input primitive. 
* Off`nonewu`-
* On`wu`-
* If Primitive does`ifprimwu`-


V Wrap`closev`\- ⊞ \- This menu determines whether the fitted surface should be wrapped in the V parametric direction. The options are to open (Off), close (On), or inherit the closure type from the input primitive. V Wrap is ignored when the input is a face. 
* Off`nonewv`-
* On`wv`-
* If Primitive does`ifprimwv`-


Fit Corners`corners`\- Specifies whether corners in the data should be preserved when doing local curve interpolation. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Fit SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• Fit • [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
