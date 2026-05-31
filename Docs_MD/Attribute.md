# Attribute

  
Attributes are data associated with [POP](<./POP.md> "POP") (or [SOP](<./SOP.md> "SOP")) geometry. [Points](<./Point.md> "Point"), [Vertex (Vertices)s](<./Vertex.md> "Vertex") and [Primitives](<./Primitive.md> "Primitive") (polygons, lines, etc) can have any number of attributes. In POPs, position (`P`) is standard, and built-in optional attributes are [normals](<./Normals.md> "Normals") (`N`), texture coordinates (`Tex`), color (`Color`), etc. 

_For attributes of SOPs see[SOP Attribute](<./SOP_Attribute.md> "SOP Attribute") as this page is being re-focused on POPs (in-progress)._

A **point attribute** is a named set of numbers, one for each point of a POP. A **scalar point attribute** is a single number for each point. A **vector point attribute** is 2, 3 or 4 numbers per point, such as the`P`(position) attribute which is a float3 (3-number) vector attribute. 

A **primitive attribute** is a named set of numbers, one for each primitive of a POP. A **scalar primitive attribute** is a single number for each primitive. A **vector primitive attribute** is 2, 3 or 4 numbers per primitive. 

A **vertex attribute** is a named set of numbers, one for each vertex of each primitive of a POP. A **scalar vertex attribute** is a single number for each vertex. A **vector vertex attribute** is 2, 3 or 4 numbers per vertex. 

### Attribute Terminolgy
* Built-in Attributes \- Attributes that are strictly reserved, like`P`,`PointScale`,`N`and`Tex`.
  * Common Attributes \- Attributes that are commonly used but not strictly controlled by TouchDesigner, like`PartMass`and`PartVel`.
  * Read-Only Attributes \- attributes that are pre-computed by TouchDesigner (like normalized point number`_PointU`) that can be used in Math POP. Math Mix, Math Combine POPs and others.
  * Components of Attributes \- For attributes that are vectors, a flaot3 has 3 "components".
  * Attribute Class - refers to Point, Vertex and Primitive classes.
  * Array Attribute - an attribute type that has per-point multiple float or float2 etc
  * Scalar Attribute vs Vector Attribute

## Common Attributes

### Normals (N)

See [Normals](<./Normals.md> "Normals"). A normal is a directional vector associated with a particular geometric entity, commonly perpendicular to it. The normal to a surface at a given point is a vector perpendicular to the surface at that point, and is computed as the cross product of the tangent vectors at that point. 

### Color (Color)

Surface color and alpha specified by RGBA. Values range from 0 to 1. The alpha component`Color.a`controls the transparency of a given element, where 1 is fully opaque, and 0 is fully transparent. 

### Texture Coordinates (Tex)

Items are located spatially by XYZ values. To differentiate texture coordinate space from XYZ space, the labels U and V and sometimes W are used instead of X and Y and Z. ​ In order to place texture maps (images) onto geometry, we must assign texture coordinates to the geometry. A texture map resides in its own (U, V) texture coordinate space. When assigned to the geometry, the (U, V) coordinates determine how to map the image onto the geometry, where U,V of 0,0 uses the bottom left of the texture image, and 1,1 use the top-right. ​ Most generator POPs like [Sphere POP](<./Sphere_POP.md> "Sphere POP") and [Plane POP](<./Plane_POP.md> "Plane POP") have texture coordinates already assigned to each point or vertex. ​ Texture coordinates can be visualized in the following manner: Texture maps have their own coordinate space. If the texture were a table cloth with a grid pattern, the color at location 3, 4 on the table cloth remains at location 3, 4 even when the cloth is wrapped around an irregularly shaped object. The color at location 3, 4 can be said to be in the table-cloth's coordinate space. ​ 

## Order of Attribute Precedence

The order of precedence for attributes from highest to lowest is: 
1. Vertex Attributes
  2. Point Attributes
  3. Primitive Attributes


Attributes with a higher order of precedence override the same attributes with a lower order of precedence. (Only the [Bone Group SOP](<./Bone_Group_SOP.md> "Bone Group SOP") has Detail attributes from skeletons imported externally.) 

