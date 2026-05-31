# Point List

The geo-detail stores all points - both those attached to primitives and those that are free-floating - in a list. These points are simply X Y Z W locations in space. The W component is the spline weight (not mass, but the amount of pull on a spline hull). Each point can also contain [attributes](<./Attribute.md> "Attribute") like color, normal, and mass. 

Every point in the point list can be referenced by one or more primitives in the primitive list. For example, a sphere primitive may reference a point in the point list as its definition for the location of its centre, and the same point might also be the control vertex of a NURBS curve. 

## What is the difference between points and vertices?

The difference between points and vertices is that a point can be shared between primitives while vertices are unique. A point is simply "a place in space" as defined by four numbers (X, Y, Z, W). 

A vertex on the other hand is a reference to a point. Primitives use vertices to reference a point (e.g. the nodes of a polygon, the center of a sphere, or the control vertex of a spline). 

For example, if three polygons have one of their vertices in exactly the same place, and share the same point in the list, that place will contain three vertices, even though it is only a single point in the point list. Similarly, each vertex may reference a unique point, even though the points coincide in space. 

It is also possible for certain primitives to use a point more than once. 

_A point being reused: There are seven points and one polygon containing eight vertices (vertex numbers shoen here) where the point at the apex is used twice._

To summarize, the vertices of a primitive are always unique, while the points they reference might be shared between one or more primitives in the geo-detail. 

See also: [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point](<./Point.md> "Point"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Prims Class](<./Prims_Class.md> "Prims Class"), [Polygon](<./Polygon.md> "Polygon"), [Vertex](<./Vertex.md> "Vertex"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](<./Point_Group.md> "Point Group"), [Primitive Groups](<./Primitive_Group.md> "Primitive Group"), [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)").
