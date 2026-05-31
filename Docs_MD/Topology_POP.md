# Topology POP

##   
  
Summary

The Topology POP gives finer control on how to combine existing points and topology (vertices and primitives), as well as their memory allocation. 

Any unsigned int attribute from the input POP or another POP, interpreted as a list of point indices, can be used to describe the topology of the POP, alongside a manual description of the number of primitives (Topology Info), either using the parameters when the number of primitives of each type are known on the CPU, or using values coming from attributes, when the number of primitives of each type are only known on the GPU. This allows to combine multiple buffers created with GLSL and GLSL Advanced POP to describe geometry for example. 

Alternatively the Topology and Topology info can be provided from another POP. Primitives and Vertices attributes can also be merged in from other POPs. 

Last but not least, for POPs whose numbers of points and primitives are known on the GPU, the maximum numbers can be updated here, if the user knows them to be smaller, to reduce the memory allocation of downstream POPs. Alternatively if the exact counts are known they can also be entered manually and the POP updated to know that its point count info and topology info are now known on the CPU, without incurring the cost and stall of a download. (Refer to Learning about POPs, Information known on CPU/GPU) 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[topologyPOP_Class](</TopologyPOP_Class> "TopologyPOP Class")

## 

Parameters - Points Page

Max Points`maxpointsmode`\- ⊞ \- Specifies how to set the maximum number of points. 
* Max Points`maxpointsmode`-
* Max Points`maxpoints`\- Sets the max number of points. If the POP point count info is on the CPU, that's the actual number of points.


Point Count Info`pointcountinfo`\- ⊞ \- Input point count source. 
* From Input`input`-
* From Max Points Parameter`fromparams`-
* From Attribute`fromattrs`-


Point Count POP`pointcountpop`\- POP that holds the point counts. 

Point Count Attribute`pointcountclass`\- ⊞ \- Attribute class of the attribute that holds the point count. 
* Point Count Attribute`pointcountclass`-
* Point Count Attribute`pointcountattr`\- Attribute that holds the point count.

## 

Parameters - Topology Page

Render`render`\- Enables rendering in the viewer. Disable when output data is in an intermediate or non-renderable state 

Primitive Source Mode`primsourcemode`\- ⊞ \- Whether the input POP is the primitive source or a different POP is used as the primitive source. Other parameters refer to the primitive source. 
* Input`input`-
* Specify POP`specpop`-


Primitive Mode`primmode`\- ⊞ \- Whether the primitive source input is used for the topology and topology info, or an attribute is used to specify the topology (the point indices), and the topology info is specified manually. 
* Source Topology and Topology Info`topo`-
* Source Attribute and Manual Topology Info`attr`-


Primitives POP`primspop`\- Specifies the POP to use for the primitive source. 

Point Index Attrib Class`pointindexattrclass`\- ⊞ \- Attribute class of the attribute that holds the point index values. 
* Point Index Attrib Class`pointindexattrclass`-
* Point Index Attrib Name`pointindexattrname`\- Attribute that holds the Point Index values.


Vertex Attribute Mode`vertattrmode`\- ⊞ \- Specifies whether the vertex attributes come from the vertex source (input or separate POP) or from a separate POP
* None`none`-
* Primitive Source`primsource`-
* Specify POP`specpop`-


Vertex Attribute POP`vertattrpop`\- The POP from which the vertex attributes come from. 

Vertex Attribute Class`vertattrclass`\- ⊞ \- The attribute class from the vertex attributes when they come from the specified POP. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Prim Attribute Mode`primattrmode`\- ⊞ \- Specifies whether the primitive attributes come from the primitive source (input or separate POP) or from a separate POP. 
* None`none`-
* Primitive Source`primsource`-
* Specify POP`specpop`-


Prim Attribute POP`primattrpop`\- The POP from which the primitive attributes come from. 

Prim Attribute Class`primattrclass`\- ⊞ \- The attribute class from the primitive attributes when they come from the specified POP. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Topology`topology`\- ⊞ \- Determines the topology mode. 
* Source Topology Reference`ref`-
* Source Topology Copy`copy`-


Max Triangles`maxtrianglesmode`\- ⊞ \- Specifies how to set the maximum number of triangle primitives. 
* Max Triangles`maxtrianglesmode`-
* Max Triangles`maxtriangles`\- Sets the max number of triangle primitives. If the POP topology info is on the CPU, that's the actual number of triangle primitives.


