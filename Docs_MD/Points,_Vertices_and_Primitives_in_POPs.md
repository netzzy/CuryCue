# Points, Vertices and Primitives in POPs

## 

Summary

It is similar but not the same. This is adapted from the [SOP Primitive](<./Primitive.md> "Primitive") Page 

## 

Primitives

Every POP has a list of Points. Points have an XYZ position, and can have attributes like Normals. 

Every POP has a list of Primitives. 

Each Primitive usually has as set of Vertices. A vertex is an index into the point list. 

Primitives are entities of a POP that refer to points and get rendered. 

A Primitive is of several types: 
* Triangle Primitive \- 3-point polygons
  * Quadrelateral (quad) Primitive \- 4-point polygons
  * Line Primitive \- 2 connected points
  * Linestrip Primitive \- a set of connected points that can be closed, but when a linestrip is closed, it is not a polygon that get filled when rendered, it is simply a sequence of connected points.
  * Point Primitive \- a single point (a single vertex that is the point index)


(unlike SOPs which have polygon, mesh, particle (same as Point in POPs). So there are no 5-point closed polygons, only 3 and 4. curve (NURBS and Bezier), patch (NURBS and Bezier), metaballs. 

There are no primitives like sphere or tube, it is all represented as triangles, quads, line strips or a set of points. 

POPs have no curve primitives at the moment, but spline subdivision on sets of control points with attributes like tension, weight, tangents are possible using the Line POP and Line Divide POP. 

Primitives are defined from [Points](</index.php?title=Points&action=edit&redlink=1> "Points \(page does not exist\)") plus other data. 

In SOPs, see also: [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point](<./Point.md> "Point"), [Point List](<./Point_List.md> "Point List"), [Point Class](<./Point_Class.md> "Point Class"), [Prims Class](<./Prims_Class.md> "Prims Class"), [Polygon](<./Polygon.md> "Polygon"), [Vertex](<./Vertex.md> "Vertex"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](</index.php?title=Point_Groups&action=edit&redlink=1> "Point Groups \(page does not exist\)"), [Primitive Groups](</index.php?title=Primitive_Groups&action=edit&redlink=1> "Primitive Groups \(page does not exist\)"), [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)"). 

Every SOP has a Primitive List, which may contain any number of primitives of the following types: 

## 

Line Strips
* **Closed or Open**


A linestrip can be closed, where the last vertex is connected to the first vertex by making the last vertex index equal to the first vertex index, or may be open, where the last vertex is not connected to the first vertex. 

A closed linestrip shares its first and last vertex and is flagged internally as "closed". Thus, if an linestrip has five vertices, it will still have five unique vertices when closed. 

This diagram should say Linestrip, not Polygon: 
* **Convex or Concave (not relevant to POPs)**


A _polygon_ can be [**convex or concave**](<./Convex_and_Concave_Polygons.md> "Convex and Concave Polygons"), as illustrated below: 

Convex _Polygons_

Concave *Polygons* 

A polygon is convex if any vertical or horizontal axis intersects it at most twice. 

See also for SOPs (POPs equivalents coming): [Geometry Detail](<./Geometry_Detail.md> "Geometry Detail"), [Point](<./Point.md> "Point"), [Point List](<./Point_List.md> "Point List"), [Point Class](<./Point_Class.md> "Point Class"), [Primitive](<./Primitive.md> "Primitive"), [Prims Class](<./Prims_Class.md> "Prims Class"), [Vertex](<./Vertex.md> "Vertex"), [SOP](<./SOP.md> "SOP"), [SOP Class](<./SOP_Class.md> "SOP Class"), [SOP to DAT](<./SOP_to_DAT.md> "SOP to DAT"), [Script SOP](<./Script_SOP.md> "Script SOP"), [Point Groups](</index.php?title=Point_Groups&action=edit&redlink=1> "Point Groups \(page does not exist\)"), [Primitive Groups](</index.php?title=Primitive_Groups&action=edit&redlink=1> "Primitive Groups \(page does not exist\)"), [Attributes](</index.php?title=Attributes&action=edit&redlink=1> "Attributes \(page does not exist\)"). 

## 

Meshes - NOT IMPLEMENTED IN POPS ATM

Meshes in SOPs are a collection of vertices that can be represented as having a number of rows and columns based on a UV co-ordinate system. They can be modified into various shapes such as tubes and spheres by changing the point coordinates and/or closing the mesh in U or V, while maintaining their row/column-like topology. 

For example, below right is a mesh modified into a sphere by wrapping the mesh in U. Both primitives have the same m x n point topology, only the point coordinates are different. What looks like individual polygons in the above figure are actually intrinsic parts of the primitive. 

A figure that doesn't have an m × n topology cannot be a primitive mesh. The mesh below-left is not a primitive mesh, it does not have an m x n topology. The mesh below-right is a 5x4 primitive mesh. 

## 

Point Primitives in POPs

Point Primitives in POPs are primitives with a single vertex (which is simply the index of a point) and can be rendered as dots. They can represent point clouds, particle systems, or any other single-point data type. 

When you read in a point cloud, for example, it creates a point list, where each point has the attributes of the file being read in, and there is a list of Point Primitives, where each primitive is the index of a point in the point list. So a 1000 point point cloud would have 1000 points and 1000 point primitives. 

Note that a POP can have a point list with no primitives. You would not see them when rendered, but they can be used for instancing or copy-templates, or a wide range of other purposes. 

Particles in SOPs: One “particle system” in SOPs contains multiple point indexes: 

A particle system in SOPs is a type of **Primitive** of a [SOP](<./SOP.md> "SOP") that consists of a group of discrete particles (points) which change over time. Each particle has its own attributes controlling size, position, velocity, etc. Particles can generate new attributes depending on their age, or they may die. Assigning values discretely to each particle enables realistic modeling of systems involving turbulence such as: smoke, wind, fire, dust, and hair.) 

See also [Point Sprite MAT](<./Point_Sprite_MAT.md> "Point Sprite MAT")

## 

Splines in SOPs

TouchDesigner allows you to create both Bézier and NURBS curves and surfaces using splines. Refer to [Splines](</index.php?title=Splines&action=edit&redlink=1> "Splines \(page does not exist\)") article for a complete discussion of these types.
