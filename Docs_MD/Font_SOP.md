# Font SOP

## 

Summary

**Note** : Font SOP deprecated build 2019.14650, use [Text SOP](<./Text_SOP.md> "Text SOP"). 

The Font SOP allows you to create text in your model from Adobe Type 1 Postscript Fonts. 

To install fonts, copy the font files to the`$TFS/touch/fonts`directory of your installation path. They will be ready to be used in the Font SOP after restarting TouchDesigner. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[fontSOP_Class](<./FontSOP_Class.md> "FontSOP Class")

## 

Parameters - Page

Primitive Type`type`\- ⊞ \- Select from the following types. For information on the different types, see the Geometry Types section. Bzier Curves and Polygons provide the most efficient use of memory, because they use polygons for letters containing straight segments, and Bzier curves for all others. 

**Note:** Due to an Open GL bug, holes in Bzier fonts may shade incorrectly. 
* Bezier Curves and Polygons`bezierpoly`-
* Beziers Only`bezier`-
* Polygons Only`poly`-


Font`file`\- Choose the font to create the text. By clicking on the + button a File Dialog will appear, and clicking menu drop down brings up a menu of the most used fonts. 

Text`text`\- Enter the text you want to generate here. 

Your text can contain the following special characters: 

  *`\`\- Take the next character literally (so you can use the / and`characters in your text);
  *``string``\- Evaluate the string contained by the backquotes (above the T key) as an expression;
  *`\n`\- Start a new line;
  *`\xxx`\- Specify a character by it's ascii code (e.g. \007).


**For Example:** If you put something like`\\$F3`in the text string, you should see all the possible characters of a font as you play the animation (set the last frame to 256). 

**Entering Expressions as Text** \- You can also use expressions for the text. 

**For Example:**`me.time.frame`\- will display the current frame.`op('null1')['chan1']`\- will display the current value of channel chan1 in CHOP`null1`.`'hello world'[int(me.time.frame)%11]`\- causes the eleven letters of the text to appear in succession during the first eleven frames. 

**Other Methods of Entering Text -** You can use the`\xxx`decimal notation to specify characters. The available characters will depend on the font type used. 

**For Example:** \065 - will display '`a`'. 

You can also use the [Par Class](<./Par_Class.md> "Par Class") to set text in the Font SOP. This can be done from the textport, a [Logic CHOP](<./Logic_CHOP.md> "Logic CHOP") or [Expression CHOP](<./Expression_CHOP.md> "Expression CHOP"), or any script. (See [Scripting](<./Introduction_to_Python_Tutorial.md> "Introduction to Python Tutorial") articles) 

**For Example:**`op('font1').par.text = 'hello world'`\- will display the words: hello world __

Center Text Horizontally`hcenter`\- This check box allows you to center the text horizontally about X = 0. 

Center Text Vertically`vcenter`\- This check box allows you to center the text vertically about Y = 0. 

Translate`t`\- ⊞ \- Translates the geometry in x, y and z. 
* X`tx`-
* Y`ty`-
* Z`tz`-


Scale`s`\- ⊞ \- Scales the text in the X and Y axis. 
* X`sx`-
* Y`sy`-


Kerning`kern`\- ⊞ \- Letter spacing in the X direction. Line spacing in the Y direction if there are multiple lines. If you need manual character-by-character, you can do it in Model mode. 
* X`kernx`-
* Y`kerny`-


Italic Angle`italic`\- Doesn't actually give an italic version of the font, but rather obliques the text by shearing it the specified number of degrees. A negative number makes the text slant to the left. 

Level of Detail`lod`\- Adobe fonts are defined by Bzier curves. If polygons only is selected, the Font SOP converts these to polygons. This value adjusts the number of points in the polygons that it gets converted to. 

Hole Faces`hole`\- Generates holes in polygons and Bzier faces. 

Texture Coordinates`texture`\- ⊞ \- This adds uv coordinates to the geometry created by the Font SOP. 
* Off`off`\- No uv coordinates added.
* Orthographic`ortho`\- Orthographic uv coordinates added.


TouchDesigner Build: Latest\nwikieditorwikieditor2021.100002018.28070before 2018.28070