Max Quads`maxquadsmode`\- ⊞ \- Specifies how to set the maximum number of quad primitives. 
* Max Quads`maxquadsmode`-
* Max Quads`maxquads`\- Sets the max number of quad primitives. If the POP topology info is on the CPU, that's the actual number of quad primitives.


Max Line Strips`maxlinestripsmode`\- ⊞ \- Specifies how to set the maximum number of line strip primitives. 
* Max Line Strips`maxlinestripsmode`-
* Max Line Strips`maxlinestrips`\- Sets the max number of line strip primitives. If the POP topology info is on the CPU, that's the actual number of line strip primitives.


Max Line Strip Verts`maxlsvertsmode`\- ⊞ \- Specifies how to set the maximum number of vertices per line strip. 
* Max Line Strip Verts`maxlsvertsmode`-
* Max Line Strip Verts`maxlsverts`\- Sets the max number of line strip vertices. If the POP topology is on the CPU, that's the actual number of line strip vertices.


Max Lines`maxlinesmode`\- ⊞ \- Specifies how to set the maximum number of line primitives. 
* Max Lines`maxlinesmode`-
* Max Lines`maxlines`\- Sets the max number of line primitives. If the POP topology info is on the CPU, that's the actual number of line primitives.


Max Point Prims`maxpointprimsmode`\- ⊞ \- Specifies how to set the maximum number of point primitives. 
* Max Point Prims`maxpointprimsmode`-
* Max Point Prims`maxpointprims`\- Sets the max number of point primitives. If the POP topology info is on the CPU, that's the actual number of point primitives.


Line Strip Info from Prim Source`lsinfofromprimsource`\- When set, uses the primitive source (Input or Specified POP) for the Line Strip Info buffer. 

Line Strip Info Update`lsinfoupdate`\- ⊞ \- Allows you to choose how the Line Strip Info buffers get updated. 
* Auto`auto`-
* Manual`manual`-


Line Strip Info POP`lsinfopop`\- POP with the attribute to use for the Line Strip Info buffer. 

Line Strip Info Attribute`lsinfoclass`\- ⊞ \- Attribute class of the attribute to use foor the Line Strip Info buffer. 
* Line Strip Info Attribute`lsinfoclass`-
* Line Strip Info Attribute`lsinfoattr`\- Attribute to use for the Line Strip Info buffer.


Line Strip Index per Vert POP`lsindexpop`\- POP with the attribute to use for the Line Strip Index per Vert buffer. 

Line Strip Index per Vert Attribute`lsindexclass`\- ⊞ \- Attribute class of the attribute to use for the Line Strip Index per Vert buffer. 
* Line Strip Index per Vert Attribute`lsindexclass`-
* Line Strip Index per Vert Attribute`lsindexattr`\- Attribute to use for the Line Strip Index per Vert buffer.


Max Verts per Line Strip`lsmaxvertsoverride`\- ⊞ \- Specifies you wan to set the max number of verts per line strip. 
* Max Verts per Line Strip`lsmaxvertsoverride`-
* Max Verts per Line Strip`lsmaxverts`\- Sets the max number of verts per line strip. Used by some downstream POPs for GPU memory allocation.


Topology Info`topoinfo`\- ⊞ \- Sets the topology information source. 
* From Primitive Source`primsource`-
* From Max Prims Parameter`fromparams`-
* From Attributes`fromattrs`-


Topology Info POP`topoinfopop`\- Sets reference to a POP where the info attribute can be found. 

Topology Info Attributes Class`topoinfoclass`\- ⊞ \- Sets the attribute class where the info attribute can be found. 
* Point`point`-
* Vertex`vertex`-
* Primitive`primitive`-


Triangle Count`trianglecountmode`\- ⊞ \- Whether to get the count of triangle primitives from the source, set it to 0, or set its value manually. 
* Triangle Count`trianglecountmode`-
* Triangle Count Attribute`trianglecountattr`\- Specifies the attribute to use to set the triangles count.


Quad Count`quadcountmode`\- ⊞ \- Whether to get the count of quad primitives from the source, set it to 0, or set its value manually. 
* Quad Count`quadcountmode`-
* Quad Count Attribute`quadcountattr`\- Specifies the attribute to use to set the quadrilaterals count.


