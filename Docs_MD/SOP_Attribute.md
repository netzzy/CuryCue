# SOP Attribute

**This page applies to attributes of[SOPs](<./SOP.md> "SOP").** For POP attributes, see [Attribute](<./Attribute.md> "Attribute").   
  
**Attributes** include information about an entity such as its color, velocity, normal, and so on. Attributes can be attached to [Points](<./Point.md> "Point"), [Vertex (Vertices)](<./Vertex.md> "Vertex"), [Primitives](<./Primitive.md> "Primitive"), or the whole geometry. 

Point and vertex attributes are interpolated across primitives, allowing more local flexibility than primitive attributes (e.g.`Color`). Vertex attributes deal with the situation where shared points need different values for the attributes at the boundary of primitives, like the seam of a polar texture map for example. Primitive colors typically take us less memory point colors, and point colors less than vertex colors. 

See also: [Point List](<./Point_List.md> "Point List"), [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Polygon](<./Polygon.md> "Polygon"), [Vertex](<./Vertex.md> "Vertex"), [Prims Class](<./Prims_Class.md> "Prims Class"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [Point SOP](<./Point_SOP.md> "Point SOP"), [Attribute SOP](<./Attribute_SOP.md> "Attribute SOP"), [Attribute Create SOP](<./Attribute_Create_SOP.md> "Attribute Create SOP"), [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](<./Point_Group.md> "Point Group"), [Primitive Groups](<./Primitive_Group.md> "Primitive Group"). 

## Common Attributes

### Normals

See [Normals](<./Normals.md> "Normals"). A normal is a directional vector associated with a particular geometric entity, commonly perpendicular to it. The normal to a surface at a given point is a vector perpendicular to the surface at that point, and is computed as the cross product of the tangent vectors at that point. 

### Colors

Surface color and alpha specified by RGBA. Values range from 0 to 1. The alpha component Cd(3) controls the transparency of a given element, where 1 is fully opaque, and 0 is fully transparent. 

### Texture Coordinates (Tex)

Items are located spatially by XYZ values. To differentiate texture coordinate space from XYZ space, the labels U and V and sometimes W are used instead of X and Y and Z. ​ In order to place texture maps (images) onto geometry, we must assign texture coordinates to the geometry. A texture map resides in its own (U, V) texture coordinate space. When assigned to the geometry, the (U, V) coordinates determine how to map the image onto the geometry, where U,V of 0,0 uses the bottom left of the texture image, and 1,1 use the top-right. Texture space should not be mistaken for the parametric space of splines. ​ Generators SOPs like [Sphere SOP](<./Sphere_SOP.md> "Sphere SOP") and [Grid SOP](<./Grid_SOP.md> "Grid SOP") have UVs already assigned to each point. The [Texture SOP](<./Texture_SOP.md> "Texture SOP"), [Point SOP](<./Point_SOP.md> "Point SOP") or the [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") with the [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP") pairs to add or modify the attributes. ​ Texture coordinates can be visualized in the following manner: Texture maps have their own coordinate space. If the texture were a table cloth with a grid pattern, the color at location 3, 4 on the table cloth remains at location 3, 4 even when the cloth is wrapped around an irregularly shaped object. The color at location 3, 4 can be said to be in the table-cloth's coordinate space. ​ _**TIP**_ : By using a [Point SOP](<./Point_SOP.md> "Point SOP"), you can swap the position and the texture coordinates. This allows you to model the "texture space". Another Point SOP allows you to swap the position and texture back to their original locations. 

## Order of Attribute Precedence

The order of precedence for attributes from highest to lowest is: 
1. Vertex Attributes
  2. Point Attributes
  3. Primitive Attributes
  4. Detail Attributes


Attributes with a higher order of precedence override tbe same attributes with a lower order of precedence. (Only the [Bone Group SOP](<./Bone_Group_SOP.md> "Bone Group SOP") has Detail attributes from skeletons imported externally.) 

## Custom Attributes

Below are the Attributes which are currently reserved for TouchDesigner use. In addition the user can create any number of custom attributes on SOPs using the [Point SOP](<./Point_SOP.md> "Point SOP"), [Vertex SOP](<./Vertex_SOP.md> "Vertex SOP") and [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP"). 

## Point Attributes

Point Attributes are Attributes on [Points](<./Point.md> "Point") in a [SOP](<./SOP.md> "SOP"). The [Point SOP](<./Point_SOP.md> "Point SOP") can create most of these attributes. 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`P`| float  | 3  | Point position  |  |  |`Pw`| float  | 1  | Point weight  |  |  |`N`| vector  | 3  | Surface Normal  |  | [Facet SOP](<./Facet_SOP.md> "Facet SOP") |`uv`| float  | 3  | Texture Coordinates  |  | [Texture SOP](<./Texture_SOP.md> "Texture SOP") |`Cd`| float  | 4  | Surface color and alpha  |  |  |`pCapt`| float  | 2  | Capture data for Deform  |  |  | contains index and weight for a transform. See [Deforming Geometry (Skinning)](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)")`v`| vector  | 3  | Velocity  |  |  | often taken from Normal`mass`| float  | 1  | Mass  |  | [Particle SOP](<./Particle_SOP.md> "Particle SOP"), [Spring SOP](<./Spring_SOP.md> "Spring SOP") |`drag`| float  | 1  | Drag  |  | [Particle SOP](<./Particle_SOP.md> "Particle SOP"), [Spring SOP](<./Spring_SOP.md> "Spring SOP") |`life`| float  | 1  | Life Expectancy  |  | [Particle SOP](<./Particle_SOP.md> "Particle SOP") |`age`| float  | 1  | Age  |  | [Particle SOP](<./Particle_SOP.md> "Particle SOP") |`id`| float  | 1  | Particle Identifying Tag |  | [Particle SOP](<./Particle_SOP.md> "Particle SOP") |`rest`| vector  | 3  | Rest Position  |  |  |`tension`| float  | 1  | Tension  |  |  |`springk`| float  | 1  | Spring constant  |  | [Spring SOP](<./Spring_SOP.md> "Spring SOP") |`up`| vector  | 3  | Up  |  |  |`pscale`| float  | 1  | Particle scale  |  |  |`radiusf xxx`| float  | 1  | Radius  |  |  |`fscalef xxx`| float  | 1  | Force scale  |  |  |`fradial`| float  | 1  | Radial force  |  |  |`normalf xxxx`| float  | 1  | Normal force  |  |  |`fedge`| float  | 1  | Edge force  |  |  |`edge_dir`| vector  | 3  | Edge direction  |  |  |`dir`| vector  | 3  | Directional force  |  |  |   
  
## Vertex Attributes

A [Polygon](<./Polygon.md> "Polygon") is made of a set of [Vertices](<./Vertex.md> "Vertex"), and each Vertex refers to a [Point](<./Point.md> "Point"). You can use the [Vertex SOP](<./Vertex_SOP.md> "Vertex SOP") to create vertex attributes. The [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") and [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP") pair can create and modify vertex attributes. 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`N`| vector  | 3  | Surface normal  | [Facet SOP](<./Facet_SOP.md> "Facet SOP"), [Attribute Create SOP](<./Attribute_Create_SOP.md> "Attribute Create SOP") |  |`uv`| float  | 3  | Texture coordinates  | [Texture SOP](<./Texture_SOP.md> "Texture SOP") |  |`Cd`| float  | 4  | Surface color and alpha  |  |  |`creaseweight`| float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP").`T`| float  | 4  | Tangents  | [Attribute Create SOP](<./Attribute_Create_SOP.md> "Attribute Create SOP") |  | two 2D vectors = 4 values`pCapt`| float  | 2  | Capture data  |  |  | contains index and weight for a transform. See [Deforming Geometry (Skinning)](<./Deforming_Geometry_\(Skinning\).md> "Deforming Geometry \(Skinning\)")  
  
## Primitive Attributes

You can use the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP") or the [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") and [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP") pair to add or modify primitive attributes. 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`N`| vector  | 3  | Surface normal  |  |  |`Cd`| float  | 4  | Surface color and alpha  |  |  |`creaseweight`| float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP").`mat`| index  | 1  | Material | [Material SOP](<./Material_SOP.md> "Material SOP") |  |   
  
plus Force dir, fedge, fvortex, fspiral xxx 

## Detail Attributes

You can use the [Primitive SOP](<./Primitive_SOP.md> "Primitive SOP") or the [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT") and [DAT to SOP](<./DAT_to_SOP.md> "DAT to SOP") pair to add or modify detail attributes. 

Name  | Type  | Size  | Description  | SOP to Create  | SOP where Used  | Notes   
---|---|---|---|---|---|---`mat`| index  | 1  | Material | [Material SOP](<./Material_SOP.md> "Material SOP") |  |`bone`| float  | 1  | Bone Info  |  |  | for deforming, with imported 3D objects.`creaseweight`| float  | 1  | Crease weights  |  |  | used in sub-division surfaces. See [Subdivide SOP](<./Subdivide_SOP.md> "Subdivide SOP").   
  
## Data Types of Attributes

There are three different attribute data types. Each is handled slightly differently internally. 

Vector Data  | This data type represents a 3D vector in space. When any transforms occur on the detail, this attribute will also be transformed. Examples of a vector attribute are normals (N) or velocity (v).   
---|---  
Floating Point Data  | This data type represents an array of floating point values. The values are not transformed when the geometry gets transformed. Some examples of this type of attribute are diffuse colors (Cd), and texture co-ordinates (uv).   
Indexed String Data  | This attribute consists of an ordered list of character strings. The attribute stored with the element is an integer representing the offset into the array of strings. A value outside the bounds of the array is considered to be "not assigned". An example of this is the material attribute.   
  
  
See also: [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point](<./Point.md> "Point"), [Point List](<./Point_List.md> "Point List"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Prims Class](<./Prims_Class.md> "Prims Class"), [Polygon](<./Polygon.md> "Polygon"), [Vertex](<./Vertex.md> "Vertex"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](<./Point_Group.md> "Point Group"), [Primitive Groups](<./Primitive_Group.md> "Primitive Group").
