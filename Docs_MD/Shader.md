# Shader

A shader in TouchDesigner is the OpenGL (pre-2022) or Vulkan (2022-) GLSL code that runs on the GPU and creates rendered images from polygons, textures, CHOP channels and parameters. 

Shaders are either embedded inside [Materials](</index.php?title=Material&action=edit&redlink=1> "Material \(page does not exist\)") or placed in [Text DATs](<./Text_DAT.md> "Text DAT") and referenced to a [GLSL Material](<./GLSL_MAT.md> "GLSL MAT") or a [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP"). 

Shaders are composed of up to three parts: Vertex Shader, Pixel Shader and Compute Shader. (Geometry Shaders are now obsolete.) 

All shaders in TouchDesigner are GLSL shaders. 

The most commonly-used materials are the [Phong MAT](<./Phong_MAT.md> "Phong MAT") or [PBR MAT](<./PBR_MAT.md> "PBR MAT") which contain numerous lighting and surface rendering options. The Phong MAT and PBR MAT can output the specific GLSL shader code that represents the features being used in the material, which is a good starting point for writing your own shaders or adapting other shaders. 

A [GLSL TOP](<./GLSL_TOP.md> "GLSL TOP") uses a GLSL shader for generating 2D images. 

See also [Write a GLSL Material](<./Write_a_GLSL_Material.md> "Write a GLSL Material").