Point and vertex attributes are interpolated across primitives, allowing more local flexibility than primitive attributes (e.g.`Color`). Vertex attributes deal with the situation where shared points need different values for the attributes at the boundary of primitives, like the longitudinal seam of a polar texture map for example. Primitive colors typically take us less memory point colors, and point colors less than vertex colors. 

## Custom Attributes

Below are the Attributes which are currently reserved for TouchDesigner use. 

## Point Attributes

Point Attributes are Attributes on [Points](<./Point.md> "Point") in a [POP](<./POP.md> "POP"). 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`P`| float  | 3  | Point position  |  |  |`Weight`| float  | 1  | Point weight  |  |  |`N`| vector  | 3  | Surface Normal  |  | [Normal POP](<./Normal_POP.md> "Normal POP"), [Facet POP](<./Facet_POP.md> "Facet POP") |`Tex`| float  | 3  | Texture Coordinates  |  | [Texture Map POP](<./Texture_Map_POP.md> "Texture Map POP") |`Color (Color.rgb and Color.a)`| float  | 4  | Surface color and alpha  |  |  |`PartVel`| vector  | 3  | Particle Velocity  |  |  |`PartMass`| float  | 1  | particle mass  |  | [Particle POP](<./Particle_POP.md> "Particle POP"), [Force Radial POP](<./Force_Radial_POP.md> "Force Radial POP") |`PartDrag`| float  | 1  | Drag  |  | [Particle POP](<./Particle_POP.md> "Particle POP"), [Force Radial POP](<./Force_Radial_POP.md> "Force Radial POP") |`PartLife`| float  | 1  | Life Expectancy  |  | [Particle POP](<./Particle_POP.md> "Particle POP") |`PartAge`| float  | 1  | Age  |  | [Particle POP](<./Particle_POP.md> "Particle POP") |`PartId`| float  | 1  | Particle Identifying Tag |  | [Particle POP](<./Particle_POP.md> "Particle POP") |`PartInitP`| vector  | 3  | Rest Position  |  |  |`PointScale`| float  | 1  | Scale of point for rendering  |  |  |   
  
## Vertex Attributes

A Triangle, Quadrelateral or Line Strip is made of a set of [Vertices](<./Vertex.md> "Vertex"), and each Vertex refers to a [Point](<./Point.md> "Point"). 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`N`| vector  | 3  | Surface normal  | [Facet SOP](<./Facet_SOP.md> "Facet SOP"), [Attribute Create SOP](<./Attribute_Create_SOP.md> "Attribute Create SOP") |  |`uv`| float  | 3  | Texture coordinates  | [Texture SOP](<./Texture_SOP.md> "Texture SOP") |  |`Cd`| float  | 4  | Surface color and alpha  |  |  |`creaseweight`| float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP").`T`| float  | 4  | Tangents  | [Attribute Create SOP](<./Attribute_Create_SOP.md> "Attribute Create SOP") |  | two 2D vectors = 4 values`pCapt`| float  | 2  | Capture data  |  |  | contains index and weight for a transform. See [Deforming Geometry (Skinning)](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)")  
  
## Primitive Attributes

You can use the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP") or the [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") and [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP") pair to add or modify primitive attributes. 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`N`| vector  | 3  | Surface normal  |  |  |`Cd`| float  | 4  | Surface color and alpha  |  |  |`creaseweight`| float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP").`mat`| index  | 1  | Material | [Material SOP](<./Material_SOP.md> "Material SOP") |  |   
  
plus Force dir, fedge, fvortex, fspiral xxx 

## Data Types of Attributes

There are three different attribute data types. Each is handled slightly differently internally. 

Vector Data  | This data type represents a 3D vector in space. When any transforms occur on the detail, this attribute will also be transformed. Examples of a vector attribute are normals (N) or velocity (PartVel).   
---|---  
Floating Point Data  | This data type represents an array of floating point values. The values are not transformed when the geometry gets transformed. Some examples of this type of attribute are diffuse colors (Cd), and texture co-ordinates (Tex).
