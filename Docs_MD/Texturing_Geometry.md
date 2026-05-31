# Texturing Geometry

## Texture Coordinates Required
* geometry needs to have uv [Texture Coordinates](</index.php?title=Point_Attributes&action=edit&redlink=1> "Point Attributes \(page does not exist\)") to apply textures or maps to it
  * to create texture coordinates set the Generator SOP's **Texture Coordinate** parameter, or use a [Point SOP](<./Point_SOP.md> "Point SOP") or a [Texture SOP](<./Texture_SOP.md> "Texture SOP") downstream in the network
  * the [Texture SOP](<./Texture_SOP.md> "Texture SOP") gives control over how the uv coordinates are mapped to the surface

## Using Images as Texture Maps
* read the image (still image or movie) into TOPs using a [Movie File In TOP](<./Movie_File_In_TOP.md> "Movie File In TOP")
  * specify the TOP's path in the **Color Map** parameter of the material ([Constant MAT](<./Constant_MAT.md> "Constant MAT"), [PBR MAT](<./PBR_MAT.md> "PBR MAT"), [Phong MAT](<./Phong_MAT.md> "Phong MAT"), and [Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT") have Color Maps)
  * a TOP can be dragged & dropped onto the Color Map parameter
  * apply the material to the geometry by assigning the MAT to the **Material** parameter of the [Geometry COMP](<./Geometry_COMP.md> "Geometry COMP") (that contains the SOP geometry).


Example file using image and video as the Color Map in a Material. 

[File:Texturing geometry.tox](</File:Texturing_geometry.tox> "File:Texturing geometry.tox")
