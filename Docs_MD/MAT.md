# MAT

## 

Summary

MATs or Materials are an [Operator Family](<./Operator_Family.md> "Operator Family") that applies a [Shader](<./Shader.md> "Shader") to a SOP or 3D Geometry Object for rendering textured surfaces with lighting. 

See also [Category:MATs](<./Category-MATs.md> "Category:MATs") for a full list of articles related to MATs. 

**Material Operators**, or **MATs** , are used to create materials for geometry. They can be applied to geometry using the **Material** parameter on the Display page of [Object Components](<./Object_Component.md> "Object Component"). 

The [Phong MAT](<./Phong_MAT.md> "Phong MAT") and [GLSL MAT](<./GLSL_MAT.md> "GLSL MAT") are designed to use [TOPs](<./TOP.md> "TOP") and [GLSL](<./GLSL.md> "GLSL") programs (pixel and vertex shaders) as inputs to create more advanced shaders. 

The most commonly used MAT is the Phong MAT. The Phong MAT contains a large number of lighting options that allow the users to create some very unique effects. 

[Phong MAT](<./Phong_MAT.md> "Phong MAT") \- applies a phong shader to the geometry. Geometry must have [normals](<./Normals.md> "Normals") for specular shading to work. Geometry must have [Texture Coordinates](</index.php?title=Point_Attributes&action=edit&redlink=1> "Point Attributes \(page does not exist\)") for any applied maps to work (ie Color Map, Bump Map, Specular Map, etc). Geometry can be deformed using the Deform parameter page. The Phong MAT offers other advanced features for [Transparency](<./Transparency.md> "Transparency"), [Rim Lights](<./Rim_Light.md> "Rim Light"), and [Shadows](<./Shadows.md> "Shadows"). 

[PBR MAT](<./PBR_MAT.md> "PBR MAT") \- applies a PBR shader to the geometry. Use in conjunction with an [Environment Light COMP](<./Environment_Light_COMP.md> "Environment Light COMP"). [Substance Designer](<http://www.allegorithmic.com/products/substance-designer>) PBR materials can also be used via .sbsar files loaded into the [Substance TOP](<./Substance_TOP.md> "Substance TOP"). 

[Line MAT](<./Line_MAT.md> "Line MAT") \- renders the geometry edges as lines and points with different geometry. 

[Constant MAT](<./Constant_MAT.md> "Constant MAT") \- this material applies a constant flat color to the geometry. There is no specular shading, ie shading is not affected by the camera or light positions. 

[PBR MAT](<./PBR_MAT.md> "PBR MAT") \- applies a PBR shader to the geometry. Use in conjunction with an [Environment Light COMP](<./Environment_Light_COMP.md> "Environment Light COMP"). [Substance Designer](<http://www.allegorithmic.com/products/substance-designer>) PBR materials can also be used via`.sbsar`files loaded into the [Substance TOP](<./Substance_TOP.md> "Substance TOP"). 

[Depth MAT](<./Depth_MAT.md> "Depth MAT") \- can be used to get depth information from the geometry for a depth-pass render. It will not render any color. 

[GLSL MAT](<./GLSL_MAT.md> "GLSL MAT") \- a powerful material operator which applies Pixel and Vertex GLSL shaders to the geometry. Geometry can be deformed on the GPU using vertex shaders. Geometry must have [Texture Coordinates](</index.php?title=Point_Attributes&action=edit&redlink=1> "Point Attributes \(page does not exist\)") and [normals](<./Normals.md> "Normals"). 

[Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT") \- special material for use with Point Sprite geometry type. The [Particle SOP](<./Particle_SOP.md> "Particle SOP") can create point sprites. 

[![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>)[MAT Class Class](</index.php?title=MAT_Class_Class&action=edit&redlink=1> "MAT Class Class \(page does not exist\)")

## Using MATs
* for Materials to texture geometry with, Phong MAT, GLSL MAT
  * setup for materials (normals, uvs, where to apply, lighting and rendering)
  * examples of applying a material, example of Rim Lighting, example of shadows
