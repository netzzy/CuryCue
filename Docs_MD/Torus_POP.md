# Torus POP

## 

Summary

The Torus POP creates rows and columns of points in a closed tube shape. The points can be connected with a variety of primitives using the Connectivity menu. 

The ring and the cross-section of the torus each have a radius parameter. 

The Connectivity menu lets you output triangles, alternating triangles, quads, lines, line strips, point primitives or no primitives (None, only points). 

You specify number of rows and columns. Columns refers to the divisions around the ring, Rows to the divisions around the cross-section circle. 

In the Connectivity menu you can create lines and line strips along Rows, Columns or both merged together. 

The torus is symmetric around an axis, Y by default, but the torus can be post-rotated and post-translated using the Rotate and Translate parameters. 

Anchor will line up the left, center or right side of the torus to X=0, Y=0 or Z=0. 

The Details page lets you make a partial torus by specifying an arc of the ring with any starting/ending angle. 

The End Caps toggle will add triangles or quads to fill the end caps and make the torus a closed volume, which still preserves the [Dimension](<./Dimension.md> "Dimension") since no points are added or removed, only primitives are added. 

[Dimension](<./Dimension.md> "Dimension"): When the torus is passed to other POPs it cannot be known for certain how many rows and columns were specified. However the Torus POP (and other generator POPs) output its Dimensions as metadata to all POPs connected to it, indicating its organizations of points in the points list. A torus has dimensions numCols numRows, which can be used by built-in attributes like`_Dim[]`or by GLSL code. 

You can output point or vertex normals (creating the`N`attribute), and you can output point or vertex texture coordinates (`Tex`attribute). 

The Torus POP takes an input which will cause the starting tube to have the same bounding box as the bounding box of the input. Then turning on Modify Bounds lets you further transform the torus. 

See also [Tube POP](<./Tube_POP.md> "Tube POP"), [Sphere POP](<./Sphere_POP.md> "Sphere POP"), [Grid POP](<./Grid_POP.md> "Grid POP"), [Field POP](<./Field_POP.md> "Field POP"), [Point Generator POP](<./Point_Generator_POP.md> "Point Generator POP"), [Revolve POP](<./Revolve_POP.md> "Revolve POP"), [Dimension](<./Dimension.md> "Dimension")

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[torusPOP_Class](</TorusPOP_Class> "TorusPOP Class")

## 

Parameters - Torus Page

Connectivity`surftype`\- ⊞ \- Determines the primitive used to connect the points. 
* None`none`-
* Point Primitives`points`-
* Rows`rows`\- Number of rows in the matrix - 2, 3 or 4.
* Columns`cols`\- Number of columns
* Rows and Columns`rowcol`-
* Triangles`triangles`-
* Alternating Triangles`alttriangles`-
* Quadrilaterals`quads`-


Line Type`linetype`\- ⊞ \- Specifies whether lines should be made of line strip primitives or lines primitives. 
* Line Strip`linestrip`-
* Lines`lines`-


Orientation`orient`\- ⊞ \- Sets the axis for the torus. 
* X Axis`x`-
* Y Axis`y`-
* Z Axis`z`-


Modify Bounds`modifybounds`\- Available only when an input is connected to the POP to set bounds for the POP. When Modify Bounds is On the parameters below will further modify the shape of the POP. 

Radius`rad`\- ⊞ \- Radii of ring and radius of swept circle. 
* Radius`radx`-
* Radius`rady`-


Columns`cols`\- 

Rows`rows`\- 

Anchor U`anchoru`\- Puts the left side, the middle or the right side at the origin 0. 

Anchor V`anchorv`\- Puts the bottom side, the middle or the top side at the origin 0. 

Anchor W`anchorw`\- Puts the back side, the middle or the front side at the origin 0. 

Translate`t`\- ⊞ \- Translate the points in the three axes. 
* Translate`tx`-
* Translate`ty`-
* Translate`tz`-


Rotate`r`\- ⊞ \- Rotate the points around the corresponding X, Y and Z axes. Angles are given in degrees. 
* Rotate`rx`-
* Rotate`ry`-
* Rotate`rz`-


Uniform Scale`scale`\- Specifies a uniform scale factor in all axes. 

Normal`normal`\- ⊞ \- Choose whether to create a normal attribute and the attribute class of the normal attribute. 
* None`none`-
* Point`pointNormals`-
* Vertex`vertNormals`-


Texture Coordinates`texture`\- ⊞ \- Sets the attribute class where the texture coordinates should be created. 
* None`none`-
* Point`pointNormals`-
* Vertex`vertNormals`-

## 

Parameters - Detail Page

U Closed`closedu`\- Enable closed geometry in U direction. 

V Closed`closedv`\- Enable closed geometry in V direction. 

Angle U`angleu`\- ⊞ \- The angle the torus covers along U. 
* Angle U`beginangleu`-
* Angle U`endangleu`-


Angle V`anglev`\- ⊞ \- The angle the torus covers along V. 
* Angle V`beginanglev`-
* Angle V`endanglev`-

## 

Parameters - Common Page

Bypass`bypass`\- Pass through the first input to the output unchanged. 

Free Extra GPU Memory`freeextragpumem`\- Free memory that has accumulated when output memory has grown and shrunk. 

Delete Input Attributes`delinputattrs`\- Only output which attributes you specify in this POP \- helps isolate attributes into a separate branch. 

## 

Operator Inputs
* Input 0:  -

## 

Info CHOP Channels

Extra Information for the Torus POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditor2025.30000

POPs   
---  
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• [Topology ](<./Topology_POP.md> "Topology POP")• Torus • [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