Line Strip Count`linestripcountmode`\- ⊞ \- Whether to get the count of line strip primitives from the source, set it to 0, or set its value manually. 
* Line Strip Count`linestripcountmode`-
* Line Strip Count Attribute`linestripcountattr`\- Specifies the attribute to use to set the line count.


Line Strip Vert Count`lsvertcountmode`\- ⊞ \- Specifies how to set the line strip vertex count. 
* Line Strip Vert Count`lsvertcountmode`-
* Line Strip Vert Count Attribute`lsvertcountattr`\- Specifies how to set the line strip vertex count.


Line Count`linecountmode`\- ⊞ \- Whether to get the count of line primitives from the source, set it to 0, or set its value manually. 
* Line Count`linecountmode`-
* Line Count Attribute`linecountattr`\- Specifies the attribute to use to set the line count.


Point Prim Count`pointprimcountmode`\- ⊞ \- Whether to get the count of point primitives from the source, set it to 0, or set its value manually. 
* Point Prim Count`pointprimcountmode`-
* Point Prim Count Attrib`pointprimcountattr`\- Specifies the attribute to use for the point primitive count.

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

Extra Information for the Topology POP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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
[Accumulate ](<./Accumulate_POP.md> "Accumulate POP")• [Alembic In ](<./Alembic_In_POP.md> "Alembic In POP")• [Analyze ](<./Analyze_POP.md> "Analyze POP")• [Attribute Combine ](<./Attribute_Combine_POP.md> "Attribute Combine POP")• [Attribute Convert ](<./Attribute_Convert_POP.md> "Attribute Convert POP")• [Attribute ](<./Attribute_POP.md> "Attribute POP")• [Blend ](<./Blend_POP.md> "Blend POP")• [Box ](<./Box_POP.md> "Box POP")• [Cache Blend ](<./Cache_Blend_POP.md> "Cache Blend POP")• [Cache ](<./Cache_POP.md> "Cache POP")• [Cache Select ](<./Cache_Select_POP.md> "Cache Select POP")• [CHOP to ](<./CHOP_to_POP.md> "CHOP to POP")• [Circle ](<./Circle_POP.md> "Circle POP")• [Connectivity ](<./Connectivity_POP.md> "Connectivity POP")• [Convert ](<./Convert_POP.md> "Convert POP")• [Copy ](<./Copy_POP.md> "Copy POP")• [CPlusPlus ](<./CPlusPlus_POP.md> "CPlusPlus POP")• [Curve ](<./Curve_POP.md> "Curve POP")• [DAT to ](<./DAT_to_POP.md> "DAT to POP")• [Delete ](<./Delete_POP.md> "Delete POP")• [Dimension ](<./Dimension_POP.md> "Dimension POP")• [DMX Fixture ](<./DMX_Fixture_POP.md> "DMX Fixture POP")• [DMX Out ](<./DMX_Out_POP.md> "DMX Out POP")• [Extrude ](<./Extrude_POP.md> "Extrude POP")• [Facet ](<./Facet_POP.md> "Facet POP")• [Feedback ](<./Feedback_POP.md> "Feedback POP")• [Field ](<./Field_POP.md> "Field POP")• [File In ](<./File_In_POP.md> "File In POP")• [File Out ](<./File_Out_POP.md> "File Out POP")• [Force Radial ](<./Force_Radial_POP.md> "Force Radial POP")• [GLSL Advanced ](<./GLSL_Advanced_POP.md> "GLSL Advanced POP")• [GLSL Copy ](<./GLSL_Copy_POP.md> "GLSL Copy POP")• [GLSL Create ](<./GLSL_Create_POP.md> "GLSL Create POP")• [GLSL ](<./GLSL_POP.md> "GLSL POP")• [GLSL Select ](<./GLSL_Select_POP.md> "GLSL Select POP")• [Grid ](<./Grid_POP.md> "Grid POP")• [Group ](<./Group_POP.md> "Group POP")• [Histogram ](<./Histogram_POP.md> "Histogram POP")• [Import Select ](<./Import_Select_POP.md> "Import Select POP")• [In ](<./In_POP.md> "In POP")• [Limit ](<./Limit_POP.md> "Limit POP")• [Line Break ](<./Line_Break_POP.md> "Line Break POP")• [Line Divide ](<./Line_Divide_POP.md> "Line Divide POP")• [Line Metrics ](<./Line_Metrics_POP.md> "Line Metrics POP")• [Line ](<./Line_POP.md> "Line POP")• [Line Resample ](<./Line_Resample_POP.md> "Line Resample POP")• [Line Smooth ](<./Line_Smooth_POP.md> "Line Smooth POP")• [Line Thick ](<./Line_Thick_POP.md> "Line Thick POP")• [Lookup Attribute ](<./Lookup_Attribute_POP.md> "Lookup Attribute POP")• [Lookup Channel ](<./Lookup_Channel_POP.md> "Lookup Channel POP")• [Lookup Texture ](<./Lookup_Texture_POP.md> "Lookup Texture POP")• [Math Combine ](<./Math_Combine_POP.md> "Math Combine POP")• [Math Mix ](<./Math_Mix_POP.md> "Math Mix POP")• [Math ](<./Math_POP.md> "Math POP")• [Merge ](<./Merge_POP.md> "Merge POP")• [Neighbor ](<./Neighbor_POP.md> "Neighbor POP")• [Noise ](<./Noise_POP.md> "Noise POP")• [Normal ](<./Normal_POP.md> "Normal POP")• [Normalize ](<./Normalize_POP.md> "Normalize POP")• [Null ](<./Null_POP.md> "Null POP")• [OAK Select ](<./OAK_Select_POP.md> "OAK Select POP")• [Out ](<./Out_POP.md> "Out POP")• [Particle ](<./Particle_POP.md> "Particle POP")• [Pattern ](<./Pattern_POP.md> "Pattern POP")• [Phaser ](<./Phaser_POP.md> "Phaser POP")• [Plane ](<./Plane_POP.md> "Plane POP")• [Point File In ](<./Point_File_In_POP.md> "Point File In POP")• [Point Generator ](<./Point_Generator_POP.md> "Point Generator POP")• [Point ](<./Point_POP.md> "Point POP")• [Points, Vertices and Primitives in s ](<./Points,_Vertices_and_Primitives_in_POPs.md> "Points, Vertices and Primitives in POPs")• [Polygonize ](<./Polygonize_POP.md> "Polygonize POP")• [POP ](<./POP.md> "POP")• [Primitive ](<./Primitive_POP.md> "Primitive POP")• [Projection ](<./Projection_POP.md> "Projection POP")• [Proximity ](<./Proximity_POP.md> "Proximity POP")• [Quantize ](<./Quantize_POP.md> "Quantize POP")• [Random ](<./Random_POP.md> "Random POP")• [Ray ](<./Ray_POP.md> "Ray POP")• [Rectangle ](<./Rectangle_POP.md> "Rectangle POP")• [ReRange ](<./ReRange_POP.md> "ReRange POP")• [Revolve ](<./Revolve_POP.md> "Revolve POP")• [Select ](<./Select_POP.md> "Select POP")• [Skin Deform ](<./Skin_Deform_POP.md> "Skin Deform POP")• [Skin ](<./Skin_POP.md> "Skin POP")• [SOP to ](<./SOP_to_POP.md> "SOP to POP")• [Sort ](<./Sort_POP.md> "Sort POP")• [Sphere ](<./Sphere_POP.md> "Sphere POP")• [Sprinkle ](<./Sprinkle_POP.md> "Sprinkle POP")• [Subdivide ](<./Subdivide_POP.md> "Subdivide POP")• [Switch ](<./Switch_POP.md> "Switch POP")• [Texture Map ](<./Texture_Map_POP.md> "Texture Map POP")• [TOP to ](<./TOP_to_POP.md> "TOP to POP")• Topology • [Torus ](<./Torus_POP.md> "Torus POP")• [Trail ](<./Trail_POP.md> "Trail POP")• [Transform ](<./Transform_POP.md> "Transform POP")• [Trig ](<./Trig_POP.md> "Trig POP")• [Tube ](<./Tube_POP.md> "Tube POP")• [Twist ](<./Twist_POP.md> "Twist POP")• [ZED ](<./ZED_POP.md> "ZED POP")
