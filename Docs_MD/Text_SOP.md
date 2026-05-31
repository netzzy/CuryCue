# Text SOP

## 

Summary

The Text SOP creates text geometry from any [TrueType](<http://en.wikipedia.org/wiki/TrueType>) or [OpenType](<http://en.wikipedia.org/wiki/OpenType>) font that is installed on the system, or any TrueType/OpenType font file on disk. [Unicode](<./Unicode.md> "Unicode") is supported. 

See also: [Text TOP](<./Text_TOP.md> "Text TOP"), [Unicode](<./Unicode.md> "Unicode"). 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[textSOP_Class](<./TextSOP_Class.md> "TextSOP Class")

## 

Parameters - Text Page

Font`font`\- Select the font for the text from this drop down menu. All fonts are provided by the OS, any [TrueType](<http://en.wikipedia.org/wiki/TrueType>) font that is loaded into the OS can be used. 

Font File`fontfile`\- Specify any TrueType or OpenType font file (`.ttf, .otf file`) to use for the text. When using a font file, the Font menu above is disabled. 

Bold`bold`\- Displays the text in **bold**. 

Italic`italic`\- Displays the text in _Italic_. 

Font Size X`fontsizex`\- Sets the font size in X (horizontal). The font size defines the distance from the baseline to the top of the layout box for the given font. The default size of 1 of the default font is close to the vertical size of capital letters with no descenders. 

Font Size Y`fontsizey`\- Sets the font size in Y (vertical). 

Keep Font Ratio`keepfontratio`\- Ignores Y value in Font Size. Sets both X and Y size to Font Size X. 

Scale Font to BBox Height`scalefontobboxheight`\- Scale the font’s vertical size so it’s based on the vertical bounding box of the font. 

Output`output`\- ⊞ \- Specify geometry output of Triangles, Closed Polygons or Open Polygons. 
* Triangles`triangles`\- The output is a triangulated mesh suitable for shaded renders.
* Closed Polygons (Filled Holes)`closedpolys`\- The output is a set of separated closed outlines, suitable for [Laser CHOP](<./Laser_CHOP.md> "Laser CHOP"), [Extrude SOP](<./Extrude_SOP.md> "Extrude SOP"), etc. Append a [Hole SOP](<./Hole_SOP.md> "Hole SOP") to preserve holes properly.
* Open Polygons`openpolys`\- The output is a set of separated open outlines, suitable for the [Laser CHOP](<./Laser_CHOP.md> "Laser CHOP"), etc. Renders as a wireframe always.


Level of Detail`levelofdetail`\- Controls the quality of the text's shape by adding/removing subdivisions to the geometry. 

Language`language`\- Language type hint to help format the glyphs correctly. This should be a abbreviation from the [Text TOP/SOP Unicode Language Abbreviations](<./Text_TOP/SOP_Unicode_Language_Abbreviations.md> "Text TOP/SOP Unicode Language Abbreviations") table. 

Reading Direction`readingdirection`\- ⊞ \- Use to set whether the language reads Left to Right or Right to Left. 
* Left To Right`lefttoright`-
* Right To Left`righttoleft`-


Kerning`kerning`\- ⊞ \- The amount of space to add between letters in X and Y. Kerning is way of adding an arbitrary offset between letters. There already is a default offset associated with each font so the letters are flush against each other. The Kerning parameter this adds to that and allows for a Y offset. 

  *`kerning1`-


  *`kerning2`-


Line Spacing`linespacing`\- Determines the amount of space between lines of text. 

Horizontal Align`alignx`\- ⊞ \- Sets the horizontal alignment. 
* In Reading Direction`reading`-
* Left`left`\- Left justifies the text.
* Center`center`\- Centers the text.
* Right`right`\- Right justifies the text.


Word Wrap`wordwrap`\- When checked text is automatically line wrapped once it takes up the space set in Word Wrap Size parameter below. 

Word Wrap Size`wordwrapsize`\- Determines the amount of 3D space used before the line wraps. 

Text`text`\- The string of text to create as geometry. If newlines or tabs are desired, the recommended way is to change this parameter to expression mode, and specify a Python string that includes \n or \t to signify newlines and tabs. E.g`'First Line\nSecond Line'`. 

Legacy Parsing`legacyparsing`\- **Note, it's recommended to use a Python expression in the Text parameter instead of enabling legacy parsing, as this parsing can easily run into issues with more complex strings.** When enabled and if the Text parameter is in Constant Mode, \t and \n character sequences will be turned into tab and newline characters respectively. Otherwise the \t and \n sequences will be left as literal \ and t and \ and n. 

## 

Parameters - Transform Page

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


Translate`t`\- ⊞ \- These three fields move the geometry in the three axes. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Rotate`r`\- ⊞ \- These three fields rotate the geometry in the three axes. 
* X`rx`-
* Y`ry`-
* Z`rz`-


Scale`s`\- ⊞ \- These three fields scale the geometry in the three axes. 
* X`sx`-
* Y`sy`-
* Z`sz`-


Pivot`p`\- ⊞ \- The pivot point for the transformations (not the same as the pivot point in the pivot channels). The pivot point parameters allow you to define the point about which geometry scales and rotates. Altering the pivot point produces different results depending on the transformation performed on the object. 

For example, during a scaling operation, if the pivot point of an object is located at:`-1, -1, 0`and you wanted to scale the object by`0.5`(reduce its size by 50%) the object would scale toward the pivot point and appear to slide down and to the left. 
* X`px`-
* Y`py`-
* Z`pz`-

## 

Info CHOP Channels

Extra Information for the Text SOP can be accessed via an [Info CHOP](<./Info_CHOP.md> "Info CHOP"). __

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


  
TouchDesigner Build: Latest\nwikieditorwikieditorwikieditor2021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Experimental:Face Track ](</Experimental:Face_Track_SOP> "Experimental:Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• [Font ](<./Font_SOP.md> "Font SOP")• [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [Experimental:POP to ](</Experimental:POP_to_SOP> "Experimental:POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• Text • [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")• [Experimental:ZED ](</Experimental:ZED_SOP> "Experimental:ZED SOP")