SOPs   
---  
[Add ](<./Add_SOP.md> "Add SOP")• [Alembic ](<./Alembic_SOP.md> "Alembic SOP")• [Align ](<./Align_SOP.md> "Align SOP")• [Arm ](<./Arm_SOP.md> "Arm SOP")• [Attribute Create ](<./Attribute_Create_SOP.md> "Attribute Create SOP")• [Attribute ](<./Attribute_SOP.md> "Attribute SOP")• [Basis ](<./Basis_SOP.md> "Basis SOP")• [Blend ](<./Blend_SOP.md> "Blend SOP")• [Bone Group ](<./Bone_Group_SOP.md> "Bone Group SOP")• [Boolean ](<./Boolean_SOP.md> "Boolean SOP")• [Box ](<./Box_SOP.md> "Box SOP")• [Bridge ](<./Bridge_SOP.md> "Bridge SOP")• [Cache ](<./Cache_SOP.md> "Cache SOP")• [Cap ](<./Cap_SOP.md> "Cap SOP")• [Capture Region ](<./Capture_Region_SOP.md> "Capture Region SOP")• [Capture ](<./Capture_SOP.md> "Capture SOP")• [Carve ](<./Carve_SOP.md> "Carve SOP")• [CHOP to ](<./CHOP_to_SOP.md> "CHOP to SOP")• [Circle ](<./Circle_SOP.md> "Circle SOP")• [Clay ](<./Clay_SOP.md> "Clay SOP")• [Clip ](<./Clip_SOP.md> "Clip SOP")• [Convert ](<./Convert_SOP.md> "Convert SOP")• [Copy ](<./Copy_SOP.md> "Copy SOP")• [CPlusPlus ](<./CPlusPlus_SOP.md> "CPlusPlus SOP")• [Creep ](<./Creep_SOP.md> "Creep SOP")• [Curveclay ](<./Curveclay_SOP.md> "Curveclay SOP")• [Curvesect ](<./Curvesect_SOP.md> "Curvesect SOP")• [DAT to ](<./DAT_to_SOP.md> "DAT to SOP")• [Deform ](<./Deform_SOP.md> "Deform SOP")• [Delete ](<./Delete_SOP.md> "Delete SOP")• [Divide ](<./Divide_SOP.md> "Divide SOP")• [Extrude ](<./Extrude_SOP.md> "Extrude SOP")• [Face Track ](<./Face_Track_SOP.md> "Face Track SOP")• [Facet ](<./Facet_SOP.md> "Facet SOP")• [File In ](<./File_In_SOP.md> "File In SOP")• [Fillet ](<./Fillet_SOP.md> "Fillet SOP")• [Fit ](<./Fit_SOP.md> "Fit SOP")• Font • [Force ](<./Force_SOP.md> "Force SOP")• [Fractal ](<./Fractal_SOP.md> "Fractal SOP")• [Grid ](<./Grid_SOP.md> "Grid SOP")• [Group ](<./Group_SOP.md> "Group SOP")• [Hole ](<./Hole_SOP.md> "Hole SOP")• [Import Select ](<./Import_Select_SOP.md> "Import Select SOP")• [In ](<./In_SOP.md> "In SOP")• [Introduction To s Vid ](<./Introduction_To_SOPs_Vid.md> "Introduction To SOPs Vid")• [Inverse Curve ](<./Inverse_Curve_SOP.md> "Inverse Curve SOP")• [Iso Surface ](<./Iso_Surface_SOP.md> "Iso Surface SOP")• [Join ](<./Join_SOP.md> "Join SOP")• [Joint ](<./Joint_SOP.md> "Joint SOP")• [Kinect ](<./Kinect_SOP.md> "Kinect SOP")• [Lattice ](<./Lattice_SOP.md> "Lattice SOP")• [Limit ](<./Limit_SOP.md> "Limit SOP")• [Line ](<./Line_SOP.md> "Line SOP")• [Line Thick ](<./Line_Thick_SOP.md> "Line Thick SOP")• [LOD ](<./LOD_SOP.md> "LOD SOP")• [LSystem ](<./LSystem_SOP.md> "LSystem SOP")• [Magnet ](<./Magnet_SOP.md> "Magnet SOP")• [Material ](<./Material_SOP.md> "Material SOP")• [Merge ](<./Merge_SOP.md> "Merge SOP")• [Metaball ](<./Metaball_SOP.md> "Metaball SOP")• [Model ](<./Model_SOP.md> "Model SOP")• [Noise ](<./Noise_SOP.md> "Noise SOP")• [Null ](<./Null_SOP.md> "Null SOP")• [Object Merge ](<./Object_Merge_SOP.md> "Object Merge SOP")• [Oculus Rift ](<./Oculus_Rift_SOP.md> "Oculus Rift SOP")• [OpenVR ](<./OpenVR_SOP.md> "OpenVR SOP")• [Out ](<./Out_SOP.md> "Out SOP")• [Particle ](<./Particle_SOP.md> "Particle SOP")• [Point ](<./Point_SOP.md> "Point SOP")• [Polyloft ](<./Polyloft_SOP.md> "Polyloft SOP")• [Polypatch ](<./Polypatch_SOP.md> "Polypatch SOP")• [Polyreduce ](<./Polyreduce_SOP.md> "Polyreduce SOP")• [Polyspline ](<./Polyspline_SOP.md> "Polyspline SOP")• [Polystitch ](<./Polystitch_SOP.md> "Polystitch SOP")• [POP to ](<./POP_to_SOP.md> "POP to SOP")• [Primitive ](<./Primitive_SOP.md> "Primitive SOP")• [Profile ](<./Profile_SOP.md> "Profile SOP")• [Project ](<./Project_SOP.md> "Project SOP")• [Rails ](<./Rails_SOP.md> "Rails SOP")• [Raster ](<./Raster_SOP.md> "Raster SOP")• [Ray ](<./Ray_SOP.md> "Ray SOP")• [Rectangle ](<./Rectangle_SOP.md> "Rectangle SOP")• [Refine ](<./Refine_SOP.md> "Refine SOP")• [Resample ](<./Resample_SOP.md> "Resample SOP")• [Revolve ](<./Revolve_SOP.md> "Revolve SOP")• [Script ](<./Script_SOP.md> "Script SOP")• [Select ](<./Select_SOP.md> "Select SOP")• [Sequence Blend ](<./Sequence_Blend_SOP.md> "Sequence Blend SOP")• [Skin ](<./Skin_SOP.md> "Skin SOP")• [SOP ](<./SOP.md> "SOP")• [Sort ](<./Sort_SOP.md> "Sort SOP")• [Sphere ](<./Sphere_SOP.md> "Sphere SOP")• [Spring ](<./Spring_SOP.md> "Spring SOP")• [Sprinkle ](<./Sprinkle_SOP.md> "Sprinkle SOP")• [Sprite ](<./Sprite_SOP.md> "Sprite SOP")• [Stitch ](<./Stitch_SOP.md> "Stitch SOP")• [Subdivide ](<./Subdivide_SOP.md> "Subdivide SOP")• [Superquad ](<./Superquad_SOP.md> "Superquad SOP")• [Surfsect ](<./Surfsect_SOP.md> "Surfsect SOP")• [Sweep ](<./Sweep_SOP.md> "Sweep SOP")• [Switch ](<./Switch_SOP.md> "Switch SOP")• [Text ](<./Text_SOP.md> "Text SOP")• [Texture ](<./Texture_SOP.md> "Texture SOP")• [Torus ](<./Torus_SOP.md> "Torus SOP")• [Trace ](<./Trace_SOP.md> "Trace SOP")• [Trail ](<./Trail_SOP.md> "Trail SOP")• [Transform ](<./Transform_SOP.md> "Transform SOP")• [Trim ](<./Trim_SOP.md> "Trim SOP")• [Tristrip ](<./Tristrip_SOP.md> "Tristrip SOP")• [Tube ](<./Tube_SOP.md> "Tube SOP")• [Twist ](<./Twist_SOP.md> "Twist SOP")• [Vertex ](<./Vertex_SOP.md> "Vertex SOP")• [Wireframe ](<./Wireframe_SOP.md> "Wireframe SOP")• [ZED ](<./ZED_SOP.md> "ZED SOP")
