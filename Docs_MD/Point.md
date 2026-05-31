# Point

  
See [Point Class](<./Point_Class.md> "Point Class") for Python API. 

Each SOP has a list of Points. A Point is an XYZ position with some optional extra attributes. The [point attributes](<./Attribute.md> "Attribute") are: 

  *`P`\- an XYZ 3D position represented as 3 floating point numbers.
  *`Cd`\- color (optional) a standard 4-value attribute where the RGB color is`Cd[0]`,`Cd[1]`,`Cd[2]`and alpha which is`Cd[3]`. (See [Point SOP](<./Point_SOP.md> "Point SOP"))
  *`uv`\- texture (optional) a standard 3-value attribute where UV are`uv[0]`and`uv[1]`, and W is`uv[2]`. (See [Point SOP](<./Point_SOP.md> "Point SOP"))
  *`N`\- normal vector (optional) a standard 3-value attribute. (See [Facet SOP](<./Facet_SOP.md> "Facet SOP") and [Point SOP](<./Point_SOP.md> "Point SOP"))
  *`T`\- tangent vector (optional) a standard 4-value attribute. (See [Attribute Create SOP](<./Attribute_Create_SOP.md> "Attribute Create SOP"))
  * user-defined attributes. (See [Point SOP](<./Point_SOP.md> "Point SOP"))


Each [Polygon](<./Polygon.md> "Polygon") is defined by a vertex list, which is a list of point numbers. 

On s SOP, MMB on the node to see a summary of the points, polygons, particle systems and other primitives, attributes and bounding box. 

Note: Points can not be rendered directly. To render points they must first be [Particles](<./Particle.md> "Particle"). Points can be converted to particles using the [Convert SOP](<./Convert_SOP.md> "Convert SOP") or generated directly by the [Particle SOP](<./Particle_SOP.md> "Particle SOP"). See also [Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT"). 

See also: [Point List](<./Point_List.md> "Point List"), [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point SOP](<./Point_SOP.md> "Point SOP"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Polygon](<./Polygon.md> "Polygon"), [Vertex](<./Vertex.md> "Vertex"), [Prims Class](<./Prims_Class.md> "Prims Class"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](<./Point_Group.md> "Point Group"), [Primitive Groups](<./Primitive_Group.md> "Primitive Group"), [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)").
