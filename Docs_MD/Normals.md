# Normals

[![](./images/thumb/b/b1/Normals.jpg/300px-Normals.jpg)](</File:Normals.jpg>)

[](</File:Normals.jpg> "Enlarge")

A box SOP with point normals (blue) and primitive normals (pink).

A **normal** is a directional vector associated with a particular geometric entity, commonly perpendicular to it. The normal to a surface at a given point is a vector perpendicular to the surface at that point, and is computed as the cross product of the tangent vectors at that point. 

The direction the normals take (up or down) is dependent on the order in which the cross product is computed (imagine a cork moving up or down depending on the direction the cork screw turns). 

Normals are used for such things as: the basis for the direction things move over time, and for determining shading. In the Model Editor you can use point and primitive normals to pick, and even translate geometry along the normal. 

Surface normals indicate the direction a surface faces. This is used to determine the amount of shading that a surface receives; the more it faces the light, the lighter the shading it receives. 

## Types of Normals

Normals come in four varieties: plane normals, point normals, vertex normals, and surface normals. They indicate the orientation (direction) of a point, plane, vertex, or surface curve. If a curve is planar and does not share its points with other primitives, its default point, vertex, and primitive normals are identical, perpendicular to the plane of the curve. 

## Activating Normals Display

Activate the Point, Vertex, and Primitive Normal Display in TouchDesigner by enabling the normals option in the [Display Options](<./Display_Options.md> "Display Options") dialog, available by right-clicking any SOP and selecting _Display Parameters_ from the context menu. 

Note that the point normals must have been computed first (in a Point SOP, for example). Primitive normals are computed on the spot and only when they are turned on for display. Some systematic primitives, like sphere and cylinder do not have a normal.
